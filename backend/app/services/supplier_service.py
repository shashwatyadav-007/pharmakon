import uuid
from datetime import datetime, timezone

from app.services import data_store


def get_all_suppliers(
    page: int = 1,
    limit: int = 20,
) -> tuple[list[dict], int]:
    """List all suppliers with pagination."""
    all_suppliers = list(data_store.suppliers.values())
    total_count = len(all_suppliers)

    start = (page - 1) * limit
    paginated = all_suppliers[start : start + limit]

    return paginated, total_count


def create_supplier(data: dict) -> dict:
    """Create a new supplier."""
    supplier_id = uuid.uuid4()
    now = datetime.now(timezone.utc)

    supplier = {
        "id": supplier_id,
        "name": data["name"],
        "contact_person": data.get("contact_person"),
        "phone": data["phone"],
        "email": data.get("email"),
        "address": data.get("address"),
        "pan_vat_number": data.get("pan_vat_number"),
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }

    data_store.suppliers[supplier_id] = supplier
    return supplier
