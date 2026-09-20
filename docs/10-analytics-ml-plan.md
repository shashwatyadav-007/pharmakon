# 10 — Analytics & ML Specification Plan

**Document status:** Finalized v1.0 — Analytics & Data Science Blueprint  
**Primary Language:** Python 3.11  
**Libraries:** Pandas, NumPy, Plotly, scikit-learn, XGBoost  
**Related documents:** `01-project-overview.md`, `03-functional-requirements.md`, `06-mvp-scope.md`, `07-system-architecture.md`, `08-database-design.md`

---

## 1. Executive Summary & Strategy

PharmaKon turns raw pharmacy transaction data into actionable decision support for the owner. 

### Staged Analytics & AI Philosophy
1. **Deterministic Analytics First:** SQL + Pandas analytics build trust by producing exact, verifiable totals that match database records.
2. **Measured Machine Learning Second:** ML demand forecasting is introduced only when transaction history supports a defensible model.
3. **Grounded AI Assistant Third:** AI is constrained strictly to executing deterministic database functions via tool calling—it never manufactures financial or stock numbers.

---

## 2. Core Business Analytics Metrics

| Metric Category | Metric Name | SQL / Calculation Formula | Visual Representation |
| :--- | :--- | :--- | :--- |
| **Sales Performance** | Daily / Monthly Revenue | $\sum (\text{grand\_total})$ grouped by date range | Line chart / Bar chart |
| **Sales Performance** | Average Order Value (AOV) | $\frac{\text{Total Revenue}}{\text{Total Invoice Count}}$ | Metric Card |
| **Product Velocity** | Top Movers (Fast-Moving) | $\sum (\text{quantity\_sold})$ per product descending | Ranked Table / Bar chart |
| **Product Velocity** | Dead Stock / Slow Movers | Products with zero or $< 5$ sales in last 60 days | Risk Alert Table |
| **Profitability** | Gross Profit Margin | $\sum ((\text{actual\_selling\_rate} - \text{purchase\_cost}) \times \text{quantity})$ | Doughnut chart / Metric Card |
| **Inventory Health** | Stock Turnover Ratio | $\frac{\text{Cost of Goods Sold (COGS)}}{\text{Average Inventory Value}}$ | Trend gauge |
| **Expiry Risk** | Expiry Valuation Risk | $\sum (\text{batch\_quantity} \times \text{purchase\_cost})$ for expiries $< 60$ days | Warning Badge & Detail Table |

---

## 3. SQL Analytics Aggregation Engine

### 3.1 Gross Profit Query
```sql
SELECT 
    p.id AS product_id,
    p.name AS product_name,
    p.category,
    SUM(si.quantity) AS total_units_sold,
    SUM(si.actual_selling_rate * si.quantity) AS total_revenue,
    SUM(si.purchase_cost * si.quantity) AS total_cogs,
    SUM((si.actual_selling_rate - si.purchase_cost) * si.quantity) AS gross_profit,
    ROUND(
        (SUM((si.actual_selling_rate - si.purchase_cost) * si.quantity) / NULLIF(SUM(si.actual_selling_rate * si.quantity), 0)) * 100, 2
    ) AS profit_margin_percentage
FROM sale_items si
JOIN products p ON si.product_id = p.id
JOIN sales s ON si.sale_id = s.id
WHERE s.voucher_date >= :start_date AND s.voucher_date <= :end_date
GROUP BY p.id, p.name, p.category
ORDER BY gross_profit DESC;
```

### 3.2 Expiry Risk Valuation Query
```sql
SELECT 
    p.code,
    p.name AS product_name,
    b.batch_number,
    b.expiry_date,
    b.quantity AS remaining_stock,
    b.purchase_cost,
    (b.quantity * b.purchase_cost) AS capital_at_risk,
    (b.expiry_date - CURRENT_DATE) AS days_until_expiry
FROM batches b
JOIN products p ON b.product_id = p.id
WHERE b.expiry_date <= (CURRENT_DATE + INTERVAL '60 days')
  AND b.quantity > 0
  AND b.is_active = TRUE
ORDER BY b.expiry_date ASC;
```

---

## 4. Machine Learning Priority 1: Time-Series Demand Forecasting

### 4.1 Problem Definition
Forecast daily product unit demand $\hat{y}_{i, t+k}$ for the next 14 to 30 days to optimize pharmacy purchasing.

### 4.2 Feature Engineering Pipeline
```text
Raw Transactions (sales & sale_items)
       ↓
Daily Resampling per Product (fill missing dates with 0)
       ↓
Feature Extraction:
  ├── Lag Features: y_{t-1}, y_{t-7}, y_{t-14}, y_{t-28}
  ├── Rolling Window Stats: 7-day & 14-day Mean, Std, Max
  ├── Calendar Features: DayOfWeek, DayOfMonth, IsWeekend, Month
  └── Categorical Features: Product Category, Price Point
```

### 4.3 Time-Aware Validation Strategy (No Data Leakage)
Strictly chronological train/validation splits are enforced. Random k-fold cross-validation is forbidden due to temporal dependence.

```text
[------------------- Train Set (80%) -------------------][--- Test Set (20%) ---]
2026-09-15                                           2026-11-15             2026-12-13
```

### 4.4 Model Selection & Evaluation Metrics
- **Models Evaluated:** Baseline (7-day Moving Average) vs **scikit-learn Random Forest Regressor** vs **XGBoost Regressor**.
- **Evaluation Metrics:**
  - **Weighted Absolute Percentage Error (WAPE):** $\frac{\sum |y_t - \hat{y}_t|}{\sum y_t}$
  - **Root Mean Squared Error (RMSE):** $\sqrt{\frac{1}{N} \sum (y_t - \hat{y}_t)^2}$

---

## 5. Machine Learning Priority 2: Customer RFM Segmentation (Conditional)

If sufficient customer transaction records exist, K-Means clustering is applied over Recency, Frequency, Monetary (RFM) features:

```text
Customer Sales Log
       ↓
RFM Extraction per Customer:
  ├── Recency (R): Days since last purchase
  ├── Frequency (F): Total invoice count
  └── Monetary (M): Total grand_total spend
       ↓
Log Transformation & StandardScaler
       ↓
K-Means Clustering (k=3 or 4, evaluated via Silhouette Score)
       ↓
Segments: "High Value Regulars", "Occasional Buyers", "At Risk"
```

---

## 6. Replenishment Recommendation Engine

Combines current stock, sales velocity, reorder levels, and demand forecast into an actionable purchasing recommendation:

$$\text{Suggested Order Qty} = \max\left(0, (\text{Forecasted Demand}_{30\text{ days}} + \text{Safety Stock}) - \text{Current Stock}\right)$$

Where:
$$\text{Safety Stock} = (\text{Max Daily Sales} \times \text{Lead Time Days}) - (\text{Avg Daily Sales} \times \text{Avg Lead Time Days})$$

---

## 7. AI Assistant Architecture & Tool Calling Rules

The AI assistant uses **LLM Function Calling** to query deterministic Python/SQL tools.

### Allowed Tool Registry
1. `get_product_stock(product_name)`: Returns current batch quantities and expiry dates.
2. `get_top_selling_products(limit, days)`: Returns top movers by volume and revenue.
3. `get_expiry_risk_report(threshold_days)`: Returns batches expiring soon.
4. `get_demand_forecast(product_id)`: Returns ML forecast predictions.

### AI Safety System Prompt Rule
> *"You are the PharmaKon Pharmacy Assistant. You MUST strictly use the provided system tools to obtain numeric pharmacy figures. You are FORBIDDEN from inventing, guessing, or estimating sales, stock, revenue, or price numbers without tool data."*
