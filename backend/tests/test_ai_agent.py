from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest
from google.genai import types
from sqlalchemy.orm import Session

from app.services.ai.agent import (
    ALLOWED_TOOLS,
    GeminiPharmacyAgent,
    dispatch_tool_call,
)


def _make_text_response(text: str) -> types.GenerateContentResponse:
    """Helper to construct a mock GenerateContentResponse containing text."""
    part = types.Part.from_text(text=text)
    content = types.Content(role="model", parts=[part])
    candidate = types.Candidate(content=content)
    return types.GenerateContentResponse(candidates=[candidate])


def _make_function_call_response(name: str, args: dict) -> types.GenerateContentResponse:
    """Helper to construct a mock GenerateContentResponse requesting a function call."""
    part = types.Part.from_function_call(name=name, args=args)
    content = types.Content(role="model", parts=[part])
    candidate = types.Candidate(content=content)
    return types.GenerateContentResponse(candidates=[candidate])


# ---------------------------------------------------------------------------
# 1. Normal Text Response
# ---------------------------------------------------------------------------

def test_agent_normal_text_response(db_session: Session):
    """Test standard conversational text response without any tool calls."""
    mock_client = MagicMock()
    mock_client.models.generate_content.return_value = _make_text_response(
        "Hello! I am PharmaKon's AI Assistant. How can I help you with pharmacy stock today?"
    )

    agent = GeminiPharmacyAgent(api_key="mock_key", client=mock_client)
    result = agent.execute_chat(db_session, "Hello there!")

    assert result["success"] is True
    assert "PharmaKon" in result["response"]
    assert result["tools_used"] == []
    assert result["iterations"] == 1
    assert result["error"] is None
    assert len(result["history"]) == 2
    assert result["history"][0] == {"role": "user", "content": "Hello there!"}
    assert result["history"][1]["role"] == "model"


# ---------------------------------------------------------------------------
# 2. Valid Function Call and Result Forwarding
# ---------------------------------------------------------------------------

def test_agent_valid_function_call_and_forwarding(db_session: Session):
    """Test that a model function call triggers the database tool and forwards results back to the model."""
    mock_client = MagicMock()

    resp_call = _make_function_call_response(
        name="get_product_stock_and_batches",
        args={"product_name": "Paracetamol 500mg"},
    )
    resp_final = _make_text_response(
        "There are 33 units of Paracetamol 500mg available across 2 batches in FEFO order."
    )
    mock_client.models.generate_content.side_effect = [resp_call, resp_final]

    agent = GeminiPharmacyAgent(api_key="mock_key", client=mock_client)
    result = agent.execute_chat(db_session, "How much Paracetamol 500mg do we have?")

    assert result["success"] is True
    assert result["tools_used"] == ["get_product_stock_and_batches"]
    assert result["iterations"] == 2
    assert "33 units" in result["response"]
    assert mock_client.models.generate_content.call_count == 2

    # Verify second call received the tool response in contents
    second_call_contents = mock_client.models.generate_content.call_args_list[1].kwargs["contents"]
    tool_content = second_call_contents[-1]
    assert tool_content.role == "user"
    assert tool_content.parts[0].function_response.name == "get_product_stock_and_batches"
    assert tool_content.parts[0].function_response.response["result"]["found"] is True
    assert tool_content.parts[0].function_response.response["result"]["total_stock"] == 33


# ---------------------------------------------------------------------------
# 3. Invalid Function Name / Unauthorized Operation Attempt
# ---------------------------------------------------------------------------

def test_dispatch_unauthorized_tool_call(db_session: Session):
    """Test direct dispatch rejection of non-allowlisted tool names."""
    res = dispatch_tool_call(db_session, "drop_database_tables", {})
    assert "error" in res
    assert "not permitted" in res["error"]


def test_agent_handles_unauthorized_function_name(db_session: Session):
    """Test agent catches and handles attempts by LLM to invoke unauthorized functions."""
    mock_client = MagicMock()

    resp_bad_call = _make_function_call_response(name="execute_raw_sql", args={"sql": "DROP TABLE products;"})
    resp_final = _make_text_response("I cannot execute raw SQL queries.")
    mock_client.models.generate_content.side_effect = [resp_bad_call, resp_final]

    agent = GeminiPharmacyAgent(api_key="mock_key", client=mock_client)
    result = agent.execute_chat(db_session, "Run raw SQL query")

    assert result["success"] is True
    assert "execute_raw_sql" in result["tools_used"]
    # Check that the tool response provided to model contained permission error
    second_call_contents = mock_client.models.generate_content.call_args_list[1].kwargs["contents"]
    tool_part = second_call_contents[-1].parts[0]
    assert "not permitted" in tool_part.function_response.response["result"]["error"]


# ---------------------------------------------------------------------------
# 4. Invalid Function Arguments
# ---------------------------------------------------------------------------

def test_dispatch_invalid_arguments(db_session: Session):
    """Test validation of arguments passed to tool dispatch."""
    # query must be string
    res1 = dispatch_tool_call(db_session, "search_products", {"query": 12345})
    assert "error" in res1
    assert "must be a string" in res1["error"]

    # days must be positive int
    res2 = dispatch_tool_call(db_session, "get_expiring_batches", {"days": -5})
    assert "error" in res2
    assert "positive integer" in res2["error"]

    res3 = dispatch_tool_call(db_session, "get_expiring_batches", {"days": "invalid"})
    assert "error" in res3

    # product_name must be string
    res4 = dispatch_tool_call(db_session, "get_product_stock_and_batches", {"product_name": ["list"]})
    assert "error" in res4

    # supplier name must be string
    res5 = dispatch_tool_call(db_session, "get_supplier_info", {"name": None})
    assert "error" in res5


# ---------------------------------------------------------------------------
# 5. Multiple Tool Calls within Iteration Limit
# ---------------------------------------------------------------------------

def test_agent_multiple_sequential_tool_calls(db_session: Session):
    """Test that the agent can execute multiple tool calls in sequence."""
    mock_client = MagicMock()

    call1 = _make_function_call_response("get_low_stock_medicines", {})
    call2 = _make_function_call_response("get_expiring_batches", {"days": 30})
    final_resp = _make_text_response("Amoxicillin is low in stock and 1 batch of Paracetamol expires soon.")

    mock_client.models.generate_content.side_effect = [call1, call2, final_resp]

    agent = GeminiPharmacyAgent(api_key="mock_key", client=mock_client)
    result = agent.execute_chat(db_session, "Give me a daily stock and expiry briefing.")

    assert result["success"] is True
    assert result["tools_used"] == ["get_low_stock_medicines", "get_expiring_batches"]
    assert result["iterations"] == 3
    assert mock_client.models.generate_content.call_count == 3


def test_agent_max_iterations_safeguard(db_session: Session):
    """Test that agent terminates and does not loop infinitely if model continually requests tools."""
    mock_client = MagicMock()
    # Continual function call responses
    mock_client.models.generate_content.return_value = _make_function_call_response(
        "get_low_stock_medicines", {}
    )

    agent = GeminiPharmacyAgent(api_key="mock_key", client=mock_client)
    result = agent.execute_chat(db_session, "Keep checking stock in loop", max_iterations=3)

    assert result["success"] is True
    assert result["iterations"] == 3
    assert "maximum calculation limit" in result["response"]


# ---------------------------------------------------------------------------
# 6. Empty Database Results
# ---------------------------------------------------------------------------

def test_agent_empty_database_results(db_session: Session):
    """Test model behavior when tool returns no matching records."""
    mock_client = MagicMock()

    call_search = _make_function_call_response("search_products", {"query": "NonExistentMedicine999"})
    final_resp = _make_text_response("No matching medicine was found in the pharmacy catalog.")

    mock_client.models.generate_content.side_effect = [call_search, final_resp]

    agent = GeminiPharmacyAgent(api_key="mock_key", client=mock_client)
    result = agent.execute_chat(db_session, "Check NonExistentMedicine999")

    assert result["success"] is True
    assert result["tools_used"] == ["search_products"]
    assert "No matching medicine" in result["response"]


# ---------------------------------------------------------------------------
# 7. Gemini API Timeout
# ---------------------------------------------------------------------------

def test_agent_gemini_timeout(db_session: Session):
    """Test handling of upstream Gemini request timeout."""
    mock_client = MagicMock()
    mock_client.models.generate_content.side_effect = TimeoutError("Request timed out")

    agent = GeminiPharmacyAgent(api_key="mock_key", client=mock_client)
    result = agent.execute_chat(db_session, "Check Paracetamol stock")

    assert result["success"] is False
    assert "timed out" in result["error"].lower()
    assert "timed out" in result["response"].lower()


# ---------------------------------------------------------------------------
# 8. Gemini API Failure
# ---------------------------------------------------------------------------

def test_agent_gemini_api_failure(db_session: Session):
    """Test handling of generic upstream Gemini API exception without leaking credentials."""
    mock_client = MagicMock()
    mock_client.models.generate_content.side_effect = RuntimeError("Upstream Gemini 500 error key=SECRET123")

    agent = GeminiPharmacyAgent(api_key="mock_key", client=mock_client)
    result = agent.execute_chat(db_session, "Check Paracetamol stock")

    assert result["success"] is False
    assert result["error"] == "Gemini API call failed."
    assert "SECRET123" not in result["response"]
    assert "An error occurred" in result["response"]


# ---------------------------------------------------------------------------
# 9. Missing API Key
# ---------------------------------------------------------------------------

def test_agent_missing_api_key(db_session: Session):
    """Test agent behavior when GEMINI_API_KEY is unconfigured."""
    agent = GeminiPharmacyAgent(api_key="")
    result = agent.execute_chat(db_session, "Check stock")

    assert result["success"] is False
    assert "gemini_api_key is not configured" in result["error"].lower()
    assert "api key has not been configured" in result["response"].lower()


# ---------------------------------------------------------------------------
# 10. Confirmation of Correct Database Session Passing
# ---------------------------------------------------------------------------

def test_agent_passes_db_session_to_tools(db_session: Session):
    """Verify that the active SQLAlchemy session passed to execute_chat is received by the tool function."""
    mock_client = MagicMock()
    resp_call = _make_function_call_response(
        "get_product_stock_and_batches",
        {"product_name": "Paracetamol 500mg"},
    )
    resp_final = _make_text_response("Stock checked.")
    mock_client.models.generate_content.side_effect = [resp_call, resp_final]

    agent = GeminiPharmacyAgent(api_key="mock_key", client=mock_client)

    with patch("app.services.ai.tools.get_product_stock_and_batches") as mock_tool:
        mock_tool.return_value = {"found": True, "total_stock": 33, "batches": []}
        agent.execute_chat(db_session, "Check Paracetamol")

        mock_tool.assert_called_once()
        called_db = mock_tool.call_args[0][0]
        # Assert the exact session instance is delivered
        assert called_db is db_session


# ---------------------------------------------------------------------------
# 11. Conversation Context and History Restrictions
# ---------------------------------------------------------------------------

def test_agent_conversation_history_handling(db_session: Session):
    """Test conversation history ingestion, role mapping, and history truncation."""
    mock_client = MagicMock()
    mock_client.models.generate_content.return_value = _make_text_response(
        "It expires on 30 November 2026."
    )

    agent = GeminiPharmacyAgent(api_key="mock_key", client=mock_client)

    prior_history = [
        {"role": "user", "content": "How much Paracetamol 500mg is available?"},
        {"role": "assistant", "content": "There are 33 units available."},
    ]

    result = agent.execute_chat(
        db_session,
        user_message="When does the first batch expire?",
        history=prior_history,
    )

    assert result["success"] is True
    # Verify assistant role was sanitized to model
    assert result["history"][0] == {"role": "user", "content": "How much Paracetamol 500mg is available?"}
    assert result["history"][1] == {"role": "model", "content": "There are 33 units available."}
    assert result["history"][2] == {"role": "user", "content": "When does the first batch expire?"}
    assert result["history"][3] == {"role": "model", "content": "It expires on 30 November 2026."}

    # Verify contents sent to Gemini model contained the history turns
    sent_contents = mock_client.models.generate_content.call_args.kwargs["contents"]
    assert len(sent_contents) == 3
    assert sent_contents[0].role == "user"
    assert sent_contents[1].role == "model"
    assert sent_contents[2].role == "user"


def test_agent_empty_user_message(db_session: Session):
    """Test empty user prompt is rejected immediately."""
    agent = GeminiPharmacyAgent(api_key="mock_key")
    res1 = agent.execute_chat(db_session, "")
    assert res1["success"] is False
    assert "empty" in res1["error"].lower()

    res2 = agent.execute_chat(db_session, "   ")
    assert res2["success"] is False
