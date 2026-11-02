import uuid
from datetime import datetime, timezone

from app.core.responses import AppError
from app.services import data_store


def _calculate_total_stock(product_id: uuid.UUID) -> int:
    """Sum all active batch quantities for a product."""
    return sum(
        b["quantity"]
        for b in data_store.batches.values()
        if b["product_id"] == product_id and b.get("is_active", True)
    )


def get_all_products(
    query: str | None = None,
    category: str | None = None,
    is_active: bool | None = None,
    page: int = 1,
    limit: int = 20,
) -> tuple[list[dict], int]:
    """List products with optional filtering and pagination."""
    filtered = []

    for product in data_store.products.values():
        if query:
            q = query.lower()
            searchable = (
                (product.get("code") or "").lower()
                + " " + (product.get("name") or "").lower()
                + " " + (product.get("barcode") or "").lower()
            )
            if q not in searchable:
                continue

        if category and product.get("category") != category:
            continue

        if is_active is not None and product.get("is_active") != is_active:
            continue

        item = product.copy()
        item["total_stock"] = _calculate_total_stock(product["id"])
        filtered.append(item)

    total_count = len(filtered)

    start = (page - 1) * limit
    paginated = filtered[start : start + limit]

    return paginated, total_count


def get_product_by_id(product_id: uuid.UUID) -> dict:
    """Get a single product with total_stock calculated."""
    if product_id not in data_store.products:
        raise AppError(
            code="PRODUCT_NOT_FOUND",
            message="Product not found",
            status_code=404,
        )

    product = data_store.products[product_id].copy()
    product["total_stock"] = _calculate_total_stock(product_id)
    return product


def create_product(data: dict) -> dict:
    """Create a new product. Product code must be unique."""
    code = data["code"]
    for existing in data_store.products.values():
        if existing["code"] == code:
            raise AppError(
                code="DUPLICATE_CODE",
                message=f"A product with code '{code}' already exists",
                status_code=400,
            )

    product_id = uuid.uuid4()
    now = datetime.now(timezone.utc)

    product = {
        "id": product_id,
        "code": data["code"],
        "name": data["name"],
        "category": data["category"],
        "unit": data["unit"],
        "mrp": data["mrp"],
        "default_purchase_price": data.get("default_purchase_price"),
        "barcode": data.get("barcode"),
        "reorder_level": data.get("reorder_level", 10),
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }

    data_store.products[product_id] = product

    result = product.copy()
    result["total_stock"] = 0
    return result


def update_product(product_id: uuid.UUID, data: dict) -> dict:
    """Update an existing product. Only provided fields are changed."""
    if product_id not in data_store.products:
        raise AppError(
            code="PRODUCT_NOT_FOUND",
            message="Product not found",
            status_code=404,
        )

    product = data_store.products[product_id]

    for key, value in data.items():
        if value is not None:
            product[key] = value

    product["updated_at"] = datetime.now(timezone.utc)

    result = product.copy()
    result["total_stock"] = _calculate_total_stock(product_id)
    return result
