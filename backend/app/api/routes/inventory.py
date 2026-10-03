from __future__ import annotations

import uuid
from datetime import date

from fastapi import APIRouter, Query, status

from app.core.config import settings
from app.core.responses import paginated_meta, success_response
from app.schemas.inventory import (
    BatchResponse,
    ExpiryRiskAlert,
    FEFOProductResponse,
    LowStockAlert,
    StockAdjustmentCreate,
    StockAdjustmentResponse,
)
from app.services import inventory_service

router = APIRouter(prefix="/inventory", tags=["Inventory & Batches"])


@router.get(
    "/batches",
    summary="List Batches",
    description="List batches, optionally filtered by product, upcoming expiry date, or low stock condition.",
    status_code=status.HTTP_200_OK,
)
def list_batches(
    product_id: uuid.UUID | None = Query(None, description="Filter by product ID"),
    expiry_before: date | None = Query(None, description="Filter batches expiring before date (YYYY-MM-DD)"),
    low_stock: bool | None = Query(None, description="Filter batches with low stock (<= 10 units)"),
    page: int = Query(1, ge=1, description="Page number"),
    limit: int = Query(settings.DEFAULT_PAGE_SIZE, ge=1, le=settings.MAX_PAGE_SIZE, description="Items per page"),
) -> dict:
    items, total = inventory_service.get_all_batches(
        product_id=product_id,
        expiry_before=expiry_before,
        low_stock=low_stock,
        page=page,
        limit=limit,
    )

    validated_items = [BatchResponse(**item).model_dump(mode="json") for item in items]
    meta = paginated_meta(page=page, limit=limit, total=total)

    return success_response(
        data=validated_items,
        message="Batches retrieved successfully",
        meta=meta,
    )


@router.get(
    "/fefo/{product_id}",
    summary="Get FEFO Batches for Product",
    description="Retrieve available in-stock batches for a product ordered strictly by First Expiry, First Out (FEFO).",
    status_code=status.HTTP_200_OK,
)
def get_fefo_batches(product_id: uuid.UUID) -> dict:
    result = inventory_service.get_fefo_batches(product_id)
    validated = FEFOProductResponse(**result).model_dump(mode="json")

    return success_response(
        data=validated,
        message="FEFO ordered batches retrieved successfully",
    )


@router.get(
    "/alerts/low-stock",
    summary="Low Stock Alerts",
    description="Fetch all products whose combined stock across all active batches is less than or equal to their reorder level.",
    status_code=status.HTTP_200_OK,
)
def get_low_stock_alerts() -> dict:
    alerts = inventory_service.get_low_stock_alerts()
    validated = [LowStockAlert(**alert).model_dump(mode="json") for alert in alerts]

    return success_response(
        data=validated,
        message="Low stock alerts retrieved successfully",
    )


@router.get(
    "/alerts/expiry-risk",
    summary="Expiry Risk Alerts",
    description="Fetch inventory batches expiring within the configured threshold (default 60 days).",
    status_code=status.HTTP_200_OK,
)
def get_expiry_risk_alerts(
    days: int = Query(settings.EXPIRY_ALERT_DAYS, ge=1, le=365, description="Days threshold for expiry risk"),
) -> dict:
    alerts = inventory_service.get_expiry_risk_alerts(days_threshold=days)
    validated = [ExpiryRiskAlert(**alert).model_dump(mode="json") for alert in alerts]

    return success_response(
        data=validated,
        message="Expiry risk alerts retrieved successfully",
    )


@router.post(
    "/adjustments",
    summary="Record Stock Adjustment",
    description="Record physical stock count adjustments and generate immutable stock movement logs.",
    status_code=status.HTTP_201_CREATED,
)
def create_stock_adjustment(payload: StockAdjustmentCreate) -> dict:
    adjustment = inventory_service.create_stock_adjustment(payload.model_dump())
    validated = StockAdjustmentResponse(**adjustment).model_dump(mode="json")

    return success_response(
        data=validated,
        message="Stock adjustment recorded successfully",
        status_code=status.HTTP_201_CREATED,
    )
