import { ApiError } from "./client";
import type { ChatApiResponse, ChatMessage, ChatResponseData } from "../../types/ai";

const API_BASE_URL =
  (import.meta.env.VITE_API_BASE_URL as string | undefined) ||
  "http://127.0.0.1:8000/api/v1";

/**
 * Send a conversational operational query to the PharmaKon AI Pharmacy Assistant.
 * Connects to POST /api/v1/ai/chat with Bearer authentication and standard envelope parsing.
 */
export async function sendAiChatMessage(
  message: string,
  history: ChatMessage[] = [],
): Promise<ChatResponseData> {
  const token = localStorage.getItem("pharmakon_token");

  const headers = new Headers();
  headers.set("Accept", "application/json");
  headers.set("Content-Type", "application/json");

  if (token) {
    headers.set("Authorization", `Bearer ${token}`);
  }

  let response: Response;

  try {
    response = await fetch(`${API_BASE_URL}/ai/chat`, {
      method: "POST",
      headers,
      body: JSON.stringify({
        message: message.trim(),
        history,
      }),
    });
  } catch {
    throw new ApiError(
      "Cannot connect to PharmaKon API. Check that the backend server is running.",
      0,
      "NETWORK_ERROR",
    );
  }

  const body = (await response.json().catch(() => null)) as
    | ChatApiResponse
    | { success: false; error: { code: string; message: string; details?: unknown } }
    | null;

  if (!response.ok || !body || body.success !== true) {
    if (response.status === 401) {
      throw new ApiError(
        "Authentication required. Please sign in to consult the AI Assistant.",
        401,
        "UNAUTHORIZED",
      );
    }
    if (response.status === 422) {
      throw new ApiError(
        "Invalid query format or message exceeds maximum character limits.",
        422,
        "VALIDATION_ERROR",
      );
    }
    if (response.status === 429) {
      const rateLimitMsg =
        body && "error" in body && body.error?.message
          ? body.error.message
          : "Google Gemini API rate limit or daily free-tier quota exceeded. Please provide a fresh API key or retry later.";
      throw new ApiError(rateLimitMsg, 429, "AI_RATE_LIMIT");
    }
    if (response.status === 503) {
      throw new ApiError(
        "AI Assistant is currently unconfigured. Please configure GEMINI_API_KEY in backend/.env.",
        503,
        "AI_NOT_CONFIGURED",
      );
    }
    if (response.status === 504) {
      throw new ApiError(
        "The request timed out while communicating with the upstream Gemini model. Please try again.",
        504,
        "AI_TIMEOUT",
      );
    }

    const errorMsg =
      body && "error" in body && body.error?.message
        ? body.error.message
        : "An unexpected error occurred while communicating with the AI Assistant.";
    const errorCode =
      body && "error" in body && body.error?.code ? body.error.code : "API_ERROR";

    throw new ApiError(errorMsg, response.status, errorCode);
  }

  return body.data;
}
