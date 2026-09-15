# 03 — Functional Requirements

## 1. Document Purpose

This document defines **what PharmaKon must do** as a functional system.

It translates the confirmed client requirements into testable system capabilities. It does not define the detailed database schema, API contracts, UI design, implementation technology, or low-level business-rule specification.

### Requirement Status

- **Confirmed** — Directly supported by the client's confirmed requirements.
- **Conditional** — Required only when the stated condition is satisfied.
- **Needs confirmation** — Client decision is still pending and must not be assumed.
- **Future** — Useful for a later version and not required for the core MVP.

---

# 2. System Functional Areas

PharmaKon shall provide functionality for:

1. Authentication and access
2. Product management
3. Batch and inventory management
4. Supplier management
5. Purchase management
6. Sales and invoicing
7. Pricing, discounts, tax and round-off
8. Customer management
9. Customer returns and refunds
10. Credit ledger
11. Damaged and expired stock
12. Stock adjustments
13. Inventory monitoring
14. Analytics and reporting
15. Purchasing/replenishment insights
16. Digital and printed invoices
17. Transaction history and traceability

Advanced ML and AI capabilities are covered as conditional/future functionality rather than being treated as mandatory core transaction functionality.

---

# 3. Authentication & Access

## FR-AUTH-001 — User Authentication

The system shall provide authentication for the initial system account.

**Status:** Confirmed

## FR-AUTH-002 — Single Initial Account

The initial system shall support one account rather than separate employee accounts.

**Status:** Confirmed

## FR-AUTH-003 — Operational Access

The authenticated account shall have the operational access required to manage stock and view analytics.

**Status:** Confirmed

## FR-AUTH-004 — Avoid Unrequired Role Complexity

The initial implementation shall not require a complex employee role/permission hierarchy.

**Status:** Confirmed

---

# 4. Product Management

## FR-PROD-001 — Create Product

The system shall allow the user to create a product.

**Status:** Confirmed

## FR-PROD-002 — Store Product Information

The system shall maintain, where applicable:

- Product name
- Product code
- Category
- Unit
- MRP
- Purchase price/cost
- Barcode
- Batch number
- Expiry date
- Stock quantity

**Status:** Confirmed

> Batch number, expiry date, and stock quantity are operationally batch/inventory information and should not be interpreted as requiring a single permanent batch field on the product itself.

## FR-PROD-003 — Edit Product

The system shall allow authorized use of the operational account to update product information.

**Status:** Confirmed

## FR-PROD-004 — Product Categories

The system shall support products across the client's stated categories:

- Medicines
- Surgical items
- Cosmetics
- Baby products
- Food products

**Status:** Confirmed

## FR-PROD-005 — Barcode Support

The system shall support barcode information where a product has a barcode.

**Status:** Confirmed

## FR-PROD-006 — Product Code

The system shall maintain a product code for product identification.

**Status:** Confirmed

---

# 5. Batch Management

## FR-BATCH-001 — Multiple Batches

The system shall allow the same product to have multiple batches.

**Status:** Confirmed

## FR-BATCH-002 — Batch Information

The system shall maintain batch-level information including:

- Batch number
- Expiry date
- Quantity
- Purchase cost

**Status:** Confirmed

## FR-BATCH-003 — FEFO Batch Selection

When selling a product with multiple available batches, the system shall use **FEFO (First Expiry, First Out)** so that the batch with the earliest expiry is selected first.

**Status:** Confirmed

## FR-BATCH-004 — Expiry-Aware Selling

The sales workflow shall account for batch expiry when selecting stock for sale.

**Status:** Confirmed

---

# 6. Inventory Management

## FR-INV-001 — Current Stock

The system shall maintain the current available quantity of products/batches.

**Status:** Confirmed

## FR-INV-002 — Prevent Negative Stock

The system shall prevent a transaction from causing available inventory to become negative.

**Status:** Confirmed

## FR-INV-003 — Purchase Stock Increase

When a purchase is recorded and accepted into stock, the system shall increase the relevant inventory quantity.

**Status:** Confirmed

## FR-INV-004 — Sale Stock Deduction

When a sale is completed, the system shall deduct the sold quantity from the relevant batch/inventory.

**Status:** Confirmed

## FR-INV-005 — Stock Adjustment

The system shall allow stock adjustment after physical stock verification.

**Status:** Confirmed

## FR-INV-006 — Adjustment Record

The system shall retain a record of stock adjustments.

**Status:** Confirmed

## FR-INV-007 — Stock Movement History

The system shall preserve stock changes resulting from operational transactions so that stock movement can be analyzed and traced.

**Status:** Confirmed

## FR-INV-008 — Periodic Physical Verification Support

The system shall support the operational process of comparing recorded stock with physically checked stock.

**Status:** Confirmed

---

# 7. Low-Stock & Expiry Monitoring

## FR-MON-001 — Configurable Reorder Level

The system shall allow a configurable reorder level for products.

**Status:** Confirmed

## FR-MON-002 — Low-Stock Visibility

The system shall identify products whose current stock is at or below the relevant reorder level.

**Status:** Confirmed

## FR-MON-003 — Low-Stock Alerts/Indicators

The system shall provide visibility or alerts for low-stock products.

**Status:** Confirmed

## FR-MON-004 — Expiry-Risk Visibility

The system shall identify inventory items that present expiry risk.

**Status:** Confirmed

## FR-MON-005 — Near-Expiry Information

The system shall provide expiry-related information that can be used to identify products/batches approaching expiry.

**Status:** Confirmed

---

# 8. Supplier Management

## FR-SUP-001 — Supplier Records

The system shall maintain supplier information required for purchasing and supplier returns.

**Status:** Confirmed

## FR-SUP-002 — Link Purchases to Supplier

The system shall associate purchase records with the relevant supplier.

**Status:** Confirmed

## FR-SUP-003 — Supplier Reference

The system shall store supplier invoice/reference information for purchases.

**Status:** Confirmed

## FR-SUP-004 — Supplier Returns

The system shall support recording damaged and expired medicines returned to suppliers.

**Status:** Confirmed

---

# 9. Purchase Management

## FR-PUR-001 — Record Purchase

The system shall allow the user to record a supplier purchase.

**Status:** Confirmed

## FR-PUR-002 — Purchase Information

A purchase record shall support:

- Supplier
- Invoice/reference
- Product
- Batch
- Expiry
- Quantity
- Purchase cost
- Payment information

**Status:** Confirmed

## FR-PUR-003 — Create Batch From Purchase

The system shall support creation/recording of batch information when purchased stock is entered.

**Status:** Confirmed

## FR-PUR-004 — Update Inventory From Purchase

The system shall update stock when purchased inventory is recorded.

**Status:** Confirmed

## FR-PUR-005 — Store Batch-Level Purchase Cost

The system shall retain purchase cost at the batch/purchase level.

**Status:** Confirmed

## FR-PUR-006 — Purchase Payment Information

The system shall record the payment information associated with a purchase.

**Status:** Confirmed

---

# 10. Sales Management

## FR-SALE-001 — Create Sale

The system shall allow the user to create a sale.

**Status:** Confirmed

## FR-SALE-002 — Multiple Products Per Sale

A single sale/invoice shall support multiple products.

**Status:** Confirmed

## FR-SALE-003 — Product Selection

The system shall allow products to be selected for a sale.

**Status:** Confirmed

## FR-SALE-004 — Product Scanning

The system shall support product/barcode scanning where barcode information is available.

**Status:** Confirmed

## FR-SALE-005 — Batch Selection

The system shall select the appropriate batch for sale according to FEFO.

**Status:** Confirmed

## FR-SALE-006 — Quantity Entry

The system shall allow the user to enter the quantity sold for each product.

**Status:** Confirmed

## FR-SALE-007 — Stock Validation Before Sale

The system shall verify sufficient available stock before completing a sale.

**Status:** Confirmed

## FR-SALE-008 — Stock Deduction

The system shall deduct the sold quantity from inventory when the sale is completed.

**Status:** Confirmed

## FR-SALE-009 — Preserve Completed Sales

The system shall preserve completed sales history.

**Status:** Confirmed

## FR-SALE-010 — Sale Cancellation/Return History

The system shall preserve the historical record of cancelled/returned transactions rather than permanently deleting the original transaction.

**Status:** Confirmed

---

# 11. Pricing, Discount, Tax & Invoice Calculation

## FR-PRICE-001 — MRP

The system shall maintain the MRP associated with a product.

**Status:** Confirmed

## FR-PRICE-002 — Custom Selling Price

The system shall allow the user to enter an actual/custom selling price for an individual sale line instead of relying only on MRP.

**Status:** Confirmed

## FR-PRICE-003 — Record Actual Selling Rate

The system shall record the actual selling rate used for every invoice line.

**Status:** Confirmed

## FR-PRICE-004 — Discount

The system shall support discounts on sales.

The client's requested default discount is 10%.

**Status:** Confirmed / behavior needs confirmation

## FR-PRICE-005 — Tax

The system shall support the client's specified 13% tax/VAT calculation.

**Status:** Confirmed / category applicability needs confirmation

## FR-PRICE-006 — Tax Applied After Base Price

The invoice calculation shall treat tax as being added after the product/base price according to the client's confirmed requirement.

**Status:** Confirmed

## FR-PRICE-007 — Invoice Calculation Breakdown

The system shall clearly calculate and display:

- Subtotal
- Discount
- Tax/VAT
- Round-off
- Grand total

**Status:** Confirmed

## FR-PRICE-008 — Round-Off

The system shall support round-off as a separate invoice adjustment.

**Status:** Confirmed

## FR-PRICE-009 — Custom Price Example

The system shall support transactions such as:

```text
Reference/product value: Rs. 67
Actual selling price:   Rs. 60
```

The invoice shall record Rs. 60 as the actual selling rate used for the sale line.

**Status:** Confirmed

---

# 12. Sales Invoices

## FR-INVCE-001 — Generate Sales Invoice

The system shall generate a proper sales invoice for a completed sale.

**Status:** Confirmed

## FR-INVCE-002 — Invoice Number

The system shall generate/maintain an invoice number.

**Status:** Confirmed

## FR-INVCE-003 — Fiscal/Year Information

The invoice shall support fiscal/year information required by the pharmacy.

**Status:** Confirmed

## FR-INVCE-004 — Reference Number

The invoice shall support a reference number where required.

**Status:** Confirmed

## FR-INVCE-005 — Voucher Date

The invoice shall record the voucher/invoice date.

**Status:** Confirmed

## FR-INVCE-006 — Buyer Information

The invoice shall support buyer/customer information.

**Status:** Confirmed

## FR-INVCE-007 — Customer Address

The invoice shall support an address field where required.

**Status:** Confirmed from previous system information

## FR-INVCE-008 — Customer Phone

The invoice shall support the customer's phone number.

**Status:** Confirmed

## FR-INVCE-009 — PAN/VAT Information

The invoice shall support PAN/VAT number where applicable.

**Status:** Confirmed from previous system information

## FR-INVCE-010 — Line-Item Information

The invoice shall support the relevant line-item information, including:

- Product
- Closing stock
- Batch number
- Expiry date
- Actual quantity
- Unit
- Alternate quantity/unit where required
- Rate
- Amount

**Status:** Confirmed from previous system information

## FR-INVCE-011 — Printable Invoice

The system shall provide a printable invoice.

**Status:** Confirmed

## FR-INVCE-012 — Digital Invoice

The system shall support generating a digital invoice that can be provided to a customer.

**Status:** Confirmed

## FR-INVCE-013 — WhatsApp/Phone Delivery

The system shall support sending the invoice to the customer's phone/WhatsApp number when requested.

The exact automated WhatsApp delivery mechanism/API remains unconfirmed.

**Status:** Needs confirmation

---

# 13. Payments

## FR-PAY-001 — Record Payment Method

The system shall record the payment method used for a sale.

**Status:** Confirmed

## FR-PAY-002 — Cash Payment

The system shall support cash payments.

**Status:** Confirmed

## FR-PAY-003 — eSewa/Banking Payment

The system shall support eSewa/banking-system payments.

**Status:** Confirmed

## FR-PAY-004 — Purchase Payment Information

The system shall retain payment information associated with purchases.

**Status:** Confirmed

---

# 14. Customer Management

## FR-CUST-001 — Create Customer

The system shall allow the user to create a customer record.

**Status:** Confirmed

## FR-CUST-002 — Customer Name

The customer record shall support the customer's name.

**Status:** Confirmed

## FR-CUST-003 — Customer Phone

The customer record shall support the customer's phone number.

**Status:** Confirmed

## FR-CUST-004 — Customer History

The system may support richer customer history in a future version.

A detailed customer history is not required for the core MVP.

**Status:** Future

---

# 15. Customer Returns & Refunds

## FR-RET-001 — Initiate Customer Return

The system shall allow a customer return to be recorded.

**Status:** Confirmed

## FR-RET-002 — Require Original Bill

The return workflow shall require the customer to provide the original bill/invoice.

**Status:** Confirmed

## FR-RET-003 — Verify Original Invoice

The system shall allow the user to verify the original invoice before processing the return.

**Status:** Confirmed

## FR-RET-004 — Record Returned Item

The system shall record the returned product and quantity.

**Status:** Confirmed

## FR-RET-005 — Process Refund

The system shall support recording/processing the refund associated with a valid return.

**Status:** Confirmed

## FR-RET-006 — Adjust Stock After Return

The system shall adjust inventory according to the condition of the returned item.

**Status:** Confirmed

## FR-RET-007 — Preserve Return History

The system shall preserve the return/cancellation history instead of deleting the original sale.

**Status:** Confirmed

---

# 16. Credit Ledger

## FR-CREDIT-001 — Mark Sale as Credit

The system shall allow a sale to be marked as a credit transaction.

**Status:** Confirmed

## FR-CREDIT-002 — Associate Credit With Customer

The system shall associate a credit sale with a customer.

**Status:** Confirmed

## FR-CREDIT-003 — Record Outstanding Amount

The system shall record the outstanding amount generated by a credit sale.

**Status:** Confirmed

## FR-CREDIT-004 — Record Later Payment

The system shall allow the user to record a later payment against an outstanding credit balance.

**Status:** Confirmed

## FR-CREDIT-005 — Update Outstanding Balance

The system shall update the remaining outstanding balance after a credit payment is recorded.

**Status:** Confirmed

## FR-CREDIT-006 — Replace Manual Credit Register

The digital credit ledger shall provide the core functionality currently handled through the manual register copy.

**Status:** Confirmed

## FR-CREDIT-007 — Due Date

The system's credit workflow may include a due date.

Whether a due date is required has not yet been confirmed.

**Status:** Needs confirmation

---

# 17. Damaged & Expired Stock

## FR-DMG-001 — Identify Non-Saleable Stock

The system shall allow damaged or expired stock to be identified as non-saleable.

**Status:** Confirmed

## FR-DMG-002 — Supplier Return Record

The system shall allow damaged/expired medicines returned to suppliers to be recorded.

**Status:** Confirmed

## FR-DMG-003 — Reduce/Adjust Stock

The system shall reduce or adjust available stock when damaged/expired items are removed for supplier return.

**Status:** Confirmed

## FR-DMG-004 — Preserve Supplier Return History

The system shall retain a record of damaged/expired stock returned to suppliers.

**Status:** Confirmed

---

# 18. Analytics & Reporting

## FR-AN-001 — Sales Trends

The system shall provide sales-trend information across relevant periods.

**Status:** Confirmed

## FR-AN-002 — Fast-Moving Products

The system shall identify fast-moving products.

**Status:** Confirmed

## FR-AN-003 — Slow-Moving Products

The system shall identify slow-moving products.

**Status:** Confirmed

## FR-AN-004 — Stock-Level Analytics

The system shall provide information about current stock levels.

**Status:** Confirmed

## FR-AN-005 — Low-Stock Analytics

The system shall provide analytics/visibility for low-stock products.

**Status:** Confirmed

## FR-AN-006 — Expiry-Risk Analytics

The system shall provide information about products/batches at expiry risk.

**Status:** Confirmed

## FR-AN-007 — Purchase Pattern Analysis

The system shall provide information about purchase patterns.

**Status:** Confirmed

## FR-AN-008 — Revenue Indicators

The system shall provide revenue indicators.

**Status:** Confirmed

## FR-AN-009 — Profit Indicators

The system shall provide profit indicators using available purchase-cost and sales information.

**Status:** Confirmed

## FR-AN-010 — Product Performance

The system shall provide information about medicine/product performance.

**Status:** Confirmed

## FR-AN-011 — Purchasing Decision Support

The system shall provide information that helps the owner decide which products should be replenished.

**Status:** Confirmed

---

# 19. Purchasing / Replenishment Insights

## FR-REPL-001 — Identify Replenishment Candidates

The system shall identify products that may require replenishment using sales movement and current stock.

**Status:** Confirmed

## FR-REPL-002 — Approximate Replenishment Quantity

The system shall provide an approximate replenishment quantity where the available data supports a defensible recommendation.

**Status:** Confirmed

## FR-REPL-003 — Use Current Stock

Replenishment recommendations shall consider current stock.

**Status:** Confirmed

## FR-REPL-004 — Use Sales Movement

Replenishment recommendations shall consider sales movement/history.

**Status:** Confirmed

## FR-REPL-005 — Owner Decision Support

Recommendations shall support the owner's purchasing decision rather than automatically replacing the owner's decision.

**Status:** Confirmed

---

# 20. Demand Forecasting

## FR-ML-001 — Historical Sales Dataset

The system may use historical sales data to prepare a dataset for demand forecasting.

**Status:** Conditional

## FR-ML-002 — Demand Forecast

The system may provide demand forecasts when sufficient historical sales data exists.

**Status:** Conditional

## FR-ML-003 — Forecast as Decision Support

Demand forecasts shall support the owner's purchasing decision and shall not replace it.

**Status:** Confirmed

## FR-ML-004 — Do Not Force ML

The system shall not depend on an ML model when insufficient data exists to produce a defensible forecast.

**Status:** Confirmed

---

# 21. Customer Segmentation

## FR-ML-005 — Customer Transaction Features

If sufficient customer transaction data is available, the system may derive customer transaction features.

**Status:** Conditional

## FR-ML-006 — Customer Segmentation

Customer segmentation may be introduced using transaction data if it is supported by the available data and project scope.

**Status:** Future / Conditional

Customer segmentation is not a mandatory core transaction requirement.

---

# 22. AI Assistant

## FR-AI-001 — Controlled Analytics Questions

If the AI assistant is included, it shall support a limited set of useful pharmacy analytics questions.

**Status:** Conditional

## FR-AI-002 — Real Pharmacy Data

AI-generated answers shall be grounded in actual pharmacy data retrieved through controlled system functions.

**Status:** Conditional

## FR-AI-003 — No Invented Business Numbers

The AI assistant shall not manufacture pharmacy sales, stock, revenue, or other business figures.

**Status:** Conditional

## FR-AI-004 — Example Supported Questions

Potential supported questions include:

- What were the top-selling medicines last month?
- Which products are low in stock?
- Which medicines have the highest expiry risk?
- What does the demand forecast suggest?

**Status:** Conditional

---

# 23. Transaction History & Traceability

## FR-HIST-001 — Preserve Historical Transactions

The system shall preserve historical sales and related transaction records.

**Status:** Confirmed

## FR-HIST-002 — Preserve Return/Cancellation History

Returns and cancellations shall not erase the original transaction history.

**Status:** Confirmed

## FR-HIST-003 — Preserve Stock Adjustment History

Stock adjustments shall retain an adjustment record.

**Status:** Confirmed

## FR-HIST-004 — Preserve Supplier Return History

Damaged/expired supplier returns shall remain historically traceable.

**Status:** Confirmed

## FR-HIST-005 — Historical Product Reference

Historical transactions should remain usable even if a product is later no longer active.

**Status:** Requirement direction supported by project business-rule examples; formal business rule to be finalized separately.

---

# 24. Dashboard / Operational Visibility

## FR-DASH-001 — Operational Overview

The system shall provide an overview of important operational information.

**Status:** Confirmed at analytics/monitoring level

The dashboard should be designed around the client's actual decisions rather than reproducing the previous ERP dashboard.

Relevant information includes:

- Sales trends
- Stock levels
- Low-stock products
- Expiry-risk products
- Fast-moving products
- Slow-moving products
- Purchasing information
- Revenue/profit indicators
- Replenishment insights

---

# 25. Previous-System Information Compatibility

The previous management system contained broad ERP functionality across accounting, inventory, purchasing, sales, reporting, product/customer/vendor masters, stock reporting, near-expiry information, product ageing, sales analysis, purchase analysis, stock demand and related functions.

PharmaKon shall preserve **necessary business information** from the previous system where it supports the confirmed requirements.

It shall not automatically implement every previous-system module.

## FR-LEGACY-001 — Preserve Required Invoice Information

The system shall retain the required invoice information from the previous workflow, including:

- Invoice number
- Fiscal/year information
- Reference number
- Voucher date
- Buyer
- Address
- Phone
- PAN/VAT number where applicable

**Status:** Confirmed

## FR-LEGACY-002 — Preserve Required Line Information

The system shall retain necessary invoice line information including:

- Product
- Closing stock
- Batch number
- Expiry date
- Actual quantity
- Unit
- Alternate quantity/unit where required
- Rate
- Amount

**Status:** Confirmed

## FR-LEGACY-003 — Preserve Invoice Calculations

The system shall retain support for:

- Discount
- VAT/tax
- Round-off
- Grand total

**Status:** Confirmed

---

# 26. Functional Requirements Excluded From Automatic Inheritance

The following principle applies to the previous ERP screenshots:

> A feature existing in the previous system is not, by itself, evidence that PharmaKon must implement it.

Examples of legacy areas that require separate scope decisions include:

- General accounting modules
- Salesman management/targets
- Customer targets
- Area management
- Currency management
- Security deposits
- Bank guarantees
- LC details
- Cheque management
- Production orders
- Extensive ERP reporting
- Other enterprise features not directly required by the client

These should only be added if later requirements explicitly justify them.

---

# 27. Cross-Functional Requirements

## FR-CROSS-001 — Consistent Inventory Updates

Purchase, sale, return, supplier-return, and stock-adjustment workflows shall update inventory consistently.

**Status:** Confirmed

## FR-CROSS-002 — Consistent Historical Records

Operational corrections shall preserve sufficient transaction history for later review.

**Status:** Confirmed

## FR-CROSS-003 — Analytics From Operational Data

Analytics shall use the system's sales, purchase, and inventory history rather than manually entered summary values.

**Status:** Confirmed

## FR-CROSS-004 — Purchase Cost Availability

Purchase cost shall remain available at the batch/purchase level so that profit-related analytics can use the appropriate cost information.

**Status:** Confirmed

---

# 28. End-to-End Functional Flows

## 28.1 Purchase Flow

**Given** a supplier purchase is being recorded  
**When** the user enters the supplier, invoice/reference, product, batch, expiry, quantity, purchase cost and payment information  
**Then** the system shall record the purchase and increase the corresponding inventory.

---

## 28.2 Sale Flow

**Given** a product has available stock  
**When** the user selects/scans the product and enters a quantity  
**Then** the system shall select the appropriate batch according to FEFO, validate available stock, calculate the invoice, record the sale, and deduct stock.

---

## 28.3 Custom Price Flow

**Given** a product has an MRP/base value of Rs. 67  
**When** the user enters Rs. 60 as the actual selling price  
**Then** the invoice shall record Rs. 60 as the actual selling rate for that line and calculate the transaction using the configured pricing rules.

---

## 28.4 Return Flow

**Given** a customer has the original invoice  
**When** the user verifies the invoice and records the returned item and quantity  
**Then** the system shall record the return, process the refund, adjust stock according to the return condition, and preserve the original transaction history.

---

## 28.5 Credit Flow

**Given** a customer purchases on credit  
**When** the user records the sale as credit  
**Then** the system shall associate the sale with the customer and create/update the outstanding balance.

**When** the customer later pays  
**Then** the system shall record the payment and update the outstanding balance.

---

## 28.6 Supplier Return Flow

**Given** stock is identified as damaged or expired  
**When** it is returned to the supplier  
**Then** the system shall record the supplier return, mark the relevant stock as non-saleable/remove it from available stock, and preserve the history.

---

## 28.7 Replenishment Insight Flow

**Given** sufficient sales and stock history exists  
**When** the system analyzes product movement and current stock  
**Then** it shall identify potential replenishment candidates and provide approximate quantities where the data supports the recommendation.

---

# 29. Requirements Requiring Confirmation Before Final Implementation

The following functional behavior cannot be finalized until the client confirms the underlying requirement:

### FR-CONF-001 — Automated WhatsApp Delivery

Determine the exact WhatsApp/API/account mechanism for automated invoice delivery.

### FR-CONF-002 — Automatic vs Selectable 10% Discount

Determine whether 10% is automatically applied or merely the default selectable discount.

### FR-CONF-003 — Tax Treatment by Category

Determine whether 13% tax applies uniformly to medicines, surgical items, cosmetics, baby products, and food products or whether category-specific treatment is required.

### FR-CONF-004 — Credit Due Dates

Determine whether credit records require a due date or only an outstanding balance.

---

# 30. Out of Scope for This Document

This document intentionally does not finalize:

- Database tables and relationships
- Database indexes
- API endpoint contracts
- Frontend screen designs
- Detailed UI component behavior
- Detailed authorization matrix
- Formal accounting rules beyond confirmed billing/payment requirements
- Detailed tax-law interpretation
- ML model selection and evaluation methodology
- AI tool/function architecture
- Deployment architecture

These will be defined in later project documents.

---

# 31. Functional Requirement Baseline

The core functional baseline for PharmaKon is:

```text
Authentication
      ↓
Product Management
      ↓
Batch + Inventory
      ↓
Purchasing ───────────────┐
      ↓                   │
Stock Monitoring          │
      ↓                   │
Sales → Invoice → Payment │
      ↓                   │
Stock Deduction           │
      ↓                   │
Returns / Credits         │
      ↓                   │
Transaction History       │
      ↓                   │
Analytics ←───────────────┘
      ↓
Purchasing / Replenishment Insights
      ↓
Conditional ML / AI
```

The core system must first provide reliable pharmacy operations. Analytics and advanced ML/AI functionality depend on the quality and availability of the underlying operational data.

---

# 32. Source of Truth

This document is derived from:

1. The client's latest confirmed requirements record.
2. The observed previous management-system screenshots.
3. The project booklet's documented project direction and development sequence.

Where the sources identify a requirement as unresolved, this document preserves that uncertainty rather than inventing a system behavior.

The client's later confirmed decisions supersede unresolved or earlier requirements and must be reflected in this document before implementation.
