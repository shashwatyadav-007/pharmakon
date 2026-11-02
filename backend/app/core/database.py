from __future__ import annotations

from typing import Generator

from sqlalchemy import create_engine, text
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from app.core.config import settings

# Engine configuration
# pool_pre_ping tests connection liveness before checking out from pool
engine_kwargs = {
    "echo": settings.DB_ECHO,
    "pool_pre_ping": True,
}

# SQLite compatibility for isolated in-memory unit tests if selected via DATABASE_URL
if settings.DATABASE_URL.startswith("sqlite"):
    engine_kwargs["connect_args"] = {"check_same_thread": False}
elif "postgresql" in settings.DATABASE_URL:
    engine_kwargs["connect_args"] = {"connect_timeout": 3}

engine = create_engine(settings.DATABASE_URL, **engine_kwargs)

# Session factory for transactional database sessions
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


class Base(DeclarativeBase):
    """SQLAlchemy 2.0 Declarative Base class for all ORM models."""
    pass


def get_db() -> Generator[Session, None, None]:
    """FastAPI dependency yielding a transactional SQLAlchemy session.
    
    Ensures sessions are closed and resources are released after request handling.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def check_db_connection() -> tuple[bool, str]:
    """Test if the database engine can connect to the target database server.
    
    Returns (True, message) if reachable, or (False, error_details) if offline.
    """
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return True, "Database connection successful"
    except Exception as exc:
        return False, str(exc)
