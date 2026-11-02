from __future__ import annotations

import uuid

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.database import get_db
from app.core.responses import paginated_meta, success_response
from app.schemas.products import ProductCreate, ProductResponse, ProductUpdate
from app.services import product_service

router = APIRouter(prefix="/products", tags=["Products"])


@router.get(
    "",
    summary="List & Search Products",
    description="List and search products with pagination, category filtering, and total stock calculations.",
    status_code=status.HTTP_200_OK,
)
def list_products(
    query: str | None = Query(None, description="Search by name, SKU code, or barcode"),
    category: str | None = Query(None, description="Filter by category (Medicine, Surgical, Cosmetic, Baby, Food)"),
    is_active: bool | None = Query(None, description="Filter by active status"),
    page: int = Query(1, ge=1, description="Page number"),
    limit: int = Query(settings.DEFAULT_PAGE_SIZE, ge=1, le=settings.MAX_PAGE_SIZE, description="Items per page"),
    db: Session = Depends(get_db),
) -> dict:
    items, total = product_service.get_all_products(
        db,
        query=query,
        category=category,
        is_active=is_active,
        page=page,
        limit=limit,
    )

    validated_items = [ProductResponse(**item).model_dump(mode="json") for item in items]
    meta = paginated_meta(page=page, limit=limit, total=total)

    return success_response(
        data=validated_items,
        message="Products retrieved successfully",
        meta=meta,
    )


@router.post(
    "",
    summary="Create Product",
    description="Create a new product catalog item in the pharmacy inventory.",
    status_code=status.HTTP_201_CREATED,
)
def create_product(payload: ProductCreate, db: Session = Depends(get_db)) -> dict:
    created = product_service.create_product(db, payload.model_dump())
    validated = ProductResponse(**created).model_dump(mode="json")

    return success_response(
        data=validated,
        message="Product created successfully",
        status_code=status.HTTP_201_CREATED,
    )


@router.get(
    "/{id}",
    summary="Get Product Profile",
    description="Get detailed product profile by unique ID including total stock across all active batches.",
    status_code=status.HTTP_200_OK,
)
def get_product(id: uuid.UUID, db: Session = Depends(get_db)) -> dict:
    product = product_service.get_product_by_id(db, id)
    validated = ProductResponse(**product).model_dump(mode="json")

    return success_response(
        data=validated,
        message="Product retrieved successfully",
    )


@router.put(
    "/{id}",
    summary="Update Product",
    description="Update product attributes, prices, reorder levels, or active status.",
    status_code=status.HTTP_200_OK,
)
def update_product(id: uuid.UUID, payload: ProductUpdate, db: Session = Depends(get_db)) -> dict:
    updated = product_service.update_product(db, id, payload.model_dump(exclude_unset=True))
    validated = ProductResponse(**updated).model_dump(mode="json")

    return success_response(
        data=validated,
        message="Product updated successfully",
    )
