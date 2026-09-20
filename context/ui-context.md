# Context: UI/UX Design System and Layout Guidelines

> **Prerequisite:** Read [`DESIGN_CONSTRAINTS.md`](../DESIGN_CONSTRAINTS.md) in the project root before writing any frontend code. It contains the binding list of prohibited visual patterns, copy rules, and launch requirements. This file defines what *to* use; that file defines what is *banned*.

---

## 1. Design System Overview

PharmaKon's frontend is designed for rapid retail pharmacy operations, clarity during high-traffic billing hours, and clean visual data analytics.

### Color Palette (Tailwind CSS)

- **Primary / Brand:** Emerald / Teal (`emerald-600` `#059669`, `emerald-700` `#047857`). Used for primary buttons, active navigation, and success indicators.
- **Background:** Slate Light (`slate-50` `#f8fafc`, `slate-100` `#f1f5f9`). Clean, high-contrast healthcare aesthetic.
- **Surface / Cards:** Pure White (`#ffffff`) with `1px` solid border (`border-slate-200`) and `shadow-sm`. No glassmorphism. No frosted glass. No backdrop-blur.
- **Text:** Slate Dark (`slate-900` `#0f172a` for headings, `slate-600` `#475569` for body text).
- **Status Badges:**
  - In Stock / Normal: `bg-emerald-100 text-emerald-800`
  - Low Stock Warning: `bg-amber-100 text-amber-800`
  - Expiry Risk / Expired: `bg-rose-100 text-rose-800`
  - Credit Outstanding: `bg-indigo-100 text-indigo-800`

### Typography

- **Primary font:** System font stack: `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif`.
- Do not use Inter as the sole or primary typeface.
- Do not pair Space Grotesk with Instrument Serif.
- Do not use serif italics for decorative accent on individual words.

### Buttons

- Rectangular shape with `border-radius: 4px` to `6px`. No pill shapes (large border-radius).
- Visible 1px border on secondary/ghost buttons.
- Hover state: instant background-color change, no fade transition longer than 100ms.
- Clear disabled state with reduced opacity and `cursor: not-allowed`.

### Icons

- Use Heroicons or Phosphor Icons. Do not default to Lucide.
- Use icons sparingly and only where they add meaning. Do not use emoji characters as icons.
- Custom SVGs are acceptable where a library icon does not fit.

### Cards and Containers

- White background, `border-slate-200`, `shadow-sm`.
- No glassmorphism, no frosted glass, no backdrop-blur overlays.
- No colored left-border accent stripe on cards.

### Animation

- No scroll-triggered entrance animations (no fade-in, no slide-up on scroll).
- No cursor-following beam, spotlight, or trail effects.
- Elements render in their final position immediately.
- Micro-interactions (button press feedback, dropdown open) are acceptable if under 150ms.

---

## 2. Key Page Layout Specifications

### 2.1 POS / Billing Screen (`/pos`)

Designed for ultra-fast keyboard and barcode scanner interaction:

- **Left Panel (70% width):**
  - Instant Product Search Bar (`F2` shortcut focus) with auto-complete.
  - Active Invoice Items Table showing Product Name, Auto-Selected FEFO Batch and Expiry, Quantity input, MRP, Custom Rate override input, and Line Subtotal.
- **Right Panel (30% width):**
  - Live Order Calculation Summary: Subtotal, Discount %, Discount Amount, 13% VAT, Round-off, Grand Total (large font).
  - Payment Method Selector (`Cash`, `eSewa`, `Banking`, `Credit`).
  - Single-click "Complete and Print Invoice" (`F9` shortcut) button.

### 2.2 Dashboard Screen (`/dashboard`)

- Top metric cards: Today's Revenue, Total Invoices, Low Stock Count, Near-Expiry Items Count. **Display real data only.** If the database is empty, show "No data yet" instead of zeros or placeholder numbers.
- Middle Section: Interactive Plotly Sales Trend Chart and Top 5 Fast Moving Medicines.
- Bottom Section: Expiry Risk Action List and Low-Stock Replenishment Quick Actions.

### 2.3 Inventory Manager (`/inventory`)

- Tabbed interface: `All Products`, `Batches and FEFO`, `Low Stock Alerts`, `Expiry Risk`, `Stock Adjustments`.
- Filters by Category, Expiry Date Range, and Search String.

### 2.4 Required Pages Before Launch

- `/privacy-policy`: Real, applicable privacy policy content. Not placeholder text.
- `/terms-and-conditions`: Real, applicable terms. Not placeholder text.

---

## 3. Copy and Content Rules

- Write specific, factual descriptions. No vague hero text ("Revolutionize your workflow").
- No generic buzzwords ("seamless", "cutting-edge", "next-gen", "leverage").
- No em dashes used as a stylistic device. Use commas, semicolons, colons, or separate sentences.
- No fake reviews, testimonials, metrics, or customer counters.
- No AI-generated stock photos or illustrations.
- No "made with AI" or "built with [tool]" tags anywhere in the UI.
