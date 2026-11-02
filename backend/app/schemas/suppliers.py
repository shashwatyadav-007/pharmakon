from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime
from typing import Optional

class SupplierCreate(BaseModel):
    name: str = Field(..., max_length=255)
    contact_person: Optional[str] = Field(None, max_length=100)
    phone: str = Field(..., max_length=20)
    email: Optional[str] = Field(None, max_length=100)
    address: Optional[str] = None
    pan_vat_number: Optional[str] = Field(None, max_length=50)

class SupplierResponse(BaseModel):
    id: UUID
    name: str
    contact_person: Optional[str]
    phone: str
    email: Optional[str]
    address: Optional[str]
    pan_vat_number: Optional[str]
    is_active: bool
    created_at: datetime
    updated_at: datetime
