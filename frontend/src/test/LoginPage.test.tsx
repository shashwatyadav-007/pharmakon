import { describe, it, expect, vi, beforeEach } from "vitest";
import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import { BrowserRouter } from "react-router-dom";
import { LoginPage } from "../features/auth/LoginPage";
import { AuthProvider } from "../features/auth/AuthContext";
import { api } from "../lib/api/client";

// Mock API module
vi.mock("../lib/api/client", () => {
  return {
    api: {
      auth: {
        login: vi.fn(),
      },
    },
    ApiError: class MockApiError extends Error {
      code: string;
      statusCode: number;
      constructor(code: string, message: string, statusCode: number) {
        super(message);
        this.code = code;
        this.statusCode = statusCode;
      }
    },
  };
});

describe("LoginPage Component", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    localStorage.clear();
  });

  it("renders login form with default credentials", () => {
    render(
      <BrowserRouter>
        <AuthProvider>
          <LoginPage />
        </AuthProvider>
      </BrowserRouter>
    );

    expect(screen.getByLabelText(/username/i)).toHaveValue("admin");
    expect(screen.getByLabelText(/password/i)).toHaveValue("SecurePassword123!");
    expect(screen.getByRole("button", { name: /sign in/i })).toBeInTheDocument();
  });

  it("displays error message on invalid credentials", async () => {
    const { ApiError } = await import("../lib/api/client");
    (api.auth.login as unknown as ReturnType<typeof vi.fn>).mockRejectedValueOnce(
      new ApiError("INVALID_CREDENTIALS", "Invalid username or password", 401)
    );

    render(
      <BrowserRouter>
        <AuthProvider>
          <LoginPage />
        </AuthProvider>
      </BrowserRouter>
    );

    const submitBtn = screen.getByRole("button", { name: /sign in/i });
    fireEvent.click(submitBtn);

    await waitFor(() => {
      expect(screen.getByText(/Invalid username or password/i)).toBeInTheDocument();
    });
  });

  it("disables submit button and shows loading state during submission", async () => {
    (api.auth.login as unknown as ReturnType<typeof vi.fn>).mockImplementationOnce(
      () => new Promise((resolve) => setTimeout(resolve, 100))
    );

    render(
      <BrowserRouter>
        <AuthProvider>
          <LoginPage />
        </AuthProvider>
      </BrowserRouter>
    );

    const submitBtn = screen.getByRole("button", { name: /sign in/i });
    fireEvent.click(submitBtn);

    expect(submitBtn).toBeDisabled();
    expect(submitBtn).toHaveTextContent(/signing in.../i);
  });
});
