from __future__ import annotations

import uuid
from datetime import date, datetime, timezone
from decimal import Decimal
from typing import TYPE_CHECKING, List, Optional

from sqlalchemy import (
    Boolean,
    CheckConstraint,
    Date,
    DateTime,
    ForeignKey,
    Index,
    Integer,
    Numeric,
    String,
    Text,
    UniqueConstraint,
    Uuid,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base

if TYPE_CHECKING:
    from app.models.product import Product


class Batch(Base):
    """Inventory lot of a specific product with discrete expiry date and unit purchase cost."""

    __tablename__ = "batches"

    __table_args__ = (
        UniqueConstraint(
            "product_id",
            "batch_number",
            "expiry_date",
            name="uq_batches_product_batch_expiry",
        ),
        CheckConstraint("quantity >= 0", name="chk_batches_quantity_nonnegative"),
        CheckConstraint("purchase_cost >= 0", name="chk_batches_purchase_cost_nonnegative"),
        Index("idx_batches_expiry_date", "expiry_date"),
        Index("idx_batches_product_id", "product_id"),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    product_id: Mapped[uuid.UUID] = mapped_column(
        Uuid(as_uuid=True),
        ForeignKey("products.id", ondelete="RESTRICT"),
        nullable=False,
    )
    batch_number: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )
    expiry_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )
    purchase_cost: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False,
    )
    quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
        server_default="true",
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
        server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        server_default=func.now(),
    )

    # Relationships
    product: Mapped[Product] = relationship(
        "Product",
        back_populates="batches",
        lazy="select",
    )
    adjustments: Mapped[List[StockAdjustment]] = relationship(
        "StockAdjustment",
        back_populates="batch",
        lazy="select",
    )
    movement_logs: Mapped[List[StockMovementLog]] = relationship(
        "StockMovementLog",
        back_populates="batch",
        lazy="select",
    )

    def __repr__(self) -> str:
        return f"<Batch id={self.id} batch_number='{self.batch_number}' qty={self.quantity}>"


class StockAdjustment(Base):
    """Audit log of physical inventory counts and stock reconciliation."""

    __tablename__ = "stock_adjustments"

    __table_args__ = (
        CheckConstraint("new_quantity >= 0", name="chk_stock_adjustments_new_quantity_nonnegative"),
        Index("idx_stock_adjustments_product_id", "product_id"),
        Index("idx_stock_adjustments_batch_id", "batch_id"),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    product_id: Mapped[uuid.UUID] = mapped_column(
        Uuid(as_uuid=True),
        ForeignKey("products.id", ondelete="RESTRICT"),
        nullable=False,
    )
    batch_id: Mapped[uuid.UUID] = mapped_column(
        Uuid(as_uuid=True),
        ForeignKey("batches.id", ondelete="RESTRICT"),
        nullable=False,
    )
    previous_quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )
    new_quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )
    adjustment_quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )
    reason: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )
    notes: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
    )
    adjusted_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
        server_default=func.now(),
    )

    # Relationships
    product: Mapped[Product] = relationship(
        "Product",
        back_populates="stock_adjustments",
        lazy="select",
    )
    batch: Mapped[Batch] = relationship(
        "Batch",
        back_populates="adjustments",
        lazy="select",
    )

    def __repr__(self) -> str:
        return f"<StockAdjustment id={self.id} delta={self.adjustment_quantity} reason='{self.reason}'>"


class StockMovementLog(Base):
    """Unified immutable ledger of all physical stock movements across the system."""

    __tablename__ = "stock_movement_logs"

    __table_args__ = (
        Index("idx_stock_movement_logs_created_at", "created_at"),
        Index("idx_stock_movement_logs_product_batch", "product_id", "batch_id"),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    product_id: Mapped[uuid.UUID] = mapped_column(
        Uuid(as_uuid=True),
        ForeignKey("products.id", ondelete="RESTRICT"),
        nullable=False,
    )
    batch_id: Mapped[uuid.UUID] = mapped_column(
        Uuid(as_uuid=True),
        ForeignKey("batches.id", ondelete="RESTRICT"),
        nullable=False,
    )
    movement_type: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )
    quantity_delta: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )
    resulting_quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )
    reference_id: Mapped[uuid.UUID] = mapped_column(
        Uuid(as_uuid=True),
        nullable=False,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
        server_default=func.now(),
    )

    # Relationships
    product: Mapped[Product] = relationship(
        "Product",
        back_populates="stock_movement_logs",
        lazy="select",
    )
    batch: Mapped[Batch] = relationship(
        "Batch",
        back_populates="movement_logs",
        lazy="select",
    )

    def __repr__(self) -> str:
        return f"<StockMovementLog id={self.id} type='{self.movement_type}' delta={self.quantity_delta}>"
