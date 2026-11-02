from __future__ import annotations

from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    username: str = Field(
        ...,
        description="Pharmacy user username",
        json_schema_extra={"example": "admin"},
    )
    password: str = Field(
        ...,
        description="Pharmacy user password",
        json_schema_extra={"example": "SecurePassword123!"},
    )


class UserSummary(BaseModel):
    username: str
    role: str


class LoginData(BaseModel):
    access_token: str
    token_type: str
    expires_in: int
    user: UserSummary


class LoginResponse(BaseModel):
    success: bool = True
    data: LoginData
    message: str = "Authentication successful"
