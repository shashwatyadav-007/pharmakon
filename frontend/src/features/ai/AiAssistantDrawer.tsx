import React, { useState, useRef, useEffect } from "react";
import { sendAiChatMessage } from "../../lib/api/aiClient";
import type { ChatMessage } from "../../types/ai";

interface AiAssistantDrawerProps {
  isOpen: boolean;
  onClose: () => void;
}

const SUGGESTED_PROMPTS = [
  "Which medicines are low in stock?",
  "Which batches are expiring soon?",
  "Find Paracetamol 500mg stock.",
  "Show available supplier information.",
];

export const AiAssistantDrawer: React.FC<AiAssistantDrawerProps> = ({
  isOpen,
  onClose,
}) => {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [toolsHistory, setToolsHistory] = useState<Record<number, string[]>>({});
  const [input, setInput] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const messagesEndRef = useRef<HTMLDivElement>(null);
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  // Auto-scroll to bottom of conversation
  useEffect(() => {
    if (
      isOpen &&
      messagesEndRef.current &&
      typeof messagesEndRef.current.scrollIntoView === "function"
    ) {
      messagesEndRef.current.scrollIntoView({ behavior: "smooth" });
    }
  }, [messages, isLoading, isOpen]);

  // Focus textarea when opened
  useEffect(() => {
    if (isOpen) {
      setTimeout(() => textareaRef.current?.focus(), 100);
    }
  }, [isOpen]);

  const handleSend = async (messageToSend?: string) => {
    const text = (messageToSend || input).trim();
    if (!text || isLoading) return;

    setError(null);
    const updatedHistory: ChatMessage[] = [
      ...messages,
      { role: "user", content: text },
    ];

    setMessages(updatedHistory);
    setInput("");
    setIsLoading(true);

    try {
      const data = await sendAiChatMessage(text, messages);
      setMessages(data.history);

      // Record which tools were used for this assistant turn
      if (data.tools_used && data.tools_used.length > 0) {
        setToolsHistory((prev) => ({
          ...prev,
          [data.history.length - 1]: data.tools_used,
        }));
      }
    } catch (err: unknown) {
      if (err instanceof Error) {
        setError(err.message);
      } else {
        setError("Failed to generate response. Please try again.");
      }
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  const handleClear = () => {
    setMessages([]);
    setToolsHistory({});
    setError(null);
  };

  // Safe formatting for assistant responses (bold, bullets, paragraphs)
  const renderFormattedText = (content: string) => {
    const lines = content.split("\n");
    return (
      <div className="space-y-1">
        {lines.map((line, idx) => {
          const trimmed = line.trim();

          // Parse **bold** tokens
          const parts = line.split(/(\*\*[^*]+\*\*)/g);
          const formattedParts = parts.map((part, pIdx) => {
            if (part.startsWith("**") && part.endsWith("**")) {
              return (
                <strong key={pIdx} className="font-semibold text-slate-900">
                  {part.slice(2, -2)}
                </strong>
              );
            }
            return part;
          });

          if (trimmed.startsWith("- ") || trimmed.startsWith("* ")) {
            return (
              <div key={idx} className="flex items-start gap-2 pl-2">
                <span className="text-emerald-600 font-bold leading-5">•</span>
                <span className="text-sm text-slate-800 leading-relaxed">
                  {formattedParts}
                </span>
              </div>
            );
          }

          if (/^\d+\.\s/.test(trimmed)) {
            return (
              <div key={idx} className="text-sm text-slate-800 font-medium pl-1 leading-relaxed">
                {formattedParts}
              </div>
            );
          }

          if (!trimmed) {
            return <div key={idx} className="h-1.5" />;
          }

          return (
            <p key={idx} className="text-sm text-slate-800 leading-relaxed">
              {formattedParts}
            </p>
          );
        })}
      </div>
    );
  };

  if (!isOpen) return null;

  return (
    <>
      {/* Mobile Backdrop (only on small screens < md) */}
      <div
        className="fixed inset-0 bg-slate-900/30 z-40 md:hidden transition-opacity"
        onClick={onClose}
        aria-hidden="true"
      />

      {/* Assistant Panel: Docked side-by-side on desktop, slide-over drawer on mobile */}
      <aside
        className="fixed inset-y-0 right-0 z-50 w-full sm:w-[420px] md:relative md:inset-auto md:z-20 md:w-[420px] lg:w-[460px] bg-white border-l border-slate-200 flex flex-col h-screen md:sticky md:top-0 shadow-xl md:shadow-none flex-shrink-0"
        role="complementary"
        aria-label="PharmaKon AI Assistant"
      >
          {/* Header */}
          <div className="h-16 px-6 bg-white border-b border-slate-200 flex items-center justify-between flex-shrink-0">
            <div className="flex items-center gap-2.5">
              <div className="w-7 h-7 rounded bg-emerald-600 flex items-center justify-center text-white font-bold text-xs">
                AI
              </div>
              <div>
                <h2 className="text-sm font-bold text-slate-900 tracking-tight">
                  PharmaKon Assistant
                </h2>
                <div className="flex items-center gap-1.5">
                  <span className="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse" />
                  <span className="text-[11px] text-slate-500">PostgreSQL Grounded</span>
                </div>
              </div>
            </div>

            <div className="flex items-center gap-2">
              {messages.length > 0 && (
                <button
                  type="button"
                  onClick={handleClear}
                  className="px-2.5 py-1 text-xs font-medium text-slate-600 hover:text-slate-900 border border-slate-200 rounded hover:bg-slate-50 transition-colors duration-75 cursor-pointer"
                  title="Clear conversation"
                >
                  Clear
                </button>
              )}
              <button
                type="button"
                onClick={onClose}
                className="p-1.5 text-slate-400 hover:text-slate-700 rounded border border-slate-200 hover:bg-slate-100 transition-colors duration-75 cursor-pointer"
                aria-label="Close assistant panel"
              >
                <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                </svg>
              </button>
            </div>
          </div>

          {/* Conversation Area */}
          <div className="flex-1 overflow-y-auto p-4 sm:p-6 space-y-4 bg-slate-50/50">
            {messages.length === 0 ? (
              <div className="h-full flex flex-col justify-center text-left py-6">
                <div className="bg-white border border-slate-200 rounded-md p-5 shadow-sm mb-6">
                  <div className="w-9 h-9 rounded bg-emerald-50 border border-emerald-200 flex items-center justify-center text-emerald-700 font-semibold mb-3">
                    <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        strokeWidth={2}
                        d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
                      />
                    </svg>
                  </div>
                  <h3 className="text-sm font-bold text-slate-900 mb-1">
                    Aayushman Pharmacy Operations Assistant
                  </h3>
                  <p className="text-xs text-slate-600 leading-relaxed">
                    Ask natural language questions about medicine stock, batch expiry dates, FEFO recommendations, and supplier contacts. All responses are verified against live database records.
                  </p>
                </div>

                <div>
                  <p className="text-xs font-semibold uppercase tracking-wider text-slate-500 mb-2 px-1">
                    Suggested Operational Queries
                  </p>
                  <div className="flex flex-col gap-2">
                    {SUGGESTED_PROMPTS.map((prompt, idx) => (
                      <button
                        key={idx}
                        type="button"
                        onClick={() => handleSend(prompt)}
                        className="text-left text-xs text-slate-700 bg-white border border-slate-200 hover:border-emerald-500 hover:bg-emerald-50/40 p-2.5 rounded-md transition-colors duration-75 cursor-pointer shadow-xs"
                      >
                        {prompt}
                      </button>
                    ))}
                  </div>
                </div>
              </div>
            ) : (
              <>
                {messages.map((msg, index) => {
                  const isUser = msg.role === "user";
                  const toolsUsed = toolsHistory[index];

                  return (
                    <div
                      key={index}
                      className={`flex flex-col ${isUser ? "items-end" : "items-start"}`}
                    >
                      <span className="text-[10px] font-semibold uppercase tracking-wider text-slate-400 mb-1 px-1">
                        {isUser ? "Operator" : "PharmaKon Assistant"}
                      </span>

                      <div
                        className={`max-w-[85%] rounded-md p-3.5 text-sm shadow-xs ${
                          isUser
                            ? "bg-slate-900 text-white rounded-br-xs"
                            : "bg-white text-slate-800 border border-slate-200 rounded-bl-xs"
                        }`}
                      >
                        {isUser ? (
                          <p className="text-sm text-white leading-relaxed">{msg.content}</p>
                        ) : (
                          renderFormattedText(msg.content)
                        )}
                      </div>

                      {/* Tool metadata badge for grounded assistant answers */}
                      {!isUser && toolsUsed && toolsUsed.length > 0 && (
                        <div className="mt-1 flex items-center gap-1 text-[11px] text-slate-500 px-1">
                          <span className="w-1.5 h-1.5 rounded-full bg-emerald-600" />
                          <span>Grounded with:</span>
                          <span className="font-mono text-[10px] bg-slate-100 border border-slate-200 px-1.5 py-0.2 rounded text-slate-700">
                            {toolsUsed.join(", ")}
                          </span>
                        </div>
                      )}
                    </div>
                  );
                })}

                {/* Loading indicator */}
                {isLoading && (
                  <div className="flex flex-col items-start">
                    <span className="text-[10px] font-semibold uppercase tracking-wider text-slate-400 mb-1 px-1">
                      PharmaKon Assistant
                    </span>
                    <div className="bg-white border border-slate-200 rounded-md p-3 shadow-xs flex items-center gap-2">
                      <span className="w-2 h-2 rounded-full bg-emerald-600 animate-ping" />
                      <span className="text-xs text-slate-600">Querying pharmacy database...</span>
                    </div>
                  </div>
                )}

                {/* Error Banner */}
                {error && (
                  <div className="p-3 bg-rose-50 border border-rose-200 rounded-md text-xs text-rose-800">
                    <p className="font-semibold mb-0.5">Assistant Error</p>
                    <p>{error}</p>
                  </div>
                )}

                <div ref={messagesEndRef} />
              </>
            )}
          </div>

          {/* Input Footer */}
          <div className="p-3 sm:p-4 bg-white border-t border-slate-200 flex-shrink-0">
            <div className="flex gap-2 items-end">
              <textarea
                ref={textareaRef}
                value={input}
                onChange={(e) => setInput(e.target.value)}
                onKeyDown={handleKeyDown}
                placeholder="Ask about stock, expiry dates, FEFO batches..."
                rows={2}
                disabled={isLoading}
                className="flex-1 resize-none border border-slate-300 rounded-md p-2.5 text-xs sm:text-sm text-slate-900 placeholder:text-slate-400 focus:outline-none focus:ring-1 focus:ring-emerald-600 focus:border-emerald-600 disabled:bg-slate-100 disabled:cursor-not-allowed"
              />
              <button
                type="button"
                onClick={() => handleSend()}
                disabled={isLoading || !input.trim()}
                className="h-[52px] px-4 bg-emerald-600 hover:bg-emerald-700 disabled:bg-slate-300 text-white font-medium text-xs rounded-md transition-colors duration-75 cursor-pointer disabled:cursor-not-allowed flex items-center justify-center shadow-xs"
              >
                Send
              </button>
            </div>
            <p className="text-[10px] text-slate-400 mt-2 text-center">
              Press Enter to send, Shift + Enter for a new line. Answers verified via PostgreSQL.
            </p>
          </div>
      </aside>
    </>
  );
};
