# Context — Coding Standards & Quality Guidelines

## 1. Backend Standards (Python 3.11 + FastAPI + SQLAlchemy)

### Code Style & Format
- Adhere strictly to **PEP 8**. Use `black` and `isort` formatting.
- Explicit type annotations are required for all function arguments and return signatures (`def calculate_vat(subtotal: Decimal) -> Decimal:`).
- Use `Decimal` or `NUMERIC(10,2)` for all monetary calculations (MRP, cost, revenue, VAT, discount). **Never use binary floating-point numbers (`float`) for currency!**

### FastAPI & Pydantic Conventions
- Define explicit request and response Pydantic models for every API endpoint.
- Use `status.HTTP_400_BAD_REQUEST` for business rule violations with clear error code strings.
- Use FastAPI Dependency Injection (`Depends()`) for database sessions and authentication.

### SQLAlchemy & Database Invariants
- Use SQLAlchemy 2.0 style queries (`select()`, `execute()`).
- Always run inventory mutations inside atomic database transactions (`async with session.begin():` or explicit commit/rollback blocks).
- Always generate a `StockMovementLog` entry when inventory quantity changes.

---

## 2. Frontend Standards (React + TypeScript + Vite)

### Code Style & Format
- Write strict TypeScript with `noImplicitAny: true`.
- Functional components with hooks only; avoid legacy class components.
- Modular component organization: `components/ui/`, `components/pos/`, `components/inventory/`, `pages/`, `services/api.ts`.

### Styling & UI
- Use **Tailwind CSS** for layout, spacing, and styling.
- Follow a clean, modern medical/healthcare color palette (Primary: Emerald/Teal `#059669`, Dark Neutral: Slate `#0f172a`, Accent: Amber `#f59e0b`).
- Ensure high contrast and touch/barcode scanner friendly focus states on the POS billing screen.

---

## 3. Testing Standards

- **Unit Tests (`pytest`):** Every service method handling pricing, tax, FEFO selection, or stock adjustment must have unit test coverage.
- **Integration Tests:** Test end-to-end POS sale creation, ensuring inventory decreases and stock movement logs are generated.
- **Negative Stock Test:** Explicit test verifying that attempting to purchase/sell more stock than available raises a 400 Bad Request error.
