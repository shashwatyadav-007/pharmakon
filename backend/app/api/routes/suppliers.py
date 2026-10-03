from __future__ import annotations

from fastapi import APIRouter, Query, status

from app.core.config import settings
from app.core.responses import paginated_meta, success_response
from app.schemas.suppliers import SupplierCreate, SupplierResponse
from app.services import supplier_service

router = APIRouter(prefix="/suppliers", tags=["Suppliers"])


@router.get(
    "",
    summary="List Suppliers",
    description="List registered pharmacy medicine suppliers and distributors with pagination.",
    status_code=status.HTTP_200_OK,
)
def list_suppliers(
    page: int = Query(1, ge=1, description="Page number"),
    limit: int = Query(settings.DEFAULT_PAGE_SIZE, ge=1, le=settings.MAX_PAGE_SIZE, description="Items per page"),
) -> dict:
    items, total = supplier_service.get_all_suppliers(page=page, limit=limit)
    validated_items = [SupplierResponse(**item).model_dump(mode="json") for item in items]
    meta = paginated_meta(page=page, limit=limit, total=total)

    return success_response(
        data=validated_items,
        message="Suppliers retrieved successfully",
        meta=meta,
    )


@router.post(
    "",
    summary="Create Supplier",
    description="Register a new medicine wholesaler/supplier record.",
    status_code=status.HTTP_201_CREATED,
)
def create_supplier(payload: SupplierCreate) -> dict:
    created = supplier_service.create_supplier(payload.model_dump())
    validated = SupplierResponse(**created).model_dump(mode="json")

    return success_response(
        data=validated,
        message="Supplier registered successfully",
        status_code=status.HTTP_201_CREATED,
    )
