import React from "react";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { AuthProvider } from "./features/auth/AuthContext";
import { ProtectedRoute } from "./components/ProtectedRoute";
import { LoginPage } from "./features/auth/LoginPage";
import { AppLayout } from "./layouts/AppLayout";
import { DashboardPage } from "./features/dashboard/DashboardPage";
import { ProductsPage } from "./features/products/ProductsPage";
import { InventoryPage } from "./features/inventory/InventoryPage";
import { SuppliersPage } from "./features/suppliers/SuppliersPage";
import { PrivacyPolicyPage, TermsPage, NotFoundPage } from "./pages/StaticPages";

export const App: React.FC = () => {
  return (
    <BrowserRouter>
      <AuthProvider>
        <Routes>
          {/* Public Authentication Route */}
          <Route path="/login" element={<LoginPage />} />

          {/* Protected Application Routes */}
          <Route
            path="/"
            element={
              <ProtectedRoute>
                <AppLayout />
              </ProtectedRoute>
            }
          >
            <Route index element={<Navigate to="/dashboard" replace />} />
            <Route path="dashboard" element={<DashboardPage />} />
            <Route path="products" element={<ProductsPage />} />
            <Route path="inventory" element={<InventoryPage />} />
            <Route path="suppliers" element={<SuppliersPage />} />

            {/* Static & Compliance Routes */}
            <Route path="privacy-policy" element={<PrivacyPolicyPage />} />
            <Route path="terms-and-conditions" element={<TermsPage />} />

            {/* Catch-all 404 */}
            <Route path="*" element={<NotFoundPage />} />
          </Route>
        </Routes>
      </AuthProvider>
    </BrowserRouter>
  );
};

export default App;
