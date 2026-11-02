from __future__ import annotations

from datetime import date
from typing import Any

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.models.inventory import Batch
from app.models.product import Product
from app.models.supplier import Supplier
from app.services import inventory_service


def search_products(
    db: Session,
    query: str,
    limit: int = 10,
) -> list[dict[str, Any]]:
    """Search medicines and catalog products by name, product code, or barcode.
    
    Returns matching products along with their total available active stock.
    Returns an empty list if query is empty or no matches are found.
    """
    if not query or not query.strip():
        return []

    clean_query = query.strip().lower()
    clamped_limit = max(1, min(limit, 100))
    today = date.today()

    stock_sub = (
        select(
            Batch.product_id,
            func.coalesce(func.sum(Batch.quantity), 0).label("total_stock"),
        )
        .where(Batch.is_active.is_(True), Batch.expiry_date >= today)
        .group_by(Batch.product_id)
        .subquery()
    )

    # Parameterized case-insensitive search
    stmt = (
        select(
            Product,
            func.coalesce(stock_sub.c.total_stock, 0).label("total_stock"),
        )
        .outerjoin(stock_sub, Product.id == stock_sub.c.product_id)
        .where(
            Product.is_active.is_(True),
            (
                func.lower(Product.name).like(f"%{clean_query}%")
                | func.lower(Product.code).like(f"%{clean_query}%")
                | func.lower(func.coalesce(Product.barcode, "")).like(f"%{clean_query}%")
            ),
        )
        .order_by(Product.name.asc())
        .limit(clamped_limit)
    )

    rows = db.execute(stmt).all()
    results: list[dict[str, Any]] = []

    for p, total_stock in rows:
        results.append(
            {
                "id": str(p.id),
                "code": p.code,
                "name": p.name,
                "category": p.category,
                "unit": p.unit,
                "mrp": float(p.mrp),
                "default_purchase_price": (
                    float(p.default_purchase_price)
                    if p.default_purchase_price is not None
                    else None
                ),
                "barcode": p.barcode,
                "reorder_level": p.reorder_level,
                "total_stock": int(total_stock),
            }
        )

    return results


def get_product_stock_and_batches(
    db: Session,
    product_name: str,
) -> dict[str, Any]:
    """Retrieve total available stock, active batch numbers, expiry dates, and unit costs for a medicine.
    
    Tries exact match first, then falls back to case-insensitive partial match or product code.
    Returns a structured dictionary indicating whether the product was found.
    """
    if not product_name or not product_name.strip():
        return {
            "found": False,
            "message": "Product name cannot be empty.",
            "total_stock": 0,
            "batches": [],
        }

    clean_name = product_name.strip().lower()

    # 1. Exact name match
    product = (
        db.execute(
            select(Product).where(
                Product.is_active.is_(True),
                func.lower(Product.name) == clean_name,
            )
        )
        .scalars()
        .first()
    )

    # 2. Product code match if exact name failed
    if not product:
        product = (
            db.execute(
                select(Product).where(
                    Product.is_active.is_(True),
                    func.lower(Product.code) == clean_name,
                )
            )
            .scalars()
            .first()
        )

    # 3. Substring match if exact match failed
    if not product:
        product = (
            db.execute(
                select(Product)
                .where(
                    Product.is_active.is_(True),
                    func.lower(Product.name).like(f"%{clean_name}%"),
                )
                .order_by(Product.name.asc())
            )
            .scalars()
            .first()
        )

    if not product:
        return {
            "found": False,
            "message": f"Product '{product_name.strip()}' not found in the pharmacy catalog.",
            "total_stock": 0,
            "batches": [],
        }

    # Retrieve all active batches with quantity > 0 in FEFO order (earliest expiry first)
    batch_stmt = (
        select(Batch)
        .where(
            Batch.product_id == product.id,
            Batch.is_active.is_(True),
            Batch.quantity > 0,
        )
        .order_by(Batch.expiry_date.asc(), Batch.id.asc())
    )
    batches = db.execute(batch_stmt).scalars().all()
    today = date.today()

    batch_list: list[dict[str, Any]] = [
        {
            "batch_id": str(b.id),
            "batch_number": b.batch_number,
            "expiry_date": b.expiry_date.isoformat(),
            "quantity": b.quantity,
            "purchase_cost": float(b.purchase_cost),
            "days_until_expiry": (b.expiry_date - today).days,
            "is_expired": b.expiry_date < today,
        }
        for b in batches
    ]

    usable_batches = [b for b in batch_list if not b["is_expired"]]
    expired_batches = [b for b in batch_list if b["is_expired"]]
    usable_stock = sum(b["quantity"] for b in usable_batches)
    expired_stock = sum(b["quantity"] for b in expired_batches)

    return {
        "found": True,
        "product_id": str(product.id),
        "product_name": product.name,
        "product_code": product.code,
        "category": product.category,
        "unit": product.unit,
        "mrp": float(product.mrp),
        "reorder_level": product.reorder_level,
        "total_stock": usable_stock,
        "usable_stock": usable_stock,
        "expired_stock": expired_stock,
        "batches": usable_batches,
        "expired_batches": expired_batches,
    }


def get_low_stock_medicines(db: Session) -> list[dict[str, Any]]:
    """Retrieve all active products currently at or below their configured reorder level.
    
    Reuses existing inventory domain alert logic.
    """
    raw_alerts = inventory_service.get_low_stock_alerts(db)

    return [
        {
            "product_id": str(alert["product_id"]),
            "product_name": alert["product_name"],
            "product_code": alert["product_code"],
            "reorder_level": alert["reorder_level"],
            "current_stock": alert["current_stock"],
        }
        for alert in raw_alerts
    ]


def get_expiring_batches(
    db: Session,
    days: int = 60,
) -> list[dict[str, Any]]:
    """Retrieve active inventory batches expiring within the specified number of days.
    
    Validates that days is a positive integer.
    Reuses inventory domain expiry risk logic.
    """
    if not isinstance(days, int) or days <= 0:
        raise ValueError("Days parameter must be a positive integer.")

    raw_alerts = inventory_service.get_expiry_risk_alerts(db, days_threshold=days)

    return [
        {
            "medicine_name": alert["product_name"],
            "product_id": str(alert["product_id"]),
            "batch_id": str(alert["batch_id"]),
            "batch_number": alert["batch_number"],
            "expiry_date": (
                alert["expiry_date"].isoformat()
                if hasattr(alert["expiry_date"], "isoformat")
                else str(alert["expiry_date"])
            ),
            "remaining_quantity": alert["quantity"],
            "days_until_expiry": alert["days_until_expiry"],
        }
        for alert in raw_alerts
    ]


def get_supplier_info(
    db: Session,
    name: str,
) -> list[dict[str, Any]]:
    """Search suppliers by company name and return available contact details.
    
    Returns an empty list if name is empty or no matching suppliers exist.
    """
    if not name or not name.strip():
        return []

    clean_name = name.strip().lower()

    stmt = (
        select(Supplier)
        .where(
            Supplier.is_active.is_(True),
            func.lower(Supplier.name).like(f"%{clean_name}%"),
        )
        .order_by(Supplier.name.asc())
    )

    suppliers = db.execute(stmt).scalars().all()

    return [
        {
            "id": str(s.id),
            "name": s.name,
            "contact_person": s.contact_person,
            "phone": s.phone,
            "email": s.email,
            "address": s.address,
            "pan_vat_number": s.pan_vat_number,
            "is_active": s.is_active,
        }
        for s in suppliers
    ]
