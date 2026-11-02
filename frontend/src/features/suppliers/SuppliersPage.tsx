import React, { useEffect, useState } from "react";
import { api, ApiError } from "../../lib/api/client";
import type { Supplier } from "../../types/api";

export const SuppliersPage: React.FC = () => {
  const [suppliers, setSuppliers] = useState<Supplier[]>([]);
  const [total, setTotal] = useState(0);
  const [page, setPage] = useState(1);
  const [limit] = useState(10);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // Registration Modal State
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [formError, setFormError] = useState<string | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);

  // Form Fields
  const [name, setName] = useState("");
  const [contactPerson, setContactPerson] = useState("");
  const [phone, setPhone] = useState("");
  const [email, setEmail] = useState("");
  const [address, setAddress] = useState("");
  const [panVatNumber, setPanVatNumber] = useState("");

  const fetchSuppliers = async () => {
    setIsLoading(true);
    setError(null);
    try {
      const res = await api.suppliers.list({ page, limit });
      setSuppliers(res.data);
      setTotal(res.meta?.total ?? 0);
    } catch (err: unknown) {
      if (err instanceof Error) {
        setError(err.message);
      } else {
        setError("Failed to fetch suppliers.");
      }
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchSuppliers();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [page]);

  const openCreateModal = () => {
    setName("");
    setContactPerson("");
    setPhone("");
    setEmail("");
    setAddress("");
    setPanVatNumber("");
    setFormError(null);
    setIsModalOpen(true);
  };

  const handleFormSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setFormError(null);

    if (!name.trim()) {
      setFormError("Supplier company name is required.");
      return;
    }
    if (!phone.trim()) {
      setFormError("Phone number is required.");
      return;
    }

    setIsSubmitting(true);
    try {
      await api.suppliers.create({
        name: name.trim(),
        contact_person: contactPerson.trim() || null,
        phone: phone.trim(),
        email: email.trim() || null,
        address: address.trim() || null,
        pan_vat_number: panVatNumber.trim() || null,
      });

      setIsModalOpen(false);
      fetchSuppliers();
    } catch (err: unknown) {
      if (err instanceof ApiError) {
        setFormError(err.message);
      } else {
        setFormError("Failed to register supplier.");
      }
    } finally {
      setIsSubmitting(false);
    }
  };

  const totalPages = Math.ceil(total / limit) || 1;

  return (
    <div className="space-y-6">
      {/* Title */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h1 className="text-2xl font-bold text-slate-900 tracking-tight">Medicine Suppliers &amp; Distributors</h1>
          <p className="text-sm text-slate-600 mt-0.5">Maintain approved pharmaceutical distributors and wholesaler credentials.</p>
        </div>
        <button
          onClick={openCreateModal}
          className="px-3.5 py-2 bg-emerald-600 hover:bg-emerald-700 text-white rounded text-sm font-medium transition-colors duration-100 flex items-center justify-center gap-1.5 cursor-pointer"
        >
          <span>+ Register New Supplier</span>
        </button>
      </div>

      {error && (
        <div className="p-4 bg-rose-50 border border-rose-200 text-rose-800 text-sm rounded">
          <span className="font-semibold">Error: </span> {error}
        </div>
      )}

      {/* Table */}
      <div className="bg-white border border-slate-200 rounded shadow-sm overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead className="bg-slate-50 text-slate-600 border-b border-slate-200 uppercase font-semibold">
              <tr>
                <th className="py-3 px-4">Supplier Name</th>
                <th className="py-3 px-4">Contact Person</th>
                <th className="py-3 px-4">Phone Number</th>
                <th className="py-3 px-4">Email Address</th>
                <th className="py-3 px-4">Address</th>
                <th className="py-3 px-4">PAN / VAT</th>
                <th className="py-3 px-4 text-center">Status</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-100">
              {isLoading ? (
                <tr>
                  <td colSpan={7} className="py-8 text-center text-slate-500">
                    Loading suppliers directory...
                  </td>
                </tr>
              ) : suppliers.length === 0 ? (
                <tr>
                  <td colSpan={7} className="py-8 text-center text-slate-500">
                    No supplier records registered.
                  </td>
                </tr>
              ) : (
                suppliers.map((s) => (
                  <tr key={s.id} className="hover:bg-slate-50">
                    <td className="py-3 px-4 font-semibold text-slate-900">{s.name}</td>
                    <td className="py-3 px-4 text-slate-700">{s.contact_person || "—"}</td>
                    <td className="py-3 px-4 font-mono text-slate-800">{s.phone}</td>
                    <td className="py-3 px-4 text-slate-600">{s.email || "—"}</td>
                    <td className="py-3 px-4 text-slate-600">{s.address || "—"}</td>
                    <td className="py-3 px-4 font-mono text-slate-700">{s.pan_vat_number || "—"}</td>
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

        {/* Pagination Footer */}
        <div className="p-4 border-t border-slate-200 flex items-center justify-between text-xs text-slate-600">
          <div>
            Showing {suppliers.length} of {total} suppliers
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

      {/* Registration Modal Dialog */}
      {isModalOpen && (
        <div className="fixed inset-0 bg-slate-900/40 flex items-center justify-center p-4 z-50">
          <div className="bg-white border border-slate-200 rounded shadow-md w-full max-w-lg p-6 max-h-[90vh] overflow-y-auto">
            <div className="flex items-center justify-between border-b border-slate-200 pb-3 mb-4">
              <h2 className="text-base font-bold text-slate-900">Register New Medicine Supplier</h2>
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
              <div>
                <label htmlFor="supName" className="block font-medium text-slate-700 mb-1">
                  Supplier / Company Name <span className="text-rose-500">*</span>
                </label>
                <input
                  id="supName"
                  type="text"
                  required
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  placeholder="e.g. Nepal Pharma Distributors"
                  className="w-full px-3 py-1.5 border border-slate-300 rounded text-slate-900 focus:outline-none focus:ring-1 focus:ring-emerald-500"
                />
              </div>

              <div className="grid grid-cols-2 gap-3">
                <div>
                  <label htmlFor="contact" className="block font-medium text-slate-700 mb-1">
                    Contact Person
                  </label>
                  <input
                    id="contact"
                    type="text"
                    value={contactPerson}
                    onChange={(e) => setContactPerson(e.target.value)}
                    placeholder="e.g. Ram Sharma"
                    className="w-full px-3 py-1.5 border border-slate-300 rounded text-slate-900 focus:outline-none focus:ring-1 focus:ring-emerald-500"
                  />
                </div>

                <div>
                  <label htmlFor="supPhone" className="block font-medium text-slate-700 mb-1">
                    Phone Number <span className="text-rose-500">*</span>
                  </label>
                  <input
                    id="supPhone"
                    type="text"
                    required
                    value={phone}
                    onChange={(e) => setPhone(e.target.value)}
                    placeholder="e.g. 9841234567"
                    className="w-full px-3 py-1.5 border border-slate-300 rounded text-slate-900 focus:outline-none focus:ring-1 focus:ring-emerald-500"
                  />
                </div>
              </div>

              <div className="grid grid-cols-2 gap-3">
                <div>
                  <label htmlFor="supEmail" className="block font-medium text-slate-700 mb-1">
                    Email Address
                  </label>
                  <input
                    id="supEmail"
                    type="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    placeholder="ram@nepalpharma.com"
                    className="w-full px-3 py-1.5 border border-slate-300 rounded text-slate-900 focus:outline-none focus:ring-1 focus:ring-emerald-500"
                  />
                </div>

                <div>
                  <label htmlFor="panVat" className="block font-medium text-slate-700 mb-1">
                    PAN / VAT Number
                  </label>
                  <input
                    id="panVat"
                    type="text"
                    value={panVatNumber}
                    onChange={(e) => setPanVatNumber(e.target.value)}
                    placeholder="301234567"
                    className="w-full px-3 py-1.5 border border-slate-300 rounded text-slate-900 focus:outline-none focus:ring-1 focus:ring-emerald-500"
                  />
                </div>
              </div>

              <div>
                <label htmlFor="supAddress" className="block font-medium text-slate-700 mb-1">
                  Physical Office Address
                </label>
                <textarea
                  id="supAddress"
                  rows={2}
                  value={address}
                  onChange={(e) => setAddress(e.target.value)}
                  placeholder="e.g. New Road, Kathmandu, Nepal"
                  className="w-full px-3 py-1.5 border border-slate-300 rounded text-slate-900 focus:outline-none focus:ring-1 focus:ring-emerald-500"
                />
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
                  {isSubmitting ? "Registering..." : "Save Supplier Record"}
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};
