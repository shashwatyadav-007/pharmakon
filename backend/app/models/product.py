from __future__ import annotations

import uuid
from datetime import datetime, timezone
from decimal import Decimal
from typing import TYPE_CHECKING, List, Optional

from sqlalchemy import (
    Boolean,
    CheckConstraint,
    DateTime,
    Index,
    Integer,
    Numeric,
    String,
    Uuid,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base

if TYPE_CHECKING:
    from app.models.inventory import Batch, StockAdjustment, StockMovementLog


class Product(Base):
    """Product catalog model representing pharmaceutical, cosmetic, and healthcare products."""

    __tablename__ = "products"

    __table_args__ = (
        CheckConstraint("mrp >= 0", name="chk_products_mrp_nonnegative"),
        CheckConstraint(
            "default_purchase_price IS NULL OR default_purchase_price >= 0",
            name="chk_products_default_purchase_price_nonnegative",
        ),
        CheckConstraint(
            "reorder_level >= 0",
            name="chk_products_reorder_level_nonnegative",
        ),
        Index("idx_products_name", "name"),
        Index("idx_products_category", "category"),
        Index("idx_products_barcode", "barcode"),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    code: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
        index=True,
    )
    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    category: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )
    unit: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )
    mrp: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False,
    )
    default_purchase_price: Mapped[Optional[Decimal]] = mapped_column(
        Numeric(10, 2),
        nullable=True,
    )
    barcode: Mapped[Optional[str]] = mapped_column(
        String(100),
        nullable=True,
    )
    reorder_level: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=10,
        server_default="10",
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
    batches: Mapped[List[Batch]] = relationship(
        "Batch",
        back_populates="product",
        lazy="select",
    )
    stock_adjustments: Mapped[List[StockAdjustment]] = relationship(
        "StockAdjustment",
        back_populates="product",
        lazy="select",
    )
    stock_movement_logs: Mapped[List[StockMovementLog]] = relationship(
        "StockMovementLog",
        back_populates="product",
        lazy="select",
    )

    def __repr__(self) -> str:
        return f"<Product id={self.id} code='{self.code}' name='{self.name}'>"
