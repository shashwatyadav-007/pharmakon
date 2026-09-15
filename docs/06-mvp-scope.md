# 06 — MVP Scope

## 1. Document Purpose

This document defines **what must be completed within the three-month PharmaKon project and what should be deferred to later versions**.

The project has a fixed approximately 90-day timeline, with:

- **Review 1 at the end of Month 1**
- **A usable core management system by the end of Month 2**
- **Analytics, ML, AI and production/deployment hardening during Month 3**

The scope is deliberately staged so that the pharmacy receives a reliable core management system before advanced analytics and AI features are added.

---

# 2. Scope Principle

The MVP must focus directly on the client's three stated problems:

1. **Unmanaged stock**
2. **Lack of useful medicine analytics/insight**
3. **Lack of proper invoices**

The project should prioritize correctness of:

- Sales
- Inventory
- Purchasing
- Billing/invoicing
- Transaction history

over visual polish or unnecessary technical complexity.

The project booklet explicitly recommends a staged MVP approach: build a reliable management system first, then add analytics, one or two strong ML capabilities, and finally an AI assistant if time and data support them.

---

# 3. Three-Month Delivery Definition

## Month 1 — Requirements, Architecture & Design

**Goal:** Freeze a coherent project definition and establish the technical foundation before broad implementation.

Month 1 is primarily design and planning rather than full application development.

### Must Finish in Month 1

- Project overview
- Client requirements baseline
- Functional requirements
- User roles/access model
- Business rules
- MVP scope
- High-level architecture
- Technology stack confirmation
- Major module boundaries
- Authentication/authorization approach
- Database entities
- ER diagram
- Inventory/batch/expiry data model
- Purchase/supplier data model
- Sales/customer/payment data model
- Auditability and stock-movement requirements
- Analytics/ML data requirements
- Initial ML candidate selection
- Project context files
- Review 1 presentation/demo narrative

### Review 1 Target

By the end of Month 1 / Day 30, the project should be able to demonstrate:

- The pharmacy problem
- Current workflow
- Confirmed users and roles
- Functional/non-functional requirements
- MVP scope
- Explicit out-of-scope items
- Business rules
- System architecture
- ER diagram/database design
- Analytics/ML plan
- Development methodology
- Working foundation where possible
- Risks, assumptions and next-month plan

Review 1 should demonstrate **coherence and technical readiness**, not a large collection of incomplete features.

---

# 4. Month 2 — Core Pharmacy Management System

**Goal:** Deliver the usable operational system.

By the end of Month 2, the core pharmacy management workflows must work end-to-end.

## 4.1 Authentication

### MVP

- Single-account authentication
- Required operational access
- Access to stock management
- Access to analytics

### Not MVP

- Separate employee accounts
- Complex role-based access control
- Staff-specific permissions

---

# 5. Product & Batch Management

## 5.1 Product Management — MVP

The MVP shall support:

- Product creation
- Product editing
- Product code
- Product name
- Category
- Unit
- MRP
- Purchase cost
- Barcode where available
- Product categorization

## 5.2 Batch Management — MVP

The MVP shall support:

- Multiple batches per product
- Batch number
- Expiry date
- Batch quantity
- Batch-level purchase cost
- FEFO batch selection

## Required Outcome

The system must be able to distinguish multiple batches of the same product and use the earliest-expiring applicable batch during sales.

---

# 6. Inventory Management — MVP

Inventory management is a **top-priority MVP area** because unmanaged stock is the client's biggest stated problem.

### Must Finish

- Current stock tracking
- Batch-level stock
- Purchase-driven stock increases
- Sale-driven stock decreases
- Negative-stock prevention
- Stock adjustments
- Adjustment history
- Stock movement visibility
- Physical stock verification support
- Configurable reorder level
- Low-stock visibility
- Expiry-risk visibility

### MVP Inventory Invariant

```text
Inventory quantity must never become negative.
```

---

# 7. Purchasing & Suppliers — MVP

### Must Finish

- Supplier records
- Purchase records
- Supplier invoice/reference
- Product
- Batch
- Expiry
- Quantity
- Purchase cost
- Payment information
- Batch creation/recording from purchases
- Inventory updates from purchases
- Damaged/expired supplier-return records

### Purchasing Outcome

The system must record enough reliable purchasing and stock data to support later analytics and purchasing recommendations.

---

# 8. Sales & Billing — MVP

Sales and proper invoices are a **top-priority MVP area**.

### Must Finish

- Create sale
- Select products
- Scan products where barcode is available
- Enter quantity
- FEFO batch selection
- Validate stock availability
- Custom selling price
- Actual selling rate per invoice line
- Discount support
- 13% tax/VAT handling as currently specified
- Subtotal
- Round-off
- Grand total
- Cash payment
- eSewa/banking payment recording
- Stock deduction
- Transaction history
- Multiple products per invoice

### Custom Pricing Must Work

The user must be able to sell a product at a custom price.

Example:

```text
Product value:       Rs. 67
Actual selling rate: Rs. 60
```

The actual rate of Rs. 60 must be retained on the sale line.

---

# 9. Invoice Management — MVP

### Must Finish

- Proper sales invoice generation
- Invoice number
- Fiscal/year information
- Reference number where required
- Voucher/invoice date
- Buyer/customer information
- Phone
- Address where required
- PAN/VAT where applicable
- Product/line information
- Batch number
- Expiry
- Quantity
- Unit
- Rate
- Amount
- Discount
- Tax/VAT
- Round-off
- Grand total
- Printable invoice
- Digital invoice generation

### WhatsApp Delivery

Digital invoice support is MVP.

The exact **automated WhatsApp/API delivery method** remains unconfirmed.

Therefore:

- Digital invoice generation belongs in MVP.
- Final automated WhatsApp integration should not be committed until the client confirms the method.

---

# 10. Customer Management — MVP

### Must Finish

- Customer creation
- Customer name
- Customer phone number
- Association of customers with relevant sales/credit transactions

### Later

- Rich customer history
- Advanced customer profiling
- Customer segmentation beyond what is required for the analytics/ML stage

A detailed customer history is explicitly not required for the core MVP.

---

# 11. Customer Returns & Refunds — MVP

### Must Finish

- Return initiation
- Original invoice verification
- Returned item recording
- Returned quantity recording
- Refund processing/recording
- Stock adjustment according to return condition
- Preservation of original transaction history

### Important Rule

```text
Return ≠ Delete Original Sale
```

The original sale must remain historically available.

---

# 12. Credit Ledger — MVP

The client currently records credit transactions manually in a register. Replacing this manual process is part of the operational MVP.

### Must Finish

- Mark sale as credit
- Associate credit sale with customer
- Record outstanding amount
- Record later payment
- Update outstanding balance

### Later / Needs Confirmation

- Formal credit due dates

The client has not yet confirmed whether due dates are required.

---

# 13. Damaged & Expired Stock — MVP

### Must Finish

- Identify damaged/expired stock
- Mark stock as non-saleable for the relevant workflow
- Record supplier return
- Reduce/adjust available stock
- Preserve return history

### Important

The exact detailed disposition rules for returned customer items remain a later business-rule definition where the client's requirement is not yet specific.

---

# 14. Monitoring — MVP

### Must Finish

- Current stock visibility
- Low-stock items
- Configurable reorder level
- Expiry-risk items
- Near-expiry visibility
- Stock movement visibility

This monitoring functionality directly addresses the client's stock-management problem.

---

# 15. Analytics — MVP / Month 3

Analytics is part of the project's core objective, but implementation follows the reliable operational data foundation.

### Must Finish During Month 3

- Sales trends
- Daily/weekly/monthly sales metrics where supported
- Revenue indicators
- Product performance
- Fast-moving products
- Slow-moving products
- Inventory analytics
- Low-stock analytics
- Expiry-risk reporting
- Purchase pattern analysis
- Profit indicators
- Analytics dashboard
- Verification of analytics against known database totals

### Analytics Principle

Analytics must use real operational data from:

```text
Sales + Purchases + Inventory
```

The dashboard should help the owner make purchasing decisions.

---

# 16. Purchasing / Replenishment Insights — MVP

### Must Finish Where Data Supports It

- Identify replenishment candidates
- Consider current stock
- Consider sales movement
- Estimate approximate replenishment quantities
- Present recommendations as decision support

### Must Not Do

The system must not automatically purchase stock or replace the owner's purchasing judgment.

---

# 17. Machine Learning — Month 3, Conditional

ML is **not the first priority**.

It should only be implemented after the core data pipeline and analytics are working.

## 17.1 Demand Forecasting

### Target

One strong demand-forecasting capability is preferred over several weak ML demonstrations.

### Must Finish if Data Supports It

- Historical sales dataset
- Data cleaning
- Exploratory analysis
- Baseline forecast
- Evaluation metric(s)
- Lag/rolling/calendar or relevant feature engineering
- First practical forecasting model
- Time-aware validation
- Leakage checks
- Measured model evaluation
- Forecast exposure through the application/API or prediction process

### Condition

```text
Sufficient historical sales data
          ↓
Forecasting is justified
```

Without sufficient data, a transparent baseline/recommendation is preferable to an unreliable ML model.

---

# 18. Customer Segmentation — Conditional / Later

Customer segmentation is not required for the core operational MVP.

It may be implemented during Month 3 **only if sufficient customer transaction data exists**.

Potential workflow:

```text
Customer Transactions
        ↓
Recency / Frequency / Monetary Features
        ↓
Scaling
        ↓
K-Means
        ↓
Evaluation
        ↓
Segment Profiling
```

### Priority

Demand forecasting has higher priority than customer segmentation.

If time or data is insufficient, segmentation should be postponed rather than weaken the core system or forecasting work.

---

# 19. AI Assistant — Conditional / Late Month 3

The AI assistant is explicitly lower priority than reliable transaction management and analytics.

### Include Only If

- Core application is stable.
- Analytics are connected to real data.
- Useful deterministic tools/functions are available.
- Time remains in the three-month schedule.
- The AI can be safely constrained to actual pharmacy data.

### Potential MVP-Level AI Questions

- What were the top-selling medicines last month?
- Which products are low in stock?
- Which medicines have the highest expiry risk?
- What does the demand forecast suggest?

### Required Guardrails

- AI must use controlled tools/functions.
- Business numbers must come from actual system data.
- AI must not invent stock/sales/revenue figures.
- AI should explain retrieved results rather than manufacture them.

---

# 20. Reporting & Legacy ERP Functionality

The previous management system had a much larger ERP scope, including accounting, MIS, inventory reporting, sales analysis, purchase analysis, ageing, stock demand and other modules.

### MVP Principle

PharmaKon should retain **necessary business information**, but should not recreate the entire previous ERP.

### Included Where Directly Required

- Sales invoices
- Purchase records
- Supplier records
- Product information
- Batch/expiry information
- Stock information
- Returns
- Credit
- Relevant sales/purchase analytics
- Relevant stock/expiry reporting
- Invoice calculations

### Not Automatically Included

Legacy functionality such as:

- Extensive general accounting modules
- Salesman targets
- Customer targets
- Area management
- Currency management
- Security deposits
- Bank guarantees
- LC management
- Cheque management
- Production orders
- Large collections of ERP reports
- Other enterprise functions not directly required by the client

A previous-system feature requires a separate scope decision before implementation.

---

# 21. Deployment & Operations — Month 3

### Must Finish

- Docker containerization
- Reproducible application build
- Environment-variable/secrets handling
- Separate production database
- Version-controlled migrations
- HTTPS
- Automated backups
- Backup restoration verification
- Basic logging/error monitoring
- Least-privilege operational access
- Recovery/rollback procedure
- GitHub Actions for test/build/deployment workflow
- Practical cloud deployment
- `.np` domain configuration

The deployment should remain simple and low-cost for a single-pharmacy system.

---

# 22. Testing — Throughout, Completed by Month 3

Critical functional paths must be tested before the system is considered complete.

### Must Finish

- Database migration tests
- Constraint/relationship tests
- Negative-stock prevention
- Purchase → stock increase
- Sale → stock decrease
- FEFO batch selection
- Custom-price calculation
- Invoice calculation
- Return behavior
- Credit balance updates
- Authorization/authentication foundation
- Analytics total verification
- ML time-aware validation and leakage checks where ML is implemented
- AI grounding checks where AI is implemented
- Backup restoration test

---

# 23. Final MVP Definition

The **PharmaKon MVP** is the smallest complete system that solves the client's primary problems while creating a reliable foundation for analytics.

## Must Be Complete by Final Delivery

### Core Operations

- Authentication
- Product management
- Batch management
- Inventory
- Suppliers
- Purchases
- Sales
- Invoice generation
- Payments
- Customer records
- Returns/refunds
- Credit ledger
- Damaged/expired stock handling
- Stock adjustments
- Low-stock monitoring
- Expiry monitoring

### Decision Support

- Sales analytics
- Product performance
- Inventory analytics
- Purchase analytics
- Revenue/profit indicators
- Replenishment insights

### Advanced Capability

- At least one meaningful ML capability, preferably demand forecasting, **if sufficient data supports it**
- Controlled AI assistant only if time, data, and safety requirements support it

### Production Readiness

- Tests
- Docker
- CI/CD
- Deployment
- HTTPS
- Backups
- Recovery verification
- `.np` domain

---

# 24. Explicitly Deferred to Later Versions

The following should normally be deferred unless the client explicitly reprioritizes them:

## V2 — Future Enhancements

- Separate employee accounts
- Detailed role-based access control
- Rich customer history
- Advanced customer analytics
- Customer segmentation if not completed during Month 3
- More advanced demand forecasting
- More sophisticated replenishment optimization
- Expanded reporting
- Broader accounting functionality from the previous ERP
- Staff targets/performance
- Additional business workflows not required by the current client scope
- Additional integrations beyond confirmed payment/invoice requirements

## V3 / Long-Term Possibilities

Potential future expansion could include:

- Multi-branch operation
- More granular employee permissions
- Advanced financial/accounting modules
- More advanced predictive analytics
- Larger AI assistant capabilities
- Additional external system integrations
- Enterprise-scale infrastructure

These are possibilities, not current requirements.

---

# 25. Scope Exclusions for the Three-Month Project

The following should not be added simply because they are technically possible or existed in the previous system:

- Microservices architecture
- Kubernetes
- Custom LLM hosting
- GPU infrastructure
- Unnecessary enterprise infrastructure
- Full recreation of the old ERP
- Large numbers of weak ML demos
- Complex RBAC without a client requirement
- Features without a clear pharmacy business purpose

The project booklet explicitly recommends keeping the architecture simple and avoiding infrastructure that the single-pharmacy workload does not justify.

---

# 26. Scope Trade-Off Rule

Because the deadline is fixed, a new feature must have an explicit schedule impact.

### Rule

```text
New Feature Added
       ↓
Deadline Impact Identified
       ↓
Priority Evaluated
       ↓
Lower-Priority Feature
Removed / Postponed
```

No feature should silently expand the project.

The three-month deadline, Review 1 milestone, and core operational milestones must be protected.

---

# 27. Priority Ladder

The implementation priority is:

```text
P0 — Correct Core Operations
     Inventory
     Purchases
     Sales
     Invoices
     Stock integrity
     Returns
     Credit

        ↓

P1 — Operational Monitoring
     Low stock
     Expiry risk
     Stock adjustments
     Supplier returns

        ↓

P2 — Analytics
     Sales
     Products
     Inventory
     Purchasing
     Revenue / Profit

        ↓

P3 — Decision Support
     Replenishment insights

        ↓

P4 — ML
     Demand forecasting
     Customer segmentation

        ↓

P5 — AI
     Controlled analytics assistant
```

If time becomes constrained, higher-priority layers must be protected before lower-priority layers.

---

# 28. Month-by-Month Delivery Summary

| Area | Month 1 | Month 2 | Month 3 | Later |
|---|---:|---:|---:|---:|
| Requirements | Must finish | — | — | Change requests |
| Architecture | Must finish | Refine | — | Major changes only |
| Database design | Must finish | Implement | Refine | Future entities |
| Authentication | Design | Implement | Harden | Individual accounts |
| Products | Design | Implement | Refine | Advanced features |
| Batches | Design | Implement | Refine | — |
| Inventory | Design | Implement | Harden/analytics | Advanced optimization |
| Purchases | Design | Implement | Refine/analytics | Advanced procurement |
| Sales | Design | Implement | Harden | Advanced workflows |
| Invoicing | Requirements | Implement | Digital/production hardening | Additional integrations |
| Returns | Requirements | Implement if MVP confirmed | Harden | Advanced policies |
| Credit ledger | Requirements | Implement | Harden | Due-date/advanced credit if confirmed |
| Monitoring | Design | Implement | Analytics | Advanced alerts |
| Analytics | Data requirements | Data foundation | Implement | Advanced BI |
| Replenishment | Design | Data foundation | Implement | Optimization |
| Demand forecasting | Plan | Prepare data | Implement if data supports | Advanced models |
| Segmentation | Plan | Prepare data | Conditional | Later |
| AI assistant | Scope | — | Conditional | Expanded AI |
| Testing | Strategy | Core tests | Full verification | Continuous |
| Docker/CI/CD | Plan | Foundation | Implement | Improve |
| Deployment | Plan | — | Implement | Scale if needed |

---

# 29. Month 2 Exit Criteria

The MVP core must have a usable operational foundation by the end of Month 2.

At minimum:

- Authentication works.
- Products work.
- Suppliers work.
- Purchases work.
- Batches work.
- Inventory works.
- Stock movements are consistent.
- Sales work.
- Stock deduction works.
- Critical business rules have tests.
- Frontend is integrated with backend APIs.
- Core database migration is reproducible.

---

# 30. Final Exit Criteria

The three-month project is complete when:

- Core pharmacy workflows work end-to-end.
- Analytics dashboard uses real data.
- At least one ML capability has been meaningfully evaluated and integrated, where data supports it.
- AI assistant, if included, is controlled and grounded in real data.
- Critical paths are tested.
- Docker build works.
- Deployment works.
- `.np` domain works.
- Backups are configured and verified.
- Documentation is complete.
- The developer can explain the major architectural and ML decisions.

---

# 31. Final Scope Boundary

The **three-month PharmaKon MVP is not “everything the old pharmacy software could do.”**

It is:

```text
Reliable Pharmacy Operations
          +
Useful Analytics
          +
Practical Decision Support
          +
One Strong ML Capability
          +
Production-Ready Deployment
```

The system must solve the client's most important problems first.

Features that do not directly support those goals should be postponed unless an explicit client decision changes the priority.

---

# 32. Source of Truth

The scope in this document is based on:

1. The confirmed client requirements.
2. The previous management-system reference.
3. The 3-month project booklet and its staged MVP strategy.

The project booklet states that the three-month project should use an MVP approach, with a reliable core management system first, followed by analytics, ML, AI and deployment hardening. It also states that new features should require an explicit trade-off against the deadline.

Any future client change must be reflected in this scope before implementation.
