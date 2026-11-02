"""Initial schema - products, suppliers, batches, stock_adjustments, stock_movement_logs

Revision ID: a1b2c3d4e5f6
Revises:
Create Date: 2026-10-14

This migration creates the five core tables for PharmaKon Phase 1 functionality.
Tables are created in dependency order so foreign-key references are satisfied:

  1. products    - no FK dependencies
  2. suppliers   - no FK dependencies
  3. batches     - FK -> products
  4. stock_adjustments   - FK -> products, batches
  5. stock_movement_logs - FK -> products, batches

Drop order is reversed.
"""
from __future__ import annotations

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "a1b2c3d4e5f6"
down_revision: str | None = None
branch_labels: str | None = None
depends_on: str | None = None


def upgrade() -> None:
    # ------------------------------------------------------------------
    # 1. products
    #    Per docs/08-database-design.md §3.1
    # ------------------------------------------------------------------
    op.create_table(
        "products",
        sa.Column("id", sa.UUID(as_uuid=True), primary_key=True),
        sa.Column("code", sa.String(50), nullable=False),
        sa.Column("name", sa.String(255), nullable=False),
        sa.Column("category", sa.String(50), nullable=False),
        sa.Column("unit", sa.String(20), nullable=False),
        sa.Column("mrp", sa.Numeric(10, 2), nullable=False),
        sa.Column("default_purchase_price", sa.Numeric(10, 2), nullable=True),
        sa.Column("barcode", sa.String(100), nullable=True),
        sa.Column("reorder_level", sa.Integer(), nullable=False, server_default="10"),
        sa.Column("is_active", sa.Boolean(), nullable=False, server_default="true"),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
        # Check constraints
        sa.CheckConstraint("mrp >= 0", name="chk_products_mrp_nonnegative"),
        sa.CheckConstraint(
            "default_purchase_price IS NULL OR default_purchase_price >= 0",
            name="chk_products_default_purchase_price_nonnegative",
        ),
        sa.CheckConstraint(
            "reorder_level >= 0",
            name="chk_products_reorder_level_nonnegative",
        ),
        # Unique constraint on code
        sa.UniqueConstraint("code", name="uq_products_code"),
    )
    # Indexes (created separately per Alembic convention)
    op.create_index("idx_products_name", "products", ["name"])
    op.create_index("idx_products_category", "products", ["category"])
    op.create_index("idx_products_barcode", "products", ["barcode"])

    # ------------------------------------------------------------------
    # 2. suppliers
    #    Per docs/08-database-design.md §3.2
    # ------------------------------------------------------------------
    op.create_table(
        "suppliers",
        sa.Column("id", sa.UUID(as_uuid=True), primary_key=True),
        sa.Column("name", sa.String(255), nullable=False),
        sa.Column("contact_person", sa.String(100), nullable=True),
        sa.Column("phone", sa.String(20), nullable=False),
        sa.Column("email", sa.String(100), nullable=True),
        sa.Column("address", sa.Text(), nullable=True),
        sa.Column("pan_vat_number", sa.String(50), nullable=True),
        sa.Column("is_active", sa.Boolean(), nullable=False, server_default="true"),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
    )
    op.create_index("idx_suppliers_name", "suppliers", ["name"])

    # ------------------------------------------------------------------
    # 3. batches
    #    Per docs/08-database-design.md §3.3
    #    Unique constraint: (product_id, batch_number, expiry_date)
    #    FK: product_id -> products.id  ON DELETE RESTRICT
    # ------------------------------------------------------------------
    op.create_table(
        "batches",
        sa.Column("id", sa.UUID(as_uuid=True), primary_key=True),
        sa.Column(
            "product_id",
            sa.UUID(as_uuid=True),
            sa.ForeignKey("products.id", ondelete="RESTRICT", name="fk_batches_product_id"),
            nullable=False,
        ),
        sa.Column("batch_number", sa.String(100), nullable=False),
        sa.Column("expiry_date", sa.Date(), nullable=False),
        sa.Column("purchase_cost", sa.Numeric(10, 2), nullable=False),
        sa.Column("quantity", sa.Integer(), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False, server_default="true"),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
        # Composite unique constraint per §3.3
        sa.UniqueConstraint(
            "product_id",
            "batch_number",
            "expiry_date",
            name="uq_batches_product_batch_expiry",
        ),
        # Check constraints
        sa.CheckConstraint("quantity >= 0", name="chk_batches_quantity_nonnegative"),
        sa.CheckConstraint(
            "purchase_cost >= 0",
            name="chk_batches_purchase_cost_nonnegative",
        ),
    )
    op.create_index("idx_batches_product_id", "batches", ["product_id"])
    op.create_index("idx_batches_expiry_date", "batches", ["expiry_date"])

    # ------------------------------------------------------------------
    # 4. stock_adjustments
    #    Per docs/08-database-design.md §3.10
    # ------------------------------------------------------------------
    op.create_table(
        "stock_adjustments",
        sa.Column("id", sa.UUID(as_uuid=True), primary_key=True),
        sa.Column(
            "product_id",
            sa.UUID(as_uuid=True),
            sa.ForeignKey(
                "products.id",
                ondelete="RESTRICT",
                name="fk_stock_adjustments_product_id",
            ),
            nullable=False,
        ),
        sa.Column(
            "batch_id",
            sa.UUID(as_uuid=True),
            sa.ForeignKey(
                "batches.id",
                ondelete="RESTRICT",
                name="fk_stock_adjustments_batch_id",
            ),
            nullable=False,
        ),
        sa.Column("previous_quantity", sa.Integer(), nullable=False),
        sa.Column("new_quantity", sa.Integer(), nullable=False),
        sa.Column("adjustment_quantity", sa.Integer(), nullable=False),
        sa.Column("reason", sa.String(50), nullable=False),
        sa.Column("notes", sa.Text(), nullable=True),
        sa.Column(
            "adjusted_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
        sa.CheckConstraint(
            "new_quantity >= 0",
            name="chk_stock_adjustments_new_quantity_nonnegative",
        ),
    )
    op.create_index(
        "idx_stock_adjustments_product_id", "stock_adjustments", ["product_id"]
    )
    op.create_index(
        "idx_stock_adjustments_batch_id", "stock_adjustments", ["batch_id"]
    )

    # ------------------------------------------------------------------
    # 5. stock_movement_logs
    #    Per docs/08-database-design.md §3.13
    #    Immutable audit ledger - no updates or soft deletes.
    # ------------------------------------------------------------------
    op.create_table(
        "stock_movement_logs",
        sa.Column("id", sa.UUID(as_uuid=True), primary_key=True),
        sa.Column(
            "product_id",
            sa.UUID(as_uuid=True),
            sa.ForeignKey(
                "products.id",
                ondelete="RESTRICT",
                name="fk_stock_movement_logs_product_id",
            ),
            nullable=False,
        ),
        sa.Column(
            "batch_id",
            sa.UUID(as_uuid=True),
            sa.ForeignKey(
                "batches.id",
                ondelete="RESTRICT",
                name="fk_stock_movement_logs_batch_id",
            ),
            nullable=False,
        ),
        sa.Column("movement_type", sa.String(30), nullable=False),
        sa.Column("quantity_delta", sa.Integer(), nullable=False),
        sa.Column("resulting_quantity", sa.Integer(), nullable=False),
        sa.Column("reference_id", sa.UUID(as_uuid=True), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
    )
    op.create_index(
        "idx_stock_movement_logs_created_at", "stock_movement_logs", ["created_at"]
    )
    op.create_index(
        "idx_stock_movement_logs_product_batch",
        "stock_movement_logs",
        ["product_id", "batch_id"],
    )


def downgrade() -> None:
    # Drop in reverse dependency order
    op.drop_index("idx_stock_movement_logs_product_batch", table_name="stock_movement_logs")
    op.drop_index("idx_stock_movement_logs_created_at", table_name="stock_movement_logs")
    op.drop_table("stock_movement_logs")

    op.drop_index("idx_stock_adjustments_batch_id", table_name="stock_adjustments")
    op.drop_index("idx_stock_adjustments_product_id", table_name="stock_adjustments")
    op.drop_table("stock_adjustments")

    op.drop_index("idx_batches_expiry_date", table_name="batches")
    op.drop_index("idx_batches_product_id", table_name="batches")
    op.drop_table("batches")

    op.drop_index("idx_suppliers_name", table_name="suppliers")
    op.drop_table("suppliers")

    op.drop_index("idx_products_barcode", table_name="products")
    op.drop_index("idx_products_category", table_name="products")
    op.drop_index("idx_products_name", table_name="products")
    op.drop_table("products")
