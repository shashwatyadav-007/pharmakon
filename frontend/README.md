# PharmaKon Frontend

Professional web client for **PharmaKon**, a Pharmacy Management and Analytics System built for **Aayushman Pharmacy, Nepal**.

---

## 1. Technology Stack

- **React 19** with **TypeScript**
- **Vite**: Ultra-fast build and development tool
- **Tailwind CSS**: Utility-first CSS configured with custom brand tokens, system font stack, and 4px-6px rectangular radii
- **React Router v7**: Client-side declarative routing and protected navigation
- **Vitest & React Testing Library**: Component and formatter unit/integration test suite

---

## 2. Prerequisites

- **Node.js**: v18.0.0 or higher (v24+ tested)
- **npm**: v9.0.0 or higher
- **PharmaKon Backend**: Running on `http://127.0.0.1:8000`

---

## 3. Installation & Setup

Navigate to the `frontend/` directory and install dependencies:

```bash
cd frontend
npm install
```

### Environment Configuration

Copy the example environment configuration:

```bash
cp .env.example .env
```

Ensure `VITE_API_BASE_URL` points to your active FastAPI backend instance:

```env
VITE_API_BASE_URL=http://127.0.0.1:8000
```

---

## 4. Running the Development Server

Start the local Vite development server:

```bash
npm run dev
```

Access the web application at: [http://localhost:5173/](http://localhost:5173/)

### Default Operational Credentials

- **Username**: `admin`
- **Password**: `SecurePassword123!`

---

## 5. Running the Backend (FastAPI)

In a separate terminal, start the PharmaKon FastAPI backend:

```bash
# Activate virtual environment (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Start the server
cd backend
uvicorn app.main:app --reload
```

---

## 6. Testing & Quality Verification

Run the frontend test suite:

```bash
npm run test
```

Run TypeScript type check:

```bash
npx tsc --noEmit
```

Build for production:

```bash
npm run build
```

---

## 7. Current Frontend Capabilities

### Authentication (`/login`)
- Integrated with `POST /api/v1/auth/login`.
- Bearer token attachment to subsequent API requests.
- Session restoration via `localStorage`.
- Protected route handling with redirect to `/login`.

### Operations Dashboard (`/dashboard`)
- Live KPI cards: Total catalog items, low-stock warnings, and batches expiring within 60 days.
- Priority FEFO batch action table displaying lots nearing expiration.
- Low-stock action table displaying items needing replenishment.
- Clearly marked planned metrics (e.g. today's revenue) to prevent fabricated figures.

### Product Catalog (`/products`)
- Full listing table with multi-criteria search (medicine name, code, barcode).
- Category filtering (`Medicine`, `Surgical`, `Cosmetic`, `Baby`, `Food`).
- Pagination aligned with backend metadata (`limit`, `page`, `total`).
- Create and edit modals validating required fields, unique SKUs, and positive MRP numbers.
- Dynamic stock display summing active batches.

### Inventory & FEFO Engine (`/inventory`)
- **All Active Batches Tab**: Lists all recorded lots with expiry dates and purchase costs.
- **FEFO Dispensing Sequence Tab**: Interactive selector rendering server-confirmed First Expiry, First Out batch ordering.
- **Low Stock Alerts Tab**: Identifies medicines $\le$ reorder levels.
- **Expiry Risk Alerts Tab**: Identifies lots expiring within 60 days.
- **Physical Stock Adjustment Tab**: Form allowing pharmacy supervisors to update lot counts with mandatory reason codes, generating immutable server audit logs.

### Suppliers (`/suppliers`)
- Distributor directory with contact person, phone, PAN/VAT, and physical address.
- Registration modal with field validation and duplicate checks.

### Compliance Pages
- `/privacy-policy`: Statutory data handling policy for Aayushman Pharmacy.
- `/terms-and-conditions`: FEFO compliance and stock audit rules.

---

## 8. Known Backend Limitations & Future Modules

1. **In-Memory Backend State**: Backend currently runs on an in-memory datastore for the development phase; restarting the backend resets mutations to initial seed records.
2. **Sales POS & Billing**: Billing checkout and invoice printing endpoints are scheduled for subsequent milestones.
3. **Purchasing Receipts**: Supplier purchase voucher creation is planned for Phase 2.
4. **Credit Ledger & Customer Profiles**: Digital customer credit tracking is planned for Phase 2.
5. **Demand Forecasting & ML**: Predictive replenishment analytics are planned for Phase 3.
