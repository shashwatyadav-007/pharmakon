import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { api } from "../../lib/api/client";
import type { LowStockAlert, ExpiryRiskAlert } from "../../types/api";

export const DashboardPage: React.FC = () => {
  const [totalProducts, setTotalProducts] = useState<number | null>(null);
  const [lowStockAlerts, setLowStockAlerts] = useState<LowStockAlert[]>([]);
  const [expiryAlerts, setExpiryAlerts] = useState<ExpiryRiskAlert[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const fetchDashboardData = async () => {
    setIsLoading(true);
    setError(null);
    try {
      const [productsRes, lowStockRes, expiryRes] = await Promise.all([
        api.products.list({ limit: 1 }),
        api.inventory.getLowStockAlerts(),
        api.inventory.getExpiryRiskAlerts(60),
      ]);

      setTotalProducts(productsRes.meta?.total ?? 0);
      setLowStockAlerts(lowStockRes);
      setExpiryAlerts(expiryRes);
    } catch (err: unknown) {
      if (err instanceof Error) {
        setError(err.message);
      } else {
        setError("Failed to load dashboard data.");
      }
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchDashboardData();
  }, []);

  return (
    <div className="space-y-6">
      {/* Title & Actions */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h1 className="text-2xl font-bold text-slate-900 tracking-tight">Operations Dashboard</h1>
          <p className="text-sm text-slate-600 mt-0.5">Real-time inventory status, active alerts, and quick actions.</p>
        </div>
        <div className="flex items-center gap-2">
          <button
            onClick={fetchDashboardData}
            disabled={isLoading}
            className="px-3 py-1.5 border border-slate-300 rounded text-xs font-medium text-slate-700 bg-white hover:bg-slate-100 transition-colors duration-100 disabled:opacity-50 cursor-pointer"
          >
            {isLoading ? "Refreshing..." : "Refresh Data"}
          </button>
          <Link
            to="/products"
            className="px-3 py-1.5 bg-emerald-600 hover:bg-emerald-700 text-white rounded text-xs font-medium transition-colors duration-100"
          >
            Manage Products
          </Link>
        </div>
      </div>

      {error && (
        <div className="p-4 bg-rose-50 border border-rose-200 text-rose-800 text-sm rounded">
          <p className="font-semibold">Unable to load operations data</p>
          <p className="mt-1">{error}</p>
          <button
            onClick={fetchDashboardData}
            className="mt-2 px-2.5 py-1 bg-white border border-rose-300 text-rose-700 rounded text-xs font-medium hover:bg-rose-100"
          >
            Retry
          </button>
        </div>
      )}

      {/* KPI Cards Grid */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        {/* Total Catalog Products */}
        <div className="bg-white border border-slate-200 rounded p-5 shadow-sm">
          <div className="flex items-center justify-between">
            <span className="text-xs font-semibold uppercase text-slate-500 tracking-wider">Catalog Items</span>
            <span className="w-2 h-2 rounded-full bg-emerald-500"></span>
          </div>
          <div className="mt-2 text-2xl font-bold text-slate-900">
            {isLoading ? "..." : totalProducts !== null ? totalProducts : "No data"}
          </div>
          <p className="mt-1 text-xs text-slate-500">Active medicines &amp; retail products</p>
        </div>

        {/* Low Stock Alerts */}
        <div className="bg-white border border-slate-200 rounded p-5 shadow-sm">
          <div className="flex items-center justify-between">
            <span className="text-xs font-semibold uppercase text-slate-500 tracking-wider">Low Stock Warnings</span>
            {lowStockAlerts.length > 0 && (
              <span className="px-1.5 py-0.5 rounded text-[10px] font-bold bg-amber-100 text-amber-800">
                Action Needed
              </span>
            )}
          </div>
          <div className="mt-2 text-2xl font-bold text-amber-600">
            {isLoading ? "..." : lowStockAlerts.length}
          </div>
          <p className="mt-1 text-xs text-slate-500">Items &le; configured reorder level</p>
        </div>

        {/* Expiry Risk Alerts */}
        <div className="bg-white border border-slate-200 rounded p-5 shadow-sm">
          <div className="flex items-center justify-between">
            <span className="text-xs font-semibold uppercase text-slate-500 tracking-wider">Expiry Risk (60 Days)</span>
            {expiryAlerts.length > 0 && (
              <span className="px-1.5 py-0.5 rounded text-[10px] font-bold bg-rose-100 text-rose-800">
                Critical
              </span>
            )}
          </div>
          <div className="mt-2 text-2xl font-bold text-rose-600">
            {isLoading ? "..." : expiryAlerts.length}
          </div>
          <p className="mt-1 text-xs text-slate-500">Batches expiring within 60 days</p>
        </div>

        {/* Planned Metric: Today's Revenue */}
        <div className="bg-white border border-slate-200 rounded p-5 shadow-sm opacity-90">
          <div className="flex items-center justify-between">
            <span className="text-xs font-semibold uppercase text-slate-400 tracking-wider">Today's Revenue</span>
            <span className="text-[10px] font-medium bg-slate-100 text-slate-600 px-1.5 py-0.5 rounded">
              POS Planned
            </span>
          </div>
          <div className="mt-2 text-2xl font-bold text-slate-400">
            —
          </div>
          <p className="mt-1 text-xs text-slate-400">Available when Sales module is deployed</p>
        </div>
      </div>

      {/* Two Column Section: Actionable Tables */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Near Expiry Batches */}
        <div className="bg-white border border-slate-200 rounded shadow-sm flex flex-col">
          <div className="p-4 border-b border-slate-200 flex items-center justify-between">
            <div>
              <h2 className="text-sm font-bold text-slate-900">Batches Approaching Expiry</h2>
              <p className="text-xs text-slate-500">Prioritize selling these batches under FEFO rules.</p>
            </div>
            <Link to="/inventory" className="text-xs font-medium text-emerald-700 hover:text-emerald-900">
              View All &rarr;
            </Link>
          </div>

          <div className="p-4 flex-1">
            {isLoading ? (
              <p className="text-xs text-slate-500 py-4 text-center">Loading batch expiry data...</p>
            ) : expiryAlerts.length === 0 ? (
              <p className="text-xs text-slate-500 py-4 text-center">No batches expiring within the next 60 days.</p>
            ) : (
              <div className="overflow-x-auto">
                <table className="w-full text-left text-xs">
                  <thead className="bg-slate-50 text-slate-600 border-b border-slate-200">
                    <tr>
                      <th className="py-2 px-3 font-semibold">Medicine</th>
                      <th className="py-2 px-3 font-semibold">Batch No.</th>
                      <th className="py-2 px-3 font-semibold">Stock</th>
                      <th className="py-2 px-3 font-semibold">Expires In</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-100">
                    {expiryAlerts.slice(0, 5).map((alert) => (
                      <tr key={alert.batch_id} className="hover:bg-slate-50">
                        <td className="py-2 px-3 font-medium text-slate-800">{alert.product_name}</td>
                        <td className="py-2 px-3 text-slate-600 font-mono text-[11px]">{alert.batch_number}</td>
                        <td className="py-2 px-3 text-slate-800">{alert.quantity} units</td>
                        <td className="py-2 px-3">
                          <span className="px-2 py-0.5 rounded text-[11px] font-semibold bg-rose-100 text-rose-800">
                            {alert.days_until_expiry} days
                          </span>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            )}
          </div>
        </div>

        {/* Low Stock Replenishment Needed */}
        <div className="bg-white border border-slate-200 rounded shadow-sm flex flex-col">
          <div className="p-4 border-b border-slate-200 flex items-center justify-between">
            <div>
              <h2 className="text-sm font-bold text-slate-900">Low Stock Replenishment Alerts</h2>
              <p className="text-xs text-slate-500">Products at or below their configured safety reorder level.</p>
            </div>
            <Link to="/inventory" className="text-xs font-medium text-emerald-700 hover:text-emerald-900">
              View Batches &rarr;
            </Link>
          </div>

          <div className="p-4 flex-1">
            {isLoading ? (
              <p className="text-xs text-slate-500 py-4 text-center">Loading stock levels...</p>
            ) : lowStockAlerts.length === 0 ? (
              <p className="text-xs text-slate-500 py-4 text-center">All active products meet safety stock levels.</p>
            ) : (
              <div className="overflow-x-auto">
                <table className="w-full text-left text-xs">
                  <thead className="bg-slate-50 text-slate-600 border-b border-slate-200">
                    <tr>
                      <th className="py-2 px-3 font-semibold">Medicine</th>
                      <th className="py-2 px-3 font-semibold">Code</th>
                      <th className="py-2 px-3 font-semibold">Current Stock</th>
                      <th className="py-2 px-3 font-semibold">Reorder Level</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-100">
                    {lowStockAlerts.slice(0, 5).map((item) => (
                      <tr key={item.product_id} className="hover:bg-slate-50">
                        <td className="py-2 px-3 font-medium text-slate-800">{item.product_name}</td>
                        <td className="py-2 px-3 text-slate-600 font-mono text-[11px]">{item.product_code}</td>
                        <td className="py-2 px-3 font-semibold text-amber-700">{item.current_stock} units</td>
                        <td className="py-2 px-3 text-slate-600">{item.reorder_level} units</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};
