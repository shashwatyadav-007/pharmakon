from __future__ import annotations

import uuid
from datetime import date, datetime, timedelta, timezone
from typing import Any

from sqlalchemy import func, or_, select
from sqlalchemy.orm import Session

from app.core.responses import AppError
from app.models.inventory import Batch, StockAdjustment, StockMovementLog
from app.models.product import Product


def _batch_to_dict(
    batch: Batch,
    product_name: str,
    product_code: str,
    category: str,
    unit: str,
) -> dict[str, Any]:
    """Convert a Batch ORM row to a rich plain dict."""
    today = date.today()
    days_until_expiry = (batch.expiry_date - today).days
    return {
        "id": batch.id,
        "product_id": batch.product_id,
        "product_name": product_name,
        "product_code": product_code,
        "category": category,
        "unit": unit,
        "batch_number": batch.batch_number,
        "expiry_date": batch.expiry_date,
        "days_until_expiry": days_until_expiry,
        "purchase_cost": batch.purchase_cost,
        "quantity": batch.quantity,
        "is_active": batch.is_active,
        "created_at": batch.created_at,
    }


def get_all_batches(
    db: Session,
    product_id: uuid.UUID | None = None,
    expiry_before: date | None = None,
    low_stock: bool | None = None,
    search: str | None = None,
    page: int = 1,
    limit: int = 20,
) -> tuple[list[dict[str, Any]], int]:
    """List batches with optional search, filters and pagination."""
    stmt = select(
        Batch,
        Product.name,
        Product.code,
        Product.category,
        Product.unit,
    ).join(Product, Batch.product_id == Product.id)

    if product_id:
        stmt = stmt.where(Batch.product_id == product_id)

    if expiry_before:
        stmt = stmt.where(Batch.expiry_date <= expiry_before)

    if low_stock:
        today = date.today()
        low_stock_prod_sub = (
            select(Batch.product_id)
            .join(Product, Batch.product_id == Product.id)
            .where(
                Batch.is_active.is_(True),
                Product.is_active.is_(True),
                Batch.expiry_date >= today,
            )
            .group_by(Batch.product_id, Product.reorder_level)
            .having(func.sum(Batch.quantity) <= Product.reorder_level)
            .scalar_subquery()
        )
        stmt = stmt.where(Batch.product_id.in_(low_stock_prod_sub))

    if search and search.strip():
        s = search.strip().lower()
        stmt = stmt.where(
            or_(
                func.lower(Product.name).like(f"%{s}%"),
                func.lower(Product.code).like(f"%{s}%"),
                func.lower(Batch.batch_number).like(f"%{s}%"),
            )
        )

    count_stmt = select(func.count()).select_from(stmt.subquery())
    total_count = db.execute(count_stmt).scalar() or 0

    # Sort in First Expiry order (FEFO) by default for inventory integrity
    stmt = (
        stmt.order_by(Batch.expiry_date.asc(), Batch.batch_number.asc())
        .offset((page - 1) * limit)
        .limit(limit)
    )
    rows = db.execute(stmt).all()

    items = [
        _batch_to_dict(batch, product_name, product_code, category, unit)
        for batch, product_name, product_code, category, unit in rows
    ]
    return items, int(total_count)


def get_fefo_batches(db: Session, product_id: uuid.UUID) -> dict[str, Any]:
    """Retrieve batches ordered strictly by First Expiry, First Out (FEFO) with full product context."""
    product = db.get(Product, product_id)
    if product is None:
        raise AppError(
            code="PRODUCT_NOT_FOUND",
            message="Product not found",
            status_code=404,
        )

    today = date.today()
    stmt = (
        select(Batch)
        .where(
            Batch.product_id == product_id,
            Batch.is_active.is_(True),
            Batch.quantity > 0,
            Batch.expiry_date >= today,
        )
        .order_by(Batch.expiry_date.asc(), Batch.id.asc())
    )
    batches = db.execute(stmt).scalars().all()

    fefo_batches = [
        {
            "batch_id": b.id,
            "batch_number": b.batch_number,
            "unit": product.unit,
            "expiry_date": b.expiry_date,
            "days_until_expiry": (b.expiry_date - today).days,
            "available_quantity": b.quantity,
            "purchase_cost": b.purchase_cost,
        }
        for b in batches
    ]

    total_stock = sum(b.quantity for b in batches)

    return {
        "product_id": product_id,
        "product_name": product.name,
        "product_code": product.code,
        "category": product.category,
        "unit": product.unit,
        "reorder_level": product.reorder_level,
        "total_stock": total_stock,
        "mrp": product.mrp,
        "fefo_batches": fefo_batches,
    }


def get_low_stock_alerts(db: Session) -> list[dict[str, Any]]:
    """Fetch all active products where combined stock across active, unexpired batches is <= reorder_level,
    strictly ordered by urgency (lowest stock first)."""
    today = date.today()
    # Subquery: total active, unexpired batch quantity per product
    stock_sub = (
        select(Batch.product_id, func.coalesce(func.sum(Batch.quantity), 0).label("total"))
        .where(Batch.is_active.is_(True), Batch.expiry_date >= today)
        .group_by(Batch.product_id)
        .subquery()
    )

    stmt = (
        select(Product, func.coalesce(stock_sub.c.total, 0).label("current_stock"))
        .outerjoin(stock_sub, Product.id == stock_sub.c.product_id)
        .where(
            Product.is_active.is_(True),
            func.coalesce(stock_sub.c.total, 0) <= Product.reorder_level,
        )
        .order_by(
            func.coalesce(stock_sub.c.total, 0).asc(),
            Product.name.asc(),
        )
    )

    rows = db.execute(stmt).all()
    alerts = []
    for product, current_stock in rows:
        stock_val = int(current_stock)
        shortfall = max(0, product.reorder_level - stock_val)
        urgency = "OUT_OF_STOCK" if stock_val == 0 else ("CRITICAL" if stock_val <= 2 else "LOW")
        alerts.append(
            {
                "product_id": product.id,
                "product_name": product.name,
                "product_code": product.code,
                "category": product.category,
                "unit": product.unit,
                "reorder_level": product.reorder_level,
                "current_stock": stock_val,
                "shortfall": shortfall,
                "urgency": urgency,
            }
        )
    return alerts


def get_expiry_risk_alerts(db: Session, days_threshold: int = 60) -> list[dict[str, Any]]:
    """Fetch inventory batches expiring within the configured threshold days, ordered by expiry date."""
    today = date.today()
    cutoff_date = today + timedelta(days=days_threshold)

    stmt = (
        select(Batch, Product.name, Product.code, Product.unit)
        .join(Product, Batch.product_id == Product.id)
        .where(
            Batch.is_active.is_(True),
            Batch.quantity > 0,
            Batch.expiry_date <= cutoff_date,
            Product.is_active.is_(True),
        )
        .order_by(Batch.expiry_date.asc())
    )
    rows = db.execute(stmt).all()

    alerts = []
    for batch, product_name, product_code, product_unit in rows:
        days_until_expiry = (batch.expiry_date - today).days
        if days_until_expiry <= days_threshold:
            if days_until_expiry <= 0:
                urgency = "EXPIRED"
            elif days_until_expiry <= 30:
                urgency = "CRITICAL"
            elif days_until_expiry <= 60:
                urgency = "HIGH"
            elif days_until_expiry <= 90:
                urgency = "MODERATE"
            else:
                urgency = "LOW"

            alerts.append(
                {
                    "batch_id": batch.id,
                    "product_id": batch.product_id,
                    "product_name": product_name,
                    "product_code": product_code,
                    "unit": product_unit,
                    "batch_number": batch.batch_number,
                    "expiry_date": batch.expiry_date,
                    "quantity": batch.quantity,
                    "days_until_expiry": days_until_expiry,
                    "urgency": urgency,
                }
            )
    return alerts


def get_recent_adjustments(db: Session, limit: int = 20) -> list[dict[str, Any]]:
    """Retrieve recent stock adjustment transactions with product and batch details."""
    stmt = (
        select(
            StockAdjustment,
            Product.name.label("product_name"),
            Product.code.label("product_code"),
            Batch.batch_number.label("batch_number"),
        )
        .join(Product, StockAdjustment.product_id == Product.id)
        .join(Batch, StockAdjustment.batch_id == Batch.id)
        .order_by(StockAdjustment.adjusted_at.desc())
        .limit(limit)
    )
    rows = db.execute(stmt).all()

    return [
        {
            "id": adj.id,
            "product_id": adj.product_id,
            "product_name": product_name,
            "product_code": product_code,
            "batch_id": adj.batch_id,
            "batch_number": batch_number,
            "previous_quantity": adj.previous_quantity,
            "new_quantity": adj.new_quantity,
            "adjustment_quantity": adj.adjustment_quantity,
            "reason": adj.reason,
            "notes": adj.notes,
            "adjusted_at": adj.adjusted_at,
        }
        for adj, product_name, product_code, batch_number in rows
    ]


def create_stock_adjustment(db: Session, data: dict[str, Any]) -> dict[str, Any]:
    """Record a physical stock count adjustment atomically."""
    product_id = data["product_id"]
    batch_id = data["batch_id"]
    new_quantity = data["new_quantity"]

    product = db.get(Product, product_id)
    if product is None:
        raise AppError(
            code="PRODUCT_NOT_FOUND",
            message="Product not found",
            status_code=404,
        )

    # Lock the batch row for this transaction
    batch = db.execute(
        select(Batch).where(Batch.id == batch_id).with_for_update()
    ).scalar_one_or_none()

    if batch is None:
        raise AppError(
            code="BATCH_NOT_FOUND",
            message="Batch not found",
            status_code=404,
        )

    if batch.product_id != product_id:
        raise AppError(
            code="INVALID_BATCH_PRODUCT",
            message="Batch does not belong to the specified product",
            status_code=400,
        )

    previous_quantity = batch.quantity
    adjustment_quantity = new_quantity - previous_quantity

    # Update batch quantity
    batch.quantity = new_quantity

    now = datetime.now(timezone.utc)
    adj_id = uuid.uuid4()

    adjustment = StockAdjustment(
        id=adj_id,
        product_id=product_id,
        batch_id=batch_id,
        previous_quantity=previous_quantity,
        new_quantity=new_quantity,
        adjustment_quantity=adjustment_quantity,
        reason=data["reason"],
        notes=data.get("notes"),
        adjusted_at=now,
    )
    db.add(adjustment)

    movement = StockMovementLog(
        id=uuid.uuid4(),
        product_id=product_id,
        batch_id=batch_id,
        movement_type="ADJUSTMENT",
        quantity_delta=adjustment_quantity,
        resulting_quantity=new_quantity,
        reference_id=adj_id,
        created_at=now,
    )
    db.add(movement)

    db.commit()
    db.refresh(adjustment)

    return {
        "id": adjustment.id,
        "product_id": adjustment.product_id,
        "batch_id": adjustment.batch_id,
        "previous_quantity": adjustment.previous_quantity,
        "new_quantity": adjustment.new_quantity,
        "adjustment_quantity": adjustment.adjustment_quantity,
        "reason": adjustment.reason,
        "notes": adjustment.notes,
        "adjusted_at": adjustment.adjusted_at,
    }


def validate_batch_uniqueness(
    db: Session,
    product_id: uuid.UUID,
    batch_number: str,
    expiry_date: date,
) -> None:
    """Enforce UNIQUE(product_id, batch_number, expiry_date) constraint."""
    existing = db.execute(
        select(Batch).where(
            Batch.product_id == product_id,
            Batch.batch_number == batch_number,
            Batch.expiry_date == expiry_date,
        )
    ).scalar_one_or_none()

    if existing is not None:
        raise AppError(
            code="DUPLICATE_BATCH",
            message=f"Batch '{batch_number}' with expiry date {expiry_date} already exists for this product.",
            status_code=400,
        )
