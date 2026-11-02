/**
 * Currency and decimal formatting helpers.
 * Financial rule: Never recalculate financial balances using binary floating point arithmetic.
 * These formatters display values cleanly without mutating the underlying numbers.
 */

export function formatNPR(amount: string | number | null | undefined): string {
  if (amount === null || amount === undefined || amount === "") {
    return "Rs. 0.00";
  }

  const num = typeof amount === "number" ? amount : parseFloat(amount);
  if (isNaN(num)) {
    return "Rs. 0.00";
  }

  // Format as Nepalese Rupees
  return `Rs. ${num.toLocaleString("en-IN", {
    minimumFractionDigits: 2,
    maximumFractionDigits: 2,
  })}`;
}

export function formatDate(dateString: string | null | undefined): string {
  if (!dateString) return "N/A";
  try {
    const d = new Date(dateString);
    if (isNaN(d.getTime())) return dateString;
    return d.toLocaleDateString("en-GB", {
      year: "numeric",
      month: "short",
      day: "2-digit",
    });
  } catch {
    return dateString;
  }
}
