from __future__ import annotations

from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI, HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.api.routes.auth import router as auth_router
from app.api.routes.inventory import router as inventory_router
from app.api.routes.products import router as products_router
from app.api.routes.suppliers import router as suppliers_router
from app.core.config import settings
from app.core.responses import AppError, app_error_handler, error_response, success_response
from app.services.data_store import seed_sample_data


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager that runs startup and shutdown tasks."""
    # Pre-populate sample in-memory data for development and testing
    seed_sample_data()
    yield


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=(
        "PharmaKon is a clean, modern pharmacy management and analytics backend API. "
        "Built with FastAPI to support retail pharmacy inventory, FEFO batch selection, "
        "supplier purchasing, and point-of-sale operations."
    ),
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    lifespan=lifespan,
)

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register Custom Exception Handlers for standard error envelope
app.add_exception_handler(AppError, app_error_handler)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
    """Format FastAPI/Pydantic validation errors into the standard API error envelope."""
    details = []
    for err in exc.errors():
        location = " -> ".join(str(loc) for loc in err.get("loc", []))
        details.append(f"{location}: {err.get('msg', 'Validation error')}")

    content = error_response(
        code="VALIDATION_ERROR",
        message="Request validation failed. Please check your payload parameters.",
        details=details,
    )
    return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content=content)


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
    """Format HTTPExceptions into the standard API error envelope."""
    content = error_response(
        code="HTTP_ERROR",
        message=str(exc.detail),
    )
    return JSONResponse(status_code=exc.status_code, content=content)


# Health Check & Root Endpoints
@app.get(
    "/",
    summary="Root",
    description="Welcome endpoint with API metadata and documentation links.",
    tags=["System"],
)
def root() -> dict[str, Any]:
    return success_response(
        data={
            "app_name": settings.APP_NAME,
            "version": settings.APP_VERSION,
            "docs": "/docs",
            "redoc": "/redoc",
            "api_prefix": settings.API_V1_PREFIX,
        },
        message="Welcome to PharmaKon Pharmacy Management API",
    )


@app.get(
    "/health",
    summary="Health Check",
    description="Liveness probe returning application health status.",
    tags=["System"],
)
def health_check() -> dict[str, Any]:
    return success_response(
        data={"status": "healthy"},
        message="PharmaKon API is running smoothly",
    )


# Register Domain Routers under /api/v1
app.include_router(auth_router, prefix=settings.API_V1_PREFIX)
app.include_router(products_router, prefix=settings.API_V1_PREFIX)
app.include_router(inventory_router, prefix=settings.API_V1_PREFIX)
app.include_router(suppliers_router, prefix=settings.API_V1_PREFIX)
