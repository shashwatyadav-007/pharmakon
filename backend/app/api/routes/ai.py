from __future__ import annotations

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.api.routes.auth import get_current_user
from app.core.database import get_db
from app.core.responses import AppError, success_response
from app.schemas.ai import ChatMessage, ChatRequest, ChatResponse
from app.schemas.auth import UserSummary
from app.services.ai.agent import GeminiPharmacyAgent

router = APIRouter(prefix="/ai", tags=["AI Assistant"])


def get_ai_agent() -> GeminiPharmacyAgent:
    """Dependency provider yielding the configured GeminiPharmacyAgent instance."""
    return GeminiPharmacyAgent()


@router.post(
    "/chat",
    summary="Chat with Pharmacy AI Assistant",
    description=(
        "Conversational operational assistant endpoint for PharmaKon. "
        "Answers natural language queries concerning product stock, batches, "
        "FEFO order, expiry alerts, and suppliers using grounded tool calling. "
        "Requires Bearer authentication."
    ),
    response_model=dict,
    status_code=status.HTTP_200_OK,
)
def chat_with_assistant(
    payload: ChatRequest,
    current_user: UserSummary = Depends(get_current_user),
    db: Session = Depends(get_db),
    agent: GeminiPharmacyAgent = Depends(get_ai_agent),
) -> dict:
    """Handle conversational turn with the grounded AI assistant."""
    raw_history = [{"role": turn.role, "content": turn.content} for turn in payload.history]

    result = agent.execute_chat(
        db=db,
        user_message=payload.message,
        history=raw_history,
    )

    if not result.get("success"):
        err = result.get("error", "")
        msg = result.get("response", "AI Assistant could not process the request.")

        if "timed out" in err.lower():
            raise AppError(
                code="AI_TIMEOUT",
                message=msg,
                status_code=status.HTTP_504_GATEWAY_TIMEOUT,
            )
        elif "gemini_api_key is not configured" in err.lower():
            raise AppError(
                code="AI_NOT_CONFIGURED",
                message=msg,
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            )
        elif "429" in str(err) or "resource_exhausted" in str(err).lower() or "quota" in str(err).lower():
            raise AppError(
                code="AI_RATE_LIMIT",
                message="Google Gemini API daily free-tier quota (20 requests/day) has been exceeded for this API key. Please provide a fresh Gemini API key in backend/.env or retry after quota reset.",
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            )
        else:
            raise AppError(
                code="AI_ERROR",
                message=msg,
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    response_data = ChatResponse(
        answer=result["response"],
        history=[
            ChatMessage(role=h["role"], content=h["content"])
            for h in result.get("history", [])
        ],
        tools_used=result.get("tools_used", []),
    )

    return success_response(
        data=response_data.model_dump(),
        message="AI response generated successfully",
    )
