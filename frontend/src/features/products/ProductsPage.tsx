import React, { useEffect, useState } from "react";
import { api, ApiError } from "../../lib/api/client";
import type { Product, ProductCategory, ProductUnit } from "../../types/api";
import { formatNPR } from "../../utils/formatters";

export const ProductsPage: React.FC = () => {
  const [products, setProducts] = useState<Product[]>([]);
  const [total, setTotal] = useState(0);
  const [page, setPage] = useState(1);
  const [limit] = useState(10);
  const [searchQuery, setSearchQuery] = useState("");
  const [categoryFilter, setCategoryFilter] = useState<string>("");
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // Modal State for Create / Edit
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [editingProduct, setEditingProduct] = useState<Product | null>(null);
  const [formError, setFormError] = useState<string | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);

  // Form Fields
  const [code, setCode] = useState("");
  const [name, setName] = useState("");
  const [category, setCategory] = useState<ProductCategory>("Medicine");
  const [unit, setUnit] = useState<ProductUnit>("Strip");
  const [mrp, setMrp] = useState("");
  const [defaultPurchasePrice, setDefaultPurchasePrice] = useState("");
  const [barcode, setBarcode] = useState("");
  const [reorderLevel, setReorderLevel] = useState("10");

  const categories: ProductCategory[] = ["Medicine", "Surgical", "Cosmetic", "Baby", "Food"];
  const units: ProductUnit[] = ["Strip", "Tablet", "Bottle", "Box", "Piece"];

  const fetchProducts = async () => {
    setIsLoading(true);
    setError(null);
    try {
      const res = await api.products.list({
        query: searchQuery || undefined,
        category: categoryFilter || undefined,
        page,
        limit,
      });
      setProducts(res.data);
      setTotal(res.meta?.total ?? 0);
    } catch (err: unknown) {
      if (err instanceof Error) {
        setError(err.message);
      } else {
        setError("Failed to fetch products.");
      }
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchProducts();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [page, categoryFilter]);

  const handleSearchSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setPage(1);
    fetchProducts();
  };

  const openCreateModal = () => {
    setEditingProduct(null);
    setCode("");
    setName("");
    setCategory("Medicine");
    setUnit("Strip");
    setMrp("");
    setDefaultPurchasePrice("");
    setBarcode("");
    setReorderLevel("10");
    setFormError(null);
    setIsModalOpen(true);
  };

  const openEditModal = (p: Product) => {
    setEditingProduct(p);
    setCode(p.code);
    setName(p.name);
    setCategory(p.category);
    setUnit(p.unit);
    setMrp(p.mrp);
    setDefaultPurchasePrice(p.default_purchase_price || "");
    setBarcode(p.barcode || "");
    setReorderLevel(String(p.reorder_level));
    setFormError(null);
    setIsModalOpen(true);
  };

  const handleFormSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setFormError(null);

    // Client-side validation
    if (!name.trim()) {
      setFormError("Product name is required.");
      return;
    }
    if (!editingProduct && !code.trim()) {
      setFormError("Product SKU code is required.");
      return;
    }
    const numMrp = parseFloat(mrp);
    if (isNaN(numMrp) || numMrp < 0) {
      setFormError("MRP must be a valid positive number.");
      return;
    }

    setIsSubmitting(true);
    try {
      if (editingProduct) {
        // Update product
        await api.products.update(editingProduct.id, {
          name: name.trim(),
          category,
          unit,
          mrp: numMrp.toFixed(2),
          default_purchase_price: defaultPurchasePrice ? parseFloat(defaultPurchasePrice).toFixed(2) : null,
          barcode: barcode.trim() || null,
          reorder_level: parseInt(reorderLevel, 10) || 10,
        });
      } else {
        // Create product
        await api.products.create({
          code: code.trim(),
          name: name.trim(),
          category,
          unit,
          mrp: numMrp.toFixed(2),
          default_purchase_price: defaultPurchasePrice ? parseFloat(defaultPurchasePrice).toFixed(2) : null,
          barcode: barcode.trim() || null,
          reorder_level: parseInt(reorderLevel, 10) || 10,
        });
      }

      setIsModalOpen(false);
      fetchProducts();
    } catch (err: unknown) {
      if (err instanceof ApiError) {
        setFormError(err.message);
      } else {
        setFormError("Failed to save product.");
      }
    } finally {
      setIsSubmitting(false);
    }
  };

  const totalPages = Math.ceil(total / limit) || 1;

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h1 className="text-2xl font-bold text-slate-900 tracking-tight">Medicine &amp; Product Catalog</h1>
          <p className="text-sm text-slate-600 mt-0.5">Maintain pharmacy master SKU records, pricing, and reorder levels.</p>
        </div>
        <button
          onClick={openCreateModal}
          className="px-3.5 py-2 bg-emerald-600 hover:bg-emerald-700 text-white rounded text-sm font-medium transition-colors duration-100 flex items-center justify-center gap-1.5 cursor-pointer"
        >
          <span>+ Add New Product</span>
        </button>
      </div>

      {/* Filter and Search Bar */}
      <div className="bg-white border border-slate-200 rounded p-4 shadow-sm flex flex-col md:flex-row gap-3 items-center justify-between">
        <form onSubmit={handleSearchSubmit} className="flex-1 w-full flex items-center gap-2">
          <input
            type="text"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            placeholder="Search by medicine name, SKU code, or barcode..."
            className="flex-1 px-3 py-1.5 border border-slate-300 rounded text-sm text-slate-900 focus:outline-none focus:ring-1 focus:ring-emerald-500 focus:border-emerald-500"
          />
          <button
            type="submit"
            className="px-3 py-1.5 bg-slate-800 hover:bg-slate-900 text-white rounded text-xs font-medium cursor-pointer"
          >
            Search
          </button>
          {searchQuery && (
            <button
              type="button"
              onClick={() => {
                setSearchQuery("");
                setPage(1);
                fetchProducts();
              }}
              className="px-2.5 py-1.5 border border-slate-300 text-slate-600 rounded text-xs hover:bg-slate-100"
            >
              Clear
            </button>
          )}
        </form>

        <div className="w-full md:w-auto flex items-center gap-2">
          <label htmlFor="catFilter" className="text-xs text-slate-600 font-medium whitespace-nowrap">
            Category:
          </label>
          <select
            id="catFilter"
            value={categoryFilter}
            onChange={(e) => {
              setCategoryFilter(e.target.value);
              setPage(1);
            }}
            className="px-2.5 py-1.5 border border-slate-300 rounded text-xs text-slate-800 bg-white focus:outline-none focus:ring-1 focus:ring-emerald-500"
          >
            <option value="">All Categories</option>
            {categories.map((c) => (
              <option key={c} value={c}>{c}</option>
            ))}
          </select>
        </div>
      </div>

      {/* Error Banner */}
      {error && (
        <div className="p-4 bg-rose-50 border border-rose-200 text-rose-800 text-sm rounded">
          <span className="font-semibold">Error: </span> {error}
        </div>
      )}

      {/* Products Table */}
      <div className="bg-white border border-slate-200 rounded shadow-sm overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead className="bg-slate-50 text-slate-600 border-b border-slate-200 uppercase font-semibold">
              <tr>
                <th className="py-3 px-4">Code / SKU</th>
                <th className="py-3 px-4">Medicine Name</th>
                <th className="py-3 px-4">Category</th>
                <th className="py-3 px-4">Unit</th>
                <th className="py-3 px-4 text-right">MRP (NPR)</th>
                <th className="py-3 px-4 text-center">Available Stock</th>
                <th className="py-3 px-4 text-center">Reorder Level</th>
                <th className="py-3 px-4 text-center">Actions</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-100">
              {isLoading ? (
                <tr>
                  <td colSpan={8} className="py-8 text-center text-slate-500">
                    Loading medicine catalog...
                  </td>
                </tr>
              ) : products.length === 0 ? (
                <tr>
                  <td colSpan={8} className="py-8 text-center text-slate-500">
                    No products match the given criteria.
                  </td>
                </tr>
              ) : (
                products.map((p) => {
                  const isLowStock = p.total_stock <= p.reorder_level;
                  return (
                    <tr key={p.id} className="hover:bg-slate-50">
                      <td className="py-3 px-4 font-mono font-medium text-slate-700">{p.code}</td>
                      <td className="py-3 px-4 font-semibold text-slate-900">
                        {p.name}
                        {p.barcode && (
                          <span className="block text-[10px] text-slate-400 font-mono">Barcode: {p.barcode}</span>
                        )}
                      </td>
                      <td className="py-3 px-4">
                        <span className="px-2 py-0.5 rounded text-[11px] font-medium bg-slate-100 text-slate-700">
                          {p.category}
                        </span>
                      </td>
                      <td className="py-3 px-4 text-slate-600">{p.unit}</td>
                      <td className="py-3 px-4 text-right font-medium text-slate-900">
                        {formatNPR(p.mrp)}
                      </td>
                      <td className="py-3 px-4 text-center">
                        <span
                          className={`px-2 py-0.5 rounded text-[11px] font-semibold ${
                            isLowStock
                              ? "bg-amber-100 text-amber-800"
                              : "bg-emerald-100 text-emerald-800"
                          }`}
                        >
                          {p.total_stock} {p.unit}s
                        </span>
                      </td>
                      <td className="py-3 px-4 text-center text-slate-600 font-medium">
                        {p.reorder_level}
                      </td>
                      <td className="py-3 px-4 text-center">
                        <button
                          onClick={() => openEditModal(p)}
                          className="px-2 py-1 text-slate-700 hover:text-emerald-700 hover:bg-slate-100 border border-slate-300 rounded font-medium cursor-pointer"
                        >
                          Edit
                        </button>
                      </td>
                    </tr>
                  );
                })
              )}
            </tbody>
          </table>
        </div>

        {/* Pagination Footer */}
        <div className="p-4 border-t border-slate-200 flex items-center justify-between text-xs text-slate-600">
          <div>
            Showing {products.length} of {total} products
          </div>
          <div className="flex items-center gap-1.5">
            <button
              onClick={() => setPage((p) => Math.max(p - 1, 1))}
              disabled={page <= 1 || isLoading}
              className="px-2.5 py-1 border border-slate-300 rounded hover:bg-slate-50 disabled:opacity-40 disabled:cursor-not-allowed"
            >
              Previous
            </button>
            <span className="px-2 py-1 font-medium">
              Page {page} of {totalPages}
            </span>
            <button
              onClick={() => setPage((p) => Math.min(p + 1, totalPages))}
              disabled={page >= totalPages || isLoading}
              className="px-2.5 py-1 border border-slate-300 rounded hover:bg-slate-50 disabled:opacity-40 disabled:cursor-not-allowed"
            >
              Next
            </button>
          </div>
        </div>
      </div>

      {/* Create / Edit Modal Dialog */}
      {isModalOpen && (
        <div className="fixed inset-0 bg-slate-900/40 flex items-center justify-center p-4 z-50">
          <div className="bg-white border border-slate-200 rounded shadow-md w-full max-w-lg p-6 max-h-[90vh] overflow-y-auto">
            <div className="flex items-center justify-between border-b border-slate-200 pb-3 mb-4">
              <h2 className="text-base font-bold text-slate-900">
                {editingProduct ? `Edit Product: ${editingProduct.code}` : "Add New Medicine / Product"}
              </h2>
              <button
                type="button"
                onClick={() => setIsModalOpen(false)}
                className="text-slate-400 hover:text-slate-600 text-lg font-bold"
              >
                &times;
              </button>
            </div>

            {formError && (
              <div className="mb-4 p-3 bg-rose-50 border border-rose-200 text-rose-800 text-xs rounded">
                <span className="font-semibold">Validation Error: </span>
                {formError}
              </div>
            )}

            <form onSubmit={handleFormSubmit} className="space-y-4 text-xs">
              {!editingProduct && (
                <div>
                  <label htmlFor="code" className="block font-medium text-slate-700 mb-1">
                    Product Code / SKU <span className="text-rose-500">*</span>
                  </label>
                  <input
                    id="code"
                    type="text"
                    required
                    value={code}
                    onChange={(e) => setCode(e.target.value)}
                    placeholder="e.g. MED-PAR-500"
                    className="w-full px-3 py-1.5 border border-slate-300 rounded text-slate-900 focus:outline-none focus:ring-1 focus:ring-emerald-500"
                  />
                  <p className="mt-0.5 text-[11px] text-slate-400">Must be unique across the catalog.</p>
                </div>
              )}

              <div>
                <label htmlFor="name" className="block font-medium text-slate-700 mb-1">
                  Medicine / Commercial Name <span className="text-rose-500">*</span>
                </label>
                <input
                  id="name"
                  type="text"
                  required
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  placeholder="e.g. Paracetamol 500mg"
                  className="w-full px-3 py-1.5 border border-slate-300 rounded text-slate-900 focus:outline-none focus:ring-1 focus:ring-emerald-500"
                />
              </div>

              <div className="grid grid-cols-2 gap-3">
                <div>
                  <label htmlFor="category" className="block font-medium text-slate-700 mb-1">
                    Category <span className="text-rose-500">*</span>
                  </label>
                  <select
                    id="category"
                    value={category}
                    onChange={(e) => setCategory(e.target.value as ProductCategory)}
                    className="w-full px-3 py-1.5 border border-slate-300 rounded text-slate-900 bg-white focus:outline-none focus:ring-1 focus:ring-emerald-500"
                  >
                    {categories.map((c) => (
                      <option key={c} value={c}>{c}</option>
                    ))}
                  </select>
                </div>

                <div>
                  <label htmlFor="unit" className="block font-medium text-slate-700 mb-1">
                    Unit <span className="text-rose-500">*</span>
                  </label>
                  <select
                    id="unit"
                    value={unit}
                    onChange={(e) => setUnit(e.target.value as ProductUnit)}
                    className="w-full px-3 py-1.5 border border-slate-300 rounded text-slate-900 bg-white focus:outline-none focus:ring-1 focus:ring-emerald-500"
                  >
                    {units.map((u) => (
                      <option key={u} value={u}>{u}</option>
                    ))}
                  </select>
                </div>
              </div>

              <div className="grid grid-cols-2 gap-3">
                <div>
                  <label htmlFor="mrp" className="block font-medium text-slate-700 mb-1">
                    Maximum Retail Price (MRP) <span className="text-rose-500">*</span>
                  </label>
                  <input
                    id="mrp"
                    type="number"
                    step="0.01"
                    min="0"
                    required
                    value={mrp}
                    onChange={(e) => setMrp(e.target.value)}
                    placeholder="60.00"
                    className="w-full px-3 py-1.5 border border-slate-300 rounded text-slate-900 focus:outline-none focus:ring-1 focus:ring-emerald-500"
                  />
                </div>

                <div>
                  <label htmlFor="defaultPurchasePrice" className="block font-medium text-slate-700 mb-1">
                    Default Purchase Cost (Optional)
                  </label>
                  <input
                    id="defaultPurchasePrice"
                    type="number"
                    step="0.01"
                    min="0"
                    value={defaultPurchasePrice}
                    onChange={(e) => setDefaultPurchasePrice(e.target.value)}
                    placeholder="45.00"
                    className="w-full px-3 py-1.5 border border-slate-300 rounded text-slate-900 focus:outline-none focus:ring-1 focus:ring-emerald-500"
                  />
                </div>
              </div>

              <div className="grid grid-cols-2 gap-3">
                <div>
                  <label htmlFor="barcode" className="block font-medium text-slate-700 mb-1">
                    Barcode (EAN/UPC)
                  </label>
                  <input
                    id="barcode"
                    type="text"
                    value={barcode}
                    onChange={(e) => setBarcode(e.target.value)}
                    placeholder="8901234567890"
                    className="w-full px-3 py-1.5 border border-slate-300 rounded text-slate-900 focus:outline-none focus:ring-1 focus:ring-emerald-500"
                  />
                </div>

                <div>
                  <label htmlFor="reorderLevel" className="block font-medium text-slate-700 mb-1">
                    Reorder Alert Level
                  </label>
                  <input
                    id="reorderLevel"
                    type="number"
                    min="0"
                    value={reorderLevel}
                    onChange={(e) => setReorderLevel(e.target.value)}
                    className="w-full px-3 py-1.5 border border-slate-300 rounded text-slate-900 focus:outline-none focus:ring-1 focus:ring-emerald-500"
                  />
                </div>
              </div>

              <div className="pt-4 border-t border-slate-200 flex items-center justify-end gap-2">
                <button
                  type="button"
                  onClick={() => setIsModalOpen(false)}
                  disabled={isSubmitting}
                  className="px-3 py-1.5 border border-slate-300 rounded text-slate-700 hover:bg-slate-100"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  disabled={isSubmitting}
                  className="px-4 py-1.5 bg-emerald-600 hover:bg-emerald-700 text-white rounded font-medium disabled:opacity-60 cursor-pointer"
                >
                  {isSubmitting ? "Saving..." : editingProduct ? "Update Product" : "Save Product"}
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};
