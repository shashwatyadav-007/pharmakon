import React from "react";
import { Link } from "react-router-dom";

export const PrivacyPolicyPage: React.FC = () => {
  return (
    <div className="max-w-4xl mx-auto py-8 px-4 space-y-6">
      <div className="border-b border-slate-200 pb-4">
        <h1 className="text-2xl font-bold text-slate-900 tracking-tight">Privacy Policy</h1>
        <p className="text-xs text-slate-500 mt-1">Effective Date: 12 October 2026 | Aayushman Pharmacy Operational System</p>
      </div>

      <div className="space-y-4 text-xs text-slate-700 leading-relaxed">
        <section className="space-y-2">
          <h2 className="text-sm font-bold text-slate-900">1. Operational Scope</h2>
          <p>
            PharmaKon operates as a dedicated internal pharmacy management system for Aayushman Pharmacy in Nepal. This policy outlines how patient, customer, transaction, and inventory data are handled within the system.
          </p>
        </section>

        <section className="space-y-2">
          <h2 className="text-sm font-bold text-slate-900">2. Customer and Transaction Data</h2>
          <p>
            The system records customer names, contact phone numbers, PAN/VAT identification, and dispensed medicine transaction histories to satisfy Nepal Drug Administration statutory record-keeping and fiscal audit requirements.
          </p>
        </section>

        <section className="space-y-2">
          <h2 className="text-sm font-bold text-slate-900">3. Data Security and Confidentiality</h2>
          <p>
            All prescription dispensing logs, medicine batch histories, and credit ledgers remain confidential property of Aayushman Pharmacy. Data is stored on secure, authenticated infrastructure and is not shared with third-party advertisers or external analytics brokers.
          </p>
        </section>

        <section className="space-y-2">
          <h2 className="text-sm font-bold text-slate-900">4. Contact Information</h2>
          <p>
            For privacy inquiries regarding recorded transaction statements, contact the pharmacy operational administrator directly at Aayushman Pharmacy, Kathmandu, Nepal.
          </p>
        </section>
      </div>

      <div className="pt-4 border-t border-slate-200">
        <Link to="/dashboard" className="text-xs font-semibold text-emerald-700 hover:text-emerald-900">
          &larr; Return to Dashboard
        </Link>
      </div>
    </div>
  );
};

export const TermsPage: React.FC = () => {
  return (
    <div className="max-w-4xl mx-auto py-8 px-4 space-y-6">
      <div className="border-b border-slate-200 pb-4">
        <h1 className="text-2xl font-bold text-slate-900 tracking-tight">Terms and Conditions of Use</h1>
        <p className="text-xs text-slate-500 mt-1">Operational Version 1.0 | Aayushman Pharmacy System Rules</p>
      </div>

      <div className="space-y-4 text-xs text-slate-700 leading-relaxed">
        <section className="space-y-2">
          <h2 className="text-sm font-bold text-slate-900">1. Authorized Operational Use</h2>
          <p>
            Access to PharmaKon is restricted to authorized pharmacy staff of Aayushman Pharmacy. Operational credentials must be protected and never shared outside the pharmacy premises.
          </p>
        </section>

        <section className="space-y-2">
          <h2 className="text-sm font-bold text-slate-900">2. First Expiry, First Out (FEFO) Compliance</h2>
          <p>
            Pharmacy dispensing operators must respect server-confirmed FEFO recommendations to prevent expired stock from reaching customers and minimize pharmaceutical waste.
          </p>
        </section>

        <section className="space-y-2">
          <h2 className="text-sm font-bold text-slate-900">3. Stock Adjustments &amp; Inventory Integrity</h2>
          <p>
            All physical count adjustments, damaged stock removals, and expiration disposals are recorded immutably in the system movement audit log. Falsification of stock counts is strictly prohibited.
          </p>
        </section>

        <section className="space-y-2">
          <h2 className="text-sm font-bold text-slate-900">4. Applicable Law</h2>
          <p>
            These terms are governed by the pharmacy operational laws and Drug Act regulations of Nepal.
          </p>
        </section>
      </div>

      <div className="pt-4 border-t border-slate-200">
        <Link to="/dashboard" className="text-xs font-semibold text-emerald-700 hover:text-emerald-900">
          &larr; Return to Dashboard
        </Link>
      </div>
    </div>
  );
};

export const NotFoundPage: React.FC = () => {
  return (
    <div className="min-h-[60vh] flex flex-col items-center justify-center text-center p-6 space-y-4">
      <div className="w-12 h-12 rounded bg-slate-200 text-slate-700 font-bold flex items-center justify-center text-xl">
        404
      </div>
      <h1 className="text-xl font-bold text-slate-900">Page Not Found</h1>
      <p className="text-xs text-slate-600 max-w-sm">
        The requested URL was not found in the PharmaKon system navigation.
      </p>
      <Link
        to="/dashboard"
        className="px-4 py-2 bg-emerald-600 hover:bg-emerald-700 text-white rounded text-xs font-medium cursor-pointer"
      >
        Return to Operational Dashboard
      </Link>
    </div>
  );
};
