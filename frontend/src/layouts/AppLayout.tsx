import React, { useState } from "react";
import { Link, NavLink, Outlet, useNavigate } from "react-router-dom";
import { useAuth } from "../features/auth/AuthContext";

export const AppLayout: React.FC = () => {
  const { user, logout } = useAuth();
  const navigate = useNavigate();
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  const handleLogout = () => {
    logout();
    navigate("/login");
  };

  const navItems = [
    { name: "Dashboard", path: "/dashboard", active: true },
    { name: "Products Catalog", path: "/products", active: true },
    { name: "Inventory & FEFO", path: "/inventory", active: true },
    { name: "Suppliers", path: "/suppliers", active: true },
    { name: "Sales (POS)", path: "/sales", active: false, badge: "Planned" },
    { name: "Purchases", path: "/purchases", active: false, badge: "Planned" },
    { name: "Customer Ledger", path: "/customers", active: false, badge: "Planned" },
    { name: "Analytics", path: "/analytics", active: false, badge: "Planned" },
    { name: "Settings", path: "/settings", active: false, badge: "Planned" },
  ];

  return (
    <div className="min-h-screen bg-slate-50 flex flex-col md:flex-row">
      {/* Sidebar for Desktop */}
      <aside className="w-full md:w-64 bg-white border-r border-slate-200 flex-shrink-0 flex flex-col justify-between">
        <div>
          {/* Brand Header */}
          <div className="h-16 flex items-center justify-between px-6 border-b border-slate-200">
            <Link to="/dashboard" className="flex items-center gap-2">
              <div className="w-7 h-7 rounded bg-emerald-600 flex items-center justify-center text-white font-bold text-sm">
                P
              </div>
              <span className="font-bold text-lg text-slate-900 tracking-tight">PharmaKon</span>
            </Link>

            {/* Mobile Hamburger */}
            <button
              type="button"
              className="md:hidden text-slate-600 hover:text-slate-900 p-1 rounded"
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              aria-label="Toggle navigation"
            >
              <svg className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                {mobileMenuOpen ? (
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                ) : (
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
                )}
              </svg>
            </button>
          </div>

          {/* Navigation Links */}
          <nav className={`px-3 py-4 space-y-1 ${mobileMenuOpen ? "block" : "hidden"} md:block`}>
            {navItems.map((item) => {
              if (item.active) {
                return (
                  <NavLink
                    key={item.path}
                    to={item.path}
                    onClick={() => setMobileMenuOpen(false)}
                    className={({ isActive }) =>
                      `flex items-center justify-between px-3 py-2 rounded text-sm font-medium transition-colors duration-100 ${
                        isActive
                          ? "bg-emerald-50 text-emerald-800 border-l-2 border-emerald-600 pl-2.5 font-semibold"
                          : "text-slate-700 hover:bg-slate-100 hover:text-slate-900"
                      }`
                    }
                  >
                    <span>{item.name}</span>
                  </NavLink>
                );
              }

              // Planned, non-functional links
              return (
                <div
                  key={item.path}
                  className="flex items-center justify-between px-3 py-2 rounded text-sm text-slate-400 bg-slate-50/50 cursor-not-allowed select-none"
                  title="Module planned in future milestones"
                >
                  <span>{item.name}</span>
                  {item.badge && (
                    <span className="text-[10px] uppercase font-semibold tracking-wider px-1.5 py-0.5 rounded bg-slate-200 text-slate-600">
                      {item.badge}
                    </span>
                  )}
                </div>
              );
            })}
          </nav>
        </div>

        {/* User Info & Logout footer */}
        <div className="p-4 border-t border-slate-200 bg-slate-50/50">
          <div className="flex items-center justify-between mb-3">
            <div>
              <p className="text-sm font-semibold text-slate-800 truncate">{user?.username || "Operator"}</p>
              <p className="text-xs text-slate-500 truncate">{user?.role || "Pharmacy User"}</p>
            </div>
            <span className="inline-block w-2 h-2 rounded-full bg-emerald-500" title="Online"></span>
          </div>

          <button
            type="button"
            onClick={handleLogout}
            className="w-full text-left flex items-center justify-center gap-1.5 px-3 py-1.5 border border-slate-300 rounded text-xs font-medium text-slate-700 bg-white hover:bg-slate-100 hover:text-slate-900 transition-colors duration-100 cursor-pointer"
          >
            <span>Sign Out</span>
          </button>
        </div>
      </aside>

      {/* Main Content Area */}
      <div className="flex-1 flex flex-col min-w-0 overflow-y-auto">
        <header className="h-16 bg-white border-b border-slate-200 px-6 flex items-center justify-between sticky top-0 z-10">
          <div className="flex items-center gap-3">
            <span className="text-xs font-semibold uppercase tracking-wider text-emerald-700 bg-emerald-50 border border-emerald-200 px-2 py-0.5 rounded">
              Aayushman Pharmacy
            </span>
            <span className="text-xs text-slate-400 hidden sm:inline">|</span>
            <span className="text-xs text-slate-500 hidden sm:inline">Operational Station 1</span>
          </div>

          <div className="text-xs text-slate-500">
            {new Date().toLocaleDateString("en-GB", { weekday: "short", day: "2-digit", month: "short", year: "numeric" })}
          </div>
        </header>

        <main className="flex-1 p-6 max-w-7xl w-full mx-auto">
          <Outlet />
        </main>

        <footer className="py-4 px-6 border-t border-slate-200 text-xs text-slate-500 flex flex-col sm:flex-row items-center justify-between gap-2 bg-white">
          <p>PharmaKon Pharmacy Management System &copy; 2026</p>
          <div className="flex items-center gap-4">
            <Link to="/privacy-policy" className="hover:text-slate-800 underline">Privacy Policy</Link>
            <Link to="/terms-and-conditions" className="hover:text-slate-800 underline">Terms and Conditions</Link>
          </div>
        </footer>
      </div>
    </div>
  );
};
