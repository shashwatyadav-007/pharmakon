import React, { useEffect, useState, useMemo } from "react";
import { api, ApiError } from "../../lib/api/client";
import type {
  Batch,
  Product,
  FEFOProductResponseData,
  LowStockAlert,
  ExpiryRiskAlert,
  StockAdjustmentReason,
  StockAdjustmentHistoryItem,
} from "../../types/api";
import { formatDate, formatNPR } from "../../utils/formatters";

type InventoryTab = "batches" | "fefo" | "low_stock" | "expiry_risk" | "adjustments";

export const InventoryPage: React.FC = () => {
  const [activeTab, setActiveTab] = useState<InventoryTab>("batches");

  // Tab 1: Batches state
  const [batches, setBatches] = useState<Batch[]>([]);
  const [batchesLoading, setBatchesLoading] = useState(true);
  const [batchesError, setBatchesError] = useState<string | null>(null);
  const [batchPage, setBatchPage] = useState(1);
  const [batchLimit] = useState(20);
  const [batchTotal, setBatchTotal] = useState(0);
  const [batchSearch, setBatchSearch] = useState("");
  const [batchLowStockOnly, setBatchLowStockOnly] = useState(false);

  // Products reference for FEFO selection and adjustment
  const [products, setProducts] = useState<Product[]>([]);
  const [productsLoading, setProductsLoading] = useState(false);

  // Tab 2: FEFO state
  const [fefoSearch, setFefoSearch] = useState("");
  const [selectedProductId, setSelectedProductId] = useState<string>("");
  const [fefoData, setFefoData] = useState<FEFOProductResponseData | null>(null);
  const [fefoLoading, setFefoLoading] = useState(false);

  // Tab 3: Low stock alerts state
  const [lowStockAlerts, setLowStockAlerts] = useState<LowStockAlert[]>([]);
  const [lowStockSearch, setLowStockSearch] = useState("");
  const [lowStockCategory, setLowStockCategory] = useState<string>("ALL");
  const [lowStockPage, setLowStockPage] = useState(1);
  const [lowStockLimit] = useState(15);
  const [lowStockLoading, setLowStockLoading] = useState(false);

  // Tab 4: Expiry alerts state
  const [expiryAlerts, setExpiryAlerts] = useState<ExpiryRiskAlert[]>([]);
  const [expiryDaysThreshold, setExpiryDaysThreshold] = useState<number>(60);
  const [expirySearch, setExpirySearch] = useState("");
  const [expiryLoading, setExpiryLoading] = useState(false);

  // Tab 5: Stock Adjustment State
  const [adjSearch, setAdjSearch] = useState("");
  const [adjProductId, setAdjProductId] = useState<string>("");
  const [adjBatches, setAdjBatches] = useState<Batch[]>([]);
  const [adjBatchesLoading, setAdjBatchesLoading] = useState(false);
  const [adjBatchId, setAdjBatchId] = useState<string>("");
  const [adjNewQuantity, setAdjNewQuantity] = useState<string>("");
  const [adjReason, setAdjReason] = useState<StockAdjustmentReason>("PHYSICAL_COUNT");
  const [adjNotes, setAdjNotes] = useState<string>("");
  const [adjSubmitting, setAdjSubmitting] = useState(false);
  const [adjSuccessMsg, setAdjSuccessMsg] = useState<string | null>(null);
  const [adjError, setAdjError] = useState<string | null>(null);
  const [recentAdjustments, setRecentAdjustments] = useState<StockAdjustmentHistoryItem[]>([]);
  const [adjustmentsLoading, setAdjustmentsLoading] = useState(false);

  // Load products list for dropdowns
  const loadProducts = async () => {
    setProductsLoading(true);
    try {
      const res = await api.products.list({ limit: 1000 });
      setProducts(res.data);
      if (res.data.length > 0) {
        setSelectedProductId((prev) => (prev ? prev : res.data[0].id));
        setAdjProductId((prev) => (prev ? prev : res.data[0].id));
      }
    } catch {
      // silent fallback
    } finally {
      setProductsLoading(false);
    }
  };

  useEffect(() => {
    loadProducts();

    // Silently pre-populate alert badge counts without blocking
    api.inventory.getLowStockAlerts().then(setLowStockAlerts).catch(() => {});
    api.inventory.getExpiryRiskAlerts(60).then(setExpiryAlerts).catch(() => {});
  }, []);

  // Fetch batches with pagination and search
  const fetchBatches = async (searchOverride?: string, pageOverride?: number) => {
    setBatchesLoading(true);
    setBatchesError(null);
    const s = searchOverride !== undefined ? searchOverride : batchSearch;
    const p = pageOverride !== undefined ? pageOverride : batchPage;
    try {
      const res = await api.inventory.listBatches({
        page: p,
        limit: batchLimit,
        search: s.trim() || undefined,
        low_stock: batchLowStockOnly || undefined,
      });
      setBatches(res.data);
      setBatchTotal(res.meta?.total ?? res.data.length);
    } catch (err: unknown) {
      if (err instanceof Error) {
        setBatchesError(err.message);
      } else {
        setBatchesError("Failed to load inventory batches.");
      }
    } finally {
      setBatchesLoading(false);
    }
  };

  // Fetch FEFO for selected product
  const fetchFEFO = async (pId: string) => {
    if (!pId) return;
    setFefoLoading(true);
    try {
      const res = await api.inventory.getFEFO(pId);
      setFefoData(res);
    } catch {
      setFefoData(null);
    } finally {
      setFefoLoading(false);
    }
  };

  // Fetch low stock alerts
  const fetchLowStockAlerts = async () => {
    setLowStockLoading(true);
    try {
      const lowRes = await api.inventory.getLowStockAlerts();
      setLowStockAlerts(lowRes);
    } finally {
      setLowStockLoading(false);
    }
  };

  // Fetch expiry risk alerts
  const fetchExpiryAlerts = async (days: number) => {
    setExpiryLoading(true);
    try {
      const expRes = await api.inventory.getExpiryRiskAlerts(days);
      setExpiryAlerts(expRes);
    } finally {
      setExpiryLoading(false);
    }
  };

  // Fetch batches for specific adjustment product
  const fetchBatchesForAdjProduct = async (pId: string) => {
    if (!pId) {
      setAdjBatches([]);
      return;
    }
    setAdjBatchesLoading(true);
    try {
      const res = await api.inventory.listBatches({ product_id: pId, limit: 50 });
      setAdjBatches(res.data);
      if (res.data.length > 0) {
        setAdjBatchId(res.data[0].id);
      } else {
        setAdjBatchId("");
      }
    } catch {
      setAdjBatches([]);
      setAdjBatchId("");
    } finally {
      setAdjBatchesLoading(false);
    }
  };

  // Fetch recent stock adjustments
  const fetchRecentAdjustments = async () => {
    setAdjustmentsLoading(true);
    try {
      const records = await api.inventory.listAdjustments(15);
      setRecentAdjustments(records);
    } catch {
      // silent fallback
    } finally {
      setAdjustmentsLoading(false);
    }
  };

  // Tab switching effect
  useEffect(() => {
    if (activeTab === "batches") {
      fetchBatches();
    } else if (activeTab === "fefo") {
      if (selectedProductId) {
        fetchFEFO(selectedProductId);
      }
    } else if (activeTab === "low_stock") {
      fetchLowStockAlerts();
    } else if (activeTab === "expiry_risk") {
      fetchExpiryAlerts(expiryDaysThreshold);
    } else if (activeTab === "adjustments") {
      fetchRecentAdjustments();
      if (adjProductId) {
        fetchBatchesForAdjProduct(adjProductId);
      }
    }
  }, [activeTab]);

  // Re-fetch batches when page or low stock toggle changes
  useEffect(() => {
    if (activeTab === "batches") {
      fetchBatches();
    }
  }, [batchPage, batchLowStockOnly]);

  // Re-fetch FEFO when selected product changes in FEFO tab
  useEffect(() => {
    if (activeTab === "fefo" && selectedProductId) {
      fetchFEFO(selectedProductId);
    }
  }, [selectedProductId, activeTab]);

  // Filtered products for FEFO selector
  const filteredFefoProducts = useMemo(() => {
    const q = fefoSearch.toLowerCase().trim();
    if (!q) return products;
    return products.filter(
      (p) =>
        p.name.toLowerCase().includes(q) ||
        p.code.toLowerCase().includes(q) ||
        (p.barcode && p.barcode.toLowerCase().includes(q))
    );
  }, [products, fefoSearch]);

  // Filtered products for Adjustment selector
  const filteredAdjProducts = useMemo(() => {
    const q = adjSearch.toLowerCase().trim();
    if (!q) return products;
    return products.filter(
      (p) =>
        p.name.toLowerCase().includes(q) ||
        p.code.toLowerCase().includes(q) ||
        (p.barcode && p.barcode.toLowerCase().includes(q))
    );
  }, [products, adjSearch]);

  // Auto-synchronize FEFO selection when search filters change
  useEffect(() => {
    if (filteredFefoProducts.length > 0) {
      const exists = filteredFefoProducts.some((p) => p.id === selectedProductId);
      if (!exists) {
        setSelectedProductId(filteredFefoProducts[0].id);
      }
    } else if (selectedProductId !== "") {
      setSelectedProductId("");
    }
  }, [filteredFefoProducts, selectedProductId]);

  // Auto-synchronize Adjustment product selection when search filters change
  useEffect(() => {
    if (filteredAdjProducts.length > 0) {
      const exists = filteredAdjProducts.some((p) => p.id === adjProductId);
      if (!exists) {
        setAdjProductId(filteredAdjProducts[0].id);
      }
    } else if (adjProductId !== "") {
      setAdjProductId("");
    }
  }, [filteredAdjProducts, adjProductId]);

  // When adjProductId changes in adjustment tab, fetch its actual batches
  useEffect(() => {
    if (activeTab === "adjustments" && adjProductId) {
      fetchBatchesForAdjProduct(adjProductId);
    }
  }, [adjProductId]);

  // Re-fetch expiry alerts when days threshold changes
  useEffect(() => {
    if (activeTab === "expiry_risk") {
      fetchExpiryAlerts(expiryDaysThreshold);
    }
  }, [expiryDaysThreshold]);

  const handleBatchSearchSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setBatchPage(1);
    fetchBatches(batchSearch, 1);
  };

  const handleAdjustmentSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setAdjError(null);
    setAdjSuccessMsg(null);

    const qty = parseInt(adjNewQuantity, 10);
    if (isNaN(qty) || qty < 0) {
      setAdjError("New quantity must be a non-negative integer.");
      return;
    }

    if (!adjProductId || !adjBatchId) {
      setAdjError("Please select both a valid product and a batch.");
      return;
    }

    setAdjSubmitting(true);
    try {
      const res = await api.inventory.recordAdjustment({
        product_id: adjProductId,
        batch_id: adjBatchId,
        new_quantity: qty,
        reason: adjReason,
        notes: adjNotes.trim() || null,
      });

      setAdjSuccessMsg(
        `Adjustment confirmed: Previous: ${res.previous_quantity}, New: ${res.new_quantity} (Delta: ${res.adjustment_quantity >= 0 ? "+" : ""}${res.adjustment_quantity}). Movement audit log appended.`
      );
      setAdjNewQuantity("");
      setAdjNotes("");
      loadProducts();
      fetchBatches();
      fetchBatchesForAdjProduct(adjProductId);
      fetchRecentAdjustments();
    } catch (err: unknown) {
      if (err instanceof ApiError) {
        setAdjError(err.message);
      } else {
        setAdjError("Failed to record stock adjustment.");
      }
    } finally {
      setAdjSubmitting(false);
    }
  };

  // Selected batch for adjustment preview
  const selectedAdjBatch = adjBatches.find((b) => b.id === adjBatchId);



  // Filtered Low Stock Alerts
  const filteredLowStock = lowStockAlerts.filter((item) => {
    const matchesSearch =
      !lowStockSearch.trim() ||
      item.product_name.toLowerCase().includes(lowStockSearch.toLowerCase()) ||
      item.product_code.toLowerCase().includes(lowStockSearch.toLowerCase());
    const matchesCategory =
      lowStockCategory === "ALL" || (item.category && item.category === lowStockCategory);
    return matchesSearch && matchesCategory;
  });

  const lowStockTotalPages = Math.ceil(filteredLowStock.length / lowStockLimit) || 1;
  const paginatedLowStock = filteredLowStock.slice(
    (lowStockPage - 1) * lowStockLimit,
    lowStockPage * lowStockLimit
  );

  // Filtered Expiry Risk Alerts
  const filteredExpiryAlerts = expiryAlerts.filter(
    (item) =>
      !expirySearch.trim() ||
      item.product_name.toLowerCase().includes(expirySearch.toLowerCase()) ||
      (item.product_code && item.product_code.toLowerCase().includes(expirySearch.toLowerCase())) ||
      item.batch_number.toLowerCase().includes(expirySearch.toLowerCase())
  );

  const batchTotalPages = Math.ceil(batchTotal / batchLimit) || 1;

  return (
    <div className="space-y-6">
      {/* Title */}
      <div>
        <h1 className="text-2xl font-bold text-slate-900 tracking-tight">Inventory &amp; Batch Management</h1>
        <p className="text-sm text-slate-600 mt-0.5">
          Real-time batch tracking, First Expiry First Out (FEFO) dispensing, threshold alerts, and physical count audit.
        </p>
      </div>

      {/* Tabs Header Navigation */}
      <div className="flex border-b border-slate-200 gap-1 overflow-x-auto text-xs">
        <button
          type="button"
          onClick={() => setActiveTab("batches")}
          className={`py-2 px-3 border-b-2 font-semibold transition-colors duration-75 cursor-pointer whitespace-nowrap ${
            activeTab === "batches"
              ? "border-emerald-600 text-emerald-700 bg-white"
              : "border-transparent text-slate-600 hover:text-slate-900 hover:border-slate-300"
          }`}
        >
          All Active Batches {batchTotal > 0 && `(${batchTotal})`}
        </button>

        <button
          type="button"
          onClick={() => setActiveTab("fefo")}
          className={`py-2 px-3 border-b-2 font-semibold transition-colors duration-75 cursor-pointer whitespace-nowrap ${
            activeTab === "fefo"
              ? "border-emerald-600 text-emerald-700 bg-white"
              : "border-transparent text-slate-600 hover:text-slate-900 hover:border-slate-300"
          }`}
        >
          FEFO Dispensing Engine
        </button>

        <button
          type="button"
          onClick={() => setActiveTab("low_stock")}
          className={`py-2 px-3 border-b-2 font-semibold transition-colors duration-75 cursor-pointer whitespace-nowrap ${
            activeTab === "low_stock"
              ? "border-emerald-600 text-emerald-700 bg-white"
              : "border-transparent text-slate-600 hover:text-slate-900 hover:border-slate-300"
          }`}
        >
          Low Stock Alerts {lowStockAlerts.length > 0 && `(${lowStockAlerts.length})`}
        </button>

        <button
          type="button"
          onClick={() => setActiveTab("expiry_risk")}
          className={`py-2 px-3 border-b-2 font-semibold transition-colors duration-75 cursor-pointer whitespace-nowrap ${
            activeTab === "expiry_risk"
              ? "border-emerald-600 text-emerald-700 bg-white"
              : "border-transparent text-slate-600 hover:text-slate-900 hover:border-slate-300"
          }`}
        >
          Expiry Risk Alerts {expiryAlerts.length > 0 && `(${expiryAlerts.length})`}
        </button>

        <button
          type="button"
          onClick={() => setActiveTab("adjustments")}
          className={`py-2 px-3 border-b-2 font-semibold transition-colors duration-75 cursor-pointer whitespace-nowrap ${
            activeTab === "adjustments"
              ? "border-emerald-600 text-emerald-700 bg-white"
              : "border-transparent text-slate-600 hover:text-slate-900 hover:border-slate-300"
          }`}
        >
          Physical Stock Adjustment
        </button>
      </div>

      {/* ========================================================================= */}
      {/* TAB 1: ALL ACTIVE BATCHES (Searchable, Paginated, Full Metrics)           */}
      {/* ========================================================================= */}
      {activeTab === "batches" && (
        <div className="bg-white border border-slate-200 rounded shadow-sm overflow-hidden space-y-4">
          {batchesError && (
            <div className="p-4 bg-rose-50 border-b border-rose-200 text-rose-800 text-xs">
              <span className="font-semibold">Error: </span> {batchesError}
            </div>
          )}

          {/* Search & Filter Toolbar */}
          <div className="p-4 border-b border-slate-200 flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-3">
            <form onSubmit={handleBatchSearchSubmit} className="flex gap-2 flex-1 max-w-md">
              <input
                type="text"
                value={batchSearch}
                onChange={(e) => setBatchSearch(e.target.value)}
                placeholder="Search batch number, medicine name, or SKU code..."
                className="flex-1 px-3 py-1.5 border border-slate-300 rounded text-xs text-slate-900 placeholder:text-slate-400 focus:outline-none focus:ring-1 focus:ring-emerald-500"
              />
              <button
                type="submit"
                className="px-3 py-1.5 bg-emerald-600 hover:bg-emerald-700 text-white rounded text-xs font-semibold cursor-pointer transition-colors"
              >
                Search
              </button>
              {batchSearch && (
                <button
                  type="button"
                  onClick={() => {
                    setBatchSearch("");
                    setBatchPage(1);
                    fetchBatches("", 1);
                  }}
                  className="px-2.5 py-1.5 border border-slate-300 text-slate-600 hover:text-slate-900 rounded text-xs cursor-pointer"
                >
                  Clear
                </button>
              )}
            </form>

            <div className="flex items-center gap-3">
              <label className="flex items-center gap-2 text-xs text-slate-700 cursor-pointer">
                <input
                  type="checkbox"
                  checked={batchLowStockOnly}
                  onChange={(e) => {
                    setBatchLowStockOnly(e.target.checked);
                    setBatchPage(1);
                  }}
                  className="rounded border-slate-300 text-emerald-600 focus:ring-emerald-500 cursor-pointer"
                />
                <span>Low Stock Only (&le; 10 units)</span>
              </label>
              <span className="text-xs text-slate-500 font-medium">
                Total: <strong className="text-slate-900">{batchTotal}</strong> batches
              </span>
            </div>
          </div>

          {/* Batches Table */}
          <div className="overflow-x-auto">
            <table className="w-full text-left text-xs">
              <thead className="bg-slate-50 text-slate-600 border-b border-slate-200 uppercase font-semibold">
                <tr>
                  <th className="py-3 px-4">Batch Number</th>
                  <th className="py-3 px-4">Medicine / Product</th>
                  <th className="py-3 px-4">Expiry Date</th>
                  <th className="py-3 px-4 text-center">Remaining Days</th>
                  <th className="py-3 px-4 text-right">Purchase Cost (NPR)</th>
                  <th className="py-3 px-4 text-center">In-Stock Quantity</th>
                  <th className="py-3 px-4 text-center">Status</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-100">
                {batchesLoading ? (
                  <tr>
                    <td colSpan={7} className="py-8 text-center text-slate-500">
                      Loading inventory batches from database...
                    </td>
                  </tr>
                ) : batches.length === 0 ? (
                  <tr>
                    <td colSpan={7} className="py-8 text-center text-slate-500">
                      No active batches found matching your search query.
                    </td>
                  </tr>
                ) : (
                  batches.map((b) => {
                    const days = b.days_until_expiry ?? 0;
                    return (
                      <tr key={b.id} className="hover:bg-slate-50">
                        <td className="py-3 px-4 font-mono font-bold text-slate-800">
                          {b.batch_number}
                        </td>
                        <td className="py-3 px-4">
                          <div className="font-medium text-slate-900">{b.product_name}</div>
                          {b.product_code && (
                            <span className="font-mono text-[11px] text-slate-500">{b.product_code}</span>
                          )}
                        </td>
                        <td className="py-3 px-4 text-slate-700 font-medium">
                          {formatDate(b.expiry_date)}
                        </td>
                        <td className="py-3 px-4 text-center">
                          <span
                            className={`px-2 py-0.5 rounded text-[10px] font-bold ${
                              days <= 30
                                ? "bg-rose-100 text-rose-800"
                                : days <= 90
                                ? "bg-amber-100 text-amber-800"
                                : "bg-slate-100 text-slate-700"
                            }`}
                          >
                            {days <= 0 ? "Expired" : `${days} days`}
                          </span>
                        </td>
                        <td className="py-3 px-4 text-right font-medium text-slate-800">
                          {formatNPR(b.purchase_cost)}
                        </td>
                        <td className="py-3 px-4 text-center font-bold text-slate-900">
                          {b.quantity} <span className="text-xs font-normal text-slate-500">{b.unit || "unit"}s</span>
                        </td>
                        <td className="py-3 px-4 text-center">
                          {b.quantity <= 5 ? (
                            <span className="px-2 py-0.5 rounded text-[11px] font-semibold bg-amber-100 text-amber-800">
                              Low Stock
                            </span>
                          ) : (
                            <span className="px-2 py-0.5 rounded text-[11px] font-medium bg-emerald-100 text-emerald-800">
                              Active
                            </span>
                          )}
                        </td>
                      </tr>
                    );
                  })
                )}
              </tbody>
            </table>
          </div>

          {/* Pagination Controls */}
          {batchTotalPages > 1 && (
            <div className="p-4 border-t border-slate-200 flex items-center justify-between text-xs text-slate-600">
              <div>
                Showing page <strong className="text-slate-900">{batchPage}</strong> of{" "}
                <strong className="text-slate-900">{batchTotalPages}</strong> ({batchTotal} total batches)
              </div>
              <div className="flex gap-2">
                <button
                  type="button"
                  disabled={batchPage <= 1}
                  onClick={() => setBatchPage((p) => Math.max(1, p - 1))}
                  className="px-3 py-1 border border-slate-300 rounded hover:bg-slate-50 disabled:opacity-50 cursor-pointer disabled:cursor-not-allowed"
                >
                  Previous
                </button>
                <button
                  type="button"
                  disabled={batchPage >= batchTotalPages}
                  onClick={() => setBatchPage((p) => Math.min(batchTotalPages, p + 1))}
                  className="px-3 py-1 border border-slate-300 rounded hover:bg-slate-50 disabled:opacity-50 cursor-pointer disabled:cursor-not-allowed"
                >
                  Next
                </button>
              </div>
            </div>
          )}
        </div>
      )}

      {/* ========================================================================= */}
      {/* TAB 2: FEFO DISPENSING ENGINE (Searchable Product Context + Dispensing)    */}
      {/* ========================================================================= */}
      {activeTab === "fefo" && (
        <div className="bg-white border border-slate-200 rounded p-6 shadow-sm space-y-6">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {/* Search and Select Product */}
            <div>
              <div className="flex items-center justify-between mb-1">
                <label htmlFor="fefoSearch" className="block text-xs font-semibold text-slate-700">
                  Search &amp; Select Product for FEFO Dispensing:
                </label>
                {products.length > 0 && (
                  <span className="text-[11px] text-slate-500 font-medium">
                    {filteredFefoProducts.length} of {products.length} medicines
                  </span>
                )}
              </div>
              <input
                id="fefoSearch"
                type="text"
                value={fefoSearch}
                onChange={(e) => setFefoSearch(e.target.value)}
                placeholder="Filter product list by name or SKU..."
                className="w-full mb-2 px-3 py-1.5 border border-slate-300 rounded text-xs text-slate-900 placeholder:text-slate-400 focus:outline-none focus:ring-1 focus:ring-emerald-500"
              />
              <select
                id="fefoProd"
                value={selectedProductId}
                onChange={(e) => {
                  setSelectedProductId(e.target.value);
                }}
                disabled={productsLoading || filteredFefoProducts.length === 0}
                className="w-full px-3 py-2 border border-slate-300 rounded text-xs text-slate-800 bg-white focus:outline-none focus:ring-1 focus:ring-emerald-500 disabled:bg-slate-100 disabled:text-slate-400"
              >
                {filteredFefoProducts.length === 0 ? (
                  <option value="" disabled>
                    {productsLoading ? "Loading medicine catalog..." : "No matching medicines found"}
                  </option>
                ) : (
                  filteredFefoProducts.map((p) => (
                    <option key={p.id} value={p.id}>
                      {p.name} ({p.code}) — {p.category}
                    </option>
                  ))
                )}
              </select>
              {productsLoading && (
                <p className="text-[11px] text-slate-400 mt-1">Loading catalog products...</p>
              )}
            </div>

            {/* Product Summary Card */}
            {fefoData && (
              <div className="p-3.5 bg-slate-50 border border-slate-200 rounded text-xs space-y-1.5">
                <div className="flex items-center justify-between">
                  <span className="font-bold text-slate-900 text-sm">{fefoData.product_name}</span>
                  <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-100 text-emerald-800">
                    {fefoData.category || "Medicine"}
                  </span>
                </div>
                <div className="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-1 text-slate-600">
                  <div>
                    <span className="text-[10px] text-slate-400 block uppercase">SKU Code</span>
                    <strong className="font-mono text-slate-800">{fefoData.product_code || "—"}</strong>
                  </div>
                  <div>
                    <span className="text-[10px] text-slate-400 block uppercase">Total Stock</span>
                    <strong className="text-emerald-700">{fefoData.total_stock} {fefoData.unit || "unit"}s</strong>
                  </div>
                  <div>
                    <span className="text-[10px] text-slate-400 block uppercase">Reorder Level</span>
                    <strong className="text-slate-800">{fefoData.reorder_level} {fefoData.unit || "unit"}s</strong>
                  </div>
                  <div>
                    <span className="text-[10px] text-slate-400 block uppercase">Unit MRP</span>
                    <strong className="text-slate-900">{formatNPR(fefoData.mrp)}</strong>
                  </div>
                </div>
              </div>
            )}
          </div>

          {/* FEFO Dispensing Priority Table */}
          <div className="border border-slate-200 rounded overflow-hidden">
            <div className="p-3 bg-slate-50 border-b border-slate-200 flex items-center justify-between">
              <div>
                <span className="text-xs font-bold text-slate-900">
                  {fefoData ? fefoData.product_name : "Product Batches"}
                </span>
                <span className="text-[11px] text-slate-500 ml-2">
                  (Strict First Expiry, First Out Sequence — Dispense in numbered order)
                </span>
              </div>
              <span className="text-[11px] font-semibold text-emerald-800 bg-emerald-100 px-2 py-0.5 rounded">
                Verified FEFO Sequence
              </span>
            </div>

            <div className="overflow-x-auto">
              <table className="w-full text-left text-xs">
                <thead className="bg-white text-slate-600 border-b border-slate-200 uppercase font-semibold">
                  <tr>
                    <th className="py-2.5 px-4 text-center">Priority</th>
                    <th className="py-2.5 px-4">Batch Number</th>
                    <th className="py-2.5 px-4">Expiry Date</th>
                    <th className="py-2.5 px-4 text-center">Days to Expiry</th>
                    <th className="py-2.5 px-4 text-center">Available Stock</th>
                    <th className="py-2.5 px-4 text-right">Purchase Cost</th>
                    <th className="py-2.5 px-4 text-center">Action</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-100">
                  {fefoLoading ? (
                    <tr>
                      <td colSpan={7} className="py-6 text-center text-slate-500">
                        Calculating FEFO dispensing sequence from database...
                      </td>
                    </tr>
                  ) : !selectedProductId ? (
                    <tr>
                      <td colSpan={7} className="py-6 text-center text-slate-500">
                        {filteredFefoProducts.length === 0
                          ? `No medicines match "${fefoSearch}". Try a different name or SKU.`
                          : "Please select a medicine from the dropdown above to view the FEFO dispensing queue."}
                      </td>
                    </tr>
                  ) : !fefoData || fefoData.fefo_batches.length === 0 ? (
                    <tr>
                      <td colSpan={7} className="py-6 text-center text-slate-500">
                        No in-stock active batches found for this product.
                      </td>
                    </tr>
                  ) : (
                    fefoData.fefo_batches.map((batch, index) => {
                      const days = batch.days_until_expiry ?? 0;
                      return (
                        <tr
                          key={batch.batch_id}
                          className={index === 0 ? "bg-emerald-50/60 font-semibold" : "hover:bg-slate-50"}
                        >
                          <td className="py-3 px-4 text-center">
                            <span
                              className={`inline-flex items-center justify-center w-6 h-6 rounded-full text-[11px] font-bold ${
                                index === 0 ? "bg-emerald-600 text-white" : "bg-slate-200 text-slate-700"
                              }`}
                            >
                              #{index + 1}
                            </span>
                          </td>
                          <td className="py-3 px-4 font-mono font-bold text-slate-800">
                            {batch.batch_number}
                          </td>
                          <td className="py-3 px-4 text-slate-700">
                            {formatDate(batch.expiry_date)}
                          </td>
                          <td className="py-3 px-4 text-center">
                            <span
                              className={`px-2 py-0.5 rounded text-[10px] font-bold ${
                                days <= 30
                                  ? "bg-rose-100 text-rose-800"
                                  : days <= 90
                                  ? "bg-amber-100 text-amber-800"
                                  : "bg-slate-100 text-slate-700"
                              }`}
                            >
                              {days <= 0 ? "Expired" : `${days} days`}
                            </span>
                          </td>
                          <td className="py-3 px-4 text-center font-bold text-slate-900">
                            {batch.available_quantity}{" "}
                            <span className="text-xs font-normal text-slate-500">{batch.unit || "unit"}s</span>
                          </td>
                          <td className="py-3 px-4 text-right font-medium text-slate-800">
                            {formatNPR(batch.purchase_cost)}
                          </td>
                          <td className="py-3 px-4 text-center">
                            {index === 0 ? (
                              <span className="text-[11px] font-bold text-emerald-700 bg-emerald-100 px-2 py-0.5 rounded">
                                Dispense First
                              </span>
                            ) : (
                              <span className="text-[10px] text-slate-500">Lot #{index + 1} in Queue</span>
                            )}
                          </td>
                        </tr>
                      );
                    })
                  )}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      )}

      {/* ========================================================================= */}
      {/* TAB 3: LOW STOCK ALERTS (Sorted by Shortage, Searchable, Paginated)       */}
      {/* ========================================================================= */}
      {activeTab === "low_stock" && (
        <div className="bg-white border border-slate-200 rounded shadow-sm overflow-hidden space-y-4">
          <div className="p-4 border-b border-slate-200 flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-3">
            <div>
              <h2 className="text-sm font-bold text-slate-900">
                Products at or Below Reorder Threshold ({lowStockAlerts.length})
              </h2>
              <p className="text-xs text-slate-500">
                Sorted strictly by stock urgency (zero-stock and critical deficits first).
              </p>
            </div>

            <div className="flex flex-wrap items-center gap-2">
              <input
                type="text"
                value={lowStockSearch}
                onChange={(e) => {
                  setLowStockSearch(e.target.value);
                  setLowStockPage(1);
                }}
                placeholder="Search medicine or SKU..."
                className="px-3 py-1.5 border border-slate-300 rounded text-xs text-slate-900 placeholder:text-slate-400 focus:outline-none focus:ring-1 focus:ring-emerald-500"
              />
              <select
                value={lowStockCategory}
                onChange={(e) => {
                  setLowStockCategory(e.target.value);
                  setLowStockPage(1);
                }}
                className="px-2.5 py-1.5 border border-slate-300 rounded text-xs text-slate-800 bg-white"
              >
                <option value="ALL">All Categories</option>
                <option value="Medicine">Medicine</option>
                <option value="Surgical">Surgical</option>
                <option value="Cosmetic">Cosmetic</option>
                <option value="Baby">Baby</option>
                <option value="Food">Food</option>
              </select>
            </div>
          </div>

          <div className="overflow-x-auto">
            <table className="w-full text-left text-xs">
              <thead className="bg-slate-50 text-slate-600 border-b border-slate-200 uppercase font-semibold">
                <tr>
                  <th className="py-3 px-4">Product Code</th>
                  <th className="py-3 px-4">Medicine Name</th>
                  <th className="py-3 px-4">Category</th>
                  <th className="py-3 px-4 text-center">Current Total Stock</th>
                  <th className="py-3 px-4 text-center">Reorder Level</th>
                  <th className="py-3 px-4 text-center">Deficit / Shortfall</th>
                  <th className="py-3 px-4 text-center">Urgency</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-100">
                {lowStockLoading ? (
                  <tr>
                    <td colSpan={7} className="py-6 text-center text-slate-500">
                      Checking stock safety limits against database...
                    </td>
                  </tr>
                ) : paginatedLowStock.length === 0 ? (
                  <tr>
                    <td colSpan={7} className="py-6 text-center text-slate-500">
                      No products matching the low-stock criteria found.
                    </td>
                  </tr>
                ) : (
                  paginatedLowStock.map((item) => (
                    <tr key={item.product_id} className="hover:bg-slate-50">
                      <td className="py-3 px-4 font-mono font-medium text-slate-700">
                        {item.product_code}
                      </td>
                      <td className="py-3 px-4 font-semibold text-slate-900">
                        {item.product_name}
                      </td>
                      <td className="py-3 px-4 text-slate-600">{item.category || "Medicine"}</td>
                      <td className="py-3 px-4 text-center font-bold text-amber-700">
                        {item.current_stock} {item.unit || "unit"}s
                      </td>
                      <td className="py-3 px-4 text-center text-slate-600">
                        {item.reorder_level} {item.unit || "unit"}s
                      </td>
                      <td className="py-3 px-4 text-center font-bold text-rose-700">
                        +{item.shortfall ?? Math.max(0, item.reorder_level - item.current_stock)}
                      </td>
                      <td className="py-3 px-4 text-center">
                        {item.current_stock === 0 ? (
                          <span className="px-2 py-0.5 rounded text-[11px] font-bold bg-rose-200 text-rose-900">
                            Out of Stock
                          </span>
                        ) : item.current_stock <= 2 ? (
                          <span className="px-2 py-0.5 rounded text-[11px] font-bold bg-rose-100 text-rose-800">
                            Critical (&le; 2)
                          </span>
                        ) : (
                          <span className="px-2 py-0.5 rounded text-[11px] font-semibold bg-amber-100 text-amber-800">
                            Reorder Required
                          </span>
                        )}
                      </td>
                    </tr>
                  ))
                )}
              </tbody>
            </table>
          </div>

          {/* Pagination Controls */}
          {lowStockTotalPages > 1 && (
            <div className="p-4 border-t border-slate-200 flex items-center justify-between text-xs text-slate-600">
              <div>
                Showing page <strong className="text-slate-900">{lowStockPage}</strong> of{" "}
                <strong className="text-slate-900">{lowStockTotalPages}</strong> ({filteredLowStock.length} items)
              </div>
              <div className="flex gap-2">
                <button
                  type="button"
                  disabled={lowStockPage <= 1}
                  onClick={() => setLowStockPage((p) => Math.max(1, p - 1))}
                  className="px-3 py-1 border border-slate-300 rounded hover:bg-slate-50 disabled:opacity-50 cursor-pointer disabled:cursor-not-allowed"
                >
                  Previous
                </button>
                <button
                  type="button"
                  disabled={lowStockPage >= lowStockTotalPages}
                  onClick={() => setLowStockPage((p) => Math.min(lowStockTotalPages, p + 1))}
                  className="px-3 py-1 border border-slate-300 rounded hover:bg-slate-50 disabled:opacity-50 cursor-pointer disabled:cursor-not-allowed"
                >
                  Next
                </button>
              </div>
            </div>
          )}
        </div>
      )}

      {/* ========================================================================= */}
      {/* TAB 4: EXPIRY RISK ALERTS (Configurable Thresholds 30/60/90/180/365 Days)  */}
      {/* ========================================================================= */}
      {activeTab === "expiry_risk" && (
        <div className="bg-white border border-slate-200 rounded shadow-sm overflow-hidden space-y-4">
          <div className="p-4 border-b border-slate-200 flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-3">
            <div>
              <h2 className="text-sm font-bold text-slate-900">
                Batches Expiring Within {expiryDaysThreshold} Days ({expiryAlerts.length})
              </h2>
              <p className="text-xs text-slate-500">
                Audit lots approaching expiration to prioritize FEFO dispensing or process supplier returns.
              </p>
            </div>

            {/* Threshold Selector Buttons */}
            <div className="flex items-center gap-1.5 bg-slate-100 p-1 rounded">
              {[30, 60, 90, 180, 365].map((days) => (
                <button
                  key={days}
                  type="button"
                  onClick={() => setExpiryDaysThreshold(days)}
                  className={`px-2.5 py-1 text-xs font-semibold rounded transition-colors cursor-pointer ${
                    expiryDaysThreshold === days
                      ? "bg-white text-emerald-800 shadow-xs"
                      : "text-slate-600 hover:text-slate-900"
                  }`}
                >
                  {days}d
                </button>
              ))}
            </div>
          </div>

          {/* Search Box */}
          <div className="px-4">
            <input
              type="text"
              value={expirySearch}
              onChange={(e) => setExpirySearch(e.target.value)}
              placeholder="Filter expiring batches by medicine, SKU, or batch lot..."
              className="w-full max-w-md px-3 py-1.5 border border-slate-300 rounded text-xs text-slate-900 placeholder:text-slate-400 focus:outline-none focus:ring-1 focus:ring-emerald-500"
            />
          </div>

          <div className="overflow-x-auto">
            <table className="w-full text-left text-xs">
              <thead className="bg-slate-50 text-slate-600 border-b border-slate-200 uppercase font-semibold">
                <tr>
                  <th className="py-3 px-4">Batch Number</th>
                  <th className="py-3 px-4">Medicine Name</th>
                  <th className="py-3 px-4">Product SKU</th>
                  <th className="py-3 px-4">Expiry Date</th>
                  <th className="py-3 px-4 text-center">Stock at Risk</th>
                  <th className="py-3 px-4 text-center">Days Remaining</th>
                  <th className="py-3 px-4 text-center">Risk Level</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-100">
                {expiryLoading ? (
                  <tr>
                    <td colSpan={7} className="py-6 text-center text-slate-500">
                      Auditing batch expiry schedules from database...
                    </td>
                  </tr>
                ) : filteredExpiryAlerts.length === 0 ? (
                  <tr>
                    <td colSpan={7} className="py-6 text-center text-slate-500">
                      No batches are expiring within the next {expiryDaysThreshold} days.
                    </td>
                  </tr>
                ) : (
                  filteredExpiryAlerts.map((b) => (
                    <tr key={b.batch_id} className="hover:bg-slate-50">
                      <td className="py-3 px-4 font-mono font-bold text-slate-800">
                        {b.batch_number}
                      </td>
                      <td className="py-3 px-4 font-semibold text-slate-900">
                        {b.product_name}
                      </td>
                      <td className="py-3 px-4 font-mono text-slate-600">
                        {b.product_code || "—"}
                      </td>
                      <td className="py-3 px-4 text-slate-700 font-medium">
                        {formatDate(b.expiry_date)}
                      </td>
                      <td className="py-3 px-4 text-center font-bold text-slate-900">
                        {b.quantity} {b.unit || "unit"}s
                      </td>                      <td className="py-3 px-4 text-center">
                        <span
                          className={`px-2.5 py-0.5 rounded text-[11px] font-bold ${
                            b.days_until_expiry < 0
                              ? "bg-red-100 text-red-900 border border-red-300"
                              : b.days_until_expiry === 0
                              ? "bg-rose-200 text-rose-950 font-extrabold"
                              : b.days_until_expiry <= 30
                              ? "bg-rose-100 text-rose-800"
                              : b.days_until_expiry <= 60
                              ? "bg-amber-100 text-amber-800"
                              : "bg-slate-100 text-slate-800"
                          }`}
                        >
                          {b.days_until_expiry < 0
                            ? "Expired"
                            : b.days_until_expiry === 0
                            ? "Today"
                            : `${b.days_until_expiry} days`}
                        </span>
                      </td>
                      <td className="py-3 px-4 text-center">
                        {b.days_until_expiry < 0 ? (
                          <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-red-600 text-white">
                            EXPIRED
                          </span>
                        ) : b.days_until_expiry === 0 ? (
                          <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-rose-200 text-rose-950">
                            Expiring Today
                          </span>
                        ) : b.days_until_expiry <= 30 ? (
                          <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-rose-200 text-rose-900">
                            Critical Risk
                          </span>
                        ) : b.days_until_expiry <= 60 ? (
                          <span className="px-2 py-0.5 rounded text-[10px] font-semibold bg-amber-100 text-amber-800">
                            High Priority
                          </span>
                        ) : (
                          <span className="px-2 py-0.5 rounded text-[10px] font-medium bg-slate-100 text-slate-700">
                            Moderate
                          </span>
                        )}
                      </td>
                    </tr>
                  ))
                )}
              </tbody>
            </table>
          </div>
        </div>
      )}

      {/* ========================================================================= */}
      {/* TAB 5: PHYSICAL STOCK ADJUSTMENT (Product Batch API Lookup + Audit Trail) */}
      {/* ========================================================================= */}
      {activeTab === "adjustments" && (
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Form */}
          <div className="lg:col-span-1 bg-white border border-slate-200 rounded p-6 shadow-sm space-y-4">
            <div className="border-b border-slate-200 pb-3">
              <h2 className="text-base font-bold text-slate-900">Record Physical Verification</h2>
              <p className="text-xs text-slate-500 mt-0.5">
                Updates in-stock lot quantity and appends an immutable movement audit log.
              </p>
            </div>

            {adjSuccessMsg && (
              <div className="p-3 bg-emerald-50 border border-emerald-200 text-emerald-800 text-xs rounded">
                <span className="font-semibold">Success: </span>
                {adjSuccessMsg}
              </div>
            )}

            {adjError && (
              <div className="p-3 bg-rose-50 border border-rose-200 text-rose-800 text-xs rounded">
                <span className="font-semibold">Adjustment Error: </span>
                {adjError}
              </div>
            )}

            <form onSubmit={handleAdjustmentSubmit} className="space-y-4 text-xs">
              {/* Product Search & Dropdown */}
              <div>
                <label htmlFor="adjSearch" className="block font-medium text-slate-700 mb-1">
                  Target Product <span className="text-rose-500">*</span>
                </label>
                <input
                  id="adjSearch"
                  type="text"
                  value={adjSearch}
                  onChange={(e) => setAdjSearch(e.target.value)}
                  placeholder="Filter product by name or SKU..."
                  className="w-full mb-1.5 px-3 py-1.5 border border-slate-300 rounded text-slate-900 placeholder:text-slate-400 focus:outline-none focus:ring-1 focus:ring-emerald-500"
                />
                <select
                  id="adjProduct"
                  value={adjProductId}
                  onChange={(e) => {
                    setAdjProductId(e.target.value);
                  }}
                  className="w-full px-3 py-1.5 border border-slate-300 rounded text-slate-900 bg-white focus:outline-none focus:ring-1 focus:ring-emerald-500"
                >
                  {filteredAdjProducts.map((p) => (
                    <option key={p.id} value={p.id}>
                      {p.name} ({p.code})
                    </option>
                  ))}
                </select>
              </div>

              {/* Batch Dropdown */}
              <div>
                <label htmlFor="adjBatch" className="block font-medium text-slate-700 mb-1">
                  Target Batch Lot <span className="text-rose-500">*</span>
                </label>
                <select
                  id="adjBatch"
                  required
                  value={adjBatchId}
                  onChange={(e) => setAdjBatchId(e.target.value)}
                  disabled={adjBatchesLoading || adjBatches.length === 0}
                  className="w-full px-3 py-1.5 border border-slate-300 rounded text-slate-900 bg-white focus:outline-none focus:ring-1 focus:ring-emerald-500 disabled:bg-slate-100"
                >
                  {adjBatchesLoading ? (
                    <option value="">Loading batches for product...</option>
                  ) : adjBatches.length === 0 ? (
                    <option value="">No active batches found for this product</option>
                  ) : (
                    adjBatches.map((b) => (
                      <option key={b.id} value={b.id}>
                        {b.batch_number} (Current Stock: {b.quantity}, Exp: {formatDate(b.expiry_date)})
                      </option>
                    ))
                  )}
                </select>
                {selectedAdjBatch && (
                  <div className="mt-2 p-2 bg-slate-50 border border-slate-200 rounded text-[11px] text-slate-600 space-y-0.5">
                    <div>
                      Current Stock: <strong className="text-slate-900">{selectedAdjBatch.quantity} {selectedAdjBatch.unit || "unit"}s</strong>
                    </div>
                    <div>
                      Locked Cost: <strong className="text-slate-900">{formatNPR(selectedAdjBatch.purchase_cost)}</strong> | Expiry: <strong className="text-slate-900">{formatDate(selectedAdjBatch.expiry_date)}</strong>
                    </div>
                  </div>
                )}
              </div>

              <div className="grid grid-cols-2 gap-3">
                <div>
                  <label htmlFor="newQty" className="block font-medium text-slate-700 mb-1">
                    New Physical Count <span className="text-rose-500">*</span>
                  </label>
                  <input
                    id="newQty"
                    type="number"
                    min="0"
                    required
                    value={adjNewQuantity}
                    onChange={(e) => setAdjNewQuantity(e.target.value)}
                    placeholder="e.g. 10"
                    className="w-full px-3 py-1.5 border border-slate-300 rounded text-slate-900 focus:outline-none focus:ring-1 focus:ring-emerald-500"
                  />
                  {selectedAdjBatch && adjNewQuantity !== "" && !isNaN(parseInt(adjNewQuantity, 10)) && (
                    <span className="text-[10px] font-semibold mt-1 block text-slate-600">
                      Delta:{" "}
                      <strong
                        className={
                          parseInt(adjNewQuantity, 10) - selectedAdjBatch.quantity >= 0
                            ? "text-emerald-700"
                            : "text-rose-700"
                        }
                      >
                        {parseInt(adjNewQuantity, 10) - selectedAdjBatch.quantity >= 0 ? "+" : ""}
                        {parseInt(adjNewQuantity, 10) - selectedAdjBatch.quantity} units
                      </strong>
                    </span>
                  )}
                </div>

                <div>
                  <label htmlFor="reason" className="block font-medium text-slate-700 mb-1">
                    Reason Code <span className="text-rose-500">*</span>
                  </label>
                  <select
                    id="reason"
                    value={adjReason}
                    onChange={(e) => setAdjReason(e.target.value as StockAdjustmentReason)}
                    className="w-full px-3 py-1.5 border border-slate-300 rounded text-slate-900 bg-white focus:outline-none focus:ring-1 focus:ring-emerald-500"
                  >
                    <option value="PHYSICAL_COUNT">PHYSICAL_COUNT (Regular Count)</option>
                    <option value="DAMAGED">DAMAGED (Damaged Stock)</option>
                    <option value="EXPIRED">EXPIRED (Expired Removal)</option>
                    <option value="CORRECTION">CORRECTION (Entry Correction)</option>
                  </select>
                </div>
              </div>

              <div>
                <label htmlFor="notes" className="block font-medium text-slate-700 mb-1">
                  Audit Notes (Optional)
                </label>
                <textarea
                  id="notes"
                  rows={2}
                  value={adjNotes}
                  onChange={(e) => setAdjNotes(e.target.value)}
                  placeholder="e.g. Verified during weekly physical count by supervisor"
                  className="w-full px-3 py-1.5 border border-slate-300 rounded text-slate-900 focus:outline-none focus:ring-1 focus:ring-emerald-500"
                />
              </div>

              <div className="pt-3 border-t border-slate-200">
                <button
                  type="submit"
                  disabled={adjSubmitting || !adjBatchId}
                  className="w-full px-4 py-2 bg-emerald-600 hover:bg-emerald-700 text-white rounded font-medium disabled:opacity-50 cursor-pointer transition-colors duration-75"
                >
                  {adjSubmitting ? "Submitting Server Transaction..." : "Confirm & Commit Stock Adjustment"}
                </button>
              </div>
            </form>
          </div>

          {/* Recent Adjustments & Audit Trail Table */}
          <div className="lg:col-span-2 bg-white border border-slate-200 rounded p-6 shadow-sm space-y-4">
            <div className="border-b border-slate-200 pb-3 flex items-center justify-between">
              <div>
                <h2 className="text-sm font-bold text-slate-900">Recent Stock Adjustments &amp; Audit Trail</h2>
                <p className="text-xs text-slate-500 mt-0.5">
                  Immutable record of physical count corrections and stock delta logs.
                </p>
              </div>
              <button
                type="button"
                onClick={fetchRecentAdjustments}
                className="px-2.5 py-1 text-xs border border-slate-200 rounded text-slate-600 hover:text-slate-900 cursor-pointer"
              >
                Refresh
              </button>
            </div>

            <div className="overflow-x-auto">
              <table className="w-full text-left text-xs">
                <thead className="bg-slate-50 text-slate-600 border-b border-slate-200 uppercase font-semibold">
                  <tr>
                    <th className="py-2.5 px-3">Date &amp; Time</th>
                    <th className="py-2.5 px-3">Medicine (SKU)</th>
                    <th className="py-2.5 px-3 font-mono">Batch Lot</th>
                    <th className="py-2.5 px-3 text-center">Prev &rarr; New</th>
                    <th className="py-2.5 px-3 text-center">Delta</th>
                    <th className="py-2.5 px-3">Reason</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-100">
                  {adjustmentsLoading ? (
                    <tr>
                      <td colSpan={6} className="py-6 text-center text-slate-500">
                        Loading audit log history...
                      </td>
                    </tr>
                  ) : recentAdjustments.length === 0 ? (
                    <tr>
                      <td colSpan={6} className="py-6 text-center text-slate-500">
                        No physical stock adjustments recorded yet.
                      </td>
                    </tr>
                  ) : (
                    recentAdjustments.map((rec) => (
                      <tr key={rec.id} className="hover:bg-slate-50">
                        <td className="py-2.5 px-3 text-slate-600 whitespace-nowrap">
                          {formatDate(rec.adjusted_at)}
                        </td>
                        <td className="py-2.5 px-3">
                          <div className="font-semibold text-slate-900">{rec.product_name}</div>
                          <span className="font-mono text-[10px] text-slate-500">{rec.product_code}</span>
                        </td>
                        <td className="py-2.5 px-3 font-mono font-bold text-slate-800">
                          {rec.batch_number}
                        </td>
                        <td className="py-2.5 px-3 text-center text-slate-700">
                          {rec.previous_quantity} &rarr; <strong className="text-slate-900">{rec.new_quantity}</strong>
                        </td>
                        <td className="py-2.5 px-3 text-center">
                          <span
                            className={`font-bold px-1.5 py-0.5 rounded text-[10px] ${
                              rec.adjustment_quantity >= 0
                                ? "bg-emerald-100 text-emerald-800"
                                : "bg-rose-100 text-rose-800"
                            }`}
                          >
                            {rec.adjustment_quantity >= 0 ? "+" : ""}
                            {rec.adjustment_quantity}
                          </span>
                        </td>
                        <td className="py-2.5 px-3">
                          <span className="px-2 py-0.5 rounded text-[10px] font-semibold bg-slate-100 text-slate-700">
                            {rec.reason}
                          </span>
                          {rec.notes && (
                            <p className="text-[10px] text-slate-500 italic mt-0.5">{rec.notes}</p>
                          )}
                        </td>
                      </tr>
                    ))
                  )}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default InventoryPage;
