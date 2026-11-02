// AI Assistant Domain Types matching backend/app/schemas/ai.py

export type ChatRole = "user" | "model" | "assistant";

export interface ChatMessage {
  role: ChatRole;
  content: string;
}

export interface ChatRequest {
  message: string;
  history?: ChatMessage[];
}

export interface ChatResponseData {
  answer: string;
  history: ChatMessage[];
  tools_used: string[];
}

export interface ChatApiResponse {
  success: true;
  data: ChatResponseData;
  message: string;
}
