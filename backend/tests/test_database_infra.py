import os
from unittest.mock import patch
from sqlalchemy.orm import Session
from app.core.config import Settings, settings
from app.core.database import Base, SessionLocal, check_db_connection, engine, get_db


def test_database_settings_configuration():
    """Verify that settings exposes DATABASE_URL and DB_ECHO with appropriate defaults."""
    assert hasattr(settings, "DATABASE_URL")
    assert hasattr(settings, "DB_ECHO")
    assert isinstance(settings.DATABASE_URL, str)
    assert settings.DATABASE_URL.startswith("postgresql+psycopg://") or settings.DATABASE_URL.startswith("postgresql://") or settings.DATABASE_URL.startswith("sqlite")


def test_custom_database_url_from_env():
    """Verify that DATABASE_URL can be overridden via environment variables."""
    with patch.dict(os.environ, {"DATABASE_URL": "postgresql+psycopg://testuser:testpass@dbhost:5432/testdb"}):
        custom_settings = Settings()
        assert custom_settings.DATABASE_URL == "postgresql+psycopg://testuser:testpass@dbhost:5432/testdb"


def test_declarative_base_instantiation():
    """Verify that Base is a valid SQLAlchemy 2.0 DeclarativeBase."""
    assert hasattr(Base, "metadata")
    assert Base.metadata is not None


def test_engine_and_session_factory():
    """Verify engine and SessionLocal session factory are configured."""
    assert engine is not None
    assert SessionLocal is not None
    assert callable(SessionLocal)


def test_get_db_generator_lifecycle():
    """Verify get_db generator properly yields a session and executes cleanup."""
    db_gen = get_db()
    session = next(db_gen)
    assert isinstance(session, Session)
    # Complete generator to trigger finally block
    try:
        next(db_gen)
    except StopIteration:
        pass


def test_check_db_connection_offline_handling():
    """Verify that check_db_connection returns a graceful (bool, str) tuple even if target DB is offline."""
    is_connected, message = check_db_connection()
    assert isinstance(is_connected, bool)
    assert isinstance(message, str)
    assert len(message) > 0
