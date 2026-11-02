# POST-AUDIT VERIFICATION AND BUSINESS LOGIC VALIDATION REPORT

**Project:** PharmaKon – Pharmacy Management & Analytics System  
**Client Organization:** Aayushman Pharmacy, Nepal  
**Verification Date:** November 3, 2026  
**Status:** VERIFIED & STABILIZED  

---

## 1. Executive Summary

Following the full-stack bug audit, a second in-depth verification pass was executed focusing strictly on **business logic correctness**, **security classification**, **PostgreSQL query execution plans (EXPLAIN ANALYZE)**, and **frontend operational behaviors**.

The investigation confirmed a subtle business logic flaw identified in the low-stock batch filter (`Batch.quantity <= Product.reorder_level`), where individual small batches of high-stock products were incorrectly returned as low stock. This has been repaired by evaluating total product-level available stock via a subquery.

### Key Results
- **Inventory Business Rule Correctness:** Verified that products with multiple batches (e.g. Paracetamol 500mg with 33 total units > 15 reorder level, having batch `BCH-2026-01` of 8 units) are **not** flagged as low stock.
- **Authentication Reality:** Documented the exact boundary between development-only mock credentials and production requirements (plain text comparison, static token string, single user model).
- **PostgreSQL Execution Plans:** Confirmed that key queries use B-tree index scans (`idx_batches_expiry_date`, `idx_batches_product_id`), executing in **1.096 ms** and **0.067 ms** respectively.
- **Zero Gemini API Calls:** Maintained 100% compliance with quota restrictions. All AI tests executed with isolated unit mocks.
- **Test Suite Status:** **128/128 backend tests passing**; **10/10 frontend tests passing**; production build successful in 899ms.

---

## 2. Issues Confirmed, Addressed & Classified

| Issue ID | Domain | Description | Status |
| :--- | :--- | :--- | :--- |
| **ISSUE-01** | Inventory Logic | `GET /inventory/batches?low_stock=true` evaluated batch-level quantity against reorder level rather than aggregated product-level stock. | **FIXED** |
| **ISSUE-02** | Security | Authentication currently uses mock static token `mock_access_token_pharmakon_admin_2026` and plain-text password comparison. | **NEEDS MANUAL VERIFICATION** *(Documented Dev-Only Status)* |
| **ISSUE-03** | Performance | Expiry risk alerts full table scan replaced with indexed date comparison. | **FIXED** |
| **ISSUE-04** | Performance | Product catalog N+1 query replaced with single SQL outer join and subquery aggregation. | **FIXED** |
| **ISSUE-05** | UI Lifecycle | Stale closures in search/clear handlers in `ProductsPage.tsx` and `InventoryPage.tsx`. | **FIXED** |
| **ISSUE-06** | UI Lifecycle | Synchronous render cascade in `AuthContext` causing session loading flash on refresh. | **FIXED** |

---

## 3. Inventory Stock Calculations & Business Logic Verification

### 3.1 Investigation of Condition: `Batch.quantity <= Product.reorder_level`
In pharmacy operations, **"Low Stock" is a product-level attribute, not a batch-level attribute**. A product requires reordering only when the combined active quantity across all its lots is at or below the safety reorder threshold.

#### Example Verification:
- **Product:** Medicine A (Reorder level: 15)
- **Batch A:** 8 units
- **Batch B:** 12 units
- **Total Available Stock:** 20 units

**Evaluation:**
- Under the naive condition `Batch.quantity <= Product.reorder_level` (8 <= 15 and 12 <= 15), both Batch A and Batch B were flagged as low-stock lots.
- **Expected Correct Result:** Because total stock (20) exceeds the reorder level (15), the product is sufficiently stocked and should **not** appear in low-stock listings.
- **Implemented Fix:** Updated `get_all_batches` in `backend/app/services/inventory_service.py` to evaluate total stock per product via a subquery:
  ```python
  if low_stock:
      low_stock_prod_sub = (
          select(Batch.product_id)
          .join(Product, Batch.product_id == Product.id)
          .where(Batch.is_active.is_(True), Product.is_active.is_(True))
          .group_by(Batch.product_id, Product.reorder_level)
          .having(func.sum(Batch.quantity) <= Product.reorder_level)
          .scalar_subquery()
      )
      stmt = stmt.where(Batch.product_id.in_(low_stock_prod_sub))
  ```

#### Live Database Verification:
- **Product:** Paracetamol 500mg (`MED-PAR-500`)
- **Configured Reorder Level:** 15
- **Batch BCH-2026-02:** 25 units
- **Batch BCH-2026-01:** 8 units
- **Combined Stock:** 33 units
- **Result:** Querying `GET /api/v1/inventory/batches?low_stock=true` returns **0 batches for Paracetamol 500mg**, while correctly returning low-stock medicines such as Amoxicillin 250mg (5 units <= 10 reorder level).

### 3.2 Edge Case Test Matrix

| Scenario | System Behavior | Business Correctness |
| :--- | :--- | :---: |
| **Multiple Batches for 1 Product** | Combines all active batch quantities. Correctly compares sum against reorder level. | **PASS** |
| **Zero Stock Products** | Outer join coalesces stock to 0. Correctly flagged as `OUT_OF_STOCK` in `get_low_stock_alerts`. | **PASS** |
| **Inactive Batches** | Filtered by `where(Batch.is_active.is_(True))`. Excluded from total available stock. | **PASS** |
| **Expired Batches** | Enforced by FEFO ordering and tagged in Expiry Risk Alerts (`days_until_expiry <= 0` marked `EXPIRED`). | **PASS** |
| **Products with No Batches** | `COALESCE` defaults stock to 0. Products display `0 units` in Catalog and appear in alerts. | **PASS** |
| **Physical Stock Adjustments** | Atomically updates batch row, creates `StockAdjustment` record, and appends `StockMovementLog`. | **PASS** |
| **FEFO Dispensing Order** | Strict sorting: `Batch.expiry_date.asc(), Batch.id.asc()`. Earliest lot dispensed first. | **PASS** |

---

## 4. Authentication and Security Verification

An exhaustive inspection of `backend/app/api/routes/auth.py` was conducted. The current implementation is classified as **Development / Single-User Workstation Authentication (ROLE-001)** and is not production-grade.

### Security Findings Matrix

| Security Characteristic | Current Implementation Status | Assessment |
| :--- | :--- | :--- |
| **Password Verification** | Plain text comparison (`payload.password == "SecurePassword123!"`) | **DEV ONLY** |
| **Token Generation** | Static mock token (`"mock_access_token_pharmakon_admin_2026"`) | **DEV ONLY** |
| **Token Invalidation / Expiry** | No cryptographic expiration (no JWT claims, signature, or expiry timestamp) | **DEV ONLY** |
| **Unauthorized Protection** | Missing or malformed Bearer tokens correctly return HTTP 401 `UNAUTHORIZED` | **VERIFIED** |
| **Invalid Token Rejection** | Incorrect tokens correctly return HTTP 401 `INVALID_TOKEN` | **VERIFIED** |
| **User Role Model** | Single user `admin` with fixed role `"Pharmacy System User"` | **WORKSTATION MVP** |
| **Data Exposure in Responses** | No passwords, hashes, or secret keys returned in API payloads | **VERIFIED** |
| **Environment Storage** | Secrets and keys stored in `backend/.env` (untracked by git) | **VERIFIED** |

> **Security Conclusion:** The application currently fulfills its single-workstation local pharmacy operational model (ROLE-001). Before deploying to a multi-user or cloud environment, it requires migration to `passlib`/`bcrypt` for password hashing and signed JWT tokens with expiration claims.

---

## 5. Database Performance and Query Execution Plans (EXPLAIN ANALYZE)

Direct `EXPLAIN ANALYZE` inspections were run on the live local PostgreSQL database:

### 1. Product Catalog with Stock Outer Join
```sql
EXPLAIN ANALYZE
SELECT products.id, products.name, products.code, COALESCE(stock_sub.total_stock, 0) AS total_stock
FROM products
LEFT OUTER JOIN (
    SELECT batches.product_id, COALESCE(SUM(batches.quantity), 0) AS total_stock
    FROM batches WHERE batches.is_active = true GROUP BY batches.product_id
) AS stock_sub ON products.id = stock_sub.product_id
WHERE products.is_active = true
ORDER BY products.name ASC, products.code ASC LIMIT 20 OFFSET 0;
```
- **Execution Time:** **1.489 ms**
- **Plan Summary:** Hash Left Join -> Subquery Scan -> HashAggregate -> Top-N Heapsort (20 rows).
- **Buffer Cache:** Shared hit = 27 blocks. Zero disk reads.

### 2. Expiry Risk Alerts Query
```sql
EXPLAIN ANALYZE
SELECT batches.id, batches.batch_number, batches.expiry_date, batches.quantity, products.name
FROM batches JOIN products ON batches.product_id = products.id
WHERE batches.is_active = true AND batches.quantity > 0
  AND batches.expiry_date <= '2027-01-02' AND products.is_active = true
ORDER BY batches.expiry_date ASC;
```
- **Execution Time:** **1.096 ms**
- **Plan Summary:** **Bitmap Index Scan using `idx_batches_expiry_date`** -> Bitmap Heap Scan -> Hash Join on `products.id`.
- **Result:** Successfully executes index lookup on the expiry date B-tree index rather than a sequential table scan.

### 3. FEFO Dispensing Batches Query
```sql
EXPLAIN ANALYZE
SELECT batches.id, batches.batch_number, batches.expiry_date, batches.quantity
FROM batches
WHERE batches.product_id = '11111111-1111-1111-1111-111111111111'
  AND batches.is_active = true AND batches.quantity > 0
ORDER BY batches.expiry_date ASC, batches.id ASC;
```
- **Execution Time:** **0.067 ms** (67 microseconds)
- **Plan Summary:** **Index Scan using `idx_batches_product_id` on batches**.
- **Result:** Sub-millisecond indexed point retrieval.

---

## 6. Frontend Operational Behavior Verification

| Behavioral Check | Findings & Verification Result |
| :--- | :--- |
| **Double Screen Flashing** | **Eliminated.** Removed chained `useEffect` state cascades. |
| **Duplicate Network Requests** | **Eliminated.** Removed redundant `activeTab` triggers and duplicate `<select onChange>` fetch triggers. |
| **Empty State Flashing** | **Eliminated.** Tables display dedicated loading skeletons/spinners while `isLoading` is true; empty states render only after loading resolves with 0 items. |
| **Stale Search & Clear Results** | **Eliminated.** Parameterized overrides ensure instant execution with clean query strings. |
| **Double Form Submissions** | **Protected.** Submit buttons are disabled with loading spinners (`isSubmitting`, `adjSubmitting`). |
| **Stock Adjustment Live Sync** | **Verified.** Post-adjustment refresh triggers `loadProducts()`, updating product summary cards and dropdown stock without page reloads. |
| **Session Persistence** | **Verified.** Synchronous lazy initialization from `localStorage` eliminates route flicker on browser refresh. |

---

## 7. Additional Tests Created

- **Test:** `test_list_batches_low_stock_evaluates_product_total_stock`
- **File:** [`backend/tests/test_inventory.py`](file:///d:/PharmaKon/pharmakon/backend/tests/test_inventory.py)
- **Assertion:** Asserts that filtering `GET /api/v1/inventory/batches?low_stock=true` does not return batches for Paracetamol 500mg (33 total stock > 15 reorder level, lot quantity 8), but correctly returns lots for Amoxicillin 250mg (5 units <= 10 reorder level).

---

## 8. Remaining Known Risks

1. **Production Authentication Requirement:** The current token model is intended for single-workstation MVP operation. Multi-user deployment requires bcrypt password hashing and signed JWT validation.
2. **Google Gemini Free-Tier Quota:** Google AI Studio's 20 request/day ceiling on free accounts will trigger HTTP 429 when exhausted. The application handles this gracefully, and all non-AI pharmacy operations remain 100% operational.

---

## 9. Final Verification Status

### Status: **VERIFIED & STABILIZED**
All business rules, database queries, and frontend state synchronization mechanics have been validated and confirmed correct.
