from __future__ import annotations

from fastapi import APIRouter, status

from app.core.responses import AppError, success_response
from app.schemas.auth import LoginData, LoginRequest, UserSummary

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post(
    "/login",
    summary="Authenticate Pharmacy User",
    description="Authenticate the single pharmacy operational system user and obtain an access token.",
    status_code=status.HTTP_200_OK,
)
def login(payload: LoginRequest) -> dict:
    # Single-user operational login for PharmaKon MVP
    if payload.username == "admin" and payload.password == "SecurePassword123!":
        login_data = LoginData(
            access_token="mock_access_token_pharmakon_admin_2026",
            token_type="bearer",
            expires_in=86400,
            user=UserSummary(
                username="admin",
                role="Pharmacy System User",
            ),
        )
        return success_response(
            data=login_data.model_dump(),
            message="User authenticated successfully",
        )

    raise AppError(
        code="INVALID_CREDENTIALS",
        message="Invalid username or password",
        status_code=status.HTTP_401_UNAUTHORIZED,
    )
