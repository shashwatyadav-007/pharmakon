from __future__ import annotations

import logging
import time
from typing import Any

from google import genai
from google.genai import errors, types
from sqlalchemy.orm import Session

from app.core.config import settings
from app.services.ai import tools
from app.services.ai.prompts import PHARMAKON_SYSTEM_PROMPT

logger = logging.getLogger(__name__)

# Allowed database tool names - strict allowlist
ALLOWED_TOOLS = {
    "search_products",
    "get_product_stock_and_batches",
    "get_low_stock_medicines",
    "get_expiring_batches",
    "get_supplier_info",
}

MAX_TOOL_ITERATIONS = 5
MAX_HISTORY_MESSAGES = 10
FALLBACK_MODELS = ["gemini-2.5-flash", "gemini-2.0-flash", "gemini-1.5-flash"]


def get_tool_declarations() -> list[types.FunctionDeclaration]:
    """Generate OpenAPI-compatible function declarations for Gemini function calling."""
    return [
        types.FunctionDeclaration(
            name="search_products",
            description=(
                "Search medicines and pharmacy catalog items by commercial name, SKU code, or barcode. "
                "Returns product catalog details including computed total active stock."
            ),
            parameters=types.Schema(
                type="OBJECT",
                properties={
                    "query": types.Schema(
                        type="STRING",
                        description="Medicine name, SKU code, or barcode to search.",
                    ),
                    "limit": types.Schema(
                        type="INTEGER",
                        description="Maximum number of products to return (default 10, max 100).",
                    ),
                },
                required=["query"],
            ),
        ),
        types.FunctionDeclaration(
            name="get_product_stock_and_batches",
            description=(
                "Retrieve total available inventory stock, individual batch numbers, expiry dates, "
                "purchase costs, and days until expiry for a specific medicine in First Expiry, First Out (FEFO) order."
            ),
            parameters=types.Schema(
                type="OBJECT",
                properties={
                    "product_name": types.Schema(
                        type="STRING",
                        description="Commercial name or SKU code of the medicine.",
                    ),
                },
                required=["product_name"],
            ),
        ),
        types.FunctionDeclaration(
            name="get_low_stock_medicines",
            description=(
                "Retrieve all active pharmacy products whose combined stock across all batches is at or below their configured reorder level."
            ),
            parameters=types.Schema(
                type="OBJECT",
                properties={},
            ),
        ),
        types.FunctionDeclaration(
            name="get_expiring_batches",
            description=(
                "Retrieve active medicine batches expiring within the specified number of days (default 60 days). "
                "Includes product name, batch number, expiry date, remaining quantity, and days remaining."
            ),
            parameters=types.Schema(
                type="OBJECT",
                properties={
                    "days": types.Schema(
                        type="INTEGER",
                        description="Days threshold for upcoming expiration (must be a positive integer, e.g. 30, 60, 90). Default is 60.",
                    ),
                },
            ),
        ),
        types.FunctionDeclaration(
            name="get_supplier_info",
            description=(
                "Search suppliers and pharmaceutical distributors by company name to retrieve contact person, phone number, email, and address."
            ),
            parameters=types.Schema(
                type="OBJECT",
                properties={
                    "name": types.Schema(
                        type="STRING",
                        description="Name or partial name of the supplier company.",
                    ),
                },
                required=["name"],
            ),
        ),
    ]


def dispatch_tool_call(
    db: Session,
    function_name: str,
    function_args: dict[str, Any],
) -> dict[str, Any]:
    """Securely dispatch a function call against the allowlist with parameterized database access.
    
    Validates arguments and passes the existing SQLAlchemy session.
    Never executes raw SQL or mutates database state.
    """
    if function_name not in ALLOWED_TOOLS:
        logger.warning("Attempted to execute unauthorized tool: %s", function_name)
        return {"error": f"Tool '{function_name}' is not permitted or does not exist."}

    try:
        if function_name == "search_products":
            query = function_args.get("query", "")
            if not isinstance(query, str):
                return {"error": "Invalid argument: 'query' must be a string."}
            limit = function_args.get("limit", 10)
            try:
                limit = int(limit)
            except (ValueError, TypeError):
                limit = 10
            return {"products": tools.search_products(db, query=query, limit=limit)}

        elif function_name == "get_product_stock_and_batches":
            product_name = function_args.get("product_name", "")
            if not isinstance(product_name, str):
                return {"error": "Invalid argument: 'product_name' must be a string."}
            return tools.get_product_stock_and_batches(db, product_name=product_name)

        elif function_name == "get_low_stock_medicines":
            return {"low_stock_medicines": tools.get_low_stock_medicines(db)}

        elif function_name == "get_expiring_batches":
            days = function_args.get("days", 60)
            try:
                days = int(days)
                if days <= 0:
                    return {"error": "Invalid argument: 'days' must be a positive integer."}
            except (ValueError, TypeError):
                return {"error": "Invalid argument: 'days' must be a valid integer."}
            return {"expiring_batches": tools.get_expiring_batches(db, days=days)}

        elif function_name == "get_supplier_info":
            name = function_args.get("name", "")
            if not isinstance(name, str):
                return {"error": "Invalid argument: 'name' must be a string."}
            return {"suppliers": tools.get_supplier_info(db, name=name)}

        return {"error": f"Unhandled tool '{function_name}'."}

    except Exception as exc:
        logger.error("Error executing tool %s: %s", function_name, exc)
        return {"error": f"Tool execution failed: {str(exc)}"}


class GeminiPharmacyAgent:
    """Agent orchestrator for PharmaKon AI Pharmacy Operations Assistant using Google GenAI SDK."""

    def __init__(
        self,
        api_key: str | None = None,
        model_name: str | None = None,
        temperature: float | None = None,
        timeout_seconds: int | None = None,
        client: genai.Client | None = None,
    ):
        self.api_key = api_key if api_key is not None else settings.GEMINI_API_KEY
        self.model_name = model_name or settings.AI_MODEL_NAME
        self.temperature = temperature if temperature is not None else settings.AI_TEMPERATURE
        self.timeout_seconds = (
            timeout_seconds if timeout_seconds is not None else settings.AI_REQUEST_TIMEOUT
        )
        self._client = client

    def get_client(self) -> genai.Client:
        """Instantiate and return the configured Google GenAI client."""
        if self._client is not None:
            return self._client
        if not self.api_key or not self.api_key.strip():
            raise ValueError("GEMINI_API_KEY is not configured in backend/.env.")

        # HttpOptions timeout is in milliseconds
        http_options = types.HttpOptions(timeout=int(self.timeout_seconds * 1000))
        self._client = genai.Client(api_key=self.api_key, http_options=http_options)
        return self._client

    def execute_chat(
        self,
        db: Session,
        user_message: str,
        history: list[dict[str, Any]] | None = None,
        max_iterations: int = MAX_TOOL_ITERATIONS,
    ) -> dict[str, Any]:
        """Execute a conversational chat turn with Gemini and handle function calling.
        
        Takes the user message and optional conversation history, calls Gemini with the 5 tools,
        iteratively executes any requested tool calls against the database session, and returns
        the final grounded response.
        """
        if not user_message or not user_message.strip():
            return {
                "success": False,
                "error": "User message cannot be empty.",
                "response": "Please provide a valid question or query.",
                "tools_used": [],
                "history": history or [],
            }

        try:
            client = self.get_client()
        except ValueError as exc:
            return {
                "success": False,
                "error": str(exc),
                "response": "The AI Assistant is currently unavailable because the Gemini API key has not been configured in the backend environment.",
                "tools_used": [],
                "history": history or [],
            }

        # Build contents from sanitized history
        contents: list[types.Content] = []
        sanitized_history: list[dict[str, str]] = []

        if history:
            # Bound history to the most recent turns
            for turn in history[-MAX_HISTORY_MESSAGES:]:
                raw_role = turn.get("role", "user")
                role = "model" if raw_role in ("model", "assistant") else "user"
                content_text = str(turn.get("content", "")).strip()
                if content_text:
                    sanitized_history.append({"role": role, "content": content_text})
                    contents.append(
                        types.Content(
                            role=role,
                            parts=[types.Part.from_text(text=content_text)],
                        )
                    )

        # Append current user prompt
        contents.append(
            types.Content(
                role="user",
                parts=[types.Part.from_text(text=user_message.strip())],
            )
        )

        tool = types.Tool(function_declarations=get_tool_declarations())
        config = types.GenerateContentConfig(
            system_instruction=PHARMAKON_SYSTEM_PROMPT,
            temperature=self.temperature,
            tools=[tool],
            automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True),
        )

        tools_used: list[str] = []
        iteration = 0
        final_text = ""

        candidate_models = [self.model_name] + [m for m in FALLBACK_MODELS if m != self.model_name]
        active_model = self.model_name

        # Function-calling loop with max iteration safeguard
        while iteration < max_iterations:
            iteration += 1
            response = None
            last_error: Exception | None = None

            for model_candidate in candidate_models:
                api_attempts = 0
                model_succeeded = False
                while api_attempts < 2:
                    api_attempts += 1
                    try:
                        response = client.models.generate_content(
                            model=model_candidate,
                            contents=contents,
                            config=config,
                        )
                        active_model = model_candidate
                        model_succeeded = True
                        break
                    except errors.APIError as api_err:
                        last_error = api_err
                        logger.warning("Gemini model %s API error: %s. Trying next candidate model...", model_candidate, api_err)
                        break
                    except TimeoutError as timeout_err:
                        last_error = timeout_err
                        logger.warning("Gemini model %s timed out. Trying next candidate...", model_candidate)
                        break
                    except Exception as exc:
                        last_error = exc
                        logger.error("Gemini API call failed on %s: %s", model_candidate, exc)
                        break

                if model_succeeded and response is not None:
                    break

            if response is None:
                logger.error("All Gemini candidate models exhausted. Last error: %s", last_error)
                is_timeout = isinstance(last_error, TimeoutError)
                err_code = getattr(last_error, "code", None)
                err_status = getattr(last_error, "status", None)
                err_str_val = str(last_error).lower()
                is_quota = (
                    err_code == 429
                    or err_status == 429
                    or "429" in err_str_val
                    or "resource_exhausted" in err_str_val
                    or "quota" in err_str_val
                    or type(last_error).__name__ in ("ClientError", "ResourceExhausted")
                )
                if is_quota:
                    err_str = "Gemini API rate limit or quota exceeded (429 RESOURCE_EXHAUSTED)."
                    resp_str = (
                        "Google Gemini API daily free-tier quota (20 requests/day) has been exceeded for this API key. "
                        "Please update GEMINI_API_KEY in backend/.env with a fresh Google AI Studio key or retry when the quota resets."
                    )
                elif is_timeout:
                    err_str = "Gemini API request timed out."
                    resp_str = "The request timed out while communicating with the AI service. Please try again."
                else:
                    err_str = "Gemini API call failed."
                    resp_str = "An error occurred while communicating with the AI service. Please try again."

                return {
                    "success": False,
                    "error": err_str,
                    "response": resp_str,
                    "tools_used": tools_used,
                    "history": sanitized_history,
                }

            # Check if Gemini requested function calls
            function_calls = response.function_calls
            if not function_calls:
                # Normal text response received
                final_text = response.text or ""
                break

            # Append the model's function-calling turn to conversation history
            if response.candidates and response.candidates[0].content:
                contents.append(response.candidates[0].content)

            # Dispatch each requested function call against PostgreSQL
            tool_response_parts: list[types.Part] = []
            for call in function_calls:
                func_name = call.name
                func_args = call.args or {}
                tools_used.append(func_name)

                # Execute with parameterized database session
                tool_output = dispatch_tool_call(db, func_name, func_args)

                tool_response_parts.append(
                    types.Part.from_function_response(
                        name=func_name,
                        response={"result": tool_output},
                    )
                )

            # Forward tool results back to Gemini as a tool response turn
            contents.append(
                types.Content(
                    role="user",
                    parts=tool_response_parts,
                )
            )

        if not final_text and iteration >= max_iterations:
            final_text = (
                "The query required multiple database operations and reached the maximum calculation limit. "
                "Please refine your question."
            )

        updated_history = sanitized_history + [
            {"role": "user", "content": user_message.strip()},
            {"role": "model", "content": final_text},
        ]

        return {
            "success": True,
            "response": final_text,
            "tools_used": tools_used,
            "iterations": iteration,
            "history": updated_history,
            "error": None,
        }
