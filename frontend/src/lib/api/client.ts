
import type {
  ApiErrorResponse,
  ApiSuccessResponse,
  Batch,
  ExpiryRiskAlert,
  FEFOProductResponseData,
  LoginData,
  LowStockAlert,
  Product,
  ProductCreateInput,
  ProductUpdateInput,
  StockAdjustmentInput,
  StockAdjustmentResult,
  StockAdjustmentHistoryItem,
  Supplier,
  SupplierCreateInput,
} from "../../types/api";

const API_BASE_URL =
  (import.meta.env.VITE_API_BASE_URL as string | undefined) ||
  "http://127.0.0.1:8000/api/v1";

export class ApiError extends Error {
  readonly status: number;
  readonly code: string;
  readonly details: unknown;

  constructor(
    message: string,
    status: number,
    code = "API_ERROR",
    details: unknown = [],
  ) {
    super(message);
    this.name = "ApiError";
    this.status = status;
    this.code = code;
    this.details = details;
  }
}

type PaginationMeta = {
  page: number;
  limit: number;
  total: number;
};

type ListResult<T> = {
  data: T[];
  message: string;
  meta?: PaginationMeta | null;
};

type ListParams = {
  page?: number;
  limit?: number;
};

type ProductListParams = ListParams & {
  query?: string;
  category?: string;
  is_active?: boolean;
};

type BatchListParams = ListParams & {
  product_id?: string;
  expiry_before?: string;
  low_stock?: boolean;
  search?: string;
};

async function request<T>(
  path: string,
  options: RequestInit = {},
): Promise<ApiSuccessResponse<T>> {
  const token = localStorage.getItem("pharmakon_token");

  const headers = new Headers(options.headers);
  headers.set("Accept", "application/json");

  if (options.body !== undefined) {
    headers.set("Content-Type", "application/json");
  }

  if (token) {
    headers.set("Authorization", `Bearer ${token}`);
  }

  let response: Response;

  try {
    response = await fetch(`${API_BASE_URL}${path}`, {
      ...options,
      headers,
    });
  } catch {
    throw new ApiError(
      "Cannot connect to PharmaKon API. Check that the backend is running.",
      0,
      "NETWORK_ERROR",
    );
  }

  const body: unknown = await response.json().catch(() => null);

  if (
    !response.ok ||
    !body ||
    typeof body !== "object" ||
    !("success" in body) ||
    body.success !== true
  ) {
    const envelope = body as ApiErrorResponse | null;

    if (envelope?.success === false && envelope.error) {
      throw new ApiError(
        envelope.error.message,
        response.status,
        envelope.error.code,
        envelope.error.details,
      );
    }

    const fallback =
      body &&
      typeof body === "object" &&
      "detail" in body &&
      typeof body.detail === "string"
        ? body.detail
        : `Request failed with status ${response.status}`;

    throw new ApiError(fallback, response.status);
  }

  return body as ApiSuccessResponse<T>;
}

function queryString(
  params: Record<string, string | number | boolean | undefined>,
): string {
  const search = new URLSearchParams();

  for (const [key, value] of Object.entries(params)) {
    if (value !== undefined) {
      search.set(key, String(value));
    }
  }

  const result = search.toString();
  return result ? `?${result}` : "";
}

function listResult<T>(
  response: ApiSuccessResponse<T[]>,
): ListResult<T> {
  return {
    data: response.data,
    message: response.message,
    meta: response.meta,
  };
}

export const api = {
  auth: {
    async login(username: string, password: string): Promise<LoginData> {
      const response = await request<LoginData>("/auth/login", {
        method: "POST",
        body: JSON.stringify({ username, password }),
      });

      return response.data;
    },
  },

  products: {
    async list(params: ProductListParams = {}): Promise<ListResult<Product>> {
      const response = await request<Product[]>(
        `/products${queryString(params)}`,
      );

      return listResult(response);
    },

    async create(input: ProductCreateInput): Promise<Product> {
      const response = await request<Product>("/products", {
        method: "POST",
        body: JSON.stringify(input),
      });

      return response.data;
    },

    async update(
      id: string,
      input: ProductUpdateInput,
    ): Promise<Product> {
      const response = await request<Product>(
        `/products/${encodeURIComponent(id)}`,
        {
          method: "PUT",
          body: JSON.stringify(input),
        },
      );

      return response.data;
    },
  },

  suppliers: {
    async list(params: ListParams = {}): Promise<ListResult<Supplier>> {
      const response = await request<Supplier[]>(
        `/suppliers${queryString(params)}`,
      );

      return listResult(response);
    },

    async create(input: SupplierCreateInput): Promise<Supplier> {
      const response = await request<Supplier>("/suppliers", {
        method: "POST",
        body: JSON.stringify(input),
      });

      return response.data;
    },
  },

  inventory: {
    async listBatches(params: BatchListParams = {}): Promise<ListResult<Batch>> {
      const response = await request<Batch[]>(
        `/inventory/batches${queryString(params)}`,
      );

      return listResult(response);
    },

    async getFEFO(productId: string): Promise<FEFOProductResponseData> {
      const response = await request<FEFOProductResponseData>(
        `/inventory/fefo/${encodeURIComponent(productId)}`,
      );

      return response.data;
    },

    async getLowStockAlerts(): Promise<LowStockAlert[]> {
      const response = await request<LowStockAlert[]>(
        "/inventory/alerts/low-stock",
      );

      return response.data;
    },

    async getExpiryRiskAlerts(days = 60): Promise<ExpiryRiskAlert[]> {
      const response = await request<ExpiryRiskAlert[]>(
        `/inventory/alerts/expiry-risk${queryString({ days })}`,
      );

      return response.data;
    },

    async listAdjustments(limit = 20): Promise<StockAdjustmentHistoryItem[]> {
      const response = await request<StockAdjustmentHistoryItem[]>(
        `/inventory/adjustments${queryString({ limit })}`,
      );
      return response.data;
    },

    async recordAdjustment(
      input: StockAdjustmentInput,
    ): Promise<StockAdjustmentResult> {
      const response = await request<StockAdjustmentResult>(
        "/inventory/adjustments",
        {
          method: "POST",
          body: JSON.stringify(input),
        },
      );

      return response.data;
    },
  },
};
