from __future__ import annotations

import uuid
from datetime import date, datetime, timezone

from sqlalchemy import func, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.responses import AppError
from app.models.inventory import Batch
from app.models.product import Product


def _product_to_dict(product: Product, total_stock: int) -> dict:
    """Convert a Product ORM row to a plain dict matching existing API shape."""
    return {
        "id": product.id,
        "code": product.code,
        "name": product.name,
        "category": product.category,
        "unit": product.unit,
        "mrp": product.mrp,
        "default_purchase_price": product.default_purchase_price,
        "barcode": product.barcode,
        "reorder_level": product.reorder_level,
        "is_active": product.is_active,
        "total_stock": total_stock,
        "created_at": product.created_at,
        "updated_at": product.updated_at,
    }


def _stock_subquery(db: Session, product_id: uuid.UUID) -> int:
    """Return total active, unexpired batch quantity for a single product."""
    today = date.today()
    result = db.execute(
        select(func.coalesce(func.sum(Batch.quantity), 0)).where(
            Batch.product_id == product_id,
            Batch.is_active.is_(True),
            Batch.expiry_date >= today,
        )
    ).scalar()
    return int(result or 0)


def get_all_products(
    db: Session,
    query: str | None = None,
    category: str | None = None,
    is_active: bool | None = None,
    page: int = 1,
    limit: int = 20,
) -> tuple[list[dict], int]:
    """List products with optional filtering and pagination using a single efficient SQL query."""
    today = date.today()
    stock_sub = (
        select(
            Batch.product_id,
            func.coalesce(func.sum(Batch.quantity), 0).label("total_stock"),
        )
        .where(
            Batch.is_active.is_(True),
            Batch.expiry_date >= today,
        )
        .group_by(Batch.product_id)
        .subquery()
    )

    base_stmt = select(
        Product,
        func.coalesce(stock_sub.c.total_stock, 0).label("total_stock"),
    ).outerjoin(stock_sub, Product.id == stock_sub.c.product_id)

    if query:
        q = f"%{query.lower()}%"
        base_stmt = base_stmt.where(
            func.lower(Product.name).like(q)
            | func.lower(Product.code).like(q)
            | func.lower(func.coalesce(Product.barcode, "")).like(q)
        )

    if category:
        base_stmt = base_stmt.where(Product.category == category)

    if is_active is not None:
        base_stmt = base_stmt.where(Product.is_active.is_(is_active))

    # Count total before pagination
    count_stmt = select(func.count()).select_from(base_stmt.subquery())
    total_count = db.execute(count_stmt).scalar() or 0

    # Order and apply pagination
    base_stmt = (
        base_stmt.order_by(Product.name.asc(), Product.code.asc())
        .offset((page - 1) * limit)
        .limit(limit)
    )
    rows = db.execute(base_stmt).all()

    items = [_product_to_dict(p, int(stock)) for p, stock in rows]
    return items, int(total_count)


def get_product_by_id(db: Session, product_id: uuid.UUID) -> dict:
    """Get a single product with total_stock calculated."""
    product = db.get(Product, product_id)
    if product is None:
        raise AppError(
            code="PRODUCT_NOT_FOUND",
            message="Product not found",
            status_code=404,
        )
    return _product_to_dict(product, _stock_subquery(db, product_id))


def create_product(db: Session, data: dict) -> dict:
    """Create a new product. Product code must be unique."""
    now = datetime.now(timezone.utc)
    product = Product(
        id=uuid.uuid4(),
        code=data["code"],
        name=data["name"],
        category=data["category"],
        unit=data["unit"],
        mrp=data["mrp"],
        default_purchase_price=data.get("default_purchase_price"),
        barcode=data.get("barcode"),
        reorder_level=data.get("reorder_level", 10),
        is_active=True,
        created_at=now,
        updated_at=now,
    )
    db.add(product)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise AppError(
            code="DUPLICATE_CODE",
            message=f"A product with code '{data['code']}' already exists",
            status_code=400,
        )
    db.refresh(product)
    return _product_to_dict(product, 0)


def update_product(db: Session, product_id: uuid.UUID, data: dict) -> dict:
    """Update an existing product. Only provided fields are changed."""
    product = db.get(Product, product_id)
    if product is None:
        raise AppError(
            code="PRODUCT_NOT_FOUND",
            message="Product not found",
            status_code=404,
        )

    updatable = {
        "name", "category", "unit", "mrp", "default_purchase_price",
        "barcode", "reorder_level", "is_active",
    }
    for key, value in data.items():
        if key in updatable and value is not None:
            setattr(product, key, value)

    product.updated_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(product)
    return _product_to_dict(product, _stock_subquery(db, product_id))
