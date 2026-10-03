from __future__ import annotations

import uuid
from datetime import date, datetime, timezone
from decimal import Decimal
from typing import Any

from app.core.responses import AppError
from app.services import data_store


def get_all_batches(
    product_id: uuid.UUID | None = None,
    expiry_before: date | None = None,
    low_stock: bool | None = None,
    page: int = 1,
    limit: int = 20,
) -> tuple[list[dict[str, Any]], int]:
    """List batches with optional filters and pagination."""
    filtered = []

    for b in data_store.batches.values():
        if product_id and b.get("product_id") != product_id:
            continue

        if expiry_before and b.get("expiry_date"):
            if b["expiry_date"] >= expiry_before:
                continue

        if low_stock and b.get("quantity", 0) > 10:
            continue

        b_copy = b.copy()
        product = data_store.products.get(b["product_id"])
        b_copy["product_name"] = product["name"] if product else "Unknown Product"
        filtered.append(b_copy)

    total_count = len(filtered)
    start_idx = (page - 1) * limit
    end_idx = start_idx + limit
    paginated_items = filtered[start_idx:end_idx]

    return paginated_items, total_count


def get_fefo_batches(product_id: uuid.UUID) -> dict[str, Any]:
    """Retrieve batches for a product ordered strictly by First Expiry, First Out (FEFO)."""
    if product_id not in data_store.products:
        raise AppError(
            code="PRODUCT_NOT_FOUND",
            message="Product not found",
            status_code=404,
        )

    product = data_store.products[product_id]

    active_batches = [
        b.copy()
        for b in data_store.batches.values()
        if b.get("product_id") == product_id and b.get("is_active", True) and b.get("quantity", 0) > 0
    ]

    # Sort strictly by expiry_date ascending (FEFO)
    active_batches.sort(key=lambda x: x["expiry_date"])

    fefo_batches = [
        {
            "batch_id": b["id"],
            "batch_number": b["batch_number"],
            "expiry_date": b["expiry_date"],
            "available_quantity": b["quantity"],
            "purchase_cost": b["purchase_cost"],
        }
        for b in active_batches
    ]

    return {
        "product_id": product_id,
        "product_name": product["name"],
        "fefo_batches": fefo_batches,
    }


def get_low_stock_alerts() -> list[dict[str, Any]]:
    """Fetch all active products where combined stock across active batches is <= reorder_level."""
    alerts = []

    for p in data_store.products.values():
        if not p.get("is_active", True):
            continue

        total_stock = sum(
            b.get("quantity", 0)
            for b in data_store.batches.values()
            if b.get("product_id") == p["id"] and b.get("is_active", True)
        )

        reorder_level = p.get("reorder_level", 10)
        if total_stock <= reorder_level:
            alerts.append(
                {
                    "product_id": p["id"],
                    "product_name": p["name"],
                    "product_code": p["code"],
                    "reorder_level": reorder_level,
                    "current_stock": total_stock,
                }
            )

    return alerts


def get_expiry_risk_alerts(days_threshold: int = 60) -> list[dict[str, Any]]:
    """Fetch inventory batches expiring within the configured threshold days."""
    alerts = []
    today = date.today()

    for b in data_store.batches.values():
        if not b.get("is_active", True) or b.get("quantity", 0) <= 0:
            continue

        exp_date = b.get("expiry_date")
        if not exp_date:
            continue

        days_until_expiry = (exp_date - today).days
        if days_until_expiry <= days_threshold:
            product = data_store.products.get(b["product_id"])
            alerts.append(
                {
                    "batch_id": b["id"],
                    "product_id": b["product_id"],
                    "product_name": product["name"] if product else "Unknown Product",
                    "batch_number": b["batch_number"],
                    "expiry_date": exp_date,
                    "quantity": b["quantity"],
                    "days_until_expiry": days_until_expiry,
                }
            )

    # Sort with nearest expiry first
    alerts.sort(key=lambda x: x["days_until_expiry"])
    return alerts


def create_stock_adjustment(data: dict[str, Any]) -> dict[str, Any]:
    """Record a physical stock count adjustment."""
    product_id = data["product_id"]
    batch_id = data["batch_id"]
    new_quantity = data["new_quantity"]

    if product_id not in data_store.products:
        raise AppError(
            code="PRODUCT_NOT_FOUND",
            message="Product not found",
            status_code=404,
        )

    if batch_id not in data_store.batches:
        raise AppError(
            code="BATCH_NOT_FOUND",
            message="Batch not found",
            status_code=404,
        )

    batch = data_store.batches[batch_id]
    if batch.get("product_id") != product_id:
        raise AppError(
            code="INVALID_BATCH_PRODUCT",
            message="Batch does not belong to the specified product",
            status_code=400,
        )

    previous_quantity = batch.get("quantity", 0)
    adjustment_quantity = new_quantity - previous_quantity

    # Update batch quantity in-place
    batch["quantity"] = new_quantity

    # Record adjustment audit record
    adj_id = uuid.uuid4()
    now = datetime.now(timezone.utc)

    adjustment = {
        "id": adj_id,
        "product_id": product_id,
        "batch_id": batch_id,
        "previous_quantity": previous_quantity,
        "new_quantity": new_quantity,
        "adjustment_quantity": adjustment_quantity,
        "reason": data["reason"],
        "notes": data.get("notes"),
        "adjusted_at": now,
    }
    data_store.stock_adjustments[adj_id] = adjustment

    # Immutable stock movement log
    movement = {
        "id": uuid.uuid4(),
        "product_id": product_id,
        "batch_id": batch_id,
        "movement_type": "ADJUSTMENT",
        "quantity_delta": adjustment_quantity,
        "resulting_quantity": new_quantity,
        "reference_id": adj_id,
        "created_at": now,
    }
    data_store.stock_movement_logs.append(movement)

    return adjustment
