import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.database import engine, get_db
from app.main import app
from app.services import data_store


@pytest.fixture(autouse=True)
def reset_data_store():
    """Reset the in-memory data store with fresh sample data before each test."""
    data_store.products.clear()
    data_store.suppliers.clear()
    data_store.batches.clear()
    data_store.stock_adjustments.clear()
    data_store.stock_movement_logs.clear()
    data_store.seed_sample_data()


@pytest.fixture
def db_session():
    """SQLAlchemy transactional session fixture for direct tool and service testing."""
    connection = engine.connect()
    trans = connection.begin()
    session = Session(bind=connection, join_transaction_mode="create_savepoint")
    try:
        yield session
    finally:
        session.close()
        trans.rollback()
        connection.close()


@pytest.fixture
def client():
    """FastAPI TestClient instance with transactional DB isolation.
    
    Each test runs inside a nested savepoint transaction that is rolled back
    when the test finishes, ensuring complete isolation and regression stability.
    """
    connection = engine.connect()
    trans = connection.begin()
    session = Session(bind=connection, join_transaction_mode="create_savepoint")

    def override_get_db():
        yield session

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()
    session.close()
    trans.rollback()
    connection.close()
