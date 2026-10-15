import React, { useEffect, useState } from "react";
import { api, ApiError } from "../../lib/api/client";
import type {
  Batch,
  Product,
  FEFOProductResponseData,
  LowStockAlert,
  ExpiryRiskAlert,
  StockAdjustmentReason,
} from "../../types/api";
import { formatDate, formatNPR } from "../../utils/formatters";

type InventoryTab = "batches" | "fefo" | "low_stock" | "expiry_risk" | "adjustments";

export const InventoryPage: React.FC = () => {
  const [activeTab, setActiveTab] = useState<InventoryTab>("batches");

  // Batches state
  const [batches, setBatches] = useState<Batch[]>([]);
  const [batchesLoading, setBatchesLoading] = useState(false);
  const [batchesError, setBatchesError] = useState<string | null>(null);

  // Products reference for FEFO selection and adjustment
  const [products, setProducts] = useState<Product[]>([]);
  const [selectedProductId, setSelectedProductId] = useState<string>("");
  const [fefoData, setFefoData] = useState<FEFOProductResponseData | null>(null);
  const [fefoLoading, setFefoLoading] = useState(false);

  // Alerts state
  const [lowStockAlerts, setLowStockAlerts] = useState<LowStockAlert[]>([]);
  const [expiryAlerts, setExpiryAlerts] = useState<ExpiryRiskAlert[]>([]);
  const [alertsLoading, setAlertsLoading] = useState(false);

  // Stock Adjustment State
  const [adjProductId, setAdjProductId] = useState<string>("");
  const [adjBatchId, setAdjBatchId] = useState<string>("");
  const [adjNewQuantity, setAdjNewQuantity] = useState<string>("");
  const [adjReason, setAdjReason] = useState<StockAdjustmentReason>("PHYSICAL_COUNT");
  const [adjNotes, setAdjNotes] = useState<string>("");
  const [adjSubmitting, setAdjSubmitting] = useState(false);
  const [adjSuccessMsg, setAdjSuccessMsg] = useState<string | null>(null);
  const [adjError, setAdjError] = useState<string | null>(null);

  // Load products list for dropdowns
  useEffect(() => {
    const loadProducts = async () => {
      try {
        const res = await api.products.list({ limit: 100 });
        setProducts(res.data);
        if (res.data.length > 0) {
          setSelectedProductId(res.data[0].id);
          setAdjProductId(res.data[0].id);
        }
      } catch {
        // silent fallback
      }
    };
    loadProducts();
  }, []);

  // Fetch batches
  const fetchBatches = async () => {
    setBatchesLoading(true);
    setBatchesError(null);
    try {
      const res = await api.inventory.listBatches({ limit: 50 });
      setBatches(res.data);
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

  // Fetch alerts
  const fetchAlerts = async () => {
    setAlertsLoading(true);
    try {
      const [lowRes, expRes] = await Promise.all([
        api.inventory.getLowStockAlerts(),
        api.inventory.getExpiryRiskAlerts(60),
      ]);
      setLowStockAlerts(lowRes);
      setExpiryAlerts(expRes);
    } finally {
      setAlertsLoading(false);
    }
  };

  useEffect(() => {
    if (activeTab === "batches") {
      fetchBatches();
    } else if (activeTab === "fefo") {
      if (selectedProductId) {
        fetchFEFO(selectedProductId);
      }
    } else if (activeTab === "low_stock" || activeTab === "expiry_risk") {
      fetchAlerts();
    }
  }, [activeTab, selectedProductId]);

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
      fetchBatches();
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

  // Batches matching the selected adjustment product
  const batchesForAdjProduct = batches.filter((b) => b.product_id === adjProductId);

  return (
    <div className="space-y-6">
      {/* Title */}
      <div>
        <h1 className="text-2xl font-bold text-slate-900 tracking-tight">Inventory &amp; Batch Management</h1>
        <p className="text-sm text-slate-600 mt-0.5">
          Track lots, enforce First Expiry First Out (FEFO) dispensing, and monitor stock integrity.
        </p>
      </div>

      {/* Tabs */}
      <div className="flex border-b border-slate-200 gap-1 overflow-x-auto text-xs font-medium">
        <button
          onClick={() => setActiveTab("batches")}
          className={`py-2 px-3 border-b-2 font-semibold transition-colors duration-100 cursor-pointer whitespace-nowrap ${
            activeTab === "batches"
              ? "border-emerald-600 text-emerald-700 bg-white"
              : "border-transparent text-slate-600 hover:text-slate-900 hover:border-slate-300"
          }`}
        >
          All Active Batches
        </button>

        <button
          onClick={() => setActiveTab("fefo")}
          className={`py-2 px-3 border-b-2 font-semibold transition-colors duration-100 cursor-pointer whitespace-nowrap ${
            activeTab === "fefo"
              ? "border-emerald-600 text-emerald-700 bg-white"
              : "border-transparent text-slate-600 hover:text-slate-900 hover:border-slate-300"
          }`}
        >
          FEFO Dispensing Engine
        </button>

        <button
          onClick={() => setActiveTab("low_stock")}
          className={`py-2 px-3 border-b-2 font-semibold transition-colors duration-100 cursor-pointer whitespace-nowrap ${
            activeTab === "low_stock"
              ? "border-emerald-600 text-emerald-700 bg-white"
              : "border-transparent text-slate-600 hover:text-slate-900 hover:border-slate-300"
          }`}
        >
          Low Stock Alerts {lowStockAlerts.length > 0 && `(${lowStockAlerts.length})`}
        </button>

        <button
          onClick={() => setActiveTab("expiry_risk")}
          className={`py-2 px-3 border-b-2 font-semibold transition-colors duration-100 cursor-pointer whitespace-nowrap ${
            activeTab === "expiry_risk"
              ? "border-emerald-600 text-emerald-700 bg-white"
              : "border-transparent text-slate-600 hover:text-slate-900 hover:border-slate-300"
          }`}
        >
          Expiry Risk Alerts {expiryAlerts.length > 0 && `(${expiryAlerts.length})`}
        </button>

        <button
          onClick={() => setActiveTab("adjustments")}
          className={`py-2 px-3 border-b-2 font-semibold transition-colors duration-100 cursor-pointer whitespace-nowrap ${
            activeTab === "adjustments"
              ? "border-emerald-600 text-emerald-700 bg-white"
              : "border-transparent text-slate-600 hover:text-slate-900 hover:border-slate-300"
          }`}
        >
          Physical Stock Adjustment
        </button>
      </div>

      {/* Tab 1: All Batches */}
      {activeTab === "batches" && (
        <div className="bg-white border border-slate-200 rounded shadow-sm overflow-hidden">
          {batchesError && (
            <div className="p-4 bg-rose-50 border-b border-rose-200 text-rose-800 text-xs">
              <span className="font-semibold">Error: </span> {batchesError}
            </div>
          )}

          <div className="overflow-x-auto">
            <table className="w-full text-left text-xs">
              <thead className="bg-slate-50 text-slate-600 border-b border-slate-200 uppercase font-semibold">
                <tr>
                  <th className="py-3 px-4">Batch Number</th>
                  <th className="py-3 px-4">Medicine / Product</th>
                  <th className="py-3 px-4">Expiry Date</th>
                  <th className="py-3 px-4 text-right">Purchase Cost (NPR)</th>
                  <th className="py-3 px-4 text-center">In-Stock Quantity</th>
                  <th className="py-3 px-4 text-center">Status</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-100">
                {batchesLoading ? (
                  <tr>
                    <td colSpan={6} className="py-8 text-center text-slate-500">
                      Loading inventory batches...
                    </td>
                  </tr>
                ) : batches.length === 0 ? (
                  <tr>
                    <td colSpan={6} className="py-8 text-center text-slate-500">
                      No batch lots recorded.
                    </td>
                  </tr>
                ) : (
                  batches.map((b) => (
                    <tr key={b.id} className="hover:bg-slate-50">
                      <td className="py-3 px-4 font-mono font-bold text-slate-800">{b.batch_number}</td>
                      <td className="py-3 px-4 font-medium text-slate-900">{b.product_name}</td>
                      <td className="py-3 px-4 text-slate-700 font-medium">{formatDate(b.expiry_date)}</td>
                      <td className="py-3 px-4 text-right font-medium text-slate-800">
                        {formatNPR(b.purchase_cost)}
                      </td>
                      <td className="py-3 px-4 text-center font-bold text-slate-900">
                        {b.quantity} <span className="text-xs font-normal text-slate-500">{b.unit || "unit"}s</span>
                      </td>
                      <td className="py-3 px-4 text-center">
                        <span className="px-2 py-0.5 rounded text-[11px] font-medium bg-emerald-100 text-emerald-800">
                          Active
                        </span>
                      </td>
                    </tr>
                  ))
                )}
              </tbody>
            </table>
          </div>
        </div>
      )}

      {/* Tab 2: FEFO Dispensing Engine */}
      {activeTab === "fefo" && (
        <div className="bg-white border border-slate-200 rounded p-6 shadow-sm space-y-6">
          <div className="max-w-md">
            <label htmlFor="fefoProd" className="block text-xs font-semibold text-slate-700 mb-1">
              Select Product for FEFO Dispensing Sequence:
            </label>
            <select
              id="fefoProd"
              value={selectedProductId}
              onChange={(e) => {
                setSelectedProductId(e.target.value);
                fetchFEFO(e.target.value);
              }}
              className="w-full px-3 py-2 border border-slate-300 rounded text-xs text-slate-800 bg-white focus:outline-none focus:ring-1 focus:ring-emerald-500"
            >
              {products.map((p) => (
                <option key={p.id} value={p.id}>
                  {p.name} ({p.code})
                </option>
              ))}
            </select>
          </div>

          <div className="border border-slate-200 rounded overflow-hidden">
            <div className="p-3 bg-slate-50 border-b border-slate-200 flex items-center justify-between">
              <div>
                <span className="text-xs font-bold text-slate-900">
                  {fefoData ? fefoData.product_name : "Product Batches"}
                </span>
                <span className="text-[11px] text-slate-500 ml-2">
                  (Ordered strictly by earliest expiry date first)
                </span>
              </div>
              <span className="text-[11px] font-semibold text-emerald-800 bg-emerald-100 px-2 py-0.5 rounded">
                Server-Confirmed FEFO Sequence
              </span>
            </div>

            <div className="overflow-x-auto">
              <table className="w-full text-left text-xs">
                <thead className="bg-white text-slate-600 border-b border-slate-200 uppercase font-semibold">
                  <tr>
                    <th className="py-2.5 px-4 text-center">Priority</th>
                    <th className="py-2.5 px-4">Batch Number</th>
                    <th className="py-2.5 px-4">Expiry Date</th>
                    <th className="py-2.5 px-4 text-center">Available Stock</th>
                    <th className="py-2.5 px-4 text-right">Locked Purchase Cost</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-100">
                  {fefoLoading ? (
                    <tr>
                      <td colSpan={5} className="py-6 text-center text-slate-500">
                        Calculating FEFO sequence...
                      </td>
                    </tr>
                  ) : !fefoData || fefoData.fefo_batches.length === 0 ? (
                    <tr>
                      <td colSpan={5} className="py-6 text-center text-slate-500">
                        No in-stock active batches found for this product.
                      </td>
                    </tr>
                  ) : (
                    fefoData.fefo_batches.map((batch, index) => (
                      <tr key={batch.batch_id} className={index === 0 ? "bg-emerald-50/50" : "hover:bg-slate-50"}>
                        <td className="py-3 px-4 text-center">
                          <span
                            className={`inline-flex items-center justify-center w-5 h-5 rounded-full text-[10px] font-bold ${
                              index === 0 ? "bg-emerald-600 text-white" : "bg-slate-200 text-slate-700"
                            }`}
                          >
                            #{index + 1}
                          </span>
                        </td>
                        <td className="py-3 px-4 font-mono font-bold text-slate-800">{batch.batch_number}</td>
                        <td className="py-3 px-4 text-slate-700 font-medium">
                          {formatDate(batch.expiry_date)}
                          {index === 0 && (
                            <span className="ml-2 text-[10px] font-semibold text-emerald-700 bg-emerald-100 px-1.5 py-0.5 rounded">
                              Dispense First
                            </span>
                          )}
                        </td>
                        <td className="py-3 px-4 text-center font-bold text-slate-900">
                          {batch.available_quantity} <span className="text-xs font-normal text-slate-500">{batch.unit || "unit"}s</span>
                        </td>
                        <td className="py-3 px-4 text-right font-medium text-slate-800">
                          {formatNPR(batch.purchase_cost)}
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

      {/* Tab 3: Low Stock Alerts */}
      {activeTab === "low_stock" && (
        <div className="bg-white border border-slate-200 rounded shadow-sm overflow-hidden">
          <div className="p-4 border-b border-slate-200">
            <h2 className="text-sm font-bold text-slate-900">Products at or Below Reorder Threshold</h2>
            <p className="text-xs text-slate-500">
              Replenishment should be initiated before inventory stock-out occurs.
            </p>
          </div>

          <div className="overflow-x-auto">
            <table className="w-full text-left text-xs">
              <thead className="bg-slate-50 text-slate-600 border-b border-slate-200 uppercase font-semibold">
                <tr>
                  <th className="py-3 px-4">Product Code</th>
                  <th className="py-3 px-4">Medicine Name</th>
                  <th className="py-3 px-4 text-center">Current Total Stock</th>
                  <th className="py-3 px-4 text-center">Configured Reorder Level</th>
                  <th className="py-3 px-4 text-center">Urgency</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-100">
                {alertsLoading ? (
                  <tr>
                    <td colSpan={5} className="py-6 text-center text-slate-500">
                      Checking stock safety limits...
                    </td>
                  </tr>
                ) : lowStockAlerts.length === 0 ? (
                  <tr>
                    <td colSpan={5} className="py-6 text-center text-slate-500">
                      No products are currently at or below safety reorder limits.
                    </td>
                  </tr>
                ) : (
                  lowStockAlerts.map((item) => (
                    <tr key={item.product_id} className="hover:bg-slate-50">
                      <td className="py-3 px-4 font-mono font-medium text-slate-700">{item.product_code}</td>
                      <td className="py-3 px-4 font-semibold text-slate-900">{item.product_name}</td>
                      <td className="py-3 px-4 text-center font-bold text-amber-700">{item.current_stock} units</td>
                      <td className="py-3 px-4 text-center text-slate-600">{item.reorder_level} units</td>
                      <td className="py-3 px-4 text-center">
                        <span className="px-2 py-0.5 rounded text-[11px] font-semibold bg-amber-100 text-amber-800">
                          Reorder Required
                        </span>
                      </td>
                    </tr>
                  ))
                )}
              </tbody>
            </table>
          </div>
        </div>
      )}

      {/* Tab 4: Expiry Risk Alerts */}
      {activeTab === "expiry_risk" && (
        <div className="bg-white border border-slate-200 rounded shadow-sm overflow-hidden">
          <div className="p-4 border-b border-slate-200">
            <h2 className="text-sm font-bold text-slate-900">Batches Expiring Within 60 Days</h2>
            <p className="text-xs text-slate-500">
              Medicines approaching expiration should be dispensed under priority FEFO or returned to suppliers.
            </p>
          </div>

          <div className="overflow-x-auto">
            <table className="w-full text-left text-xs">
              <thead className="bg-slate-50 text-slate-600 border-b border-slate-200 uppercase font-semibold">
                <tr>
                  <th className="py-3 px-4">Batch Number</th>
                  <th className="py-3 px-4">Medicine Name</th>
                  <th className="py-3 px-4">Expiry Date</th>
                  <th className="py-3 px-4 text-center">Stock at Risk</th>
                  <th className="py-3 px-4 text-center">Days Remaining</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-100">
                {alertsLoading ? (
                  <tr>
                    <td colSpan={5} className="py-6 text-center text-slate-500">
                      Auditing batch expiry schedules...
                    </td>
                  </tr>
                ) : expiryAlerts.length === 0 ? (
                  <tr>
                    <td colSpan={5} className="py-6 text-center text-slate-500">
                      No batches are expiring within the next 60 days.
                    </td>
                  </tr>
                ) : (
                  expiryAlerts.map((b) => (
                    <tr key={b.batch_id} className="hover:bg-slate-50">
                      <td className="py-3 px-4 font-mono font-bold text-slate-800">{b.batch_number}</td>
                      <td className="py-3 px-4 font-semibold text-slate-900">{b.product_name}</td>
                      <td className="py-3 px-4 text-slate-700 font-medium">{formatDate(b.expiry_date)}</td>
                      <td className="py-3 px-4 text-center font-bold text-slate-900">{b.quantity} units</td>
                      <td className="py-3 px-4 text-center">
                        <span className="px-2.5 py-0.5 rounded text-[11px] font-bold bg-rose-100 text-rose-800">
                          {b.days_until_expiry} days
                        </span>
                      </td>
                    </tr>
                  ))
                )}
              </tbody>
            </table>
          </div>
        </div>
      )}

      {/* Tab 5: Physical Stock Adjustment */}
      {activeTab === "adjustments" && (
        <div className="bg-white border border-slate-200 rounded p-6 shadow-sm max-w-xl">
          <div className="border-b border-slate-200 pb-3 mb-4">
            <h2 className="text-base font-bold text-slate-900">Record Physical Stock Verification</h2>
            <p className="text-xs text-slate-500 mt-0.5">
              Updates in-stock lot quantity and appends an immutable record to the movement audit log.
            </p>
          </div>

          {adjSuccessMsg && (
            <div className="mb-4 p-3 bg-emerald-50 border border-emerald-200 text-emerald-800 text-xs rounded">
              <span className="font-semibold">Success: </span>
              {adjSuccessMsg}
            </div>
          )}

          {adjError && (
            <div className="mb-4 p-3 bg-rose-50 border border-rose-200 text-rose-800 text-xs rounded">
              <span className="font-semibold">Adjustment Error: </span>
              {adjError}
            </div>
          )}

          <form onSubmit={handleAdjustmentSubmit} className="space-y-4 text-xs">
            <div>
              <label htmlFor="adjProduct" className="block font-medium text-slate-700 mb-1">
                Target Product <span className="text-rose-500">*</span>
              </label>
              <select
                id="adjProduct"
                value={adjProductId}
                onChange={(e) => {
                  setAdjProductId(e.target.value);
                  setAdjBatchId("");
                }}
                className="w-full px-3 py-1.5 border border-slate-300 rounded text-slate-900 bg-white focus:outline-none focus:ring-1 focus:ring-emerald-500"
              >
                {products.map((p) => (
                  <option key={p.id} value={p.id}>
                    {p.name} ({p.code})
                  </option>
                ))}
              </select>
            </div>

            <div>
              <label htmlFor="adjBatch" className="block font-medium text-slate-700 mb-1">
                Target Batch Lot <span className="text-rose-500">*</span>
              </label>
              <select
                id="adjBatch"
                required
                value={adjBatchId}
                onChange={(e) => setAdjBatchId(e.target.value)}
                className="w-full px-3 py-1.5 border border-slate-300 rounded text-slate-900 bg-white focus:outline-none focus:ring-1 focus:ring-emerald-500"
              >
                <option value="">Select Batch...</option>
                {batchesForAdjProduct.map((b) => (
                  <option key={b.id} value={b.id}>
                    {b.batch_number} (Current Stock: {b.quantity}, Exp: {formatDate(b.expiry_date)})
                  </option>
                ))}
              </select>
              {batchesForAdjProduct.length === 0 && (
                <p className="mt-1 text-[11px] text-amber-600">
                  No active batches recorded for this product yet.
                </p>
              )}
            </div>

            <div className="grid grid-cols-2 gap-3">
              <div>
                <label htmlFor="newQty" className="block font-medium text-slate-700 mb-1">
                  New Physical Count Quantity <span className="text-rose-500">*</span>
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
                className="w-full px-4 py-2 bg-emerald-600 hover:bg-emerald-700 text-white rounded font-medium disabled:opacity-50 cursor-pointer transition-colors duration-100"
              >
                {adjSubmitting ? "Submitting Server Transaction..." : "Confirm & Commit Stock Adjustment"}
              </button>
            </div>
          </form>
        </div>
      )}
    </div>
  );
};
