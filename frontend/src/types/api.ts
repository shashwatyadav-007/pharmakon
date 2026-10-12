// API Envelope and Common Types matching backend/app/core/responses.py

export interface PaginationMeta {
  page: number;
  limit: number;
  total: number;
}

export interface ApiSuccessResponse<T> {
  success: true;
  data: T;
  message: string;
  meta?: PaginationMeta | null;
}

export interface ApiErrorDetail {
  field?: string;
  issue?: string;
  [key: string]: unknown;
}

export interface ApiErrorPayload {
  code: string;
  message: string;
  details?: string[] | ApiErrorDetail[];
}

export interface ApiErrorResponse {
  success: false;
  error: ApiErrorPayload;
}

export type ApiResponse<T> = ApiSuccessResponse<T> | ApiErrorResponse;

// Auth domain
export interface UserSummary {
  username: string;
  role: string;
}

export interface LoginData {
  access_token: string;
  token_type: string;
  expires_in: number;
  user: UserSummary;
}

// Product domain
export type ProductCategory = "Medicine" | "Surgical" | "Cosmetic" | "Baby" | "Food";
export type ProductUnit = "Strip" | "Tablet" | "Bottle" | "Box" | "Piece";

export interface Product {
  id: string;
  code: string;
  name: string;
  category: ProductCategory;
  unit: ProductUnit;
  mrp: string; // decimal string from API
  default_purchase_price?: string | null;
  barcode?: string | null;
  reorder_level: number;
  is_active: boolean;
  total_stock: number;
  created_at: string;
  updated_at: string;
}

export interface ProductCreateInput {
  code: string;
  name: string;
  category: ProductCategory;
  unit: ProductUnit;
  mrp: string;
  default_purchase_price?: string | null;
  barcode?: string | null;
  reorder_level?: number;
}

export interface ProductUpdateInput {
  name?: string;
  category?: ProductCategory;
  unit?: ProductUnit;
  mrp?: string;
  default_purchase_price?: string | null;
  barcode?: string | null;
  reorder_level?: number;
  is_active?: boolean;
}

// Inventory & Batches domain
export interface Batch {
  id: string;
  product_id: string;
  product_name: string;
  batch_number: string;
  expiry_date: string;
  purchase_cost: string;
  quantity: number;
  is_active: boolean;
  created_at: string;
}

export interface FEFOBatch {
  batch_id: string;
  batch_number: string;
  expiry_date: string;
  available_quantity: number;
  purchase_cost: string;
}

export interface FEFOProductResponseData {
  product_id: string;
  product_name: string;
  fefo_batches: FEFOBatch[];
}

export interface LowStockAlert {
  product_id: string;
  product_name: string;
  product_code: string;
  reorder_level: number;
  current_stock: number;
}

export interface ExpiryRiskAlert {
  batch_id: string;
  product_id: string;
  product_name: string;
  batch_number: string;
  expiry_date: string;
  quantity: number;
  days_until_expiry: number;
}

export type StockAdjustmentReason = "PHYSICAL_COUNT" | "DAMAGED" | "EXPIRED" | "CORRECTION";

export interface StockAdjustmentInput {
  product_id: string;
  batch_id: string;
  new_quantity: number;
  reason: StockAdjustmentReason;
  notes?: string | null;
}

export interface StockAdjustmentResult {
  id: string;
  product_id: string;
  batch_id: string;
  previous_quantity: number;
  new_quantity: number;
  adjustment_quantity: number;
  reason: StockAdjustmentReason;
  notes?: string | null;
  adjusted_at: string;
}

// Supplier domain
export interface Supplier {
  id: string;
  name: string;
  contact_person?: string | null;
  phone: string;
  email?: string | null;
  address?: string | null;
  pan_vat_number?: string | null;
  is_active: boolean;
  created_at: string;
  updated_at: string;
}

export interface SupplierCreateInput {
  name: string;
  contact_person?: string | null;
  phone: string;
  email?: string | null;
  address?: string | null;
  pan_vat_number?: string | null;
}
