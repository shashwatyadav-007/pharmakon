"""
ORM model tests for Phase 3 - run without a live PostgreSQL connection.

These tests verify:
- All model classes import and instantiate correctly
- Column mappings, types, and defaults are correct
- Relationships are defined without circular import errors
- Table names and registered metadata match the documented schema
- Composite unique constraints and check constraints are registered
- Alembic env.py picks up Base.metadata containing all tables
"""
from __future__ import annotations

import uuid
from datetime import date, datetime, timezone
from decimal import Decimal

import pytest
import sqlalchemy as sa

from app.core.database import Base
import app.models  # registers all models on Base.metadata
from app.models import (
    Batch,
    Product,
    StockAdjustment,
    StockMovementLog,
    Supplier,
)


# ---------------------------------------------------------------------------
# 1. Import and __all__ verification
# ---------------------------------------------------------------------------

def test_all_models_importable():
    """All five ORM model classes can be imported from app.models."""
    assert Product is not None
    assert Supplier is not None
    assert Batch is not None
    assert StockAdjustment is not None
    assert StockMovementLog is not None


def test_models_init_exports_all():
    """app.models.__all__ covers all five model classes."""
    import app.models as m
    for name in ("Product", "Supplier", "Batch", "StockAdjustment", "StockMovementLog"):
        assert name in m.__all__, f"{name} missing from __all__"


# ---------------------------------------------------------------------------
# 2. Table names
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("model, expected_table", [
    (Product, "products"),
    (Supplier, "suppliers"),
    (Batch, "batches"),
    (StockAdjustment, "stock_adjustments"),
    (StockMovementLog, "stock_movement_logs"),
])
def test_table_names(model, expected_table):
    assert model.__tablename__ == expected_table


# ---------------------------------------------------------------------------
# 3. All tables registered on shared Base.metadata
# ---------------------------------------------------------------------------

def test_all_tables_in_metadata():
    registered = set(Base.metadata.tables.keys())
    required = {"products", "suppliers", "batches", "stock_adjustments", "stock_movement_logs"}
    assert required.issubset(registered), f"Missing tables: {required - registered}"


# ---------------------------------------------------------------------------
# 4. Column presence per table
# ---------------------------------------------------------------------------

def _cols(model) -> set[str]:
    return {c.name for c in model.__table__.columns}


def test_product_columns():
    expected = {
        "id", "code", "name", "category", "unit",
        "mrp", "default_purchase_price", "barcode",
        "reorder_level", "is_active", "created_at", "updated_at",
    }
    assert expected == _cols(Product)


def test_supplier_columns():
    expected = {
        "id", "name", "contact_person", "phone", "email",
        "address", "pan_vat_number", "is_active", "created_at", "updated_at",
    }
    assert expected == _cols(Supplier)


def test_batch_columns():
    expected = {
        "id", "product_id", "batch_number", "expiry_date",
        "purchase_cost", "quantity", "is_active", "created_at", "updated_at",
    }
    assert expected == _cols(Batch)


def test_stock_adjustment_columns():
    expected = {
        "id", "product_id", "batch_id",
        "previous_quantity", "new_quantity", "adjustment_quantity",
        "reason", "notes", "adjusted_at",
    }
    assert expected == _cols(StockAdjustment)


def test_stock_movement_log_columns():
    expected = {
        "id", "product_id", "batch_id",
        "movement_type", "quantity_delta", "resulting_quantity",
        "reference_id", "created_at",
    }
    assert expected == _cols(StockMovementLog)


# ---------------------------------------------------------------------------
# 5. Primary key types are UUID
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("model", [Product, Supplier, Batch, StockAdjustment, StockMovementLog])
def test_primary_key_is_uuid(model):
    pk_col = model.__table__.c["id"]
    assert isinstance(pk_col.type, sa.Uuid), f"{model.__name__}.id is not Uuid"
    assert pk_col.primary_key


# ---------------------------------------------------------------------------
# 6. Numeric monetary columns use NUMERIC(10,2)
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("model, col_name", [
    (Product, "mrp"),
    (Product, "default_purchase_price"),
    (Batch, "purchase_cost"),
])
def test_monetary_columns_are_numeric(model, col_name):
    col = model.__table__.c[col_name]
    assert isinstance(col.type, sa.Numeric), f"{model.__name__}.{col_name} is not Numeric"
    assert col.type.precision == 10
    assert col.type.scale == 2


# ---------------------------------------------------------------------------
# 7. Timestamp columns are timezone-aware DateTime
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("model, col_name", [
    (Product, "created_at"),
    (Product, "updated_at"),
    (Supplier, "created_at"),
    (Supplier, "updated_at"),
    (Batch, "created_at"),
    (Batch, "updated_at"),
    (StockAdjustment, "adjusted_at"),
    (StockMovementLog, "created_at"),
])
def test_timestamp_columns_are_timezone_aware(model, col_name):
    col = model.__table__.c[col_name]
    assert isinstance(col.type, sa.DateTime), f"{model.__name__}.{col_name} is not DateTime"
    assert col.type.timezone is True, f"{model.__name__}.{col_name} must be timezone-aware"


# ---------------------------------------------------------------------------
# 8. Foreign keys on Batch, StockAdjustment, StockMovementLog
# ---------------------------------------------------------------------------

def test_batch_has_product_fk():
    fk_targets = {fk.target_fullname for fk in Batch.__table__.foreign_keys}
    assert "products.id" in fk_targets


def test_stock_adjustment_has_product_and_batch_fks():
    fk_targets = {fk.target_fullname for fk in StockAdjustment.__table__.foreign_keys}
    assert "products.id" in fk_targets
    assert "batches.id" in fk_targets


def test_stock_movement_log_has_product_and_batch_fks():
    fk_targets = {fk.target_fullname for fk in StockMovementLog.__table__.foreign_keys}
    assert "products.id" in fk_targets
    assert "batches.id" in fk_targets


def test_batch_fk_on_delete_restrict():
    for fk in Batch.__table__.foreign_keys:
        if fk.target_fullname == "products.id":
            assert fk.ondelete == "RESTRICT", "Batch.product_id FK must be ON DELETE RESTRICT"


def test_stock_adjustment_fks_on_delete_restrict():
    for fk in StockAdjustment.__table__.foreign_keys:
        assert fk.ondelete == "RESTRICT", f"StockAdjustment FK {fk} must be ON DELETE RESTRICT"


def test_stock_movement_log_fks_on_delete_restrict():
    for fk in StockMovementLog.__table__.foreign_keys:
        assert fk.ondelete == "RESTRICT", f"StockMovementLog FK {fk} must be ON DELETE RESTRICT"


# ---------------------------------------------------------------------------
# 9. Unique and check constraints
# ---------------------------------------------------------------------------

def _constraint_names(model) -> set[str]:
    return {c.name for c in model.__table__.constraints if c.name}


def test_product_code_unique():
    # products.code has unique=True; expressed as an implicit unique constraint or index
    code_col = Product.__table__.c["code"]
    assert code_col.unique or any(
        "code" in [c.name for c in idx.columns]
        for idx in Product.__table__.indexes
        if idx.unique
    ), "Product.code must be marked unique"


def test_batch_composite_unique_constraint():
    names = _constraint_names(Batch)
    assert "uq_batches_product_batch_expiry" in names, (
        "Batch must have UNIQUE(product_id, batch_number, expiry_date)"
    )


def test_batch_nonnegative_quantity_constraint():
    names = _constraint_names(Batch)
    assert "chk_batches_quantity_nonnegative" in names


def test_batch_nonnegative_purchase_cost_constraint():
    names = _constraint_names(Batch)
    assert "chk_batches_purchase_cost_nonnegative" in names


def test_product_mrp_nonnegative_constraint():
    names = _constraint_names(Product)
    assert "chk_products_mrp_nonnegative" in names


def test_stock_adjustment_new_quantity_nonnegative():
    names = _constraint_names(StockAdjustment)
    assert "chk_stock_adjustments_new_quantity_nonnegative" in names


# ---------------------------------------------------------------------------
# 10. Indexes present
# ---------------------------------------------------------------------------

def _index_names(model) -> set[str]:
    return {idx.name for idx in model.__table__.indexes}


def test_products_has_fefo_supporting_indexes():
    idx = _index_names(Product)
    assert "idx_products_name" in idx
    assert "idx_products_category" in idx
    assert "idx_products_barcode" in idx


def test_batches_has_fefo_supporting_indexes():
    idx = _index_names(Batch)
    assert "idx_batches_expiry_date" in idx
    assert "idx_batches_product_id" in idx


def test_stock_movement_logs_audit_indexes():
    idx = _index_names(StockMovementLog)
    assert "idx_stock_movement_logs_created_at" in idx
    assert "idx_stock_movement_logs_product_batch" in idx


# ---------------------------------------------------------------------------
# 11. Python-level object construction (no DB required)
# ---------------------------------------------------------------------------

def test_product_instantiation():
    p = Product(
        id=uuid.UUID("11111111-1111-1111-1111-111111111111"),
        code="MED-PAR-500",
        name="Paracetamol 500mg",
        category="Medicine",
        unit="Strip",
        mrp=Decimal("60.00"),
        default_purchase_price=Decimal("45.00"),
        barcode="8901234567890",
        reorder_level=15,
        is_active=True,
        created_at=datetime.now(timezone.utc),
        updated_at=datetime.now(timezone.utc),
    )
    assert p.code == "MED-PAR-500"
    assert p.mrp == Decimal("60.00")
    assert p.is_active is True


def test_supplier_instantiation():
    s = Supplier(
        id=uuid.uuid4(),
        name="Nepal Pharma Distributors",
        phone="9841234567",
        email="ram@nepalpharma.com",
        is_active=True,
        created_at=datetime.now(timezone.utc),
        updated_at=datetime.now(timezone.utc),
    )
    assert s.name == "Nepal Pharma Distributors"
    assert s.contact_person is None


def test_batch_instantiation():
    b = Batch(
        id=uuid.UUID("bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbb01"),
        product_id=uuid.UUID("11111111-1111-1111-1111-111111111111"),
        batch_number="BCH-2026-01",
        expiry_date=date(2026, 11, 30),
        purchase_cost=Decimal("42.00"),
        quantity=8,
        is_active=True,
        created_at=datetime.now(timezone.utc),
        updated_at=datetime.now(timezone.utc),
    )
    assert b.batch_number == "BCH-2026-01"
    assert b.quantity == 8
    assert b.purchase_cost == Decimal("42.00")


def test_stock_adjustment_instantiation():
    adj = StockAdjustment(
        id=uuid.uuid4(),
        product_id=uuid.UUID("11111111-1111-1111-1111-111111111111"),
        batch_id=uuid.UUID("bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbb01"),
        previous_quantity=8,
        new_quantity=15,
        adjustment_quantity=7,       # 15 - 8 = 7
        reason="PHYSICAL_COUNT",
        notes="Counted during audit",
        adjusted_at=datetime.now(timezone.utc),
    )
    assert adj.adjustment_quantity == adj.new_quantity - adj.previous_quantity
    assert adj.reason == "PHYSICAL_COUNT"


def test_stock_movement_log_instantiation():
    log = StockMovementLog(
        id=uuid.uuid4(),
        product_id=uuid.UUID("11111111-1111-1111-1111-111111111111"),
        batch_id=uuid.UUID("bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbb01"),
        movement_type="ADJUSTMENT",
        quantity_delta=7,
        resulting_quantity=15,
        reference_id=uuid.uuid4(),
        created_at=datetime.now(timezone.utc),
    )
    assert log.movement_type == "ADJUSTMENT"
    assert log.resulting_quantity == 15


# ---------------------------------------------------------------------------
# 12. Relationship attributes are defined
# ---------------------------------------------------------------------------

def test_product_has_relationship_attributes():
    assert hasattr(Product, "batches")
    assert hasattr(Product, "stock_adjustments")
    assert hasattr(Product, "stock_movement_logs")


def test_batch_has_relationship_attributes():
    assert hasattr(Batch, "product")
    assert hasattr(Batch, "adjustments")
    assert hasattr(Batch, "movement_logs")


def test_stock_adjustment_has_relationship_attributes():
    assert hasattr(StockAdjustment, "product")
    assert hasattr(StockAdjustment, "batch")


def test_stock_movement_log_has_relationship_attributes():
    assert hasattr(StockMovementLog, "product")
    assert hasattr(StockMovementLog, "batch")


# ---------------------------------------------------------------------------
# 13. repr strings are informative
# ---------------------------------------------------------------------------

def test_product_repr():
    p = Product(code="X-001", name="Test Drug")
    assert "X-001" in repr(p)
    assert "Test Drug" in repr(p)


def test_batch_repr():
    b = Batch(batch_number="BCH-TEST", quantity=5)
    assert "BCH-TEST" in repr(b)
    assert "5" in repr(b)
