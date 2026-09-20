# Context — System Architecture & Layering Rules

## Architecture Overview
PharmaKon is built as a **Modular Monolith** designed for reliability, fast POS responsiveness, and clean maintainability.

```text
React + TypeScript (Vite + Tailwind CSS)
       │
    REST API
       │
FastAPI Routers (Request Validation & OpenAPI)
       │
Service / Domain Layer (FEFO, Pricing Rules, Stock Calculations)
       │
Repository Layer (SQLAlchemy ORM Data Access)
       │
PostgreSQL Database (Transactional Source of Truth)
```

## Layer Responsibilities

### 1. Frontend Layer (`frontend/`)
- Pure presentation and user interaction.
- Handles UI state, form input validation, and API error messaging.
- **Rule:** Never execute core business logic (such as stock deduction calculation or FEFO batch selection) on the client side alone.

### 2. Router / API Layer (`backend/app/api/`)
- Manages HTTP endpoints, route parameters, and CORS.
- Uses Pydantic schemas to validate incoming payloads and serialize responses.
- Delegates all business processing to the Service Layer.

### 3. Service / Domain Layer (`backend/app/services/`)
- **Authoritative home of all pharmacy business rules.**
- Enforces FEFO batch ordering, negative-stock checks, custom price adjustments, VAT/discount computations, and stock movement log generation.
- Executes database operations within atomic transactions.

### 4. Repository Layer (`backend/app/repositories/`)
- Abstracts SQLAlchemy queries.
- Keeps raw database queries separate from domain business logic.

### 5. Analytics & ML Engine (`backend/app/analytics/` & `ml/`)
- Executes analytical SQL aggregations using Pandas and NumPy.
- Exposes demand forecasting models trained via scikit-learn/XGBoost.
- Provides grounded tool execution for the AI Assistant.
