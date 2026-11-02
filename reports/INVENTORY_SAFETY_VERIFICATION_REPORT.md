# PharmaKon – Inventory Safety Verification & AI Assistant Error Diagnosis

**Audit Date:** November 3, 2026  
**Status:** Verification Passed | Clean Build | 129/129 Backend Tests | 10/10 Frontend Tests  
**Gemini Quota Safeguard:** Active (0 Live Gemini API Calls Made; 100% Mocked in Automated Testing)

---

## 1. Executive Summary

A safety audit was conducted across the full PharmaKon stack covering:
1. **Pharmacy Inventory Safety & Expiry Handling:** Strict separation between usable dispensing stock and expired inventory.
2. **FEFO Dispensing Engine:** Verification that expired batches are completely excluded from dispensing recommendations.
3. **AI Assistant Error Diagnosis:** Root-cause analysis and resolution for the Assistant Error shown in the UI (`media_1793647951123_2706fe9c.png`).

---

## 2. AI Assistant Error Diagnosis & Repair

### Root Cause Analysis (`media_1793647951123_2706fe9c.png`)
When the user sent the query *"Find Paracetamol 500mg stock."*, the drawer displayed:
> **Assistant Error**  
> *An error occurred while communicating with the AI service. Please try again.*

**Root Causes Identified:**
1. **Invalid Model Identifier:** In `backend/.env` and [config.py](file:///d:/PharmaKon/pharmakon/backend/app/core/config.py), `AI_MODEL_NAME` was configured as `gemini-3.1-flash-lite`.
2. **Invalid Fallback Candidate List:** In [agent.py](file:///d:/PharmaKon/pharmakon/backend/app/services/ai/agent.py), `FALLBACK_MODELS` was hardcoded to `["gemini-3.1-flash-lite", "gemini-3.5-flash", "gemini-3-flash-preview"]`.
3. None of these identifiers exist in the Google AI Studio / Gemini API catalog (which uses `gemini-2.5-flash`, `gemini-2.0-flash`, `gemini-1.5-flash`). Upstream Google API returned HTTP 404 (Model Not Found) across all candidate loops.
4. The error handler fell back to a generic 500 `AI_ERROR` message.

### Fixes Implemented:
1. Updated [config.py](file:///d:/PharmaKon/pharmakon/backend/app/core/config.py) and `backend/.env` to default to `gemini-2.5-flash`.
2. Updated [agent.py](file:///d:/PharmaKon/pharmakon/backend/app/services/ai/agent.py) `FALLBACK_MODELS` to `["gemini-2.5-flash", "gemini-2.0-flash", "gemini-1.5-flash"]`.
3. Preserved strict zero-call policy during development/testing while ensuring that live credentials (when used by the user) route to valid production endpoints.

---

## 3. Inventory Safety & Expiry Handling Audit

### Clinical Safety Rule: Expired Stock Must NEVER Count as Usable Stock
In a clinical pharmacy environment:
$$\text{Usable Dispensing Stock} = \sum_{\text{Batch}} \text{quantity} \quad \text{where } \text{is\_active} = \text{true} \land \text{expiry\_date} \ge \text{today}$$

### Defect Identified & Corrected:
Previously, SQL subqueries in [product_service.py](file:///d:/PharmaKon/pharmakon/backend/app/services/product_service.py), [inventory_service.py](file:///d:/PharmaKon/pharmakon/backend/app/services/inventory_service.py), and [tools.py](file:///d:/PharmaKon/pharmakon/backend/app/services/ai/tools.py) checked `Batch.is_active == True` but did not filter `Batch.expiry_date >= date.today()`.

**Risk:** If a product had 20 expired units and 5 valid units with a reorder level of 15:
- Total stock was calculated as $20 + 5 = 25 > 15$, masking a dangerous stockout.
- Under FEFO (earliest expiry first), the expired lot with quantity > 0 was recommended first to dispense!

### Fixes Applied:
1. **[product_service.py](file:///d:/PharmaKon/pharmakon/backend/app/services/product_service.py):**
   - `_stock_subquery`: Added `Batch.expiry_date >= today`.
   - `get_all_products`: Stock subquery adds `Batch.expiry_date >= today`.
2. **[inventory_service.py](file:///d:/PharmaKon/pharmakon/backend/app/services/inventory_service.py):**
   - `get_fefo_batches`: Added `Batch.expiry_date >= today`. Expired lots are completely excluded from dispensing guidance.
   - `get_low_stock_alerts`: Filtered with `Batch.expiry_date >= today`. Expired batches cannot mask low stock.
   - `get_all_batches(low_stock=True)`: Updated subquery with `Batch.expiry_date >= today`.
3. **[tools.py](file:///d:/PharmaKon/pharmakon/backend/app/services/ai/tools.py):**
   - `search_products`: Added `Batch.expiry_date >= today` in `stock_sub`.
   - `get_product_stock_and_batches`: Only unexpired active batches count towards `total_stock`. Expired lots are isolated in `expired_batches`.
4. **[InventoryPage.tsx](file:///d:/PharmaKon/pharmakon/frontend/src/features/inventory/InventoryPage.tsx):**
   - Prominently displays `EXPIRED` badge for lots with `days_until_expiry < 0` and `Today` for `days_until_expiry == 0`.

---

## 4. Verification & Test Suite

### New Automated Verification Test
Added `test_expired_batches_excluded_from_usable_stock_and_trigger_low_stock` in [test_inventory.py](file:///d:/PharmaKon/pharmakon/backend/tests/test_inventory.py):
- **Scenario:** Product "Medicine Safety A" with Reorder Level = 15.
  - Batch A: 20 units (Expired 5 days ago).
  - Batch B: 5 units (Valid for 90 days).
- **Assertions Verified:**
  1. Product catalog report: `total_stock == 5` (Usable only).
  2. FEFO Dispensing API: Returns ONLY Batch B (5 units). Batch A is excluded.
  3. Low Stock Alerts: Product is flagged with `current_stock == 5`, `shortfall == 10`.
  4. Expiry Risk Alerts: Batch A appears with urgency `EXPIRED`.
  5. AI Tool: Returns `total_stock == 5` and `expired_stock == 20`.

### Overall Test Results
- **Backend:** 129/129 tests passed (0 failures, 100% pass rate).
- **Frontend:** 10/10 tests passed (Vitest).
- **Production Build:** Clean (`tsc -b && vite build` succeeded in 7.64s).
- **Gemini Quota:** 0 live calls consumed.
