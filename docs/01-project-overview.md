# 01 --- Project Overview

**Document status:** Draft v1.1 --- updated with legacy-system reference, success metrics, risks/assumptions and glossary
**Last updated:** 15 September 2026 (Day 1)
**Author:** Project lead
**Related documents:** `PharmaKon_Client_Confirmed_Requirements.docx`, `Pharmacy_Management_Analytics_3_Month_Project_Booklet.pdf`
**Supersession rule:** If a later client conversation changes a requirement recorded here, the newer confirmed requirement takes precedence. Record the change and the date it was confirmed rather than silently editing history.

---

## 1. Project Identity

**Project Name:** PharmaKon\
**Client:** Aayushman Pharmacy\
**Deployment:** Single retail pharmacy\
**Project Type:** Pharmacy Management and Analytics System\
**Project Timeline:** Approximately 3 months / 90 days (15 Sep 2026 -- 13 Dec 2026)\
**Primary Users:** Pharmacy owner and 3 staff members\
**Locale / Currency:** Nepal; all amounts in NPR (Rs.); VAT and eSewa references follow Nepali business practice.

PharmaKon is a web-based pharmacy management and analytics system
designed for Aayushman Pharmacy. The system will focus on improving the
pharmacy's day-to-day inventory and sales operations while providing the
owner with useful analytics and purchasing insights.

The project is being developed as a staged MVP: first establish a
reliable core management system, then add analytics and data-driven
capabilities, followed by ML/AI features where the available data and
project timeline justify them.

---

## 2. Client Objective

The client's main objective is to replace important manual pharmacy
processes with a reliable digital system that improves stock management,
billing, and decision-making.

The client identified three major operational problems:

1.  **Unmanaged stock**
2.  **Lack of useful medicine analytics and insights**
3.  **Lack of proper sales invoices**

PharmaKon should therefore provide a central system for managing
products, batches, stock, purchases, sales, invoices, returns, credit
transactions, and analytics.

The analytics component should help the owner understand stock movement
and product performance so that purchasing decisions can be made using
actual sales and inventory information.

### 2.1 Core Objectives

-   Maintain accurate product, batch, expiry, and stock information.
-   Prevent inventory from becoming negative.
-   Use **FEFO (First Expiry, First Out)** when selling products with
    multiple batches.
-   Provide proper sales invoices with transparent subtotal, tax,
    discount/custom pricing, round-off, and final total calculations.
-   Allow the user to record the **actual selling price** used for each
    product.
-   Support cash and eSewa/banking payments.
-   Support printed invoices and digital invoice delivery when
    requested.
-   Digitize the pharmacy's existing manual credit ledger.
-   Record purchases and supplier information at the batch/purchase
    level.
-   Track damaged and expired stock returned to suppliers.
-   Provide low-stock and expiry-risk visibility.
-   Provide analytics for sales, products, inventory, purchasing, and
    revenue/profit indicators.
-   Provide purchasing/replenishment insights based on sales and current
    stock.
-   Introduce demand forecasting only after sufficient historical sales
    data is available.
-   Preserve transaction history instead of permanently deleting
    completed transactions.

### 2.2 Success Metrics

These are not yet client-confirmed targets, only proposed measures so
"success" can be evaluated objectively at Review 1 and at final
delivery rather than judged only by feature count. Each should be
confirmed or replaced with the client's own numbers during the
interview.

| Problem | Proposed measure of success |
|---|---|
| Unmanaged stock | Owner can see current stock, low-stock items and expiry-risk items for any product in under a few seconds, without a manual count. |
| No medicine analytics | Owner can identify top/slow-moving products and get a purchasing suggestion directly from the system, not from memory or a notebook. |
| No proper invoices | 100% of sales produce a printed or digital invoice with correct subtotal, discount, tax and round-off; zero invoices calculated by hand. |
| Credit sales on paper | All new credit sales are recorded digitally with an auditable outstanding balance, replacing the register copy going forward. |
| Data trust | Analytics totals reconcile exactly against raw database totals (see Testing Checklist in the project booklet). |

---

## 3. Users

### 3.1 Owner

The owner is the primary decision-maker and the main consumer of
analytics.

The owner needs to:

-   Manage and monitor pharmacy stock.
-   Review sales and product performance.
-   Identify fast-moving and slow-moving products.
-   Identify low-stock and expiry-risk items.
-   Understand revenue/profit indicators.
-   Use sales and stock information to make purchasing decisions.
-   Review purchasing/replenishment recommendations.

### 3.2 Pharmacy Staff

The pharmacy has **3 staff members** who operate the pharmacy's
day-to-day processes.

Their operational activities include:

-   Managing stock-related information.
-   Recording purchases.
-   Processing sales.
-   Generating invoices.
-   Handling customer returns/refunds.
-   Recording credit transactions and later payments.
-   Performing stock adjustments after physical verification.

### 3.3 Authentication / Access Model

For the initial system, the client explicitly does **not** require
separate employee accounts.

The initial system will use **one account** with access to manage stock
and view analytics. Advanced role-based accounts are outside the current
requirement.

This access model should remain simple for the MVP and should not be
expanded into a complex permission system unless the client later
changes the requirement.

---

## 4. Pharmacy Context

Aayushman Pharmacy is a **single retail pharmacy**.

The pharmacy has approximately **1,500 products**, covering:

-   Medicines
-   Surgical items
-   Cosmetics
-   Baby products
-   Food products

Products may have multiple batches. Product records need to support
information such as:

-   Product name
-   Product code
-   Category
-   Unit
-   MRP
-   Purchase price/cost
-   Barcode, where available
-   Batch number
-   Expiry date
-   Stock quantity

Purchase cost must be maintained at the batch/purchase level so that
profit analysis can be based on the actual cost associated with stock.

---

## 5. Legacy System Reference (Fields to Preserve)

The pharmacy previously produced invoices through an existing
paper/manual or prior billing process. PharmaKon should preserve the
business information the client already relies on rather than silently
dropping fields, while simplifying the interface and automating
calculations and stock updates.

**Invoice header information to preserve:**

-   Invoice number
-   Fiscal/year information
-   Reference number
-   Voucher date
-   Buyer name, address and phone
-   PAN/VAT number, where applicable

**Line-item information to preserve:**

-   Product
-   Closing stock
-   Batch number
-   Expiry date
-   Actual quantity
-   Unit and alternate quantity/unit where required
-   Rate and amount

**Invoice calculations to preserve:**

-   Discount
-   VAT/tax
-   Round-off
-   Grand total

PharmaKon's improvement over the legacy process is not to remove this
information, but to **simplify the interface and automate the
calculations and stock updates** so staff no longer compute totals by
hand.

---

## 6. Current Workflow

This section records the client's current operational process and the
problems that PharmaKon is intended to address. It should not be treated
as a redesigned future-state workflow.

### 6.1 Stock and Inventory

The pharmacy currently monitors stock to decide purchasing requirements.

Physical stock is checked periodically; the client previously stated
that this is done **weekly**.

Purchasing decisions are based on:

-   Current stock
-   Sales movement

The pharmacy also has damaged and expired medicines that are sent back
to suppliers.

Stock adjustments may be required after physical stock verification.

**Current Problems**

The client identified **unmanaged stock** as the biggest problem. The
current process does not provide the level of structured stock
visibility and automated monitoring required for efficient management.

### 6.2 Purchasing

Medicine purchasing decisions are currently based on sales and current
stock.

The required purchase quantity is decided from the movement of products
and the amount of stock currently available.

Purchase information needs to include:

-   Supplier
-   Invoice/reference
-   Product
-   Batch
-   Expiry
-   Quantity
-   Purchase cost
-   Payment information

Damaged and expired medicines are sent back to suppliers.

### 6.3 Sales and Billing

The pharmacy sells multiple products in a single transaction.

The current billing process has a significant problem: the pharmacy does
not consistently generate proper sales invoices. The lack of proper
invoices was identified as one of the client's biggest problems.

The required billing process must support:

-   Product selection/scanning
-   Batch selection using FEFO
-   Quantity
-   Actual/custom selling price
-   Default 10% discount requirement
-   13% tax/VAT
-   Round-off
-   Grand total
-   Payment
-   Invoice generation
-   Stock deduction

The client specifically highlighted that products are sometimes sold at
custom prices without proper calculation. For example, a medicine with a
value of **Rs. 67** may be sold for **Rs. 60**.

Therefore, the actual selling rate used for every invoice line must be
recorded clearly.

The client's confirmed payment methods are mainly:

-   Cash
-   eSewa/banking systems

The pharmacy has a printer, so printable invoices are required.

When a customer requests a digital bill, the invoice should be capable
of being sent to the customer's phone/WhatsApp number.

### 6.4 Customer Returns

The current confirmed return requirement is that the customer must
return the original bill/invoice to receive a refund.

The return process is:

1.  Customer provides the original bill.
2.  The invoice is verified.
3.  The returned item and quantity are recorded.
4.  A refund is processed.
5.  Stock is adjusted according to the condition of the returned item.
6.  The original transaction history is preserved.

Sales cancellation/return must not permanently delete the historical
transaction.

### 6.5 Credit Sales

Credit transactions are currently written manually in a **register
copy**.

This creates a need for a basic digital credit ledger.

The intended process is:

1.  Create the sale.
2.  Mark the sale as credit.
3.  Record the customer.
4.  Record the outstanding amount.
5.  When the customer later pays, record the payment.
6.  Update the remaining balance.

For the initial customer record, the required details are:

-   Customer name
-   Customer phone number

A more extensive customer history is useful for future implementation
but is not required for the core MVP.

### 6.6 Damaged and Expired Stock

Damaged and expired medicines are sent back to suppliers.

The intended operational record should capture the process of:

1.  Identifying the item.
2.  Marking it as non-saleable.
3.  Recording the supplier return.
4.  Reducing/adjusting the available stock.
5.  Retaining the historical record.

---

## 7. Current → Future Workflow Direction

The client-confirmed workflow establishes the following core operational
chain:

``` text
Supplier Purchase
       ↓
Product / Batch / Expiry / Quantity / Cost
       ↓
Stock Increase
       ↓
Inventory Monitoring
       ↓
Sales / Stock Movement
       ↓
FEFO Batch Selection
       ↓
Actual Selling Price / Discount
       ↓
13% Tax + Round-off
       ↓
Invoice + Payment
       ↓
Stock Deduction
       ↓
Sales & Stock History
       ↓
Analytics
       ↓
Purchasing / Replenishment Decision
```

Additional flows:

``` text
Customer Return
    ↓
Original Bill Verification
    ↓
Return Item / Quantity
    ↓
Refund
    ↓
Stock Adjustment
    ↓
Historical Record Preserved
```

``` text
Credit Sale
    ↓
Customer + Outstanding Amount
    ↓
Digital Credit Ledger
    ↓
Later Payment
    ↓
Outstanding Balance Updated
```

``` text
Damaged / Expired Stock
    ↓
Mark Non-Saleable
    ↓
Supplier Return
    ↓
Stock Adjustment
    ↓
History Preserved
```

These flows represent the confirmed operational direction and will be
refined into formal functional requirements and business rules in
subsequent project documents.

---

## 8. Information and Decision Needs

The system is not intended to be only a digital billing application. A
major objective is to turn pharmacy transaction and stock data into
useful operational information.

The owner needs visibility into:

-   Sales trends
-   Fast-moving products
-   Slow-moving products
-   Current stock levels
-   Low-stock products
-   Expiry-risk products
-   Purchase patterns
-   Revenue indicators
-   Profit indicators

The system should use this information to support purchasing decisions
by identifying products that need replenishment and estimating
approximate quantities where the available data supports a defensible
recommendation.

Demand forecasting may be introduced after enough historical sales data
has accumulated. Forecasting should **support, not replace, the owner's
purchasing decision**.

---

## 9. Confirmed Business Constraints Relevant to the Overview

The following constraints are confirmed by the client's latest interview
responses:

-   The system is for one retail pharmacy.
-   There are 3 staff members plus the owner.
-   The initial system uses one account rather than separate employee
    accounts.
-   Approximately 1,500 products are managed.
-   Products can have multiple batches.
-   Sales should follow FEFO.
-   Negative stock is not allowed.
-   Low-stock monitoring should use a configurable reorder level.
-   Damaged and expired medicines are returned to suppliers.
-   Stock adjustments must retain an adjustment record.
-   Proper sales invoices are required.
-   Tax/VAT is currently specified by the client as 13% and is added
    after the base price.
-   The default discount requested by the client is 10%.
-   Custom selling prices must be supported.
-   The actual selling rate must be recorded on the invoice.
-   Customer returns require the original bill/invoice.
-   Completed transaction history must be preserved.
-   Customer name and phone number are sufficient for the initial
    customer record.
-   Credit sales must be supported through a digital ledger.
-   Purchase cost must be stored at batch/purchase level.
-   Purchasing decisions are based on sales movement and current stock.

---

## 10. Known Gaps / Items Still Requiring Confirmation

The following points are explicitly identified by the client record as
not yet fully confirmed:

1.  **WhatsApp delivery**
    -   Exact WhatsApp delivery method/API/account to be used for
        automated invoice sending.
2.  **10% discount**
    -   Whether 10% should be automatically applied or merely offered as
        the default selectable value.
3.  **13% tax/VAT**
    -   Whether 13% applies uniformly to every product category,
        including cosmetics, surgical items, baby products, and food, or
        whether different legal treatment applies to any category.
4.  **Credit due date**
    -   Whether credit transactions require a due date or only an
        outstanding balance.

These items must remain explicitly marked as unresolved rather than
being silently assumed during implementation.

---

## 11. Risks & Assumptions

Recorded here so they can be raised explicitly at Review 1, per the
booklet's requirement to present "risks, assumptions and next-month
plan." This list should be revisited and updated as the project
progresses, not written once and forgotten.

### 11.1 Assumptions (not yet client-confirmed)

-   The pharmacy has no existing digital sales history to migrate;
    analytics and ML will build up from PharmaKon's own recorded
    transactions going forward.
-   Barcode scanning is optional/partial (some products have barcodes,
    others do not) rather than a hard requirement for every item.
-   Internet connectivity at the pharmacy is reliable enough for a
    web-based system during business hours.
-   The single WhatsApp/phone number contact channel is enough for
    digital invoice delivery; no separate SMS gateway is required.
-   VAT/tax and discount rules will stay stable enough during the
    3-month build that hardcoding today's confirmed values (13% VAT,
    10% discount) as configurable settings, rather than a full rules
    engine, is acceptable for MVP.

### 11.2 Risks

| Risk | Potential impact | Mitigation direction |
|---|---|---|
| Only ~90 days available, single developer | Feature creep could threaten Review 1 or final delivery | Strict MVP scope control (Section 12) and the booklet's scope-control rules |
| No historical digital sales data at project start | Demand forecasting (ML) may lack enough data to be reliable within 3 months | Treat forecasting as a stretch goal; ship a well-evaluated baseline or defer it rather than force a weak model |
| ~1,500 products to onboard | Manual data entry could delay Month 2 milestones | Confirm whether a product list/spreadsheet exists that can be bulk-imported instead of entered by hand |
| Four requirements still unconfirmed (Sec. 10) | Wrong assumptions could require rework of invoicing/credit logic | Resolve before SPEC-writing for sales/billing and credit-ledger features |
| Single-account access model | No audit trail of which staff member performed an action | Acceptable for MVP per client's explicit request; flag as a V2 candidate if disputes over accountability arise |
| eSewa/WhatsApp third-party integrations | External API changes or account setup delays could block invoice delivery features | Treat as an isolated, swappable module; core invoicing must work without them |

---

## 12. Initial Project Direction

Based on the confirmed client requirements, PharmaKon's initial focus
should be:

### Highest-priority operational areas

1.  Product and batch inventory
2.  Purchases and suppliers
3.  Sales and invoicing
4.  Custom pricing and discounts
5.  Returns and refunds
6.  Credit ledger
7.  Stock, expiry, and low-stock monitoring
8.  Analytics dashboard
9.  Purchasing insights
10. Automated backup

The project should prioritize **correctness of sales, inventory, and
accounting-related workflows** over visual polish or unnecessary
technical complexity.

Analytics should be built on reliable transactional data before ML
capabilities are introduced. ML should only be used where sufficient
data and measurable evaluation support it.

---

## 13. Glossary

| Term | Meaning |
|---|---|
| **FEFO** | First Expiry, First Out --- sell the batch with the earliest expiry date before other batches of the same product. |
| **MRP** | Maximum Retail Price --- the printed ceiling price of a product. |
| **VAT** | Value Added Tax --- the 13% tax applied to the base price during billing (client-confirmed rate, pending category-level confirmation). |
| **eSewa** | A widely used Nepali digital wallet/payment gateway; one of the client's confirmed non-cash payment methods. |
| **Batch** | A specific purchased lot of a product, carrying its own expiry date, purchase cost and quantity. |
| **Reorder level** | The configurable stock threshold below which a product is flagged as low-stock. |
| **RFM** | Recency, Frequency, Monetary --- customer features used for the optional segmentation ML feature (Priority 2 in the booklet). |
| **MVP** | Minimum Viable Product --- the smallest reliable version of the system that addresses the client's three core problems. |

---

## 14. Scope Boundary for This Document

This project overview establishes:

-   What PharmaKon is.
-   Who will use it.
-   Why the client needs it.
-   The client's major operational problems and how success will be measured.
-   How the pharmacy currently operates, including what the legacy invoicing process must not lose.
-   The confirmed direction of the core workflows.
-   The main information and decision needs.
-   Known unresolved requirements, and the risks/assumptions around them.

Detailed system behavior, complete functional requirements, user
permissions, formal business rules, MVP/V2 scope, architecture, database
design, API contracts, and analytics/ML specifications will be
documented separately in the subsequent project documents.

**Source of truth:** The latest confirmed client requirements should
take precedence over earlier assumptions if the client changes a
requirement. The project booklet defines the development sequence and
methodology; client-confirmed requirements define the actual business
behavior.