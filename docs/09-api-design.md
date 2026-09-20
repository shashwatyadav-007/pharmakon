# 09 — API Design & Interface Specification

**Document status:** Finalized v1.0 — Complete REST API Contract Specification  
**Framework:** FastAPI (Python 3.11+)  
**API Specification Standard:** OpenAPI 3.0 (Swagger UI available at `/docs`)  
**Base Path:** `/api/v1`  
**Related documents:** `03-functional-requirements.md`, `05-business-rules.md`, `07-system-architecture.md`, `08-database-design.md`

---

## 1. Global API Conventions

### 1.1 Standard Request/Response Formats
All requests and responses use `application/json` content type unless downloading file formats (e.g. PDF invoice downloads).

#### Success Response Envelope Structure
```json
{
  "success": true,
  "data": { ... },
  "message": "Operation completed successfully",
  "meta": {
    "page": 1,
    "limit": 20,
    "total": 1500
  }
}
```

#### Error Response Envelope Structure
```json
{
  "success": false,
  "error": {
    "code": "INSUFFICIENT_STOCK",
    "message": "Requested quantity (10) exceeds available FEFO stock (4) for product Paracetamol 500mg.",
    "details": [
      {
        "field": "items[0].quantity",
        "issue": "Stock check failed"
      }
    ]
  }
}
```

### 1.2 HTTP Status Code Standard
- `200 OK`: Successful retrieval or modification.
- `201 Created`: Resource successfully created.
- `400 Bad Request`: Validation error or business rule violation (e.g. negative stock attempt).
- `401 Unauthorized`: Missing or invalid authentication token.
- `404 Not Found`: Target entity missing.
- `422 Unprocessable Entity`: Schema format invalid.
- `500 Internal Server Error`: Unhandled server exception.

---

## 2. API Endpoints by Domain

### 2.1 Authentication (`/api/v1/auth`)

#### `POST /api/v1/auth/login`
Authenticate the single pharmacy operational system user.
- **Request Body:**
```json
{
  "username": "admin",
  "password": "SecurePassword123!"
}
```
- **Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6...",
    "token_type": "bearer",
    "expires_in": 86400,
    "user": {
      "username": "admin",
      "role": "Pharmacy System User"
    }
  }
}
```

---

### 2.2 Product Management (`/api/v1/products`)

#### `GET /api/v1/products`
List and search products with pagination.
- **Query Parameters:** `query` (search code/name/barcode), `category`, `is_active`, `page`, `limit`
- **Response (200 OK):** Array of product summaries including total available stock across all active batches.

#### `POST /api/v1/products`
Create a new product catalog item.
- **Request Body:**
```json
{
  "code": "MED-PAR-500",
  "name": "Paracetamol 500mg",
  "category": "Medicine",
  "unit": "Strip",
  "mrp": 60.00,
  "default_purchase_price": 45.00,
  "barcode": "8901234567890",
  "reorder_level": 15
}
```

#### `GET /api/v1/products/{id}`
Get detailed product profile including all batch quantities and expiry status.

#### `PUT /api/v1/products/{id}`
Update product information.

---

### 2.3 Batch & Inventory Management (`/api/v1/inventory`)

#### `GET /api/v1/inventory/batches`
List batches, optionally filtered by `product_id`, `expiry_before`, or `low_stock`.

#### `GET /api/v1/inventory/fefo/{product_id}`
Retrieve batches for a product ordered strictly by **FEFO (Earliest Expiry First)**.
- **Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "product_id": "c39e...1b",
    "product_name": "Paracetamol 500mg",
    "fefo_batches": [
      {
        "batch_id": "b11a...01",
        "batch_number": "BCH-2026-01",
        "expiry_date": "2026-11-30",
        "available_quantity": 8,
        "purchase_cost": 42.00
      },
      {
        "batch_id": "b11a...02",
        "batch_number": "BCH-2026-02",
        "expiry_date": "2027-05-15",
        "available_quantity": 25,
        "purchase_cost": 45.00
      }
    ]
  }
}
```

#### `GET /api/v1/inventory/alerts/low-stock`
Fetch all products where combined stock is $\le$ `reorder_level`.

#### `GET /api/v1/inventory/alerts/expiry-risk`
Fetch inventory batches expiring within the configured threshold (e.g. within 60 days).

#### `POST /api/v1/inventory/adjustments`
Record physical stock count adjustments.
- **Request Body:**
```json
{
  "product_id": "c39e...1b",
  "batch_id": "b11a...01",
  "new_quantity": 10,
  "reason": "PHYSICAL_COUNT",
  "notes": "Verified count during weekly inventory check"
}
```

---

### 2.4 Supplier & Purchase Management (`/api/v1/purchases`)

#### `GET /api/v1/suppliers` / `POST /api/v1/suppliers`
Manage vendor records.

#### `POST /api/v1/purchases`
Record a supplier invoice and automatically increment batch inventory.
- **Request Body:**
```json
{
  "supplier_id": "s88a...99",
  "invoice_reference": "SUP-INV-9921",
  "voucher_date": "2026-09-20",
  "payment_status": "PAID",
  "items": [
    {
      "product_id": "c39e...1b",
      "batch_number": "BCH-2026-03",
      "expiry_date": "2027-12-31",
      "quantity": 100,
      "unit_purchase_cost": 44.00
    }
  ]
}
```

#### `POST /api/v1/purchases/supplier-returns`
Record damaged/expired stock returned to suppliers.

---

### 2.5 Sales POS & Invoicing (`/api/v1/sales` & `/api/v1/invoices`)

#### `POST /api/v1/sales`
Create and complete a sales invoice (Validates FEFO stock, calculates VAT & discount, deducts stock).
- **Request Body:**
```json
{
  "customer_id": "cust-1234-uuid",
  "payment_method": "CASH",
  "is_credit": false,
  "discount_amount": 10.00,
  "items": [
    {
      "product_id": "c39e...1b",
      "quantity": 2,
      "actual_selling_rate": 60.00
    }
  ]
}
```
- **Response (201 Created):**
```json
{
  "success": true,
  "data": {
    "sale_id": "sale-5555-uuid",
    "invoice_number": "INV-2026-0089",
    "fiscal_year": "2083/84",
    "subtotal": 120.00,
    "discount_amount": 10.00,
    "tax_amount": 14.30,
    "round_off": -0.30,
    "grand_total": 124.00,
    "payment_method": "CASH",
    "dispensed_batches": [
      {
        "batch_number": "BCH-2026-01",
        "quantity_dispensed": 2,
        "expiry_date": "2026-11-30"
      }
    ]
  }
}
```

#### `GET /api/v1/invoices/{id}`
Fetch formatted invoice for print view.

#### `GET /api/v1/invoices/{id}/pdf`
Generate downloadable PDF invoice file.

#### `POST /api/v1/invoices/{id}/digital-send`
Generate digital invoice link formatted for WhatsApp/SMS notification.

---

### 2.6 Customer & Credit Ledger (`/api/v1/customers` & `/api/v1/credit-ledger`)

#### `GET /api/v1/customers` / `POST /api/v1/customers`
Manage customer profiles.

#### `GET /api/v1/credit-ledger/{customer_id}`
Fetch customer credit ledger statement and outstanding balance.

#### `POST /api/v1/credit-ledger/payments`
Record later credit payments against an outstanding balance.
- **Request Body:**
```json
{
  "customer_id": "cust-1234-uuid",
  "amount": 500.00,
  "payment_method": "ESEWA",
  "notes": "Partial repayment via eSewa"
}
```

---

### 2.7 Returns & Refunds (`/api/v1/returns`)

#### `POST /api/v1/returns`
Process customer item returns using original invoice verification.
- **Request Body:**
```json
{
  "sale_id": "sale-5555-uuid",
  "items": [
    {
      "sale_item_id": "item-999-uuid",
      "quantity": 1,
      "condition": "RESTOCKABLE"
    }
  ]
}
```

---

### 2.8 Analytics & Replenishment (`/api/v1/analytics`)

#### `GET /api/v1/analytics/overview`
Dashboard metrics summary (Daily/weekly/monthly revenue, orders, low-stock count, expiry alerts).

#### `GET /api/v1/analytics/product-performance`
Top-selling and slow-moving product rankings over a date range.

#### `GET /api/v1/analytics/profitability`
Gross profit calculation using recorded `actual_selling_rate` vs `purchase_cost`.

#### `GET /api/v1/analytics/replenishment-recommendations`
Rule-based replenishment suggestions based on current stock, sales velocity, and reorder levels.

---

### 2.9 ML & AI Endpoints (`/api/v1/ml` & `/api/v1/ai`)

#### `GET /api/v1/ml/forecast/{product_id}`
Fetch ML demand forecast for a product over the next 30 days.

#### `POST /api/v1/ai/query`
Controlled natural language query endpoint for owner decision support.
- **Request Body:**
```json
{
  "question": "Which medicines have the highest expiry risk next month?"
}
```
- **Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "answer": "You currently have 2 batches of Amoxicillin 250mg expiring in 45 days with a combined stock of 18 strips. Based on current sales velocity, estimated sales will be 10 strips, leaving 8 strips at risk of expiring.",
    "tool_used": "get_expiry_risk_report",
    "grounded_data": [ ... ]
  }
}
```
