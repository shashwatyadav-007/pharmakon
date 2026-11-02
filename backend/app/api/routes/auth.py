from __future__ import annotations

from fastapi import APIRouter, Depends, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.core.responses import AppError, success_response
from app.schemas.auth import LoginData, LoginRequest, UserSummary

router = APIRouter(prefix="/auth", tags=["Authentication"])

security = HTTPBearer(auto_error=False)


def get_current_user(
    credentials: HTTPAuthorizationCredentials | None = Depends(security),
) -> UserSummary:
    """Validate Bearer access token for operational user.
    
    Preserves single-user operational model (ROLE-001) using token issued by /auth/login.
    """
    if not credentials or not credentials.credentials:
        raise AppError(
            code="UNAUTHORIZED",
            message="Authentication required. Please provide a valid Bearer token.",
            status_code=status.HTTP_401_UNAUTHORIZED,
        )

    token = credentials.credentials
    # Validates operational token issued by login endpoint
    if token == "mock_access_token_pharmakon_admin_2026":
        return UserSummary(
            username="admin",
            role="Pharmacy System User",
        )

    raise AppError(
        code="INVALID_TOKEN",
        message="Invalid or expired access token.",
        status_code=status.HTTP_401_UNAUTHORIZED,
    )


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
