from __future__ import annotations

import uuid
from datetime import datetime, timezone

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.core.responses import AppError
from app.models.supplier import Supplier


def _supplier_to_dict(supplier: Supplier) -> dict:
    """Convert a Supplier ORM row to a plain dict matching existing API shape."""
    return {
        "id": supplier.id,
        "name": supplier.name,
        "contact_person": supplier.contact_person,
        "phone": supplier.phone,
        "email": supplier.email,
        "address": supplier.address,
        "pan_vat_number": supplier.pan_vat_number,
        "is_active": supplier.is_active,
        "created_at": supplier.created_at,
        "updated_at": supplier.updated_at,
    }


def get_all_suppliers(
    db: Session,
    page: int = 1,
    limit: int = 20,
) -> tuple[list[dict], int]:
    """List all suppliers with pagination."""
    count_total = db.execute(select(func.count(Supplier.id))).scalar() or 0

    stmt = select(Supplier).offset((page - 1) * limit).limit(limit)
    suppliers = db.execute(stmt).scalars().all()

    return [_supplier_to_dict(s) for s in suppliers], int(count_total)


def create_supplier(db: Session, data: dict) -> dict:
    """Create a new supplier."""
    now = datetime.now(timezone.utc)
    supplier = Supplier(
        id=uuid.uuid4(),
        name=data["name"],
        contact_person=data.get("contact_person"),
        phone=data["phone"],
        email=data.get("email"),
        address=data.get("address"),
        pan_vat_number=data.get("pan_vat_number"),
        is_active=True,
        created_at=now,
        updated_at=now,
    )
    db.add(supplier)
    try:
        db.commit()
    except Exception:
        db.rollback()
        raise AppError(
            code="SUPPLIER_SAVE_ERROR",
            message="Failed to register supplier due to a database error.",
            status_code=400,
        )
    db.refresh(supplier)
    return _supplier_to_dict(supplier)
