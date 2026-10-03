import pytest
from fastapi.testclient import TestClient

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
def client():
    """FastAPI TestClient instance."""
    return TestClient(app)
