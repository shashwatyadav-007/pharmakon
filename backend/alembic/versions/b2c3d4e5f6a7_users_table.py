"""Users table migration

Revision ID: b2c3d4e5f6a7
Revises: a1b2c3d4e5f6
Create Date: 2026-10-15

This migration tracks the users table for authentication and access control.
"""
from __future__ import annotations

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "b2c3d4e5f6a7"
down_revision: str | None = "a1b2c3d4e5f6"
branch_labels: str | None = None
depends_on: str | None = None


def upgrade() -> None:
    # Check if table already exists (as in current database)
    conn = op.get_bind()
    inspector = sa.inspect(conn)
    tables = inspector.get_table_names()
    if "users" not in tables:
        op.create_table(
            "users",
            sa.Column("id", sa.UUID(as_uuid=True), primary_key=True),
            sa.Column("email", sa.String(255), nullable=False),
            sa.Column("username", sa.String(100), nullable=False),
            sa.Column("full_name", sa.String(255), nullable=True),
            sa.Column("hashed_password", sa.String(255), nullable=True),
            sa.Column(
                "auth_provider",
                sa.String(50),
                nullable=False,
                server_default="email",
            ),
            sa.Column("google_sub", sa.String(255), nullable=True),
            sa.Column("avatar_url", sa.String(500), nullable=True),
            sa.Column(
                "role",
                sa.String(50),
                nullable=False,
                server_default="Pharmacy System User",
            ),
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
            sa.UniqueConstraint("email", name="uq_users_email"),
            sa.UniqueConstraint("username", name="uq_users_username"),
            sa.UniqueConstraint("google_sub", name="uq_users_google_sub"),
        )
        op.create_index("idx_users_username", "users", ["username"])
        op.create_index("idx_users_email", "users", ["email"])


def downgrade() -> None:
    op.drop_table("users")
