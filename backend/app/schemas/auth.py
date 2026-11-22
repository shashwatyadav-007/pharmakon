from __future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    username: str = Field(
        ...,
        description="Pharmacy user username or email",
        json_schema_extra={"example": "admin"},
    )
    password: str = Field(
        ...,
        description="Pharmacy user password",
        json_schema_extra={"example": "SecurePassword123!"},
    )


class UserSummary(BaseModel):
    id: Optional[str] = None
    username: str
    email: Optional[str] = None
    role: str = "Pharmacy System User"
    full_name: Optional[str] = None


class LoginData(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int
    user: UserSummary


class LoginResponse(BaseModel):
    success: bool = True
    data: LoginData
    message: str = "Authentication successful"
