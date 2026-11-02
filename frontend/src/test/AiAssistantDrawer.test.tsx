import { describe, it, expect, vi, beforeEach } from "vitest";
import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import { AiAssistantDrawer } from "../features/ai/AiAssistantDrawer";
import * as aiClient from "../lib/api/aiClient";

vi.mock("../lib/api/aiClient", () => ({
  sendAiChatMessage: vi.fn(),
}));

describe("AiAssistantDrawer Component", () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  it("does not render when isOpen is false", () => {
    const { container } = render(
      <AiAssistantDrawer isOpen={false} onClose={vi.fn()} />
    );
    expect(container.firstChild).toBeNull();
  });

  it("renders header, suggested prompts and input when isOpen is true", () => {
    render(<AiAssistantDrawer isOpen={true} onClose={vi.fn()} />);

    expect(screen.getByText("PharmaKon Assistant")).toBeInTheDocument();
    expect(screen.getByText("PostgreSQL Grounded")).toBeInTheDocument();
    expect(screen.getByText("Which medicines are low in stock?")).toBeInTheDocument();
    expect(screen.getByPlaceholderText(/Ask about stock/i)).toBeInTheDocument();
  });

  it("sends question and displays answer with tool badge", async () => {
    (aiClient.sendAiChatMessage as unknown as ReturnType<typeof vi.fn>).mockResolvedValueOnce({
      answer: "There are 33 units of Paracetamol in stock.",
      history: [
        { role: "user", content: "Paracetamol stock?" },
        { role: "model", content: "There are 33 units of Paracetamol in stock." },
      ],
      tools_used: ["get_product_stock_and_batches"],
    });

    render(<AiAssistantDrawer isOpen={true} onClose={vi.fn()} />);

    const input = screen.getByPlaceholderText(/Ask about stock/i);
    fireEvent.change(input, { target: { value: "Paracetamol stock?" } });

    const sendBtn = screen.getByRole("button", { name: "Send" });
    fireEvent.click(sendBtn);

    await waitFor(() => {
      expect(screen.getByText("There are 33 units of Paracetamol in stock.")).toBeInTheDocument();
      expect(screen.getByText("get_product_stock_and_batches")).toBeInTheDocument();
    });
  });

  it("calls onClose when close button is clicked", () => {
    const handleClose = vi.fn();
    render(<AiAssistantDrawer isOpen={true} onClose={handleClose} />);

    const closeBtn = screen.getByLabelText("Close assistant panel");
    fireEvent.click(closeBtn);

    expect(handleClose).toHaveBeenCalledOnce();
  });

  it("displays error message when API call fails", async () => {
    (aiClient.sendAiChatMessage as unknown as ReturnType<typeof vi.fn>).mockRejectedValueOnce(
      new Error("API timeout error")
    );

    render(<AiAssistantDrawer isOpen={true} onClose={vi.fn()} />);

    const input = screen.getByPlaceholderText(/Ask about stock/i);
    fireEvent.change(input, { target: { value: "Trigger error" } });

    const sendBtn = screen.getByRole("button", { name: "Send" });
    fireEvent.click(sendBtn);

    await waitFor(() => {
      expect(screen.getByText("API timeout error")).toBeInTheDocument();
    });
  });
});
