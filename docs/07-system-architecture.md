# PharmaKon — System Architecture & Technology Stack

**Project:** PharmaKon  
**Client:** Aayushman Pharmacy  
**Deployment model:** Single retail pharmacy  
**Architecture style:** Modular monolith / layered web application  
**Primary API style:** REST API  
**Document role:** Project context and architectural reference  
**Status:** Initial architecture baseline  
**Last updated:** 17 September 2026

---

# 1. Architecture Objective

PharmaKon is a web-based Pharmacy Management and Analytics System for a single retail pharmacy. The architecture is designed to:

- provide reliable day-to-day pharmacy operations;
- maintain consistent product, batch, inventory, purchase and sales data;
- enforce pharmacy business rules centrally;
- provide analytics directly from operational data;
- support practical ML capabilities when sufficient historical data exists;
- optionally provide a controlled AI assistant;
- remain simple enough to develop, deploy and maintain within the three-month project.

The architecture deliberately avoids unnecessary enterprise complexity. The project is **not** designed as a microservices system.

---

# 2. Architecture Principles

## 2.1 Modular, Not Over-Engineered

The initial system uses a **modular monolithic architecture**. Major business areas are separated logically inside the application, while the system remains deployable as a small number of services/components.

Microservices, Kubernetes, custom LLM hosting and GPU infrastructure are explicitly outside the three-month scope unless a concrete requirement later justifies them.

## 2.2 Business Rules Are Backend-Owned

Business rules must not exist only in frontend validation.

The main flow is:

```text
Frontend
   ↓
FastAPI Router
   ↓
Service / Domain Layer
   ↓
Business Rule Validation
   ↓
Repository / Data Access
   ↓
PostgreSQL Transaction
```

This ensures rules such as negative-stock prevention remain true regardless of which supported interface triggers an operation.

## 2.3 PostgreSQL Is the Operational Source of Truth

Operational pharmacy data is stored in PostgreSQL.

Analytics, ML and AI capabilities consume controlled data from the operational system rather than maintaining an independent source of truth.

## 2.4 Historical Data Is Preserved

Completed sales, returns, stock adjustments and supplier returns must remain historically traceable. The architecture therefore favors transaction records and movement history over destructive updates/deletes.

## 2.5 Analytics and ML Depend on Reliable Operational Data

Analytics is derived from transactional data.

ML is introduced only when sufficient historical data exists. Demand forecasting is the primary ML candidate; customer segmentation is conditional on data availability.

## 2.6 AI Must Be Grounded in Real Data

If the AI assistant is implemented, the LLM does not directly invent or calculate pharmacy business numbers.

The intended flow is:

```text
User Question
      ↓
LLM
      ↓
Controlled Tool / Function
      ↓
Database / Analytics Result
      ↓
LLM Explanation
      ↓
User
```

Business figures must come from deterministic system data.

---

# 3. High-Level System Architecture

```text
                         ┌─────────────────────┐
                         │      .np DOMAIN     │
                         │       HTTPS         │
                         └──────────┬──────────┘
                                    │
                                    ▼
                    ┌────────────────────────────┐
                    │   React + TypeScript       │
                    │        Frontend            │
                    └──────────────┬─────────────┘
                                   │
                              REST API
                                   │
                                   ▼
                    ┌────────────────────────────┐
                    │      Python + FastAPI      │
                    │        Backend API         │
                    └──────────────┬─────────────┘
                                   │
             ┌─────────────────────┼──────────────────────┐
             │                     │                      │
             ▼                     ▼                      ▼
    ┌────────────────┐   ┌──────────────────┐   ┌──────────────────┐
    │ Business /     │   │ Analytics Layer  │   │   AI Layer       │
    │ Service Layer  │   │ SQL + Pandas +   │   │ LLM API +        │
    │                │   │ NumPy + Plotly   │   │ Tool Calling     │
    └───────┬────────┘   └────────┬─────────┘   └────────┬─────────┘
            │                     │                      │
            ▼                     │                      │
    ┌────────────────┐            │                      │
    │ Repository /   │            │                      │
    │ SQLAlchemy     │            │                      │
    └───────┬────────┘            │                      │
            │                     │                      │
            └──────────────┬──────┴──────────────────────┘
                           ▼
                 ┌────────────────────┐
                 │    PostgreSQL      │
                 │ Operational Data   │
                 └─────────┬──────────┘
                           │
                           ▼
                 ┌────────────────────┐
                 │ Forecasts /        │
                 │ Insights / Reports │
                 └────────────────────┘
```

---

# 4. Complete Technology Stack

The following technologies are part of the project architecture defined by the project documents.

| Layer | Technology | Purpose | Status |
|---|---|---|---|
| Frontend | **React** | Web application UI | Confirmed |
| Frontend language | **TypeScript** | Type-safe frontend development | Confirmed |
| API | **REST API** | Communication between frontend and backend | Confirmed |
| Backend language | **Python** | Backend and data/ML ecosystem | Confirmed |
| Backend framework | **FastAPI** | REST API and backend application | Confirmed |
| Database | **PostgreSQL** | Primary relational operational database | Confirmed |
| ORM | **SQLAlchemy** | Structured Python database access | Confirmed |
| Database migrations | **Alembic** | Version-controlled database schema migrations | Confirmed |
| Database querying | **SQL** | Operational queries and analytics | Confirmed |
| Analytics | **Pandas** | Data extraction, transformation and analysis | Confirmed |
| Analytics / numerical computing | **NumPy** | Numerical and feature-processing operations | Confirmed |
| Visualization | **Plotly** | Analytics dashboard visualizations | Confirmed |
| Machine learning | **scikit-learn** | Practical ML models and evaluation | Confirmed |
| Machine learning | **XGBoost** | Practical tabular/time-series ML candidate | Confirmed |
| AI | **LLM API** | Controlled natural-language analytics assistant | Conditional |
| AI integration | **Tool / function calling** | Restrict AI access to approved system operations/data | Conditional |
| Containerization | **Docker** | Reproducible application packaging | Confirmed |
| CI/CD | **GitHub Actions** | Automated tests, builds and deployment workflow | Confirmed |
| Source control / repository | **GitHub repository** | Source code and project collaboration | Confirmed |
| Hosting | **Cloud deployment** | Production hosting | Confirmed, provider TBD |
| Domain | **.np domain** | Public application domain | Planned |
| Transport security | **HTTPS** | Secure production communication | Required |
| Backups | **Automated database backups** | Data protection and recovery | Required |

### Important Technology-Selection Boundary

The source documents do **not** specify:

- exact versions of React, TypeScript, Python, FastAPI, PostgreSQL, SQLAlchemy, Alembic, Pandas, NumPy, Plotly, scikit-learn or XGBoost;
- a specific cloud provider;
- a specific LLM provider/model;
- a specific WhatsApp API/provider;
- a specific frontend state-management library;
- a specific frontend routing library;
- a specific authentication library;
- a specific testing framework.

These should be selected during implementation/design where necessary rather than being treated as already-confirmed project requirements.

---

# 5. Frontend Architecture

## 5.1 Technology

- React
- TypeScript

The frontend is a browser-based application intended to run on the pharmacy's existing computer(s).

## 5.2 Responsibilities

The frontend is responsible for:

- authentication interface;
- application navigation;
- product management screens;
- batch and inventory screens;
- supplier and purchase workflows;
- sales and billing workflow;
- invoice display/printing;
- customer and credit workflows;
- returns/refunds;
- stock adjustment interfaces;
- low-stock and expiry-risk visibility;
- analytics dashboards;
- ML output visualization where implemented;
- controlled AI interaction where implemented.

## 5.3 Frontend Boundary

The frontend should handle:

- presentation;
- user interaction;
- client-side form/input validation;
- API communication;
- displaying API responses and errors.

The frontend must **not** be the authoritative location for pharmacy business rules.

For example, checking whether a sale would create negative inventory cannot depend only on a frontend validation message.

---

# 6. Backend Architecture

## 6.1 Technology

- Python
- FastAPI
- REST API
- SQLAlchemy
- Alembic
- SQL
- LLM API integration where AI is implemented

## 6.2 Backend Layering

The recommended backend flow is:

```text
Router
  ↓
Service / Domain
  ↓
Repository
  ↓
PostgreSQL
```

### Router Layer

Responsible for:

- receiving HTTP requests;
- request/response contracts;
- authentication/access checks;
- invoking appropriate services;
- returning API responses and errors.

### Service / Domain Layer

Responsible for:

- business workflows;
- business-rule enforcement;
- transaction orchestration;
- FEFO batch selection;
- inventory validation;
- pricing/tax/discount calculations;
- return/refund behavior;
- credit balance updates;
- stock movement generation.

### Repository Layer

Responsible for:

- database access;
- querying;
- persistence;
- isolating database implementation from business logic.

### Database Layer

PostgreSQL provides:

- relational persistence;
- transactions;
- constraints;
- indexes;
- joins;
- aggregations;
- analytical SQL queries.

---

# 7. Core Backend Modules

The backend should be divided into logical modules corresponding to the confirmed system functional areas.

```text
Authentication
Product Management
Batch Management
Inventory
Suppliers
Purchases
Sales
Pricing / Discounts / Tax
Invoices
Customers
Returns / Refunds
Credit Ledger
Damaged / Expired Stock
Stock Adjustments
Monitoring
Analytics
Replenishment
ML
AI
```

The modules remain part of one backend application rather than separate microservices.

---

# 8. Core Business Data Domains

The architecture must support the following related data domains:

```text
Product
   │
   └── Batch
         │
         └── Inventory / Stock Movement

Supplier
   │
   └── Purchase
         │
         └── Purchase Item
                │
                └── Batch

Customer
   │
   ├── Sale
   │     └── Sale Item
   │            └── Batch / Inventory
   │
   └── Credit Ledger / Payments

Sale
   │
   ├── Invoice
   ├── Payment
   └── Return / Refund
```

The exact database schema and ERD belong in `08-database-design.md`.

---

# 9. Inventory Architecture

Inventory is a critical architectural area because unmanaged stock is the client's primary problem.

## Required behavior

The system must support:

- current stock tracking;
- batch-level stock;
- multiple batches per product;
- purchase-driven stock increases;
- sale-driven stock decreases;
- negative-stock prevention;
- FEFO batch selection;
- stock adjustments;
- stock adjustment history;
- stock movement visibility;
- configurable reorder levels;
- low-stock monitoring;
- expiry-risk monitoring;
- damaged/expired stock handling;
- supplier returns.

## Inventory Invariant

```text
Inventory quantity >= 0
```

A transaction that would create negative stock must be rejected.

## Stock Movement Principle

```text
Purchase
   ↓
Stock Increase

Sale
   ↓
Stock Decrease

Customer Return
   ↓
Return Handling / Stock Adjustment

Supplier Return
   ↓
Stock Reduction / Adjustment

Physical Verification
   ↓
Stock Adjustment
```

Every relevant movement must remain traceable.

---

# 10. Batch and FEFO Architecture

A product can have multiple batches.

Batch-level data includes:

- batch number;
- expiry date;
- quantity;
- purchase cost.

When selling a product with multiple applicable batches:

```text
Available Batches
       ↓
Check Expiry
       ↓
Sort by Earliest Expiry
       ↓
Select Earliest Applicable Batch
       ↓
Deduct Stock
```

This implements the confirmed **FEFO (First Expiry, First Out)** requirement.

Whether expired batches must be hard-blocked from sale is still a client-confirmation item and should not be silently treated as a confirmed business rule until resolved.

---

# 11. Sales and Billing Architecture

The sales workflow is one of the highest-priority operational paths.

```text
Product Search / Barcode
          ↓
Quantity
          ↓
FEFO Batch Selection
          ↓
Stock Validation
          ↓
Actual Selling Price
          ↓
Discount
          ↓
Subtotal
          ↓
Tax / VAT
          ↓
Round-off
          ↓
Grand Total
          ↓
Payment
          ↓
Sale Transaction
          ↓
Inventory Deduction
          ↓
Invoice
```

The system must preserve the actual selling rate used for each sale line.

MRP must not be treated as the historical selling price.

The current client-specified tax rate is 13%, with tax added after the base price. Uniform tax applicability across all product categories remains subject to client confirmation.

The client-requested default discount is 10%, but whether this is automatically applied or merely presented as the default selectable value remains unresolved.

---

# 12. Invoice Architecture

Invoices must preserve required information from the previous system while automating calculations.

The invoice architecture should support:

- invoice number;
- fiscal/year information;
- reference number where required;
- voucher/invoice date;
- buyer/customer information;
- phone;
- address where required;
- PAN/VAT where applicable;
- product;
- batch number;
- expiry;
- quantity;
- unit;
- alternate quantity/unit where required;
- actual selling rate;
- line amount;
- discount;
- tax/VAT;
- round-off;
- grand total.

Output requirements:

- printable invoice;
- digital invoice generation.

The exact automated WhatsApp/API delivery mechanism remains a client-confirmation item.

---

# 13. Purchasing and Supplier Architecture

Purchases are linked to suppliers and must create reliable inventory/batch information.

```text
Supplier
   ↓
Purchase
   ↓
Purchase Items
   ↓
Product + Batch + Expiry + Quantity + Cost
   ↓
Inventory Increase
```

Purchase records must retain:

- supplier;
- invoice/reference;
- product;
- batch;
- expiry;
- quantity;
- purchase cost;
- payment information.

Purchase cost is stored at the batch/purchase level because it is required for accurate profit analysis.

Damaged and expired stock can follow:

```text
Stock
  ↓
Damaged / Expired
  ↓
Non-Saleable Handling
  ↓
Supplier Return
  ↓
Stock Adjustment
  ↓
Return History
```

Exact inventory disposition rules for every return condition require further definition.

---

# 14. Customer and Credit Architecture

The initial customer record requires:

- customer name;
- phone number.

Customer data is associated with relevant sales and credit transactions.

Credit workflow:

```text
Credit Sale
    ↓
Customer
    ↓
Outstanding Amount
    ↓
Digital Credit Ledger
    ↓
Later Payment
    ↓
Outstanding Balance Updated
```

Whether formal credit due dates are required remains unconfirmed.

---

# 15. Returns and Historical Data

Customer returns require the original bill/invoice.

The architecture follows:

```text
Original Sale
     ↓
Return Request
     ↓
Original Invoice Verification
     ↓
Return Item / Quantity
     ↓
Refund
     ↓
Stock Handling
     ↓
Historical Record Preserved
```

A return must **not** delete the original sale.

This preserves transaction history and supports auditability.

---

# 16. Authentication and Access Architecture

The confirmed initial access model is intentionally simple.

```text
PharmaKon
    │
    ▼
Single Account
    │
    ├── Operational Access
    │
    └── Analytics Access
```

The initial system does not require:

- separate employee accounts;
- individual staff profiles;
- complex RBAC;
- staff-specific permissions;
- staff-specific dashboards.

The one account represents the pharmacy's operational system user.

Because the system uses one shared account, the initial architecture cannot reliably attribute a transaction to an individual staff member.

The exact authentication implementation/library has not yet been specified in the source requirements and must be selected during technical design.

---

# 17. Analytics Architecture

Analytics is derived from operational PostgreSQL data.

```text
PostgreSQL
    ↓
SQL Queries / Data Extraction
    ↓
Pandas / NumPy
    ↓
Metric Calculation
    ↓
Analytics Service / API
    ↓
React + Plotly Dashboard
```

Required analytics areas include:

- sales trends;
- fast-moving products;
- slow-moving products;
- stock levels;
- low-stock products;
- expiry-risk products;
- purchase patterns;
- revenue indicators;
- profit indicators;
- replenishment insights.

Analytics totals must be verified against known database totals.

---

# 18. Machine Learning Architecture

ML is conditional on sufficient data.

The primary ML candidate is **demand forecasting**.

## 18.1 Demand Forecasting Flow

```text
PostgreSQL
    ↓
Historical Sales Extraction
    ↓
Data Cleaning
    ↓
Exploratory Analysis
    ↓
Feature Engineering
    ├── Lag Features
    ├── Rolling Features
    ├── Calendar Features
    └── Relevant Business Features
    ↓
Baseline Forecast
    ↓
Model Training
    ↓
Time-Aware Validation
    ↓
Leakage Checks
    ↓
Model Evaluation
    ↓
Prediction
    ↓
API / Scheduled Prediction
    ↓
Frontend Dashboard
```

Technology:

- Pandas
- NumPy
- scikit-learn
- XGBoost

The model must support the owner's purchasing decision rather than replace it.

## 18.2 Customer Segmentation

Customer segmentation is conditional and may be implemented only if sufficient transaction data exists.

Potential flow:

```text
Customer Transactions
        ↓
RFM Features
        ↓
Scaling
        ↓
K-Means
        ↓
Evaluation
        ↓
Segment Profiling
```

Segmentation is not required for the core operational MVP.

---

# 19. Replenishment Decision Support

Replenishment insights combine operational and, where available, ML information.

Conceptual flow:

```text
Current Stock
      +
Sales Movement
      +
Reorder Level
      +
Forecast (if available)
      +
Lead-Time Assumptions (if available)
      ↓
Replenishment Logic
      ↓
Recommended Products
      +
Approximate Quantity
```

The system provides decision support; the owner remains responsible for the purchasing decision.

---

# 20. AI Assistant Architecture

The AI assistant is a conditional late-Month-3 capability.

It must only be added if:

- the core application is stable;
- analytics are connected to real data;
- deterministic tools/functions exist;
- sufficient project time remains;
- the AI can be safely constrained to actual pharmacy data.

## AI Technology

- LLM API
- Tool/function calling

The exact LLM provider/model is **not yet specified**.

## Controlled AI Flow

```text
User Question
      ↓
LLM
      ↓
Intent / Tool Selection
      ↓
Approved Tool / Function
      ↓
Database / Analytics Query
      ↓
Deterministic Result
      ↓
LLM Explanation
      ↓
User
```

Potential questions include:

- What were the top-selling medicines last month?
- Which products are low in stock?
- Which medicines have the highest expiry risk?
- What does the demand forecast suggest?

## AI Guardrails

The AI must:

- use controlled tools/functions;
- obtain business numbers from actual system data;
- avoid inventing stock, sales or revenue figures;
- explain retrieved results instead of manufacturing them.

---

# 21. API Architecture

The frontend communicates with the backend through REST APIs.

Conceptually:

```text
React + TypeScript
       │
       │ HTTP / REST
       ▼
FastAPI
       │
       ├── Authentication
       ├── Products
       ├── Batches
       ├── Inventory
       ├── Suppliers
       ├── Purchases
       ├── Sales
       ├── Invoices
       ├── Customers
       ├── Returns
       ├── Credit
       ├── Monitoring
       ├── Analytics
       ├── Replenishment
       ├── ML
       └── AI
```

Detailed endpoints, request/response contracts and error structures belong in `09-api-design.md`.

---

# 22. Database Architecture

PostgreSQL is selected because the pharmacy domain is relationship-heavy and transaction consistency is critical.

The database must support:

- relational relationships;
- transactions;
- constraints;
- indexes;
- joins;
- aggregations;
- analytical SQL;
- historical transaction records;
- batch-level inventory;
- stock movement traceability.

SQLAlchemy provides structured Python access to PostgreSQL.

Alembic provides version-controlled schema migrations.

The detailed schema belongs in `08-database-design.md`.

---

# 23. Data Integrity and Transaction Boundaries

Critical operations should be executed transactionally.

Examples:

### Sale

```text
Validate Stock
    ↓
Select FEFO Batch
    ↓
Create Sale / Sale Items
    ↓
Record Payment
    ↓
Deduct Inventory
    ↓
Record Stock Movement
    ↓
Commit
```

### Purchase

```text
Validate Purchase
    ↓
Create Purchase / Purchase Items
    ↓
Create or Record Batch
    ↓
Increase Inventory
    ↓
Record Stock Movement
    ↓
Commit
```

### Return

```text
Verify Original Sale
    ↓
Record Return
    ↓
Record Refund
    ↓
Apply Stock Handling
    ↓
Record Stock Movement
    ↓
Preserve Original Sale
    ↓
Commit
```

The exact database constraints and transaction boundaries will be formalized in the database/API specifications.

---

# 24. Testing Architecture

Testing is required throughout development and must cover critical paths before final delivery.

Required test areas include:

- database migrations;
- database constraints and relationships;
- negative-stock prevention;
- purchase → stock increase;
- sale → stock decrease;
- FEFO batch selection;
- custom-price calculation;
- invoice calculation;
- return behavior;
- credit balance updates;
- authentication/authorization foundation;
- analytics total verification;
- ML time-aware validation and leakage checks where ML is implemented;
- AI grounding checks where AI is implemented;
- backup restoration.

The exact testing framework/library is not specified in the source documents and will be selected during implementation.

---

# 25. Deployment Architecture

The deployment target is intentionally small and low-cost because PharmaKon serves one pharmacy.

## Required deployment technologies

- Docker
- GitHub Actions
- Cloud hosting
- PostgreSQL
- HTTPS
- `.np` domain
- automated backups
- environment variables/secrets
- logging/error monitoring

Conceptual deployment:

```text
                  .np DOMAIN
                       │
                     HTTPS
                       │
                       ▼
              ┌─────────────────┐
              │ Cloud Application│
              │    Deployment   │
              └────────┬────────┘
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
      React Frontend       FastAPI Backend
                               │
                               ▼
                         PostgreSQL DB
                               │
                               ▼
                       Automated Backups
```

The exact cloud provider is not yet specified.

---

# 26. Containerization

Docker is used to create a reproducible application build.

The project should be deployable from the same application artifacts used for testing.

The deployment architecture should remain simple and should not introduce Kubernetes or an unnecessary orchestration platform.

---

# 27. CI/CD Architecture

GitHub Actions is the planned CI/CD platform.

Conceptual flow:

```text
Developer
    ↓
GitHub Repository
    ↓
GitHub Actions
    ├── Tests
    ├── Build
    └── Deployment Workflow
             ↓
       Cloud Deployment
```

The exact workflow files and deployment strategy will be defined during implementation.

---

# 28. Configuration and Secrets

Production configuration must not be hard-coded into the source code.

The deployment requirements include:

- environment-variable handling;
- externalized secrets;
- separate production database;
- production credentials kept outside source control.

Potential secrets/configuration areas include:

- database connection;
- authentication secrets;
- LLM API credentials if AI is enabled;
- external integration credentials if later confirmed.

Exact variable names are implementation details and should be defined in the deployment specification.

---

# 29. Security Architecture

The current source requirements define security at a high level rather than specifying a complete security implementation.

Required architectural direction:

- authentication before protected application access;
- sensitive customer/credit information protected from unauthenticated access;
- production HTTPS;
- externalized secrets;
- least-privilege operational access;
- no unnecessary permission complexity;
- backend enforcement of business rules.

The proposed NFRs are not yet client-confirmed and must be revisited with the client before being treated as final non-functional requirements.

---

# 30. Backup and Recovery

Production deployment must include:

- automated backups;
- backup restoration verification;
- a documented recovery/rollback procedure.

The client has not yet confirmed:

- existing backup practices;
- required legal retention period;
- exact retention policy.

Therefore, backup frequency and retention should remain implementation decisions subject to client confirmation.

---

# 31. Observability

The production system must provide at least:

- basic application logging;
- error monitoring;
- enough information to diagnose critical operational failures.

Detailed observability tooling is not specified by the source documents and should remain proportional to the single-pharmacy deployment.

---

# 32. Architecture by Project Phase

## Month 1 — Architecture and Design

Complete:

- architecture;
- technology stack confirmation;
- major module boundaries;
- authentication/authorization approach;
- database entities;
- ER diagram;
- inventory/batch/expiry model;
- purchase/supplier model;
- sales/customer/payment model;
- auditability and stock-movement requirements;
- analytics/ML data requirements.

## Month 2 — Core Application

Build:

- PostgreSQL foundation;
- SQLAlchemy;
- Alembic;
- FastAPI backend;
- authentication foundation;
- products;
- suppliers;
- purchases;
- batches;
- inventory;
- customers;
- sales;
- returns/refunds where included;
- React + TypeScript frontend.

## Month 3 — Analytics, ML, AI and Production

Build/refine:

- analytics service/API;
- Plotly dashboard;
- historical-sales ML dataset;
- demand forecasting if data supports it;
- replenishment insights;
- customer segmentation if data supports it;
- controlled AI assistant if time/data/safety support it;
- tests;
- Docker;
- GitHub Actions;
- cloud deployment;
- HTTPS;
- backups;
- recovery verification;
- `.np` domain.

---

# 33. Explicitly Out of Scope

The architecture must not expand into the following without a new confirmed requirement:

- microservices;
- Kubernetes;
- custom LLM hosting;
- GPU infrastructure;
- unnecessary enterprise infrastructure;
- full recreation of the old ERP;
- complex RBAC;
- large numbers of weak ML demonstrations;
- enterprise-scale infrastructure.

Future possibilities include multi-branch operation, granular employee permissions, advanced accounting, advanced predictive analytics and expanded AI capabilities, but these are not current architectural requirements.

---

# 34. Architecture Decisions Summary

| Decision | Choice | Reason |
|---|---|---|
| Application style | Modular monolith | Appropriate for one pharmacy and a three-month timeline |
| Frontend | React + TypeScript | Professional web UI and portfolio value |
| Backend | Python + FastAPI | Aligns backend with analytics/ML ecosystem |
| API | REST | Simple frontend/backend separation |
| Database | PostgreSQL | Relationship-heavy transactional domain |
| ORM | SQLAlchemy | Structured Python database access |
| Migrations | Alembic | Reproducible schema evolution |
| Analytics | SQL + Pandas + NumPy + Plotly | Direct operational analytics and visualization |
| ML | scikit-learn + XGBoost | Practical tabular/time-series ML |
| AI | LLM API + tool/function calling | Controlled access to real pharmacy data |
| Containers | Docker | Reproducible builds/deployment |
| CI/CD | GitHub Actions | Automated test/build/deployment workflow |
| Hosting | Small cloud deployment | Proportional to single-pharmacy workload |
| Domain | `.np` | Planned project domain |
| Database source of truth | PostgreSQL | Central operational data authority |
| Business-rule location | Backend service/domain layer | Prevents rule bypass |
| Inventory strategy | Batch-level + FEFO | Required pharmacy inventory behavior |
| Advanced architecture | Avoided | Not justified by current scope |

---

# 35. Technology Stack — Quick Reference

```text
FRONTEND
React
TypeScript

        │
        │ REST API
        ▼

BACKEND
Python
FastAPI
SQLAlchemy
Alembic

        │
        ▼

DATABASE
PostgreSQL
SQL

        │
        ├──────────────────────────────┐
        ▼                              ▼

ANALYTICS / ML                     AI
SQL                                LLM API
Pandas                             Tool / Function Calling
NumPy
Plotly
scikit-learn
XGBoost

        │
        ▼

PRODUCTION
Docker
GitHub Actions
Cloud
HTTPS
.np Domain
Automated Backups
Logging / Error Monitoring
```

---

# 36. Source and Scope Note

This architecture is derived from the current PharmaKon project overview, client requirements, functional requirements, user-role definition, business rules, MVP scope, and the three-month project booklet.

Where the source documents identify a requirement as **Needs confirmation**, this architecture does not silently convert it into a final business rule or technology commitment.

The detailed implementation documents that should follow this architecture are:

```text
08-database-design.md
09-api-design.md
10-analytics-ml-plan.md
context/coding-standards.md
context/ai-workflow.md
context/ui-context.md
```

The architecture should be updated if later client-confirmed requirements change the current system boundaries.
