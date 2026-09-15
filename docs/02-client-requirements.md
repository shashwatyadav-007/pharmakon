h# 02 — Client Requirements

**Document status:** Draft v1.1 — added requirement IDs for traceability, a Non-Functional Requirements section, and six additional open questions
**Last updated:** 15 September 2026 (Day 1)
**Related documents:** `01-project-overview.md`, `PharmaKon_Client_Confirmed_Requirements.docx`

## 1. Document Purpose

This document records the client's requirements for **PharmaKon**, the pharmacy management and analytics system for **Aayushman Pharmacy**.

The requirements below are based on the client's latest interview responses and are treated as **confirmed business requirements unless the client changes them**.

Requirements that the client has not yet confirmed are explicitly separated in the final section. They must not be implemented based on assumptions.

Each requirement below carries a short **ID** (e.g. `INV-03`) so that the functional-requirements, business-rules, database-design and spec documents can reference the exact client requirement they trace back to, instead of re-describing it in prose each time.

---

# 2. Business & Users

| ID | Requirement | Client Requirement | Status |
|---|---|---|---|
| BU-01 | Pharmacy | Aayushman Pharmacy | Confirmed |
| BU-02 | Branches | Single retail pharmacy | Confirmed |
| BU-03 | Staff | 3 staff members plus the owner | Confirmed |
| BU-04 | User accounts | Do not create separate employee accounts for the initial system. Use one account with access to manage stock and view analytics. | Confirmed |
| BU-05 | Access model | Keep authentication simple. The single account should have the required operational access. Advanced role-based accounts are not part of the current requirement. | Confirmed |

### Requirement Notes

The initial version should not introduce separate employee accounts or a complex role/permission hierarchy. The access model should remain simple unless the client later changes this requirement.

---

# 3. Inventory & Products

| ID | Requirement | Client Requirement | Status |
|---|---|---|---|
| INV-01 | Product volume | Approximately 1,500 products | Confirmed |
| INV-02 | Product categories | Medicines, surgical items, cosmetics, baby products and food products | Confirmed |
| INV-03 | Product information | Product name, code, category, unit, MRP, purchase price/cost, barcode where available, batch number, expiry date and stock quantity | Confirmed |
| INV-04 | Multiple batches | The same product can have multiple batches | Confirmed |
| INV-05 | Batch selling | Use FEFO: sell the batch with the earliest expiry first | Confirmed |
| INV-06 | Negative stock | Not allowed | Confirmed |
| INV-07 | Stock monitoring | Current stock is monitored to decide purchasing requirements | Confirmed |
| INV-08 | Physical stock | Stock is checked periodically; the client previously stated weekly checking | Confirmed |
| INV-09 | Low stock | Provide low-stock visibility/alerts using a configurable reorder level | Confirmed |
| INV-10 | Damaged/expired stock | Damaged and expired medicines are sent back to suppliers | Confirmed |
| INV-11 | Stock adjustment | Allow stock adjustment after physical verification and retain a record of the adjustment | Confirmed |

### Requirement Interpretation

Inventory is one of the client's primary problem areas. The system therefore needs to maintain reliable stock quantities and batch-level information rather than treating a product as a single undifferentiated stock quantity.

---

# 4. Sales, Pricing & Billing

| ID | Requirement | Client Requirement | Status |
|---|---|---|---|
| SPB-01 | Sales invoices | PharmaKon must generate proper sales invoices. The current lack of invoices is one of the pharmacy's biggest problems. | Confirmed |
| SPB-02 | Invoice delivery | When a customer requests a bill, the system should generate an invoice that can be sent to the customer's phone/WhatsApp number. | Confirmed |
| SPB-03 | Tax | 13% tax/VAT is applied to each product. | Confirmed* |
| SPB-04 | Tax calculation | Tax is excluded from the product/base price and added afterward during billing. | Confirmed* |
| SPB-05 | Tax display | Clearly show subtotal, tax and final total. | Confirmed |
| SPB-06 | Default discount | Default discount requested is 10%. There is no maximum discount limit requirement at present. | Confirmed* |
| SPB-07 | Custom selling price | User must be able to enter a custom selling price instead of relying only on MRP. | Confirmed |
| SPB-08 | Actual selling rate | Invoice must clearly record the actual selling rate used for each line. | Confirmed |
| SPB-09 | Multiple products | One invoice can contain multiple products. | Confirmed |
| SPB-10 | Payment methods | Mainly cash and eSewa/banking systems. | Confirmed |
| SPB-11 | Printed invoice | Printable invoice must be supported because the pharmacy has a printer. | Confirmed |
| SPB-12 | Customer returns | Customer must return the bill/invoice to receive a refund. | Confirmed |
| SPB-13 | Transaction history | Sales cancellation/return must preserve transaction history rather than permanently deleting the record. | Confirmed |
| SPB-14 | Round-off | Support round-off as a separate invoice adjustment. | Confirmed |

\* The exact applicability of tax across all product categories and the exact behavior of the default discount still require clarification; see Section 12.

### Custom Pricing Requirement

The client specifically reported that some medicines are sold below their stated value without proper calculation.

Example:

```text
Product value: Rs. 67
Actual selling price: Rs. 60
```

PharmaKon must therefore support an actual selling rate per invoice line. The system must not assume that MRP is always the final selling price.

---

# 5. Customers & Credit

| ID | Requirement | Client Requirement | Status |
|---|---|---|---|
| CC-01 | Customer information | Name and phone number are sufficient for the initial customer record. | Confirmed |
| CC-02 | Customer history | Useful for future implementation, but not required for the core MVP. | Confirmed |
| CC-03 | Credit sales | Credit transactions are currently written in a register copy. | Confirmed |
| CC-04 | Credit management | Provide a basic digital credit ledger so credit sales and later payments can be recorded instead of relying on the register. | Confirmed |
| CC-05 | Digital bill recipient | Customer phone/WhatsApp number should be available when the customer requests a digital invoice. | Confirmed |

### Credit Requirement

The digital credit ledger should replace the current manual register process.

The confirmed operational flow is:

```text
Credit Sale
    ↓
Customer
    ↓
Outstanding Amount
    ↓
Later Payment
    ↓
Updated Balance
```

Whether a formal due date is required has not yet been confirmed.

---

# 6. Purchases & Suppliers

| ID | Requirement | Client Requirement | Status |
|---|---|---|---|
| PS-01 | Purchasing decision | Medicine purchasing decisions are based on sales and stock monitoring. | Confirmed |
| PS-02 | Purchase quantity | Required quantity is decided from sales movement and current stock. | Confirmed |
| PS-03 | Supplier returns | Damaged and expired medicines are sent back to suppliers. | Confirmed |
| PS-04 | Purchase records | Maintain supplier, invoice/reference, product, batch, expiry, quantity, purchase cost and payment information. | Confirmed |
| PS-05 | Purchase price | Store purchase cost at batch/purchase level to support accurate profit analysis. | Confirmed |

### Purchasing Requirement

Purchasing is currently a decision based on observed sales movement and available stock.

PharmaKon should preserve these inputs so that the owner can later receive data-driven replenishment support.

---

# 7. Analytics & Decision Support

| ID | Requirement | Client Requirement | Status |
|---|---|---|---|
| AD-01 | Biggest problem | Unmanaged stock | Confirmed |
| AD-02 | Second major problem | No useful medicine analytics/insight | Confirmed |
| AD-03 | Third major problem | No proper invoices | Confirmed |
| AD-04 | Analytics objective | Provide clear information about stock movement and medicine performance so the owner can make purchasing decisions. | Confirmed |
| AD-05 | Sales analytics | Sales trends | Confirmed |
| AD-06 | Product analytics | Fast-moving and slow-moving products | Confirmed |
| AD-07 | Inventory analytics | Stock levels and low-stock items | Confirmed |
| AD-08 | Expiry analytics | Expiry-risk items | Confirmed |
| AD-09 | Purchasing analytics | Purchase patterns | Confirmed |
| AD-10 | Financial indicators | Revenue/profit indicators | Confirmed |
| AD-11 | Purchasing support | Recommend which products need replenishment and approximate quantities. | Confirmed |
| AD-12 | Demand forecasting | May be introduced after sufficient historical sales data is available. | Conditional |
| AD-13 | Forecasting role | Forecasting should support, not replace, the owner's purchasing decision. | Confirmed |

### Required Decision Support

The analytics system should help answer practical questions such as:

- Which products are selling quickly?
- Which products are moving slowly?
- Which products are currently low in stock?
- Which products are at risk of expiry?
- What products may need replenishment?
- Approximately how much should be purchased?

ML should not be forced into the system when insufficient historical data exists.

---

# 8. Non-Functional Requirements

The client interview so far has focused on **what** the system must do (functional requirements). It has not yet covered **how well** the system must do it — the qualities that affect architecture, hosting, and testing decisions but are easy to skip past in a features-only conversation. None of the rows below are client-confirmed; they are proposed defaults for a single-pharmacy, single-account system and must be confirmed or corrected with the client before they drive design decisions.

| ID | Requirement | Proposed Default | Status |
|---|---|---|---|
| NFR-01 | Security | Single shared account is protected by a password; no sensitive data (customer phone numbers, credit balances) is exposed without authentication. | Needs confirmation |
| NFR-02 | Backup & data retention | Automated daily backup of the database; transaction history retained indefinitely rather than purged. | Needs confirmation — see CR-010 |
| NFR-03 | Performance | The system stays responsive for the pharmacy's actual daily transaction volume (see CR-005) on ordinary retail hardware. | Needs confirmation |
| NFR-04 | Availability | The system should be usable during pharmacy operating hours; brief planned downtime for maintenance is acceptable. | Needs confirmation |
| NFR-05 | Usability | Staff with no prior software experience can process a sale within a short, defined learning period; the billing screen prioritizes speed over configurability. | Needs confirmation |
| NFR-06 | Device compatibility | The system runs in a standard web browser on the pharmacy's existing computer(s); no specialized hardware beyond the existing printer is assumed unless confirmed otherwise (see CR-009). | Needs confirmation |
| NFR-07 | Data privacy | Customer name/phone and credit-ledger data are not shared outside the system except where the client explicitly requests digital invoice delivery. | Needs confirmation |

---

# 9. Previous System — Information to Preserve

The client previously used a broader management/ERP system. The previous system screenshots show functionality covering inventory, purchasing, sales, accounting, MIS reporting, product/customer/vendor masters, stock reporting, near-expiry information, product ageing, sales analysis and purchase analysis.

The client's confirmed requirement is to **retain necessary business information while simplifying the interface and automating calculations and stock updates**.

The following previous-system information has been confirmed as relevant to preserve:

## Invoice Information

- Invoice number
- Fiscal/year information
- Reference number
- Voucher date
- Buyer
- Address
- Phone
- PAN/VAT number where applicable

## Invoice Line Information

- Product
- Closing stock
- Batch number
- Expiry date
- Actual quantity
- Unit
- Alternate quantity/unit where required
- Rate
- Amount

## Invoice Calculations

- Discount
- VAT/tax
- Round-off
- Grand total

### Legacy-System Principle

The presence of a feature in the previous management system does **not** automatically make it a required PharmaKon feature.

Each legacy capability must be evaluated against the confirmed client requirements and the project's MVP scope before implementation.

---

# 10. Confirmed Core Workflows

The client-confirmed requirements establish the following core workflows.

## 10.1 Purchase → Inventory

```text
Supplier Purchase
        ↓
Purchase Invoice / Reference
        ↓
Product + Batch + Expiry + Quantity + Cost
        ↓
Stock Increase
        ↓
Payment Status
```

## 10.2 Sale → Invoice → Stock

```text
Invoice
   ↓
Select / Scan Product
   ↓
FEFO Batch Selection
   ↓
Quantity
   ↓
Actual / Custom Selling Price
   ↓
Default 10% Discount Where Applicable
   ↓
13% Tax
   ↓
Round-off
   ↓
Grand Total
   ↓
Payment
   ↓
Invoice
   ↓
Stock Deduction
```

## 10.3 Customer Return

```text
Customer Provides Original Bill
            ↓
Verify Invoice
            ↓
Record Returned Item / Quantity
            ↓
Process Refund
            ↓
Adjust Stock According to Return Condition
            ↓
Preserve Transaction History
```

## 10.4 Damaged / Expired Stock

```text
Identify Item
     ↓
Mark Non-Saleable
     ↓
Record Supplier Return
     ↓
Reduce / Adjust Stock
     ↓
Retain History
```

## 10.5 Credit Sale

```text
Create Sale
    ↓
Mark as Credit
    ↓
Record Customer
    ↓
Record Outstanding Amount
    ↓
Later Payment
    ↓
Update Balance
```

## 10.6 Analytics → Purchasing

```text
Sales History + Stock History
             ↓
Product / Inventory Analysis
             ↓
Fast / Slow / Low / Expiry-Risk Identification
             ↓
Purchasing Insight
             ↓
Recommended Replenishment
```

---

# 11. Client Pain Points

The client's requirements are driven by three major problems.

## 11.1 Unmanaged Stock

The pharmacy needs better visibility and control over:

- Current stock
- Product batches
- Expiry dates
- Low-stock products
- Stock adjustments
- Damaged/expired products
- Stock movement

## 11.2 Lack of Useful Analytics

The owner currently lacks useful information for understanding medicine performance and making purchasing decisions.

PharmaKon should turn sales and inventory history into actionable information.

## 11.3 Lack of Proper Invoices

The current lack of proper invoices is a major operational issue.

PharmaKon must provide reliable invoice generation, calculation, printing, transaction history, and digital delivery support when requested.

---

# 12. Requirements Still Requiring Client Confirmation

The following requirements are explicitly unresolved and must not be silently assumed.

## CR-001 — WhatsApp Invoice Delivery

**Question:** What exact WhatsApp delivery method/API/account should be used for automated invoice sending?

**Current status:** Needs confirmation.

---

## CR-002 — Default 10% Discount Behavior

**Question:** Should the 10% discount be automatically applied to sales, or should it merely be offered as the default selectable value?

**Current status:** Needs confirmation.

---

## CR-003 — Tax Applicability by Product Category

**Question:** Does the 13% tax/VAT apply uniformly to every product category, including:

- Medicines
- Surgical items
- Cosmetics
- Baby products
- Food products

Or does any category have different legal treatment?

**Current status:** Needs confirmation.

---

## CR-004 — Credit Due Date

**Question:** Should credit transactions include a due date, or should the system track only the outstanding balance?

**Current status:** Needs confirmation.

---

## CR-005 — Sales Volume / Scale

**Question:** Approximately how many sales/invoices occur per day or per week? Are there peak hours or seasonal spikes (e.g. flu season, festivals)?

**Why it matters:** This directly affects database sizing, analytics data volume, and whether a demand-forecasting model will have enough transaction history to be reliable within the 3-month timeline.

**Current status:** Needs confirmation.

---

## CR-006 — Manual Reports Currently Prepared

**Question:** What reports, if any, does the owner currently prepare by hand (daily cash summary, stock count sheets, supplier statements, etc.)? What information does the owner wish they had but currently cannot get?

**Why it matters:** Directly shapes the analytics dashboard so it replaces real manual work rather than guessing at useful metrics.

**Current status:** Needs confirmation.

---

## CR-007 — Refund Method

**Question:** When a customer return is approved, is the refund normally given as cash back, store credit, or a product exchange?

**Why it matters:** Determines whether the returns workflow needs a "store credit" concept in addition to a straightforward cash refund and stock adjustment.

**Current status:** Needs confirmation.

---

## CR-008 — Return Time Window

**Question:** Is there a time limit within which a customer can return a product (e.g. within 7 days of purchase), or is it decided case-by-case?

**Why it matters:** Affects whether the return workflow needs a validation rule tied to invoice date.

**Current status:** Needs confirmation.

---

## CR-009 — Hardware & Device Setup

**Question:** How many computers/terminals will run PharmaKon? Is there a barcode scanner in use today, and for how many products? What type of printer is used for invoices (thermal receipt printer vs. standard A4 printer)?

**Why it matters:** Affects the billing-screen UI (scan-first vs. search-first), invoice layout/print template, and whether the single shared account will ever be used from more than one device at the same time.

**Current status:** Needs confirmation.

---

## CR-010 — Backup & Data Retention Expectations

**Question:** Does the pharmacy have any existing backup practice today (even manual, e.g. exporting the register)? Is there a legal or personal requirement to retain sales/invoice records for a minimum number of years?

**Why it matters:** Directly drives NFR-02 and the deployment checklist's backup/restore requirement; also relevant to Nepali tax record-keeping norms, which the client should confirm rather than PharmaKon assuming.

**Current status:** Needs confirmation.

---

# 13. Requirement Priority

Based on the client's stated problems, the initial priority is:

### Priority 1 — Core Operational Reliability

- Product and batch inventory
- Purchases
- Sales
- Proper invoices
- Stock deduction/increase
- Negative-stock prevention
- Returns
- Custom pricing
- Discounts
- Tax and round-off

### Priority 2 — Operational Monitoring

- Low-stock monitoring
- Expiry-risk monitoring
- Stock adjustments
- Supplier returns
- Credit ledger
- Automated backup (NFR-02)

### Priority 3 — Decision Support

- Sales trends
- Product performance
- Inventory analytics
- Purchasing analysis
- Revenue/profit indicators
- Replenishment recommendations

### Priority 4 — Advanced Data Features

- Demand forecasting
- Customer segmentation, if transaction data supports it
- Controlled AI assistant, if data and architecture support it

---

# 14. Requirement Change Policy

These requirements represent the current client-approved understanding.

If the client changes a requirement:

1. Record the change explicitly.
2. Identify affected functional requirements.
3. Identify affected business rules.
4. Identify database/API/UI implications.
5. Identify the effect on the 3-month deadline.
6. Decide whether another lower-priority feature must be postponed or removed.
7. Update the relevant project documents before implementation.

No significant feature should be added merely because it existed in the previous ERP system or because it appears technically interesting.

---

# 15. Source and Status

**Primary source:** Latest client interview / confirmed requirements record.

**Supporting reference:** Previous management-system screenshots and the PharmaKon 3-month project booklet.

**Requirement status convention:**

- **Confirmed** — Explicitly stated or confirmed by the client.
- **Conditional** — Valid only when a stated condition is satisfied.
- **Needs confirmation** — Client decision is still required.
- **Future** — Useful for later versions but not required for the current MVP.

This document should be used as the structured client-requirements baseline before creating the detailed functional requirements, user-role, business-rule, and MVP documents.