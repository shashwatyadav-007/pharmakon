from __future__ import annotations

from datetime import date, datetime
from decimal import Decimal
from typing import Literal, Optional
from uuid import UUID

from pydantic import BaseModel, Field


class BatchResponse(BaseModel):
    id: UUID
    product_id: UUID
    product_name: str
    product_code: str = ""
    category: str = "Medicine"
    unit: str = "Piece"
    batch_number: str
    expiry_date: date
    days_until_expiry: int = 0
    purchase_cost: Decimal
    quantity: int
    is_active: bool
    created_at: datetime


class FEFOBatchResponse(BaseModel):
    batch_id: UUID
    batch_number: str
    unit: str = "Piece"
    expiry_date: date
    days_until_expiry: int = 0
    available_quantity: int
    purchase_cost: Decimal


class FEFOProductResponse(BaseModel):
    product_id: UUID
    product_name: str
    product_code: str = ""
    category: str = "Medicine"
    unit: str = "Piece"
    reorder_level: int = 10
    total_stock: int = 0
    mrp: Decimal = Decimal("0.00")
    fefo_batches: list[FEFOBatchResponse]


class StockAdjustmentCreate(BaseModel):
    product_id: UUID
    batch_id: UUID
    new_quantity: int = Field(..., ge=0)
    reason: Literal["PHYSICAL_COUNT", "DAMAGED", "EXPIRED", "CORRECTION"]
    notes: Optional[str] = None


class StockAdjustmentResponse(BaseModel):
    id: UUID
    product_id: UUID
    batch_id: UUID
    previous_quantity: int
    new_quantity: int
    adjustment_quantity: int
    reason: str
    notes: Optional[str]
    adjusted_at: datetime


class StockAdjustmentHistoryItem(BaseModel):
    id: UUID
    product_id: UUID
    product_name: str
    product_code: str
    batch_id: UUID
    batch_number: str
    previous_quantity: int
    new_quantity: int
    adjustment_quantity: int
    reason: str
    notes: Optional[str] = None
    adjusted_at: datetime


class LowStockAlert(BaseModel):
    product_id: UUID
    product_name: str
    product_code: str
    category: str = "Medicine"
    unit: str = "Piece"
    reorder_level: int
    current_stock: int
    shortfall: int = 0
    urgency: str = "LOW"


class ExpiryRiskAlert(BaseModel):
    batch_id: UUID
    product_id: UUID
    product_name: str
    product_code: str = ""
    unit: str = "Piece"
    batch_number: str
    expiry_date: date
    quantity: int
    days_until_expiry: int
    urgency: str = "CRITICAL"
