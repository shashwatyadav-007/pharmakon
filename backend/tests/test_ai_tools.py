from __future__ import annotations

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.core.database import Base
from app.services.ai.tools import (
    get_expiring_batches,
    get_low_stock_medicines,
    get_product_stock_and_batches,
    get_supplier_info,
    search_products,
)


# ---------------------------------------------------------------------------
# 1. Product Search Tests
# ---------------------------------------------------------------------------

def test_search_products_valid_query(db_session: Session):
    """Test searching products by valid partial or exact name."""
    results = search_products(db_session, query="Paracetamol")
    assert len(results) >= 1
    item = results[0]
    assert "Paracetamol" in item["name"]
    assert item["code"] == "MED-PAR-500"
    assert item["category"] == "Medicine"
    assert item["unit"] in ("Strip", "Tablet")
    assert item["mrp"] > 0
    assert item["total_stock"] >= 0


def test_search_products_by_code(db_session: Session):
    """Test searching products by exact product SKU code."""
    results = search_products(db_session, query="MED-AMX-250")
    assert len(results) == 1
    assert results[0]["name"] == "Amoxicillin 250mg"


def test_search_products_invalid_query_returns_empty(db_session: Session):
    """Test searching products with a non-existent name returns empty list."""
    results = search_products(db_session, query="NonExistentMedicineXYZ999")
    assert results == []


def test_search_products_empty_or_whitespace_query(db_session: Session):
    """Test empty and whitespace query strings return empty lists gracefully."""
    assert search_products(db_session, query="") == []
    assert search_products(db_session, query="   ") == []


def test_search_products_limit_clamping(db_session: Session):
    """Test limit clamping behavior."""
    results = search_products(db_session, query="a", limit=1)
    assert len(results) <= 1


# ---------------------------------------------------------------------------
# 2. Stock and Batch Details Tests
# ---------------------------------------------------------------------------

def test_get_product_stock_and_batches_success(db_session: Session):
    """Test stock and FEFO batch details retrieval for an existing product."""
    res = get_product_stock_and_batches(db_session, product_name="Paracetamol 500mg")
    assert res["found"] is True
    assert res["product_name"] == "Paracetamol 500mg"
    assert res["total_stock"] == 33
    assert len(res["batches"]) == 2
    # Check FEFO ordering: earliest expiry first
    assert res["batches"][0]["expiry_date"] <= res["batches"][1]["expiry_date"]
    assert res["batches"][0]["batch_number"] == "BCH-2026-01"


def test_get_product_stock_and_batches_by_code(db_session: Session):
    """Test stock retrieval using product code."""
    res = get_product_stock_and_batches(db_session, product_name="MED-AMX-250")
    assert res["found"] is True
    assert res["product_name"] == "Amoxicillin 250mg"
    assert res["total_stock"] == 5


def test_get_product_stock_and_batches_not_found(db_session: Session):
    """Test graceful response when product does not exist."""
    res = get_product_stock_and_batches(db_session, product_name="UnknownSyrup999")
    assert res["found"] is False
    assert "not found" in res["message"].lower()
    assert res["total_stock"] == 0
    assert res["batches"] == []


def test_get_product_stock_and_batches_empty_string(db_session: Session):
    """Test stock retrieval with empty string."""
    res = get_product_stock_and_batches(db_session, product_name="")
    assert res["found"] is False
    assert res["total_stock"] == 0
    assert res["batches"] == []


# ---------------------------------------------------------------------------
# 3. Low Stock Identification Tests
# ---------------------------------------------------------------------------

def test_get_low_stock_medicines(db_session: Session):
    """Test identifying products whose stock is at or below reorder level."""
    alerts = get_low_stock_medicines(db_session)
    assert isinstance(alerts, list)
    assert len(alerts) >= 2

    alert_names = [a["product_name"] for a in alerts]
    # Amoxicillin (stock 5 <= reorder 10) and Face Wash (stock 3 <= reorder 5)
    assert "Amoxicillin 250mg" in alert_names
    assert "Face Wash 100ml" in alert_names

    for item in alerts:
        assert item["current_stock"] <= item["reorder_level"]
        assert "product_id" in item
        assert "product_code" in item


# ---------------------------------------------------------------------------
# 4. Expiry Risk Filtering Tests
# ---------------------------------------------------------------------------

def test_get_expiring_batches_within_window(db_session: Session):
    """Test retrieving batches expiring within 60 days."""
    batches = get_expiring_batches(db_session, days=60)
    assert isinstance(batches, list)
    assert len(batches) >= 1

    first = batches[0]
    assert first["batch_number"] == "BCH-2026-01"
    assert first["medicine_name"] == "Paracetamol 500mg"
    assert first["remaining_quantity"] == 8
    assert first["days_until_expiry"] <= 60


def test_get_expiring_batches_large_window(db_session: Session):
    """Test retrieving batches within a 365-day window includes more items."""
    batches_365 = get_expiring_batches(db_session, days=365)
    batches_30 = get_expiring_batches(db_session, days=30)
    assert len(batches_365) >= len(batches_30)


def test_get_expiring_batches_invalid_days_raises_value_error(db_session: Session):
    """Test that zero, negative, or invalid days parameter raises ValueError."""
    with pytest.raises(ValueError, match="positive integer"):
        get_expiring_batches(db_session, days=0)

    with pytest.raises(ValueError, match="positive integer"):
        get_expiring_batches(db_session, days=-15)

    with pytest.raises(ValueError, match="positive integer"):
        get_expiring_batches(db_session, days="60")  # type: ignore


# ---------------------------------------------------------------------------
# 5. Supplier Search Tests
# ---------------------------------------------------------------------------

def test_get_supplier_info_valid_name(db_session: Session):
    """Test searching for an existing supplier by name."""
    suppliers = get_supplier_info(db_session, name="Himalayan")
    assert len(suppliers) >= 1
    s = suppliers[0]
    assert "Himalayan" in s["name"]
    assert "phone" in s
    assert s["phone"] != ""


def test_get_supplier_info_not_found(db_session: Session):
    """Test searching for non-existent supplier returns empty list."""
    suppliers = get_supplier_info(db_session, name="NonExistentDistributor999")
    assert suppliers == []


def test_get_supplier_info_empty_string(db_session: Session):
    """Test empty string returns empty list."""
    assert get_supplier_info(db_session, name="") == []
    assert get_supplier_info(db_session, name="   ") == []


# ---------------------------------------------------------------------------
# 6. Isolated Empty Database Tests
# ---------------------------------------------------------------------------

def test_all_tools_against_empty_database():
    """Verify that all AI tools handle a completely empty database gracefully."""
    test_engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(test_engine)

    with Session(test_engine) as empty_db:
        # 1. Search products
        assert search_products(empty_db, query="Paracetamol") == []

        # 2. Stock retrieval
        res = get_product_stock_and_batches(empty_db, product_name="Paracetamol")
        assert res["found"] is False
        assert res["total_stock"] == 0
        assert res["batches"] == []

        # 3. Low stock medicines
        assert get_low_stock_medicines(empty_db) == []

        # 4. Expiring batches
        assert get_expiring_batches(empty_db, days=60) == []

        # 5. Supplier info
        assert get_supplier_info(empty_db, name="Himalayan") == []
