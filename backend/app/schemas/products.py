from pydantic import BaseModel, Field
from decimal import Decimal
from uuid import UUID
from datetime import datetime
from typing import Optional, Literal

class ProductCreate(BaseModel):
    code: str = Field(..., max_length=50)
    name: str = Field(..., max_length=255)
    category: Literal["Medicine", "Surgical", "Cosmetic", "Baby", "Food"]
    unit: Literal["Strip", "Tablet", "Bottle", "Box", "Piece"]
    mrp: Decimal = Field(..., ge=0, max_digits=10, decimal_places=2)
    default_purchase_price: Optional[Decimal] = Field(None, ge=0)
    barcode: Optional[str] = Field(None, max_length=100)
    reorder_level: int = Field(10, ge=0)

class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=255)
    category: Optional[Literal["Medicine", "Surgical", "Cosmetic", "Baby", "Food"]] = None
    unit: Optional[Literal["Strip", "Tablet", "Bottle", "Box", "Piece"]] = None
    mrp: Optional[Decimal] = Field(None, ge=0, max_digits=10, decimal_places=2)
    default_purchase_price: Optional[Decimal] = Field(None, ge=0)
    barcode: Optional[str] = Field(None, max_length=100)
    reorder_level: Optional[int] = Field(None, ge=0)
    is_active: Optional[bool] = None

class ProductResponse(BaseModel):
    id: UUID
    code: str
    name: str
    category: str
    unit: str
    mrp: Decimal
    default_purchase_price: Optional[Decimal]
    barcode: Optional[str]
    reorder_level: int
    is_active: bool
    total_stock: int
    created_at: datetime
    updated_at: datetime
