from __future__ import annotations

from typing import Any
from fastapi import Request
from fastapi.responses import JSONResponse

class AppError(Exception):
    def __init__(self, code: str, message: str, status_code: int = 400, details: list[str] | None = None):
        super().__init__(message)
        self.code = code
        self.message = message
        self.status_code = status_code
        self.details = details or []

def success_response(
    data: Any, 
    message: str = "Operation completed successfully", 
    meta: dict[str, Any] | None = None, 
    status_code: int = 200
) -> dict[str, Any]:
    return {
        "success": True,
        "data": data,
        "message": message,
        "meta": meta
    }

def error_response(code: str, message: str, details: list[str] | None = None) -> dict[str, Any]:
    return {
        "success": False,
        "error": {
            "code": code,
            "message": message,
            "details": details or []
        }
    }

def paginated_meta(page: int, limit: int, total: int) -> dict[str, int]:
    return {
        "page": page,
        "limit": limit,
        "total": total
    }

async def app_error_handler(request: Request, exc: AppError) -> JSONResponse:
    content = error_response(code=exc.code, message=exc.message, details=exc.details)
    return JSONResponse(status_code=exc.status_code, content=content)
