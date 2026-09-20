# 💊 PharmaKon — Pharmacy Management & Analytics System

[![Project Status: Phase 1 Specification Complete](https://img.shields.io/badge/Status-Phase_1_Specs_Complete-emerald.svg)](docs/06-mvp-scope.md)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688.svg)](https://fastapi.tiangolo.com/)
[![React 18+](https://img.shields.io/badge/React-18+-61DAFB.svg)](https://react.dev/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-336791.svg)](https://www.postgresql.org/)

**PharmaKon** is a web-based pharmacy management, inventory analytics, and AI-assisted decision support system designed for **Aayushman Pharmacy** (a single retail pharmacy in Nepal). 

The platform optimizes day-to-day retail operations (POS billing, FEFO batch tracking, custom pricing, digital credit ledger, and returns) while transforming transaction history into actionable inventory replenishment insights and machine-learning demand forecasts.

---

## 🎯 Primary Problem Solved

1. **Unmanaged Stock:** Eliminates stockouts and expired inventory losses via **FEFO (First Expiry, First Out)** automated batch selection, configurable reorder level alerts, and real-time stock movement logging.
2. **Lack of Invoicing:** Replaces manual billing with automated, tax-compliant invoices supporting 10% default discounts, 13% VAT, custom selling price overrides, round-offs, printing, and digital dispatch.
3. **Absence of Analytics:** Converts raw transaction history into fast/slow mover identification, gross profit tracking, safety stock recommendations, and time-series demand forecasting.

---

## 🏗️ System Architecture

```text
React + TypeScript (Vite + Tailwind CSS)
       │
    REST API (OpenAPI 3.0)
       │
FastAPI Routers (Request Validation & OpenAPI)
       │
Service / Domain Layer (FEFO Engine, Pricing Rules, Stock Calculations)
       │
Repository Layer (SQLAlchemy ORM 2.0 Data Access)
       │
PostgreSQL Database (Transactional Source of Truth)
       │
       ├── Analytics Engine (Pandas + NumPy + Plotly)
       ├── ML Pipeline (scikit-learn + XGBoost Time-Series Forecasting)
       └── AI Assistant (Grounded LLM Tool Calling)
```

---

## 📚 Technical Documentation Index

All core architectural specifications and business requirements are documented in [`docs/`](docs/):

| Document | Description |
| :--- | :--- |
| 📄 [01-project-overview.md](docs/01-project-overview.md) | Business identity, problem context, success metrics, and risk assessment. |
| 📄 [02-client-requirements.md](docs/02-client-requirements.md) | Client requirement traceability matrix and non-functional requirements (NFRs). |
| 📄 [03-functional-requirements.md](docs/03-functional-requirements.md) | Comprehensive functional specification (`FR-AUTH`, `FR-PROD`, `FR-INV`, `FR-SALE`). |
| 📄 [04-user-roles.md](docs/04-user-roles.md) | User structure and single-account operational access model. |
| 📄 [05-business-rules.md](docs/05-business-rules.md) | Authoritative business invariants, FEFO rules, and calculation formulas. |
| 📄 [06-mvp-scope.md](docs/06-mvp-scope.md) | 90-day staged MVP roadmap, phase exit criteria, and priority ladder. |
| 📄 [07-system-architecture.md](docs/07-system-architecture.md) | Technology stack, modular monolith architecture, and security guidelines. |
| 📄 [08-database-design.md](docs/08-database-design.md) | PostgreSQL 3NF Schema, Mermaid ERD, indexing strategy, and table DDL specs. |
| 📄 [09-api-design.md](docs/09-api-design.md) | REST API endpoints, Pydantic schemas, and OpenAPI contracts. |
| 📄 [10-analytics-ml-plan.md](docs/10-analytics-ml-plan.md) | Analytics metrics, SQL queries, demand forecasting ML, and AI tool registry. |

---

## 🧠 Development Context Guidelines

Developer rules and AI assistant operating guidelines are located in [`context/`](context/):
- [`context/architecture.md`](context/architecture.md): Service layer responsibilities and dependency direction.
- [`context/coding-standards.md`](context/coding-standards.md): PEP 8, TypeScript strict mode, Decimal currency rules, and pytest standards.
- [`context/ai-workflow.md`](context/ai-workflow.md): Spec-driven development operating rules and commit safeguards.
- [`context/ui-context.md`](context/ui-context.md): Tailwind CSS design system, POS keyboard-first UX, and layout guide.
- [`context/progress.md`](context/progress.md): Live project progress log and milestone tracker.

---

## 🚀 Quick Setup & Roadmap

### Project Timeline (90 Days)
- **Phase 1 (Days 1–30):** Requirements, Architecture, Database & API Specs *(Completed)*
- **Phase 2 (Days 31–60):** Backend Services, Database Migrations, POS Billing & UI Implementation *(Current)*
- **Phase 3 (Days 61–90):** Analytics Dashboards, ML Demand Forecasting, Dockerization & Cloud Deployment

### Repository Directory Structure
```text
pharmakon/
├── backend/            # FastAPI application, SQLAlchemy models, Alembic migrations
├── frontend/           # React + TypeScript SPA (Vite + Tailwind CSS)
├── ml/                 # Data cleaning, feature engineering & XGBoost forecasting models
├── docker/             # Dockerfile & docker-compose configuration
├── docs/               # Technical specifications (01 to 10)
├── context/            # Developer context & coding guidelines
├── tests/              # Pytest test suite for backend & business rules
└── README.md
```
