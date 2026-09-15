# 05 — Business Rules

## 1. Document Purpose

This document defines the **business rules that must always hold** in PharmaKon.

A business rule is a constraint on pharmacy operations that the system must enforce consistently, regardless of which screen, API endpoint, or workflow triggers the operation.

The rules below are derived from the client's confirmed requirements. Where the client has not yet made a decision, the rule is explicitly marked **Needs confirmation** rather than being invented.

---

# 2. Rule Status

- **Confirmed** — Explicitly supported by the client's confirmed requirements.
- **Needs confirmation** — The underlying client requirement is unresolved.
- **Derived / To formalize** — A logical system invariant indicated by the confirmed workflow, but requiring formalization during detailed design.

---

# 3. Inventory Rules

## BR-INV-001 — Negative Stock Is Forbidden

**Rule:** Inventory quantity must never become negative.

**Status:** Confirmed

The system must reject an operation if completing it would cause available stock to fall below zero.

**Related requirements:** `FR-INV-002`, `FR-SALE-007`

---

## BR-INV-002 — Stock Must Reflect Completed Inventory Movements

**Rule:** Purchases, sales, returns, supplier returns, and approved stock adjustments must produce the corresponding inventory movement.

**Status:** Confirmed

The inventory quantity must remain consistent with the operational transactions recorded by the system.

**Related requirements:** `FR-INV-003`, `FR-INV-004`, `FR-INV-005`, `FR-INV-007`

---

## BR-INV-003 — Stock Adjustments Must Be Recorded

**Rule:** A stock adjustment performed after physical verification must retain an adjustment record.

**Status:** Confirmed

An adjustment must not silently overwrite the previous stock quantity without retaining the adjustment history.

**Related requirement:** `FR-INV-006`

---

## BR-INV-004 — Physical Verification Can Trigger Adjustment

**Rule:** When physical stock verification identifies a difference between recorded and actual stock, the system must support an adjustment process.

**Status:** Confirmed

The adjustment must remain traceable.

---

# 4. Batch Rules

## BR-BATCH-001 — A Product May Have Multiple Batches

**Rule:** The same product may have more than one inventory batch.

**Status:** Confirmed

Batch-level information must therefore be maintained independently enough to distinguish different batches of the same product.

**Related requirement:** `FR-BATCH-001`

---

## BR-BATCH-002 — Batch Information Must Be Retained

**Rule:** Batch number, expiry date, quantity, and purchase cost must be retained at the batch/purchase level.

**Status:** Confirmed

This information is required for inventory operation and accurate profit analysis.

**Related requirements:** `FR-BATCH-002`, `FR-PUR-005`

---

## BR-BATCH-003 — FEFO Must Be Used for Sales

**Rule:** When a product has multiple available batches, the batch with the earliest expiry must be sold first.

**Status:** Confirmed

This is the client's confirmed **FEFO (First Expiry, First Out)** requirement.

**Related requirement:** `FR-BATCH-003`

---

# 5. Expiry Rules

## BR-EXP-001 — Expiry Must Be Considered During Batch Selection

**Rule:** The sales workflow must consider batch expiry when selecting inventory for sale.

**Status:** Confirmed

**Related requirement:** `FR-BATCH-004`

---

## BR-EXP-002 — Expiry Risk Must Be Visible

**Rule:** The system must provide visibility into products/batches that present expiry risk.

**Status:** Confirmed

This rule supports the client's requirement for expiry-risk information and purchasing/stock decisions.

**Related requirement:** `FR-MON-004`

---

## BR-EXP-003 — Expired-Sale Restriction

**Rule:** Expired medicine batches should not be sold.

**Status:** Derived / To formalize

The project booklet lists “Expired medicine batches cannot be sold” as an example business rule to confirm, while the client requirements explicitly require expiry tracking and expiry-risk monitoring. Therefore this rule is **not treated as client-confirmed yet**.

It must be formally confirmed before being marked as a hard business rule.

---

# 6. Low-Stock Rules

## BR-STOCK-001 — Reorder Level Must Be Configurable

**Rule:** Low-stock evaluation must use a configurable reorder level.

**Status:** Confirmed

**Related requirement:** `FR-MON-001`

---

## BR-STOCK-002 — Low Stock Must Be Identifiable

**Rule:** The system must identify products whose stock reaches the relevant low-stock/reorder condition.

**Status:** Confirmed

**Related requirements:** `FR-MON-002`, `FR-MON-003`

---

# 7. Purchase Rules

## BR-PUR-001 — Purchases Must Identify the Supplier

**Rule:** A purchase must be associated with the relevant supplier.

**Status:** Confirmed

**Related requirement:** `FR-PUR-002`

---

## BR-PUR-002 — Purchased Stock Must Carry Batch Information

**Rule:** Purchased stock must support recording the relevant batch, expiry, quantity, and purchase cost.

**Status:** Confirmed

**Related requirements:** `FR-PUR-002`, `FR-PUR-003`, `FR-PUR-005`

---

## BR-PUR-003 — Purchase Cost Must Be Preserved

**Rule:** Purchase cost must be stored at batch/purchase level.

**Status:** Confirmed

This is required to support accurate profit analysis.

**Related requirement:** `FR-PUR-005`

---

## BR-PUR-004 — Purchase Recording Updates Stock

**Rule:** When purchased stock is recorded into inventory, the relevant stock quantity must increase.

**Status:** Confirmed

**Related requirement:** `FR-PUR-004`

---

# 8. Sales Rules

## BR-SALE-001 — A Sale Must Use Available Stock

**Rule:** A sale must not result in negative inventory.

**Status:** Confirmed

The system must validate available stock before completing the sale.

**Related requirements:** `FR-INV-002`, `FR-SALE-007`

---

## BR-SALE-002 — FEFO Applies to Batch Selection

**Rule:** When multiple batches are available for the product being sold, the earliest-expiring applicable batch must be selected first.

**Status:** Confirmed

**Related requirement:** `FR-SALE-005`

---

## BR-SALE-003 — Actual Selling Price Must Be Recorded

**Rule:** The actual selling rate used for each invoice line must be recorded.

**Status:** Confirmed

The system must not rely only on the product's MRP when determining the historical selling rate.

**Related requirements:** `FR-PRICE-002`, `FR-PRICE-003`

---

## BR-SALE-004 — Custom Selling Prices Are Allowed

**Rule:** The user may sell a product at a custom selling price instead of its MRP.

**Status:** Confirmed

Example:

```text
Product value / MRP: Rs. 67
Actual selling price: Rs. 60
```

The invoice must preserve the actual rate used.

**Related requirement:** `FR-PRICE-009`

---

## BR-SALE-005 — Multiple Products May Be Included in One Sale

**Rule:** A sales invoice may contain multiple product lines.

**Status:** Confirmed

**Related requirement:** `FR-SALE-002`

---

## BR-SALE-006 — Completed Sales Must Affect Inventory

**Rule:** Completing a sale must deduct the sold quantity from the relevant inventory.

**Status:** Confirmed

**Related requirement:** `FR-SALE-008`

---

# 9. Pricing, Discount & Tax Rules

## BR-PRICE-001 — Tax Is Added After the Base Price

**Rule:** Tax/VAT is calculated after the product/base price according to the client's specified billing method.

**Status:** Confirmed

**Related requirement:** `FR-PRICE-006`

---

## BR-PRICE-002 — 13% Tax/VAT

**Rule:** The client's current specified tax/VAT rate is 13%.

**Status:** Confirmed, with applicability pending confirmation

The client stated that 13% tax/VAT is applied to each product. However, whether the same treatment legally applies to every category has not yet been confirmed.

Therefore, the **rate is recorded as confirmed**, while the **uniform category applicability remains unresolved**.

**Related requirement:** `FR-PRICE-005`

---

## BR-PRICE-003 — Tax Breakdown Must Be Visible

**Rule:** The invoice must clearly show the relevant subtotal, tax, and final total.

**Status:** Confirmed

**Related requirement:** `FR-PRICE-007`

---

## BR-PRICE-004 — Discount Must Be Supported

**Rule:** The system must support discounts on sales.

**Status:** Confirmed

The client requested a default discount of 10%.

**Related requirement:** `FR-PRICE-004`

---

## BR-PRICE-005 — Default 10% Discount Behavior Is Not Yet Fixed

**Rule:** The system must not assume whether the 10% discount is automatically applied or merely presented as the default selectable value until the client confirms the intended behavior.

**Status:** Needs confirmation

This distinction affects invoice calculation and user interaction.

---

## BR-PRICE-006 — No Maximum Discount Limit Is Currently Required

**Rule:** There is currently no client-confirmed maximum discount limit.

**Status:** Confirmed

The system should not invent a maximum discount restriction without a new client requirement.

---

## BR-PRICE-007 — Round-Off Is a Separate Invoice Adjustment

**Rule:** Any round-off applied to an invoice must be represented as a separate invoice adjustment.

**Status:** Confirmed

**Related requirement:** `FR-PRICE-008`

---

# 10. Invoice Rules

## BR-INVOICE-001 — Proper Invoice Must Be Generated for Sales

**Rule:** PharmaKon must generate a proper sales invoice for a completed sale.

**Status:** Confirmed

This directly addresses one of the client's three major problems.

**Related requirement:** `FR-INVCE-001`

---

## BR-INVOICE-002 — Invoice Must Preserve the Actual Selling Rate

**Rule:** The invoice must record the actual selling rate used for each line.

**Status:** Confirmed

**Related requirement:** `FR-INVCE-010`

---

## BR-INVOICE-003 — Invoice Must Show Required Calculation Components

**Rule:** The invoice calculation must account for discount, tax/VAT, round-off, and grand total.

**Status:** Confirmed

**Related requirement:** `FR-INVCE-003`

---

## BR-INVOICE-004 — Printed Invoice Must Be Supported

**Rule:** The system must support printing an invoice.

**Status:** Confirmed

The client has a printer.

---

## BR-INVOICE-005 — Digital Invoice Must Be Supported

**Rule:** When requested by the customer, the system must support providing a digital invoice.

**Status:** Confirmed

---

## BR-INVOICE-006 — Automated WhatsApp Delivery Mechanism Is Unresolved

**Rule:** The exact automated WhatsApp/API delivery mechanism must not be assumed until confirmed by the client.

**Status:** Needs confirmation

---

# 11. Payment Rules

## BR-PAY-001 — Sale Must Record Payment Information

**Rule:** The payment information associated with a sale must be recorded.

**Status:** Confirmed

---

## BR-PAY-002 — Cash Must Be Supported

**Rule:** Cash must be supported as a sale payment method.

**Status:** Confirmed

---

## BR-PAY-003 — eSewa/Banking Payments Must Be Supported

**Rule:** eSewa/banking-system payments must be supported as sale payment methods.

**Status:** Confirmed

---

# 12. Customer Rules

## BR-CUST-001 — Customer Name and Phone Are Sufficient for MVP

**Rule:** The initial customer record must support at least the customer's name and phone number.

**Status:** Confirmed

---

## BR-CUST-002 — Detailed Customer History Is Not Required for Core MVP

**Rule:** A more extensive customer-history feature must not be treated as a core MVP requirement.

**Status:** Confirmed

It may be considered for future implementation.

---

# 13. Customer Return & Refund Rules

## BR-RETURN-001 — Original Bill Is Required for a Return

**Rule:** A customer must provide the original bill/invoice to receive a refund.

**Status:** Confirmed

**Related requirement:** `FR-RET-002`

---

## BR-RETURN-002 — Return Must Reference the Original Invoice

**Rule:** A valid customer return must be associated with the original sale/invoice being returned.

**Status:** Confirmed

**Related requirement:** `FR-RET-003`

---

## BR-RETURN-003 — Returned Quantity Must Be Recorded

**Rule:** The returned product and quantity must be recorded.

**Status:** Confirmed

**Related requirement:** `FR-RET-004`

---

## BR-RETURN-004 — Refund Must Be Recorded

**Rule:** A valid customer return must include the corresponding refund process/record.

**Status:** Confirmed

**Related requirement:** `FR-RET-005`

---

## BR-RETURN-005 — Returned Stock Must Be Handled According to Condition

**Rule:** Inventory must be adjusted according to the condition of the returned item.

**Status:** Confirmed

The confirmed requirement does not specify the exact stock disposition rules for every possible return condition; those detailed rules must be defined separately.

**Related requirement:** `FR-RET-006`

---

## BR-RETURN-006 — Original Sale Must Not Be Deleted

**Rule:** Processing a return/cancellation must preserve the historical sale rather than permanently deleting it.

**Status:** Confirmed

**Related requirement:** `FR-RET-007`

---

# 14. Credit Rules

## BR-CREDIT-001 — Credit Sale Must Be Identified as Credit

**Rule:** A credit transaction must be explicitly recorded as a credit sale.

**Status:** Confirmed

---

## BR-CREDIT-002 — Credit Must Be Associated With a Customer

**Rule:** A credit sale must be associated with the relevant customer.

**Status:** Confirmed

---

## BR-CREDIT-003 — Outstanding Amount Must Be Recorded

**Rule:** A credit sale must create/record the corresponding outstanding amount.

**Status:** Confirmed

---

## BR-CREDIT-004 — Later Payment Must Reduce Outstanding Balance

**Rule:** A later payment against a credit transaction must update the outstanding balance.

**Status:** Confirmed

---

## BR-CREDIT-005 — Credit Due Date Is Unresolved

**Rule:** The system must not require or enforce a credit due date until the client confirms whether due dates are needed.

**Status:** Needs confirmation

The currently confirmed requirement is an outstanding balance; the requirement for a due date remains unresolved.

---

# 15. Damaged & Expired Stock Rules

## BR-DMG-001 — Damaged/Expired Stock Must Be Identifiable

**Rule:** Damaged and expired medicines must be identifiable for supplier-return handling.

**Status:** Confirmed

---

## BR-DMG-002 — Damaged/Expired Stock Is Returned to Suppliers

**Rule:** Damaged and expired medicines are sent back to suppliers.

**Status:** Confirmed

---

## BR-DMG-003 — Returned Non-Saleable Stock Must Not Remain Available as Normal Stock

**Rule:** Stock identified for damaged/expired supplier return must be removed from normal available stock through the appropriate adjustment/return process.

**Status:** Confirmed

---

## BR-DMG-004 — Supplier Return History Must Be Retained

**Rule:** Supplier returns for damaged/expired stock must retain a historical record.

**Status:** Confirmed

---

# 16. Transaction History Rules

## BR-HIST-001 — Historical Sales Must Be Preserved

**Rule:** Completed sales must remain historically available.

**Status:** Confirmed

---

## BR-HIST-002 — Returns Must Preserve History

**Rule:** A return must not permanently erase the original sale.

**Status:** Confirmed

---

## BR-HIST-003 — Stock Adjustments Must Preserve History

**Rule:** Stock adjustments must retain an adjustment record.

**Status:** Confirmed

---

## BR-HIST-004 — Supplier Returns Must Preserve History

**Rule:** Damaged/expired supplier returns must retain their records.

**Status:** Confirmed

---

## BR-HIST-005 — Stock Changes Must Be Traceable

**Rule:** Stock changes must be traceable to the corresponding approved operational event.

**Status:** Derived / To formalize

The project booklet explicitly identifies traceability of stock changes to purchases, sales, returns, adjustments, or other approved events as a business-rule example to confirm. The client has separately confirmed the underlying purchase, sale, return, supplier-return, and adjustment workflows.

The exact audit/traceability model must be formalized during detailed design.

---

# 17. Analytics Rules

## BR-AN-001 — Analytics Must Use Operational Data

**Rule:** Analytics must be based on the pharmacy's sales, purchase, and inventory information.

**Status:** Confirmed

---

## BR-AN-002 — Analytics Must Support Purchasing Decisions

**Rule:** Analytics should provide information that helps the owner make purchasing decisions.

**Status:** Confirmed

---

## BR-AN-003 — Replenishment Must Consider Sales and Stock

**Rule:** Purchasing/replenishment insights must consider sales movement and current stock.

**Status:** Confirmed

---

## BR-AN-004 — Replenishment Recommendations Are Decision Support

**Rule:** System recommendations must support the owner's purchasing decision rather than automatically replacing it.

**Status:** Confirmed

---

# 18. Machine Learning Rules

## BR-ML-001 — ML Requires Sufficient Historical Data

**Rule:** Demand forecasting should only be introduced when sufficient historical sales data is available.

**Status:** Confirmed

---

## BR-ML-002 — Forecasting Must Support, Not Replace, the Owner

**Rule:** A demand forecast must support the owner's purchasing decision.

**Status:** Confirmed

---

## BR-ML-003 — Do Not Force an ML Model

**Rule:** PharmaKon must not depend on an ML model when insufficient data exists to produce a defensible result.

**Status:** Confirmed

---

# 19. AI Assistant Rules

## BR-AI-001 — AI Must Use Controlled Data Access

**Rule:** If an AI assistant is implemented, it must obtain pharmacy information through controlled tools/functions.

**Status:** Conditional

---

## BR-AI-002 — AI Must Not Invent Business Numbers

**Rule:** AI-generated answers must not manufacture sales, stock, revenue, profit, or other pharmacy figures.

**Status:** Conditional

---

## BR-AI-003 — AI Explains Retrieved Results

**Rule:** The AI should explain results obtained from deterministic system functions rather than independently generating unsupported business figures.

**Status:** Conditional

---

# 20. Data Integrity Rules

## BR-DATA-001 — Product and Batch Relationship Must Remain Valid

**Rule:** Inventory batch information must correspond to an actual product.

**Status:** Derived / To formalize

The project booklet identifies “Every inventory batch belongs to a medicine” as a business-rule example to confirm. The client has confirmed that products can have multiple batches.

---

## BR-DATA-002 — Completed Sale Must Contain Sale Items

**Rule:** A completed sale should contain at least one sale item.

**Status:** Derived / To formalize

The project booklet lists this as an example business rule to confirm. The client has confirmed that invoices can contain multiple products, but has not explicitly confirmed the minimum-line rule.

---

# 21. Pricing Data Integrity

## BR-DATA-003 — Historical Selling Rate Must Not Be Reconstructed From Current MRP

**Rule:** Historical invoice analysis must use the actual selling rate recorded on the sale line.

**Status:** Derived from confirmed requirement

Because the client requires custom selling prices and explicit recording of the actual selling rate, historical sales must retain the rate actually used rather than depending on a later product price/MRP.

---

## BR-DATA-004 — Purchase Cost Must Remain Available for Historical Profit Analysis

**Rule:** Historical profit analysis must use the purchase cost stored at the batch/purchase level rather than assuming the current product purchase price.

**Status:** Confirmed

The client explicitly requires purchase cost to be stored at batch/purchase level for accurate profit analysis.

---

# 22. Single-Account Access Rule

## BR-ACCESS-001 — Initial System Uses One Account

**Rule:** The initial system must operate using one account rather than separate employee accounts.

**Status:** Confirmed

---

## BR-ACCESS-002 — Do Not Invent Separate Employee Permissions

**Rule:** The system must not introduce separate staff/owner permission restrictions unless the client changes the access requirement.

**Status:** Confirmed

---

# 23. Legacy-System Rules

## BR-LEGACY-001 — Legacy Features Are Not Automatically Requirements

**Rule:** A feature that existed in the previous management system must not automatically be implemented in PharmaKon.

**Status:** Confirmed project-scope principle

Each legacy feature must be evaluated against the confirmed client requirements and MVP scope.

---

## BR-LEGACY-002 — Necessary Business Information Should Be Preserved

**Rule:** Necessary business information from the previous system should be retained where it supports the confirmed pharmacy workflows.

**Status:** Confirmed

The client specifically wants necessary information retained while simplifying the interface and automating calculations and stock updates.

---

# 24. Rules Requiring Client Confirmation

The following rules cannot be finalized until the corresponding client decisions are obtained.

| Rule | Decision Required | Status |
|---|---|---|
| `BR-EXP-003` | Whether expired medicine batches must be strictly blocked from sale | Needs confirmation |
| `BR-PRICE-005` | Whether 10% discount is automatic or merely the default selectable value | Needs confirmation |
| `BR-PRICE-002` | Whether 13% tax applies uniformly to every product category | Needs confirmation |
| `BR-CREDIT-005` | Whether credit transactions require a due date | Needs confirmation |
| `BR-INVOICE-006` | Exact automated WhatsApp delivery/API mechanism | Needs confirmation |
| `BR-RETURN-005` | Exact inventory disposition rules for every return condition | Needs detailed definition |
| `BR-HIST-005` | Exact audit/traceability model for stock movements | Needs detailed definition |
| `BR-DATA-001` | Formal database/business invariant for batch → product ownership | Needs detailed formalization |
| `BR-DATA-002` | Formal minimum sale-line rule | Needs detailed formalization |

---

# 25. Rule Enforcement Principle

Business rules must be enforced in the **backend/domain/service layer**, not only in the frontend.

For example:

```text
Frontend
   ↓
FastAPI
   ↓
Business / Service Layer
   ↓
Rule Validation
   ↓
Database Transaction
```

A UI validation message alone is not sufficient for a rule such as negative-stock prevention.

The same business rule must remain true regardless of whether an operation originates from a future UI, API client, automated process, or another supported interface.

---

# 26. Critical Invariants

The following invariants are especially important to the reliability of PharmaKon:

```text
Inventory quantity >= 0
```

```text
Sale → inventory decreases
Purchase → inventory increases
```

```text
Multiple batches → FEFO selection
```

```text
Actual selling rate → preserved on sale line
```

```text
Purchase cost → preserved at batch/purchase level
```

```text
Return → original sale remains historically available
```

```text
Stock adjustment → adjustment history retained
```

```text
Supplier return → return history retained
```

```text
Credit payment → outstanding balance updated
```

```text
Analytics → derived from operational data
```

These invariants should become explicit acceptance criteria and automated tests during implementation.

---

# 27. Source of Truth

This document is based on the client's confirmed requirements record and the project's development booklet.

The project booklet contains several **examples of business rules to confirm**. Those examples have deliberately not been presented here as client-confirmed facts unless the client's requirements independently support them.

The following principles therefore apply:

1. **Client-confirmed requirements override assumptions.**
2. **Unresolved requirements remain marked as unresolved.**
3. **Legacy-system behavior is not automatically a business rule.**
4. **Detailed technical enforcement belongs in later architecture/database/API specifications.**
5. **Business rules should be testable and enforced centrally.**

Before implementation, all rules marked **Needs confirmation** must either be confirmed by the client or explicitly removed from the scope.
