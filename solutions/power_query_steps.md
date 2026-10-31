# Suggested Power Query solution

These are **UI-oriented transformation instructions**, not a ready-to-paste M script. Apply and verify each step in Power BI Desktop.

1. In **Transform Data**, retain the original CSV query as a reference (e.g. `Sales_Raw`) for audit.
2. Add an index if you want to see where duplicates appeared. **Before de-duplicating, exclude the added index from the duplicate comparison.** Select only the eight original columns and choose **Remove Duplicates**. Expect 120 rows.
3. Create an audit query listing rows with blank/empty Quantity; expect **4 distinct orders**. Keep this separate from the final reportable query.
4. Duplicate/reference the deduplicated query to create `Sales_Reportable`. Filter blank Quantity out. Expect 116 rows.
5. For `Region`, Trim → Clean → Capitalize Each Word. Expect `North`, `South`, `East`, `West` only.
6. For `OrderDate`, parse dates explicitly using either `yyyy-MM-dd` or `dd/MM/yyyy`. A single automatic locale conversion is not reliable for both formats; test both known patterns. Ensure the column is Date.
7. For `UnitPrice`, replace `₹` with blank and `,` with blank, then set **Decimal Number** using an appropriate locale. No price is missing in this exercise.
8. Convert `Quantity` to Whole Number.
9. In CustomerName and PaymentMethod, replace blank/empty text with `Unknown Customer` and `Not Provided`, respectively. This is an exercise-specific assumption.
10. Add `LineTotal` as a Decimal Number custom column: `[Quantity] * [UnitPrice]`.
11. Close & Apply. Compare row counts and `LineTotal` sum to `data/expected_summary.json`.

## Common errors to check
- Incorrect locale may turn `03/10/2026` into March 10 instead of October 3.
- Deduplicating on `OrderID` alone changes the task; the requested rule is exact-record deduplication.
- Replacing a missing quantity with zero changes exception handling and should not happen silently.
- A formatted string like `₹1,250.00` must be converted to a numeric type before aggregation.
- The report model must not accidentally include excluded rows in sales measures.
