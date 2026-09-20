# Context — UI/UX Design System & Layout Guidelines

## 1. Design System Overview

PharmaKon's frontend is designed for rapid retail pharmacy operations, clarity during high-traffic billing hours, and clean visual data analytics.

### Color Palette (Tailwind CSS)
- **Primary / Brand:** Emerald / Teal (`emerald-600` `#059669`, `emerald-700` `#047857`) — Used for primary buttons, active navigation, and success indicators.
- **Background:** Slate Light (`slate-50` `#f8fafc`, `slate-100` `#f1f5f9`) — Clean, high-contrast healthcare aesthetic.
- **Surface / Cards:** Pure White (`#ffffff`) with subtle border `border-slate-200` and shadow `shadow-sm`.
- **Text:** Slate Dark (`slate-900` `#0f172a` for headings, `slate-600` `#475569` for body).
- **Status Badges:**
  - *In Stock / Normal:* `bg-emerald-100 text-emerald-800`
  - *Low Stock Warning:* `bg-amber-100 text-amber-800`
  - *Expiry Risk / Expired:* `bg-rose-100 text-rose-800`
  - *Credit Outstanding:* `bg-indigo-100 text-indigo-800`

---

## 2. Key Page Layout Specifications

### 2.1 POS / Billing Screen (`/pos`)
Designed for ultra-fast keyboard & barcode scanner interaction:
- **Left Panel (70% width):**
  - Instant Product Search Bar (`F2` shortcut focus) with auto-complete.
  - Active Invoice Items Table showing Product Name, Auto-Selected FEFO Batch & Expiry, Quantity input, MRP, Custom Rate override input, and Line Subtotal.
- **Right Panel (30% width):**
  - Live Order Calculation Summary: Subtotal, Discount %, Discount Amount, 13% VAT, Round-off, Grand Total (Large font).
  - Payment Method Selector (`Cash`, `eSewa`, `Banking`, `Credit`).
  - Single-Click "Complete & Print Invoice" (`F9` shortcut) button.

### 2.2 Dashboard Screen (`/dashboard`)
- Top metric cards: Today's Revenue, Total Invoices, Low Stock Count, Near-Expiry Items Count.
- Middle Section: Interactive Plotly Sales Trend Chart & Top 5 Fast Moving Medicines.
- Bottom Section: Expiry Risk Action List and Low-Stock Replenishment Quick Actions.

### 2.3 Inventory Manager (`/inventory`)
- Tabbed interface: `All Products`, `Batches & FEFO`, `Low Stock Alerts`, `Expiry Risk`, `Stock Adjustments`.
- Filters by Category, Expiry Date Range, and Search String.
