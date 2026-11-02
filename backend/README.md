# PharmaKon Backend

## Purpose

PharmaKon Backend is a pharmacy management and analytics REST API built with **FastAPI**. It handles retail pharmacy inventory management, FEFO (First Expiry, First Out) batch tracking, medicine catalog searching, supplier management, and low-stock/expiry-risk alerting.

---

## Technology

- **Python 3.11+**
- **FastAPI**: Modern, high-performance web framework for building APIs
- **Pydantic V2**: Data validation, typing, and schema serialization
- **Uvicorn**: Lightning-fast ASGI web server
- **Pytest & HTTPX**: Automated testing and API client simulation

---

## Project Structure

```text
backend/
├── app/
│   ├── main.py               # FastAPI application entrypoint, middleware, and router setup
│   ├── api/
│   │   └── routes/           # Domain API route handlers
│   │       ├── auth.py       # Authentication endpoint (/api/v1/auth/login)
│   │       ├── products.py   # Product catalog CRUD & search (/api/v1/products)
│   │       ├── inventory.py  # Batches, FEFO, alerts & adjustments (/api/v1/inventory)
│   │       └── suppliers.py  # Supplier management (/api/v1/suppliers)
│   ├── core/
│   │   ├── config.py         # App settings and environment constants
│   │   └── responses.py      # Standard success/error envelopes and exception handlers
│   ├── schemas/              # Pydantic request and response validation models
│   │   ├── auth.py           # Login request & response models
│   │   ├── products.py       # Product create, update, and response schemas
│   │   ├── inventory.py      # Batch, FEFO, alert, and adjustment schemas
│   │   └── suppliers.py      # Supplier schemas
│   ├── services/             # Business logic layer and data store
│   │   ├── data_store.py     # In-memory storage and seed data
│   │   ├── product_service.py# Product business operations and stock calculation
│   │   ├── inventory_service.py # FEFO ordering, alerts, and stock adjustments
│   │   └── supplier_service.py # Supplier business logic
│   └── models/               # (Reserved for future ORM models)
├── tests/                    # Automated Pytest test suite
│   ├── conftest.py           # Test fixtures and TestClient setup
│   ├── test_auth.py          # Authentication tests
│   ├── test_products.py      # Product CRUD & search tests
│   ├── test_inventory.py     # FEFO, alerts, and adjustment tests
│   └── test_suppliers.py     # Supplier tests
├── requirements.txt          # Python dependencies
├── .env.example              # Environment variables template
└── README.md                 # Backend documentation
```

---

## Running the Backend

### 1. Create and Activate Virtual Environment

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment (Windows PowerShell)
.venv\Scripts\Activate.ps1

# Or Windows Command Prompt:
# .venv\Scripts\activate.bat

# Or Linux / macOS:
# source .venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Development Server

Navigate to the `backend` directory and start Uvicorn:

```bash
cd backend
uvicorn app.main:app --reload
```

---

## Accessing the API

Once the server is running, you can access:

- **Root API Status**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Interactive Swagger Documentation**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc Alternative Documentation**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
- **OpenAPI JSON Schema**: [http://127.0.0.1:8000/openapi.json](http://127.0.0.1:8000/openapi.json)

---

## Running Automated Tests

Run the complete test suite with `pytest`:

```bash
pytest tests/ -v
```
