import { describe, it, expect } from "vitest";
import { formatNPR, formatDate } from "../utils/formatters";

describe("Financial and Date Formatters", () => {
  it("formats NPR amounts correctly without precision loss", () => {
    expect(formatNPR("60.00")).toBe("Rs. 60.00");
    expect(formatNPR("1250.50")).toBe("Rs. 1,250.50");
    expect(formatNPR(100)).toBe("Rs. 100.00");
    expect(formatNPR(null)).toBe("Rs. 0.00");
    expect(formatNPR("")).toBe("Rs. 0.00");
  });

  it("formats dates into clean day-month-year representation", () => {
    expect(formatDate("2026-11-30")).toBe("30 Nov 2026");
    expect(formatDate(null)).toBe("N/A");
  });
});
