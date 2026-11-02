# 11 - AI Integration Specification and Review 1 Roadmap

**Project:** PharmaKon  
**Client:** Aayushman Pharmacy  
**Document Status:** Finalized v1.0 - Specification and Review 1 Strategy  
**Target Milestone:** Review 1 (End of Phase 1 / Month 1) and Production Staging  
**Related Documents:** [`docs/06-mvp-scope.md`](file:///d:/PharmaKon/pharmakon/docs/06-mvp-scope.md), [`docs/07-system-architecture.md`](file:///d:/PharmaKon/pharmakon/docs/07-system-architecture.md), [`docs/09-api-design.md`](file:///d:/PharmaKon/pharmakon/docs/09-api-design.md), [`docs/10-analytics-ml-plan.md`](file:///d:/PharmaKon/pharmakon/docs/10-analytics-ml-plan.md)

---

## 1. Executive Summary

PharmaKon integrates Artificial Intelligence (AI) and Machine Learning (ML) to transform traditional pharmacy workflows into an intelligent operational system. Rather than treating AI as an ungrounded chatbot, PharmaKon uses a **Grounded Tool-Calling Architecture** where AI interfaces directly with deterministic database queries and predictive algorithms.

For the **Phase 1 Review (Review 1)**, AI integration is mandatory. This document provides:
1. A concise catalog of practical AI capabilities tailored for retail pharmacy operations.
2. A phased implementation breakdown aligning with the 90-day roadmap.
3. An exact list of what this project can demonstrate during the Review 1 presentation.

---

## 2. Catalog of AI Feature Concepts

### 2.1 Natural Language Pharmacy Assistant (Grounded SQL and Tool Calling)
- **Concept:** Pharmacists ask operational questions in plain conversational language (e.g., "Which medicines are expiring within 45 days?", "What was our total revenue from antibiotics yesterday?", "Show customers with credit balance above Rs. 5,000").
- **Mechanism:** The Large Language Model (LLM) extracts user intent and calls predefined FastAPI tool endpoints. The tool executes deterministic SQL queries on PostgreSQL and returns structured data. The LLM then formats the response.
- **Safety Rule:** The LLM is forbidden from inventing or calculating financial and stock numbers directly.

### 2.2 Time-Series Demand Forecasting and Smart Replenishment
- **Concept:** Predict future daily sales volume (14 to 30 days ahead) for high-velocity medicines and automatically calculate optimal purchase order quantities.
- **Mechanism:** Supervised ML regressor (XGBoost / Random Forest) trained on historical sale transactions, rolling 7-day/14-day sales means, lag features, day-of-week seasonality, and product categories.
- **Formula:** Suggested Order = Max(0, [Forecasted Demand + Safety Stock] - Current Stock).

### 2.3 Prescription and Supplier Invoice OCR (Multimodal Extraction)
- **Concept:** Digitize paper prescriptions and paper supplier bills/challans using optical character recognition (OCR) and multimodal LLM extraction.
- **Mechanism:** The pharmacist captures or uploads an image of a doctor prescription or supplier invoice. The extraction pipeline extracts medicine names, dosages, pack sizes, batch numbers, and purchase costs, matching them against the `products` catalog to pre-populate POS billing or purchase receipt forms.

### 2.4 Generic Substitution and Alternative Medicine Finder
- **Concept:** When a requested brand is out of stock or low in inventory, suggest available therapeutic alternatives with identical active salts, strength, and formulation.
- **Mechanism:** Semantic search or rule-based vector matching over active ingredients, therapeutic categories, and in-stock batch quantities.

### 2.5 Drug Interaction and Safety Advisory
- **Concept:** Real-time clinical safety checks at the point of sale (POS) when dispensing multiple items on a single bill.
- **Mechanism:** Automated screening of selected bill items against known drug-drug interaction pairs and duplicate therapy rules (e.g., advising if two drugs contain overlapping paracetamol dosages), providing an instant non-blocking warning badge on the POS screen.

### 2.6 Customer Credit Risk Scoring and Payment Pattern Insights
- **Concept:** Identify credit customers who are likely to delay settlements based on payment history and outstanding balance duration.
- **Mechanism:** Classification model or RFM (Recency, Frequency, Monetary) clustering grouping credit customers into low, medium, and high collection risk categories.

---

## 3. Staged Implementation Breakdown

To ensure reliability, AI features are introduced across three distinct development phases.

```text
Phase 1 (Month 1): Architecture, Contracts, Tool Registry & Prototype Demo
  │
  ▼
Phase 2 (Month 2): Operational Integration (NL Assistant & Grounded Tools)
  │
  ▼
Phase 3 (Month 3): Advanced ML Forecasting, OCR, and Production Hardening
```

### Stage 1: Phase 1 (Days 1 to 30) - Technical Foundation and Review 1 Target
- **Focus:** AI architecture specification, OpenAPI tool function contracts, system prompt design, and review demonstrations.
- **Deliverables:**
  - Complete AI architecture and safety boundary documentation.
  - Defined OpenAPI schemas and tool definitions for the assistant (`get_product_stock`, `get_top_selling_products`, `get_expiry_risk_report`, `get_sales_metrics`).
  - Interactive demonstration showing LLM tool-calling execution against seeded backend endpoints.
  - Machine learning feature engineering pipeline blueprint.

### Stage 2: Phase 2 (Days 31 to 60) - Operational Assistant and Safety Checks
- **Focus:** Connect the AI assistant to the live PostgreSQL database and integrate assistive checks into the UI.
- **Deliverables:**
  - Functional Natural Language Query API (`POST /api/v1/ai/query`) accepting queries and dispatching tool executions.
  - In-stock generic substitution recommender integrated into the POS product search bar.
  - Drug interaction advisory warning service integrated into billing validation.

### Stage 3: Phase 3 (Days 61 to 90) - Machine Learning and Multimodal Capabilities
- **Focus:** Deploy trained predictive models and multimodal document ingestion.
- **Deliverables:**
  - Automated 14-day and 30-day demand forecasting model using XGBoost.
  - Replenishment recommendation card on the dashboard showing suggested order quantities.
  - Experimental prescription and supplier invoice OCR ingestion pipeline.
  - Performance monitoring and evaluation logs (WAPE, RMSE, precision).

---

## 4. What This Project Can Demonstrate for Review 1 (Tomorrow)

During the Phase 1 Review, you can demonstrate the following concrete, working components:

### 4.1 Grounded AI System Architecture
- **Demonstration:** Present the architectural diagram showing the boundary between the conversational LLM and deterministic PostgreSQL data:
  ```text
  User Voice / Text Query
            │
            ▼
     FastAPI AI Router (/api/v1/ai/query)
            │
            ▼
      LLM Agent (Intent Extraction)
            │
            ▼
     Predefined Tool Execution (e.g. get_expiry_risk_report)
            │
            ▼
     PostgreSQL Transactional Database (Exact Totals)
            │
            ▼
     Formatted Natural Language Response
  ```
- **Value to Reviewers:** Proves that the system is engineered against financial hallucination and guarantees data integrity.

### 4.2 Defined Tool Calling Registry and API Contracts
- **Demonstration:** Walk through the standardized OpenAPI tool specifications that allow any modern LLM (e.g., Gemini, Claude, OpenAI) to invoke PharmaKon backend functions:
  1. `get_product_stock(product_name: str)`
  2. `get_expiry_risk_report(threshold_days: int)`
  3. `get_top_selling_products(limit: int, days: int)`
  4. `get_sales_metrics(start_date: str, end_date: str)`
  5. `get_customer_credit_status(customer_name_or_phone: str)`

### 4.3 Interactive LLM Tool Execution Prototype
- **Demonstration:** Execute an interactive live demonstration (or test trace) showing a user prompt translated into a backend function call against seeded data:
  - **User Input:** "Show me all medicines expiring within the next 60 days."
  - **AI Model Output:** Triggers `get_expiry_risk_report(threshold_days=60)`.
  - **Backend Output:** Returns batch `AMX-202608` of Amoxicillin 500mg (expiry 2026-11-20, 45 units remaining).
  - **AI Response:** "There is 1 medicine batch expiring within 60 days: Amoxicillin 500mg (Batch AMX-202608), expiring on 20 November 2026 with 45 units remaining."

### 4.4 Machine Learning Demand Forecasting Pipeline Architecture
- **Demonstration:** Present the time-series forecasting pipeline specified in [`docs/10-analytics-ml-plan.md`](file:///d:/PharmaKon/pharmakon/docs/10-analytics-ml-plan.md):
  - Daily sales unit resampling.
  - Feature extraction matrix: lag features ($y_{t-1}, y_{t-7}, y_{t-14}, y_{t-28}$), 7-day rolling mean, day of week, and category.
  - Chronological split strategy to eliminate data leakage.
  - Evaluation metric standards: Weighted Absolute Percentage Error (WAPE) and RMSE.

### 4.5 Safety and Governance Protocols
- **Demonstration:** Present the strict system prompt and validation safeguards:
  - Hard constraint: "The AI assistant is strictly forbidden from generating or guessing stock quantities, prices, or revenue numbers without an active tool response."
  - Auditing: All AI-triggered operations are logged with timestamps and execution metadata.

---

## 5. Review 1 Slide and Presentation Script Outline

When presenting to evaluators tomorrow, use this 4-step sequence:

1. **The Problem:** Single retail pharmacies struggle with manual inventory records and paper invoices, leading to expired stock and inaccurate purchasing.
2. **The Solution:** PharmaKon combines a robust modular monolith POS system with an intelligent, grounded AI and ML engine.
3. **The AI Architecture:** Highlight that AI does not replace core transactional logic; it provides natural language access and predictive foresight through deterministic tool calling and ML demand forecasting.
4. **Current Status and Roadmap:** Phase 1 specifications and tool contracts are complete; Phase 2 connects live database transactions; Phase 3 delivers trained predictive models.
