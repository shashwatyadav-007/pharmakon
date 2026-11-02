# Session Summary: Backend Foundation (Part 1)

## Overview

This session established the initial backend foundation for the **PharmaKon** Pharmacy Management and Analytics System using **FastAPI**, **Pydantic V2**, and **Uvicorn**.

The implementation directly aligns with the specifications defined in [`docs/09-api-design.md`](file:///d:/PharmaKon/pharmakon/docs/09-api-design.md), [`docs/07-system-architecture.md`](file:///d:/PharmaKon/pharmakon/docs/07-system-architecture.md), and [`docs/08-database-design.md`](file:///d:/PharmaKon/pharmakon/docs/08-database-design.md).

For this initial learning phase, the backend uses an **in-memory data store** pre-seeded with sample pharmacy records. This allows you to explore, test, and understand FastAPI mechanics, routing, Pydantic validation, and service layering without the overhead of database migrations.

---

## What Was Created and Changed

### 1. Directory Structure

The backend directory was organized into clean, modular layers:

```text
backend/
├── app/
│   ├── main.py                   # Master FastAPI application, CORS, and exception handling
│   ├── api/
│   │   └── routes/               # API route definitions
│   │       ├── auth.py           # Authentication route (/api/v1/auth/login)
│   │       ├── products.py       # Product catalog CRUD & search (/api/v1/products)
│   │       ├── inventory.py      # Batches, FEFO, alerts & adjustments (/api/v1/inventory)
│   │       └── suppliers.py      # Supplier registry (/api/v1/suppliers)
│   ├── core/
│   │   ├── config.py             # Global application settings and constants
│   │   └── responses.py          # Response envelope wrappers and AppError definition
│   ├── schemas/                  # Pydantic V2 request and response models
│   │   ├── auth.py               # Authentication schemas
│   │   ├── products.py           # Product create, update, and response schemas
│   │   ├── inventory.py          # Batch, FEFO, alert, and adjustment schemas
│   │   └── suppliers.py          # Supplier schemas
│   └── services/                 # Domain logic and data access
│       ├── data_store.py         # In-memory storage dictionaries and seed data
│       ├── product_service.py    # Product business rules, SKU uniqueness, and stock aggregation
│       ├── inventory_service.py  # FEFO sorting, low-stock alerts, and stock adjustments
│       └── supplier_service.py   # Supplier business logic and pagination
├── tests/                        # Automated Pytest test suite (20 test cases)
│   ├── conftest.py               # Fixtures and TestClient setup
│   ├── test_auth.py              # Auth endpoint tests
│   ├── test_products.py          # Product CRUD & search tests
│   ├── test_inventory.py         # FEFO, alerts, and stock adjustment tests
│   └── test_suppliers.py         # Supplier endpoint tests
├── requirements.txt              # Core project dependencies
├── .env.example                  # Environment configuration template
└── README.md                     # Backend documentation
```

---

## Detailed File Breakdown

### 1. Core Layer (`app/core/`)

- [`app/core/config.py`](file:///d:/PharmaKon/pharmakon/backend/app/core/config.py):
  Contains the `Settings` class holding configuration constants such as `APP_NAME`, `APP_VERSION`, `API_V1_PREFIX = "/api/v1"`, `DEFAULT_PAGE_SIZE = 20`, and `EXPIRY_ALERT_DAYS = 60`.
- [`app/core/responses.py`](file:///d:/PharmaKon/pharmakon/backend/app/core/responses.py):
  Implements the standard API envelope structures required by the API specification:
  - `success_response(data, message, meta)` produces `{"success": true, "data": ..., "message": ..., "meta": ...}`.
  - `error_response(code, message, details)` produces `{"success": false, "error": {"code": ..., "message": ..., "details": [...]}}`.
  - `AppError` is a custom exception class holding a business error code, human-readable message, HTTP status code, and optional field details.

---

### 2. Schemas Layer (`app/schemas/`)

Pydantic models validate incoming HTTP request bodies and serialize outgoing responses.

- [`app/schemas/auth.py`](file:///d:/PharmaKon/pharmakon/backend/app/schemas/auth.py):
  - `LoginRequest`: Validates username and password.
  - `LoginResponse`: Formats login token and user info.
- [`app/schemas/products.py`](file:///d:/PharmaKon/pharmakon/backend/app/schemas/products.py):
  - `ProductCreate`: Validates SKU code, name, category (`Literal["Medicine", "Surgical", "Cosmetic", "Baby", "Food"]`), unit (`Literal["Strip", "Tablet", "Bottle", "Box", "Piece"]`), MRP (`Decimal >= 0`), and reorder level.
  - `ProductUpdate`: Allows partial updating of product attributes.
  - `ProductResponse`: Serializes full product profile including computed `total_stock`.
- [`app/schemas/inventory.py`](file:///d:/PharmaKon/pharmakon/backend/app/schemas/inventory.py):
  - `BatchResponse`: Serializes batch numbers, expiry dates, purchase costs, and quantities.
  - `FEFOProductResponse`: Formats FEFO-ordered batch lists for a product.
  - `StockAdjustmentCreate`: Validates physical stock verification inputs.
  - `LowStockAlert` and `ExpiryRiskAlert`: Format automated alert notifications.
- [`app/schemas/suppliers.py`](file:///d:/PharmaKon/pharmakon/backend/app/schemas/suppliers.py):
  - `SupplierCreate` and `SupplierResponse`: Models for vendor records.

---

### 3. Services and Data Store Layer (`app/services/`)

- [`app/services/data_store.py`](file:///d:/PharmaKon/pharmakon/backend/app/services/data_store.py):
  Provides in-memory dictionaries for `products`, `suppliers`, `batches`, `stock_adjustments`, and `stock_movement_logs`.
  The `seed_sample_data()` function pre-populates realistic records:
  - Paracetamol 500mg with 2 active batches (one expiring within 60 days to test expiry alerts and FEFO sorting).
  - Amoxicillin 250mg with 1 active batch (quantity 5, below reorder level 10 to test low-stock alerts).
  - Face Wash 100ml with 1 active batch.
  - Nepal Pharma Distributors supplier record.
- [`app/services/product_service.py`](file:///d:/PharmaKon/pharmakon/backend/app/services/product_service.py):
  Enforces business rules:
  - Validates SKU code uniqueness (`DUPLICATE_CODE` error on conflict).
  - Calculates dynamic `total_stock` across all active batches for a product.
  - Handles multi-field search (by code, name, and barcode) and category filtering with pagination.
- [`app/services/inventory_service.py`](file:///d:/PharmaKon/pharmakon/backend/app/services/inventory_service.py):
  Enforces inventory invariants:
  - `get_fefo_batches()` sorts batches by `expiry_date ASC` so that earliest-expiring stock is dispensed first.
  - `get_low_stock_alerts()` finds products where combined stock is less than or equal to `reorder_level`.
  - `get_expiry_risk_alerts()` identifies batches expiring within the specified days threshold (default 60 days).
  - `create_stock_adjustment()` verifies batch ownership, updates physical quantity, and appends an immutable record to `stock_movement_logs`.
- [`app/services/supplier_service.py`](file:///d:/PharmaKon/pharmakon/backend/app/services/supplier_service.py):
  Provides supplier listing, pagination, and registration.

---

### 4. API Routes Layer (`app/api/routes/`)

- [`app/api/routes/auth.py`](file:///d:/PharmaKon/pharmakon/backend/app/api/routes/auth.py):
  `POST /api/v1/auth/login` validates credentials and returns a Bearer access token.
- [`app/api/routes/products.py`](file:///d:/PharmaKon/pharmakon/backend/app/api/routes/products.py):
  Implements `GET /api/v1/products`, `POST /api/v1/products`, `GET /api/v1/products/{id}`, and `PUT /api/v1/products/{id}`.
- [`app/api/routes/inventory.py`](file:///d:/PharmaKon/pharmakon/backend/app/api/routes/inventory.py):
  Implements `GET /api/v1/inventory/batches`, `GET /api/v1/inventory/fefo/{product_id}`, `GET /api/v1/inventory/alerts/low-stock`, `GET /api/v1/inventory/alerts/expiry-risk`, and `POST /api/v1/inventory/adjustments`.
- [`app/api/routes/suppliers.py`](file:///d:/PharmaKon/pharmakon/backend/app/api/routes/suppliers.py):
  Implements `GET /api/v1/suppliers` and `POST /api/v1/suppliers`.

---

### 5. Application Entrypoint (`app/main.py`)

[`app/main.py`](file:///d:/PharmaKon/pharmakon/backend/app/main.py):
- Initializes the `FastAPI` app with metadata and documentation URLs (`/docs`, `/redoc`).
- Sets up lifespan startup to populate sample seed data.
- Adds CORS middleware for future frontend connection.
- Registers global exception handlers:
  - `AppError` returns clean JSON error envelopes.
  - `RequestValidationError` formats Pydantic validation errors into the standard error envelope.
  - `HTTPException` wraps generic HTTP errors.
- Mounts all domain routers under `/api/v1`.
- Exposes `GET /` (API metadata) and `GET /health` (liveness probe).

---

## Key FastAPI Concepts to Learn

### 1. Request Lifecycle Flow

```text
HTTP Request (Client)
      ↓
Uvicorn ASGI Server
      ↓
FastAPI Application (app.main:app)
      ↓
Router Matching (app/api/routes/*.py)
      ↓
Pydantic Request Validation (app/schemas/*.py)
      ↓
Service Layer Execution (app/services/*.py)
      ↓
In-Memory Store Mutation (app/services/data_store.py)
      ↓
Pydantic Response Serialization
      ↓
Standard Envelope Formatting (app/core/responses.py)
      ↓
HTTP JSON Response
```

### 2. Why We Use Decimal Instead of Float

In pharmacy calculations (such as MRP, unit purchase cost, and taxes), floating-point arithmetic introduces rounding inaccuracies due to binary fraction representation. Using Python's `Decimal` type ensures exact precision down to the cent/paisa.

### 3. How /docs Works

FastAPI automatically reads Python type annotations, Pydantic models, docstrings, query parameters, and status codes. It compiles them into an OpenAPI 3.1 schema accessible at `/openapi.json`. Swagger UI reads this JSON file and generates the interactive documentation at `/docs`.

---

## Implemented API Endpoints

| Method | URL Path | Description | Status Code |
| :--- | :--- | :--- | :--- |
| `GET` | `/` | API Root information and documentation links | 200 OK |
| `GET` | `/health` | Liveness health probe | 200 OK |
| `POST` | `/api/v1/auth/login` | Operational user login | 200 OK |
| `GET` | `/api/v1/products` | Search and list products with pagination | 200 OK |
| `POST` | `/api/v1/products` | Create a new product SKU | 201 Created |
| `GET` | `/api/v1/products/{id}` | Get product details and total available stock | 200 OK |
| `PUT` | `/api/v1/products/{id}` | Update product details | 200 OK |
| `GET` | `/api/v1/inventory/batches` | List inventory batches with filters | 200 OK |
| `GET` | `/api/v1/inventory/fefo/{product_id}` | Retrieve batches sorted by earliest expiry first | 200 OK |
| `GET` | `/api/v1/inventory/alerts/low-stock` | Retrieve products with stock at or below reorder level | 200 OK |
| `GET` | `/api/v1/inventory/alerts/expiry-risk` | Retrieve batches expiring within threshold days | 200 OK |
| `POST` | `/api/v1/inventory/adjustments` | Record physical stock adjustment and audit log | 201 Created |
| `GET` | `/api/v1/suppliers` | List registered suppliers with pagination | 200 OK |
| `POST` | `/api/v1/suppliers` | Register a new supplier | 201 Created |

---

## Verification and Testing

The backend includes a comprehensive automated test suite in [`backend/tests/`](file:///d:/PharmaKon/pharmakon/backend/tests/):

- **`test_auth.py`**: Validates login success, credential rejection, and missing parameter validation.
- **`test_products.py`**: Validates product listing, search by text, category filtering, ID lookup, 404 responses, creation, duplicate SKU rejection, and update operations.
- **`test_inventory.py`**: Validates batch listing, FEFO sort order verification, low-stock threshold detection, expiry-risk threshold calculation, and stock adjustments with batch validation.
- **`test_suppliers.py`**: Validates supplier listing and creation.

### Test Execution Command

```bash
cd backend
pytest tests/ -v
```

**Result:** 20 out of 20 test cases passed.

---

## Next Steps for Future Sessions

1. **Database Integration**: Introduce PostgreSQL with SQLAlchemy 2.0 ORM and Alembic migrations to persist data beyond in-memory state.
2. **Sales POS & Billing**: Implement sales invoice generation, FEFO stock deduction upon sale, 13% VAT calculation, and custom selling rates.
3. **Purchasing Invoices**: Record supplier bills and automatically create/increment batch stock.
4. **Credit Ledger & Customer Returns**: Implement credit sale tracking and return verification.
