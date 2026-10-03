from __future__ import annotations

from pydantic import BaseModel, Field
from decimal import Decimal
from uuid import UUID
from datetime import datetime, date
from typing import Optional, Literal

class BatchResponse(BaseModel):
    id: UUID
    product_id: UUID
    product_name: str
    batch_number: str
    expiry_date: date
    purchase_cost: Decimal
    quantity: int
    is_active: bool
    created_at: datetime

class FEFOBatchResponse(BaseModel):
    batch_id: UUID
    batch_number: str
    expiry_date: date
    available_quantity: int
    purchase_cost: Decimal

class FEFOProductResponse(BaseModel):
    product_id: UUID
    product_name: str
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

class LowStockAlert(BaseModel):
    product_id: UUID
    product_name: str
    product_code: str
    reorder_level: int
    current_stock: int

class ExpiryRiskAlert(BaseModel):
    batch_id: UUID
    product_id: UUID
    product_name: str
    batch_number: str
    expiry_date: date
    quantity: int
    days_until_expiry: int
