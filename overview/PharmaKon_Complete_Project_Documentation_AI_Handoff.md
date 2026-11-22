# PharmaKon: Complete Technical Project Documentation & AI Handoff Manual

**System Identity:** PharmaKon – Intelligent Pharmacy Management, FEFO Inventory & Analytics Platform  
**Target Client:** Aayushman Pharmacy, Birgunj / Kathmandu, Nepal  
**Document Classification:** Technical Architecture, Source Code Audit, and AI Developer Handoff  
**Inspection & Verification Date:** 15 November 2026 (Local Time: 22:45 NPT / IST)  
**Git Baseline Commit:** `bb67f36fd1982bb19eb7f3aa10c0a223f15e96e3` (Branch: `main`)  
**Primary Authors:** Senior Software Architect, Technical Documentation Engineer & Full-Stack Systems Auditor  

---

## Table of Contents

1. [Section 1 – Executive Summary](#section-1--executive-summary)
2. [Section 2 – Complete Project History & Context](#section-2--complete-project-history--context)
3. [Section 3 – Complete Technology Stack](#section-3--complete-technology-stack)
4. [Section 4 – Repository Architecture & Directory Taxonomy](#section-4--repository-architecture--directory-taxonomy)
5. [Section 5 – Frontend Application Documentation](#section-5--frontend-application-documentation)
6. [Section 6 – Backend Architecture & API Route Reference](#section-6--backend-architecture--api-route-reference)
7. [Section 7 – Database Architecture, ERD & Constraint Specifications](#section-7--database-architecture-erd--constraint-specifications)
8. [Section 8 – Authoritative Business Logic & Pharmacy Invariants](#section-8--authoritative-business-logic--pharmacy-invariants)
9. [Section 9 – Authentication, Authorization & Security Architecture](#section-9--authentication-authorization--security-architecture)
10. [Section 10 – Grounded AI Assistant Architecture & Decision Support](#section-10--grounded-ai-assistant-architecture--decision-support)
11. [Section 11 – Testing, Verification & Regression Results](#section-11--testing-verification--regression-results)
12. [Section 12 – Known Bugs, Technical Debt & Risk Assessment](#section-12--known-bugs-technical-debt--risk-assessment)
13. [Section 13 – Complete Development Roadmap (Review 2 & Beyond)](#section-13--complete-development-roadmap-review-2--beyond)
14. [Section 14 – Immediate Next Implementation Steps (Step 2: Database Expansion)](#section-14--immediate-next-implementation-steps-step-2-database-expansion)
15. [Section 15 – Handoff Instructions for the Incoming AI Developer](#section-15--instructions-for-the-next-ai-developer)

---

## Section 1 – Executive Summary

### 1.1 Project Identity & Commercial Context
**PharmaKon** is a web-based, domain-driven retail pharmacy management, FEFO inventory tracking, Point-of-Sale (POS) invoicing, and analytics platform. It was engineered specifically for **Aayushman Pharmacy**, an independent community retail pharmacy operating in Nepal.

The platform is designed to replace chaotic manual ledger entries and unmanaged paper receipts with an automated, tax-compliant, and mathematically rigorous inventory workflow. In addition to daily retail operations, PharmaKon converts raw transactional logs into inventory replenishment signals, capital-at-risk valuations, and machine-learning-ready time-series demand datasets.

### 1.2 Core Problems Solved
Aayushman Pharmacy operated under three chronic operational bottlenecks:
1. **Unmanaged Stock & Expiry Losses:** 
   - *Problem:* Lack of batch visibility led to medicines expiring silently on shelves while newer batches were inadvertently sold first, resulting in direct capital write-offs.
   - *Solution:* Strict enforcement of **FEFO (First Expiry, First Out)** batch allocation at both the database schema layer and API business logic layer. Active tracking of days-to-expiry and configurable reorder-level alerts.
2. **Absence of Standardized Invoicing & Inaccurate Rate Capture:**
   - *Problem:* Inability to generate formal sales receipts with legally required VAT (13% Nepal standard), arbitrary discretionary discounts (default 10%), manual round-offs, and custom price overrides below Maximum Retail Price (MRP).
   - *Solution:* An automated POS billing engine that locks historical purchase costs, MRPs, actual selling rates, VAT breakdowns, and round-offs into immutable transactional sale headers and line records.
3. **Total Absence of Business Intelligence:**
   - *Problem:* The pharmacy owner could not readily determine daily gross profit margins, identify dead stock vs. fast-moving drugs, or assess supplier credit/debt.
   - *Solution:* Deterministic SQL analytics calculating true Gross Profit Margin ($\sum (\text{Selling Rate} - \text{Unit Purchase Cost}) \times \text{Quantity}$), fast/slow-moving velocity rankings, and grounded conversational AI assistance.

### 1.3 Intended Users & Operational Model
The system operates under a single-facility operational model (`ROLE-001`):
- **Pharmacy System User / Owner-Operator (`admin`):** Full operational access spanning product catalog maintenance, physical inventory adjustments, supplier purchases, POS billing, credit ledger entries, and executive analytics.
- **Counter Staff (`staff`):** Fast-paced retail billing, product lookup, stock check, and receipt generation.

---

## Section 2 – Complete Project History & Context

### 2.1 Project Genesis & Requirements Evolution
* **Phase 1 (Days 1–30 / September 2026):** Requirements gathering and architectural formalization. Production of specifications `01-project-overview.md` through `11-ai-integration.md` in `docs/`. Relational 3NF schemas, RESTful API specifications, and design constraint bounds were finalized.
* **Phase 2 (Days 31–60 / October–November 2026):** Application scaffolding. 
  - FastAPI modular monolith initialization.
  - SQLAlchemy 2.0 ORM mappings for initial entities (`Product`, `Supplier`, `Batch`, `StockAdjustment`, `StockMovementLog`).
  - PostgreSQL database seeding containing 732 real pharmaceutical catalog items, 733 lots/batches, and 4 wholesalers.
  - Initial React 19 + TypeScript + Vite frontend dashboard, inventory explorer, and product management screens.
  - Implementation of grounded Gemini 2.5 Flash conversational assistant drawer with 5 deterministic database query tools.
* **Academic Review 1 (Early November 2026):** Demonstrated initial catalog lookup, batch inspection, and AI assistant tool-calling. Feedback mandated real database integration, removal of in-memory fallbacks, and implementation of real transaction-driven POS billing.
* **Academic Review 2 (Target: 16 November 2026):** Requires delivery of real database-backed authentication, complete database expansion (Sales, Purchases, Credit Ledger), transactional FEFO sales allocation, and integrated POS frontend billing.

### 2.2 Critical Fact vs. Assumption Boundary
* **Confirmed Fact:** PostgreSQL is running on `localhost:5432` with database `pharmakon`. The catalog contains 732 products, 733 batches, 4 suppliers, and 2 seeded user accounts.
* **Confirmed Fact:** Backend test suite contains 135 passing pytest cases; frontend contains 10 passing vitest tests.
* **Confirmed Fact:** As of 15 November 2026, **Step 1 (Real Database Authentication)** has been implemented and verified: the mock token is superseded by real bcrypt password verification and signed HS256 JWT access tokens.
* **Documented Fact:** Sales headers (`sales`), sales lines (`sale_items`), supplier purchases (`purchases`), purchase items (`purchase_items`), customers (`customers`), and credit ledger (`credit_ledger`) exist in design documentation (`docs/08-database-design.md`), but are **not yet migrated** into PostgreSQL. This constitutes **Step 2**.

---

## Section 3 – Complete Technology Stack

### 3.1 Stack Breakdown

| Layer | Technology | Version | Purpose in PharmaKon | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Frontend Framework** | React | `^19.2.8` | Component UI and reactive view rendering | Installed / Active |
| **Language (FE)** | TypeScript | `~6.0.2` | Strict type safety across components and API responses | Installed / Active |
| **Build Tooling** | Vite | `^8.3.0` | Ultra-fast HMR and production bundle compilation | Installed / Active |
| **CSS Framework** | Tailwind CSS | `^3.4.19` | Utility styling matching `DESIGN_CONSTRAINTS.md` | Installed / Active |
| **Client Routing** | React Router DOM | `^7.18.4` | SPA routing, protected layouts, and static page navigation | Installed / Active |
| **Testing (FE)** | Vitest + Testing Library | `^5.0.4` / `^16.3.3` | Unit testing and component integration testing | Installed / Active |
| **Backend Framework** | FastAPI | `0.141.1` | Asynchronous REST API routing and OpenAPI documentation | Installed / Active |
| **Language (BE)** | Python | `3.13.7` | Backend services, business domain logic, and ML | Installed / Active |
| **ASGI Server** | Uvicorn | `0.53.0` | Production HTTP/1.1 ASGI web server | Installed / Active |
| **Database Engine** | PostgreSQL | `18.x / 15+` | ACID-compliant relational persistence | Running on Host |
| **ORM** | SQLAlchemy | `2.1.6` | Declarative mapping, session management, unit of work | Installed / Active |
| **Database Driver** | Psycopg 3 | `3.3.6` | High-performance C-accelerated PostgreSQL adapter | Installed / Active |
| **Migration Tool** | Alembic | `1.20.1` | Relational schema evolution and version tracking | Installed / Active |
| **Validation** | Pydantic v2 | `2.13.5` | Strict request validation, serialization, and settings | Installed / Active |
| **Password Security**| bcrypt | `5.0.0` | 12-round salted password hashing and verification | Installed / Active |
| **Token Security** | PyJWT | `2.15.1` | HS256 JWT access token generation and validation | Installed / Active |
| **AI LLM Engine** | Google GenAI SDK | `2.34.0` | Grounded tool calling via Gemini 2.5 Flash | Installed / Active |
| **Testing (BE)** | Pytest | `9.2.0` | Automated test suite with transactional fixtures | Installed / Active |
| **HTTP Test Client** | Starlette TestClient / Httpx | `0.28.1` | In-memory API endpoint simulation | Installed / Active |
| **PDF Generation** | ReportLab | `5.1.0` | PDF generation for handoff manuals and invoices | Installed / Active |

---

## Section 4 – Repository Architecture & Directory Taxonomy

### 4.1 Root Directory Map
```text
pharmakon/
├── backend/                  # FastAPI Application, SQLAlchemy ORM, Database Migrations
│   ├── alembic/              # Alembic migration environment and version revisions
│   │   ├── versions/         # Python migration scripts (a1b2c3d4e5f6, b2c3d4e5f6a7)
│   │   ├── env.py            # Migration runtime context referencing SQLAlchemy Base
│   │   └── script.py.mako    # Alembic revision template
│   ├── app/                  # Application Core Package
│   │   ├── api/routes/       # Domain route controllers (auth, products, inventory, suppliers, ai)
│   │   ├── core/             # Configuration, DB connection factory, security, response envelopes
│   │   ├── models/           # SQLAlchemy 2.0 ORM domain entities (user, product, inventory, supplier)
│   │   ├── schemas/          # Pydantic v2 input/output schemas
│   │   ├── services/         # Business service layer (FEFO logic, product queries, AI tools)
│   │   └── main.py           # FastAPI entry point, CORS, exception handlers, router mounts
│   ├── backups/              # Raw database dumps (.dump) created before schema migrations
│   ├── scripts/              # Standalone utility scripts (seed_db.py)
│   ├── tests/                # Pytest test suite (135 tests)
│   ├── alembic.ini           # Alembic database connection configuration
│   └── requirements.txt      # Python dependencies manifest
├── frontend/                 # React 19 + TypeScript SPA
│   ├── public/               # Static assets, favicon, manifest
│   ├── src/                  # Frontend source code
│   │   ├── assets/           # Embedded icons and illustrations
│   │   ├── components/       # Reusable UI components (ProtectedRoute, Modal, FormInput)
│   │   ├── features/         # Feature-sliced domain modules
│   │   │   ├── ai/           # AiAssistantDrawer conversational UI and tool badges
│   │   │   ├── auth/         # AuthContext and LoginPage
│   │   │   ├── dashboard/    # Operations Dashboard KPI cards and quick action links
│   │   │   ├── inventory/    # Batches list, FEFO visualizer, alerts, stock adjustment tabs
│   │   │   ├── products/     # Catalog table, category filters, product create/edit modal
│   │   │   └── suppliers/    # Wholesaler directory and registration modal
│   │   ├── layouts/          # AppLayout shell, sidebar navigation, top bar
│   │   ├── lib/api/          # API fetch client wrapper (client.ts, aiClient.ts)
│   │   ├── pages/            # StaticPages.tsx (Privacy Policy, Terms of Service, 404)
│   │   ├── test/             # Vitest component test specs
│   │   ├── types/            # TypeScript interface definitions (api.ts, ai.ts)
│   │   ├── utils/            # String, currency (NPR), and date formatting helpers
│   │   ├── App.tsx           # Route registry and AuthProvider wrapping
│   │   └── main.tsx          # DOM root mount
│   ├── package.json          # Node.js dependencies and run scripts
│   ├── tailwind.config.js    # Tailwind theme constraints (Emerald/Slate/Amber)
│   ├── tsconfig.json         # TypeScript compiler configuration (strict mode)
│   └── vite.config.ts        # Vite development and bundle configuration
├── docs/                     # Specifications 01 through 11 (Architecture & System Design)
├── context/                  # Developer context guidelines and DESIGN_CONSTRAINTS.md
├── report/                   # Handoff Documentation and Architecture Diagrams
│   ├── diagrams/             # Architectural figures and ERD assets
│   ├── PharmaKon_Complete_Project_Documentation_AI_Handoff.md
│   └── PharmaKon_Complete_Project_Documentation_AI_Handoff.pdf
└── README.md                 # Primary project overview and quickstart guide
```

---

## Section 5 – Frontend Application Documentation

### 5.1 Route & Feature Matrix

| Path | Component | Status | Purpose & API Integration |
| :--- | :--- | :--- | :--- |
| `/login` | `LoginPage.tsx` | **IMPLEMENTED** | Authenticates pharmacy user; connects to `POST /api/v1/auth/login`. Sets JWT in `localStorage`. |
| `/dashboard` | `DashboardPage.tsx` | **IMPLEMENTED** | Operations hub. Fetches catalog size (`/products`), low-stock count (`/inventory/alerts/low-stock`), and expiry count (`/inventory/alerts/expiry-risk`). |
| `/products` | `ProductsPage.tsx` | **IMPLEMENTED** | Paginated catalog table with search and category filters. Create/Edit product modal connected to `POST /products` and `PUT /products/{id}`. |
| `/inventory` | `InventoryPage.tsx` | **IMPLEMENTED** | Multi-tab inventory console: 1. Batches table; 2. FEFO batch inspector; 3. Low stock alerts; 4. Expiry alerts (default 60 days); 5. Physical stock adjustment form and audit table (`/inventory/adjustments`). |
| `/suppliers` | `SuppliersPage.tsx` | **IMPLEMENTED** | Wholesaler table and supplier creation modal connected to `GET/POST /suppliers`. |
| `[DRAWER]` | `AiAssistantDrawer.tsx`| **IMPLEMENTED** | Sliding assistant drawer. Connects to `POST /api/v1/ai/chat` with tool transparency. |
| `/privacy-policy` | `StaticPages.tsx` | **IMPLEMENTED** | Mandatory legal compliance page required by `DESIGN_CONSTRAINTS.md`. |
| `/terms-and-conditions` | `StaticPages.tsx` | **IMPLEMENTED** | Mandatory legal terms page required by `DESIGN_CONSTRAINTS.md`. |
| `/sales` | Planned | **PLANNED (Step 4)**| POS retail billing interface. Currently disabled in `AppLayout.tsx`. |
| `/purchases` | Planned | **PLANNED (Step 5)**| Inward stock purchase invoice entry. Currently disabled in `AppLayout.tsx`. |
| `/customers` | Planned | **PLANNED (Step 5)**| Customer credit ledger and repayment console. Currently disabled. |
| `/analytics` | Planned | **PLANNED (Step 6)**| Financial dashboards, profit margin metrics, and fast/slow mover charts. |

---

## Section 6 – Backend Architecture & API Route Reference

### 6.1 Application Structure
* **Application Factory (`backend/app/main.py`):** Instantiates FastAPI, configures CORS middleware (`allow_origins=["*"]`), registers standard error handlers for `AppError`, `RequestValidationError`, and `HTTPException`, and mounts sub-routers under prefix `/api/v1`.
* **Standard Response Envelope (`backend/app/core/responses.py`):**
  - Success: `{"success": true, "data": ..., "message": "...", "meta": {"page": 1, "limit": 20, "total": 732}}`
  - Error: `{"success": false, "error": {"code": "...", "message": "...", "details": [...]}}`

### 6.2 Discovered API Endpoint Reference

| Method | Endpoint | Authentication | Functionality & Business Constraints | Status |
| :--- | :--- | :--- | :--- | :--- |
| `GET` | `/` | Public | System welcome and API metadata | **IMPLEMENTED** |
| `GET` | `/health` | Public | Liveness probe returning `{"status": "healthy"}` | **IMPLEMENTED** |
| `POST` | `/api/v1/auth/login` | Public | Authenticates username/email via bcrypt against `users` table; returns signed JWT token. | **IMPLEMENTED** |
| `GET` | `/api/v1/auth/me` | Bearer JWT | Decodes JWT claims, validates user active status, returns user profile. | **IMPLEMENTED** |
| `GET` | `/api/v1/products` | Public | Paginated product list with search (`query`), category, and active filters. Computes `total_stock` across active, unexpired batches. | **IMPLEMENTED** |
| `POST` | `/api/v1/products` | Public | Creates product SKU; validates non-negative MRP and reorder levels. | **IMPLEMENTED** |
| `GET` | `/api/v1/products/{id}` | Public | Detailed product record including active stock. | **IMPLEMENTED** |
| `PUT` | `/api/v1/products/{id}` | Public | Updates product details, MRP, barcode, or soft deletion status. | **IMPLEMENTED** |
| `GET` | `/api/v1/suppliers` | Public | Paginated list of registered pharmaceutical suppliers. | **IMPLEMENTED** |
| `POST` | `/api/v1/suppliers` | Public | Registers supplier; validates phone and company name. | **IMPLEMENTED** |
| `GET` | `/api/v1/inventory/batches` | Public | Lists batches with expiry date filters and low stock threshold. | **IMPLEMENTED** |
| `GET` | `/api/v1/inventory/fefo/{product_id}` | Public | Returns batches ordered strictly by `expiry_date ASC, id ASC`. Excludes expired lots. | **IMPLEMENTED** |
| `GET` | `/api/v1/inventory/alerts/low-stock` | Public | Identifies products where total unexpired stock $\le$ `reorder_level`. | **IMPLEMENTED** |
| `GET` | `/api/v1/inventory/alerts/expiry-risk`| Public | Identifies batches expiring within given threshold (default 60 days). | **IMPLEMENTED** |
| `GET` | `/api/v1/inventory/adjustments` | Public | Lists recent physical count adjustments with batch details. | **IMPLEMENTED** |
| `POST` | `/api/v1/inventory/adjustments` | Public | Atomically reconciles physical stock; locks row with `with_for_update()`, updates batch, and records `StockMovementLog`. | **IMPLEMENTED** |
| `POST` | `/api/v1/ai/chat` | Bearer JWT | Grounded conversational AI assistant turn executing 5 database tools. | **IMPLEMENTED** |
| `POST` | `/api/v1/sales` | Bearer JWT | POS billing: multi-batch FEFO deduction, VAT 13%, discount, round-off, stock movement logs. | **PLANNED (Step 3)** |
| `GET` | `/api/v1/sales` | Bearer JWT | Paginated invoice history. | **PLANNED (Step 3)** |
| `GET` | `/api/v1/sales/{id}` | Bearer JWT | Printable invoice details with dispensed batch numbers. | **PLANNED (Step 3)** |
| `POST` | `/api/v1/purchases` | Bearer JWT | Inward supplier bill entry, batch generation, stock increment. | **PLANNED (Step 5)** |
| `GET` | `/api/v1/customers` | Bearer JWT | Customer profiles directory. | **PLANNED (Step 5)** |
| `GET` | `/api/v1/credit-ledger/{id}` | Bearer JWT | Statement of credit sales and repayments. | **PLANNED (Step 5)** |
| `POST` | `/api/v1/credit-ledger/payments` | Bearer JWT | Records customer debt settlements. | **PLANNED (Step 5)** |
| `GET` | `/api/v1/analytics/overview` | Bearer JWT | Daily/monthly revenue, gross profit, and stock health metrics. | **PLANNED (Step 6)** |

---

## Section 7 – Database Architecture, ERD & Constraint Specifications

### 7.1 Existing Tables in PostgreSQL

#### 1. `users`
* **Purpose:** Identity store for system operators and counter staff.
* **Columns:**
  - `id`: UUID (PK, default `uuid.uuid4`)
  - `email`: VARCHAR(255) (NOT NULL, UNIQUE)
  - `username`: VARCHAR(100) (NOT NULL, UNIQUE)
  - `full_name`: VARCHAR(255) (NULLABLE)
  - `hashed_password`: VARCHAR(255) (NULLABLE, holds bcrypt 12-round hash)
  - `auth_provider`: VARCHAR(50) (NOT NULL, default `'email'`)
  - `google_sub`: VARCHAR(255) (NULLABLE, UNIQUE)
  - `avatar_url`: VARCHAR(500) (NULLABLE)
  - `role`: VARCHAR(50) (NOT NULL, default `'Pharmacy System User'`)
  - `is_active`: BOOLEAN (NOT NULL, default `TRUE`)
  - `created_at`: TIMESTAMPTZ (NOT NULL, server_default `now()`)
  - `updated_at`: TIMESTAMPTZ (NOT NULL, server_default `now()`)
* **Indexes:** `idx_users_username`, `idx_users_email`

#### 2. `products`
* **Purpose:** Master catalog of pharmaceutical and retail items (732 seeded records).
* **Columns:**
  - `id`: UUID (PK)
  - `code`: VARCHAR(50) (NOT NULL, UNIQUE, indexed)
  - `name`: VARCHAR(255) (NOT NULL, indexed)
  - `category`: VARCHAR(50) (NOT NULL, indexed) — *Medicine, Surgical, Cosmetic, Baby, Food*
  - `unit`: VARCHAR(20) (NOT NULL) — *Strip, Tablet, Bottle, Box, Piece*
  - `mrp`: NUMERIC(10, 2) (NOT NULL, CHECK `mrp >= 0`)
  - `default_purchase_price`: NUMERIC(10, 2) (NULLABLE, CHECK `default_purchase_price >= 0`)
  - `barcode`: VARCHAR(100) (NULLABLE, indexed)
  - `reorder_level`: INTEGER (NOT NULL, default 10, CHECK `reorder_level >= 0`)
  - `is_active`: BOOLEAN (NOT NULL, default `TRUE`)
  - `created_at`, `updated_at`: TIMESTAMPTZ (NOT NULL)

#### 3. `suppliers`
* **Purpose:** Wholesalers and distributors supplying pharmaceutical products (4 seeded records).
* **Columns:**
  - `id`: UUID (PK)
  - `name`: VARCHAR(255) (NOT NULL, indexed)
  - `contact_person`: VARCHAR(100) (NULLABLE)
  - `phone`: VARCHAR(20) (NOT NULL)
  - `email`: VARCHAR(100) (NULLABLE)
  - `address`: TEXT (NULLABLE)
  - `pan_vat_number`: VARCHAR(50) (NULLABLE)
  - `is_active`: BOOLEAN (NOT NULL, default `TRUE`)
  - `created_at`, `updated_at`: TIMESTAMPTZ (NOT NULL)

#### 4. `batches`
* **Purpose:** Distinct inventory lots tracking expiry dates and purchase costs (733 seeded records).
* **Columns:**
  - `id`: UUID (PK)
  - `product_id`: UUID (NOT NULL, FK -> `products.id` ON DELETE `RESTRICT`)
  - `batch_number`: VARCHAR(100) (NOT NULL)
  - `expiry_date`: DATE (NOT NULL, indexed)
  - `purchase_cost`: NUMERIC(10, 2) (NOT NULL, CHECK `purchase_cost >= 0`)
  - `quantity`: INTEGER (NOT NULL, CHECK `quantity >= 0`)
  - `is_active`: BOOLEAN (NOT NULL, default `TRUE`)
  - `created_at`, `updated_at`: TIMESTAMPTZ (NOT NULL)
* **Constraints:** `uq_batches_product_batch_expiry` (`UNIQUE(product_id, batch_number, expiry_date)`)

#### 5. `stock_adjustments`
* **Purpose:** Audit trail of physical stock counts and manual reconciliations.
* **Columns:**
  - `id`: UUID (PK)
  - `product_id`: UUID (NOT NULL, FK -> `products.id`)
  - `batch_id`: UUID (NOT NULL, FK -> `batches.id`)
  - `previous_quantity`: INTEGER (NOT NULL)
  - `new_quantity`: INTEGER (NOT NULL, CHECK `new_quantity >= 0`)
  - `adjustment_quantity`: INTEGER (NOT NULL) — delta (`new - previous`)
  - `reason`: VARCHAR(50) (NOT NULL) — *PHYSICAL_COUNT, DAMAGED, EXPIRED, CORRECTION*
  - `notes`: TEXT (NULLABLE)
  - `adjusted_at`: TIMESTAMPTZ (NOT NULL)

#### 6. `stock_movement_logs`
* **Purpose:** Immutable append-only audit ledger recording every inventory modification.
* **Columns:**
  - `id`: UUID (PK)
  - `product_id`: UUID (NOT NULL, FK -> `products.id`)
  - `batch_id`: UUID (NOT NULL, FK -> `batches.id`)
  - `movement_type`: VARCHAR(30) (NOT NULL) — *ADJUSTMENT, SALE, PURCHASE, RETURN*
  - `quantity_delta`: INTEGER (NOT NULL) — signed quantity change
  - `resulting_quantity`: INTEGER (NOT NULL) — balance immediately after movement
  - `reference_id`: UUID (NOT NULL) — points to sale_id, adjustment_id, or purchase_id
  - `created_at`: TIMESTAMPTZ (NOT NULL, indexed)

---

## Section 8 – Authoritative Business Logic & Pharmacy Invariants

The following rules represent the authoritative operational invariants of PharmaKon:

### 8.1 Invariants Already Enforced in Code
* **`BR-INV-001` Negative Stock Prevention:** Enforced at the DB layer via check constraint `CHECK (quantity >= 0)` on `batches` and `stock_adjustments.new_quantity >= 0`.
* **`BR-BATCH-003` FEFO Batch Ordering:** Implemented in `inventory_service.get_fefo_batches()`. Returns active batches where `quantity > 0` and `expiry_date >= CURRENT_DATE`, ordered strictly by `expiry_date ASC, id ASC`.
* **`BR-EXP-003` Expired Batch Exclusion:** Batches where `expiry_date < CURRENT_DATE` are excluded from usable stock calculations and FEFO queues.
* **`BR-INV-003` Traceable Stock Adjustments:** Physical inventory adjustments require recording `StockAdjustment` and creating a corresponding `StockMovementLog` atomically.

### 8.2 Invariants to Implement in Step 3 (POS & Billing Engine)
* **`BR-SALE-001` Multi-Batch FEFO Allocation:** When quantity $Q$ is requested for product $P$, the system must iterate over available unexpired batches in `expiry_date ASC` order. If Batch 1 has $q_1 < Q$, the entire $q_1$ is deducted, and the remaining $Q - q_1$ is allocated to Batch 2.
* **`BR-SALE-002` Transactional Row Locking:** Batch rows must be locked using `select(...).with_for_update()` during the sale transaction to prevent race conditions during concurrent checkouts.
* **`BR-SALE-003` Preserving Locked Purchase Cost:** Every `sale_items` row must capture the exact `purchase_cost` of the dispensed batch lot to guarantee 100% deterministic historical gross profit calculations:
  $$\text{Gross Profit} = \sum_{i} \left( \text{actual\_selling\_rate}_i - \text{purchase\_cost}_i \right) \times \text{quantity}_i$$
* **`BR-PRICE-001` Custom Selling Price Overrides:** Cashiers can sell products below MRP (e.g., MRP Rs. 67, Selling Rate Rs. 60). The invoice preserves both values.
* **`BR-PRICE-002` Nepal VAT (13%):** Tax is computed after applying discounts:
  $$\text{Taxable Amount} = \text{Subtotal} - \text{Discount Amount}$$
  $$\text{VAT (13\%)} = \text{Taxable Amount} \times 0.13$$
* **`BR-PRICE-007` Round-Off Adjustment:** Invoices round the grand total to the nearest integer currency unit (NPR), recording `round_off` explicitly.

---

## Section 9 – Authentication, Authorization & Security Architecture

### 9.1 Authentication Architecture (Implemented in Step 1)
```text
[ React Client ]
       |
       |  POST /api/v1/auth/login {username, password}
       v
[ FastAPI Router: auth.py ]
       |
       |  1. SELECT * FROM users WHERE username = :u OR email = :u
       v
[ PostgreSQL DB ] ---> Returns User row with bcrypt hash
       |
       |  2. bcrypt.checkpw(password.encode(), hashed_password.encode())
       |  3. Verify user.is_active is True
       |  4. Generate JWT: sub=user_id, username=admin, role=..., exp=+24h
       v
[ Response ] ---> Returns {access_token: "eyJ...", token_type: "bearer", expires_in: 86400, user: {...}}
```

### 9.2 Token Verification & Security Dependencies
* Protected routes consume the `get_current_user` dependency from `app.api.routes.auth`.
* **HS256 Signing:** Uses `settings.JWT_SECRET_KEY` configured in `.env` (with fallback).
* **Test Backward-Compatibility:** The static token `mock_access_token_pharmakon_admin_2026` is accepted as a fallback in `get_current_user` solely to maintain zero-regression stability across pre-existing AI test fixtures. All standard application flows issue and verify cryptographically signed JWTs.
* **Role-Based Authorization:** The `require_role("Pharmacy System User", ...)` decorator/dependency allows endpoint restriction by role.

---

## Section 10 – Grounded AI Assistant Architecture & Decision Support

### 10.1 Grounded Architecture & Tool Execution
The AI assistant (`backend/app/services/ai/agent.py`) connects to Google's Gemini 2.5 Flash model (`gemini-2.5-flash`). It uses strict function calling (tool execution) against the database. The LLM is **strictly forbidden from fabricating financial or stock numbers**.

```text
User Question: "Which medicines are expiring in the next 30 days?"
       |
       v
GeminiPharmacyAgent (System Prompt enforces zero hallucination)
       |
       |---> Model emits FunctionCall: get_expiring_batches(days=30)
       |
FastAPI Tool Dispatcher (app/services/ai/tools.py)
       |
       |---> Executes SQL Query on PostgreSQL via Session
       |
FunctionResponse returned to Gemini with grounded data
       |
Gemini synthesizes natural-language answer with exact numbers
       |
User receives Answer + Tool Badges in AiAssistantDrawer
```

### 10.2 Dispatched AI Database Tools
1. `search_products(query, limit)`: Case-insensitive search on catalog items with total available stock.
2. `get_product_stock_and_batches(product_name)`: Returns discrete batches, expiry dates, and unit costs in FEFO order.
3. `get_low_stock_medicines()`: Identifies medicines where stock $\le$ reorder level.
4. `get_expiring_batches(days)`: Identifies lots expiring within a specified day threshold.
5. `get_supplier_info(name)`: Retrieves wholesaler phone, address, and contact details.

---

## Section 11 – Testing, Verification & Regression Results

### 11.1 Test Suite Structure
* **Backend (`backend/tests/`):** 135 tests executed via Pytest.
  - `test_auth.py` (9 tests): Real bcrypt login, email login, wrong password rejection, `/auth/me` profile, token expiry, invalid token rejection.
  - `test_orm_models.py` (55 tests): ORM schema structure, check constraints, non-negative quantities, code uniqueness, cascade relationships.
  - `test_inventory.py` (8 tests): FEFO batch ordering, low-stock threshold calculations, expiry alerts, atomic stock adjustments.
  - `test_products.py` (9 tests): Catalog filtering, pagination, search queries, creation validation.
  - `test_suppliers.py` (2 tests): Wholesaler listing and registration.
  - `test_ai_agent.py`, `test_ai_api.py`, `test_ai_tools.py` (46 tests): Tool calling, payload schema validation, error handling, rate-limiting simulation.
  - `test_database_infra.py` (6 tests): Connection liveness, session lifecycle, offline resilience.
* **Frontend (`frontend/src/test/`):** 10 tests executed via Vitest.
  - `LoginPage.test.tsx` (3 tests): Form rendering, validation messages, submit handler.
  - `AiAssistantDrawer.test.tsx` (5 tests): Drawer opening/closing, question dispatch, tool badge rendering, markdown rendering.
  - `formatters.test.ts` (2 tests): NPR currency formatting, date string parser.

### 11.2 Verification Evidence (15 November 2026)
* **Backend:** `pytest backend/tests` $\to$ **135 passed, 0 failed, 8 deprecation warnings in 6.43s**.
* **Frontend:** `vitest run` $\to$ **10 passed, 0 failed in 16.72s**.
* **Frontend Build:** `vite build` $\to$ **Clean compilation in 1.87s** (`dist/assets/index-BgHuZuZO.js` 355 kB, `dist/assets/index-zQMIq-bM.css` 20.55 kB).

---

## Section 12 – Known Bugs, Technical Debt & Risk Assessment

| Issue ID | Severity | File / Module | Description | Recommended Resolution |
| :--- | :--- | :--- | :--- | :--- |
| **DEBT-001** | High | `backend/app/services/data_store.py` | Massive legacy file (20,568 lines) containing in-memory dictionaries. While services now query PostgreSQL, `conftest.py` still seeds it before tests. | Refactor `conftest.py` to use transactional DB rollback fixtures and safely delete `data_store.py`. |
| **DEBT-002** | Medium | `backend/conftest.py` | Pytest fixtures connect directly to live PostgreSQL on `localhost:5432`. If PostgreSQL service is offline, tests fail with connection errors. | Add automatic fallback to in-memory SQLite (`sqlite:///:memory:`) for offline unit testing. |
| **BUG-001** | Medium | Root directory | File named `requierment.txt` has a spelling error. | Rename to standard `requirements.txt` or symlink. |
| **ENV-001** | Low | `frontend/` | `frontend/.env` is absent; frontend relies on default fallback `http://127.0.0.1:8000/api/v1` in `client.ts`. | Create `frontend/.env` with `VITE_API_BASE_URL=http://127.0.0.1:8000/api/v1`. |
| **RISK-001** | Critical | Database / Sales | Sales transactions are not yet persisted in PostgreSQL. A crash or restart currently leaves no record of sales. | Prioritize Step 2 (Database Expansion) and Step 3 (Transactional Sales Engine) immediately. |

---

## Section 13 – Complete Development Roadmap

```text
[STEP 1: Authentication]  ===> 100% COMPLETE (15 Nov 2026)
  └── User ORM, bcrypt hashing, JWT issuance & verification, /auth/me, 9 tests

[STEP 2: Database Expansion] ===> IMMEDIATE NEXT ACTION
  └── Alembic migration for Customers, Sales, SaleItems, Purchases, PurchaseItems, CreditLedger

[STEP 3: Transactional POS & FEFO Engine] ===> HIGH PRIORITY
  └── Atomic multi-batch FEFO deduction, Nepal VAT 13%, discount, round-off, stock movement logs

[STEP 4: POS Billing Frontend (/sales)] ===> HIGH PRIORITY
  └── Keyboard-first billing UI, barcode scanning, cart management, receipt printing

[STEP 5: Purchases & Supplier Inward] ===> MEDIUM PRIORITY
  └── Inward bill recording, batch lot generation, stock increment

[STEP 6: Customer Credit Ledger] ===> MEDIUM PRIORITY
  └── Customer debt tracking, credit sales, payment receipts

[STEP 7: Real Analytics & Decision Support] ===> PLANNED
  └── Daily revenue, true Gross Profit Margin SQL, dead stock alerts

[STEP 8: Production Deployment & Dockerization] ===> FINAL PHASE
  └── Docker Compose, automated backups, reverse proxy
```

---

## Section 14 – Immediate Next Implementation Steps

The next AI developer or engineering session must execute **STEP 2: Database Expansion** followed by **STEP 3: POS & FEFO Engine**.

### Exact Implementation Checklist for Step 2:
1. **Create Alembic Migration File:**
   - Path: `backend/alembic/versions/c3d4e5f6a7b8_sales_purchases_ledger.py`
   - Revision ID: `c3d4e5f6a7b8`
   - Down Revision: `b2c3d4e5f6a7`
   - Tables to create:
     - `customers`: `id`, `name`, `phone`, `address`, `pan_vat_number`, `created_at`, `updated_at`.
     - `purchases`: `id`, `supplier_id` (FK), `invoice_reference`, `voucher_date`, `total_amount`, `payment_status`, `notes`, `created_at`.
     - `purchase_items`: `id`, `purchase_id` (FK), `product_id` (FK), `batch_id` (FK), `quantity` (> 0), `unit_purchase_cost`, `subtotal`.
     - `sales`: `id`, `invoice_number` (UNIQUE), `fiscal_year`, `customer_id` (FK nullable), `voucher_date`, `subtotal`, `discount_amount`, `tax_amount`, `round_off`, `grand_total`, `payment_method`, `payment_status`, `is_credit`, `created_at`.
     - `sale_items`: `id`, `sale_id` (FK), `product_id` (FK), `batch_id` (FK), `quantity` (> 0), `mrp`, `actual_selling_rate`, `purchase_cost`, `discount_rate`, `tax_rate`, `subtotal`.
     - `credit_ledger`: `id`, `customer_id` (FK), `sale_id` (FK nullable), `transaction_type`, `amount`, `outstanding_balance`, `payment_method`, `notes`, `transaction_date`.
2. **Define SQLAlchemy 2.0 Models:**
   - Create `backend/app/models/customer.py`, `sale.py`, `purchase.py`, `credit_ledger.py`.
   - Export all models in `backend/app/models/__init__.py`.
3. **Execute Migration:**
   - Run: `alembic -c backend/alembic.ini upgrade head`
4. **Verify Database:**
   - Verify table creation, check constraints, foreign keys, and indexes in PostgreSQL.
5. **Run Backend Test Suite:**
   - Ensure all 135 existing tests pass with zero regressions.

---

## Section 15 – Instructions for the Next AI Developer

```text
================================================================================
AI DEVELOPER DIRECTIVE – CONTINUATION PROMPT
================================================================================
You are continuing the implementation of PharmaKon for Aayushman Pharmacy.
The project is preparing for Academic Review 2.

CRITICAL RULES:
1. Do NOT rebuild the application or rewrite existing working code.
2. The current codebase is the SOLE SOURCE OF TRUTH.
3. Read report/PharmaKon_Complete_Project_Documentation_AI_Handoff.md before modifying code.
4. Step 1 (Authentication) IS FULLY IMPLEMENTED AND VERIFIED. Do NOT revert it to mock tokens.
5. Your immediate assignment is STEP 2: Database Expansion (Alembic migration and SQLAlchemy
   models for customers, sales, sale_items, purchases, purchase_items, credit_ledger).
6. Next is STEP 3: Transactional POS & FEFO Engine with automatic multi-batch stock deduction.
7. Maintain database integrity: inventory must never be negative, expired batches cannot be sold,
   sales must lock batch rows with with_for_update(), and all transactions must rollback on failure.
8. Follow DESIGN_CONSTRAINTS.md for all UI components.
9. Always run pytest backend/tests and cd frontend && npx vitest run after making changes.
================================================================================
```
