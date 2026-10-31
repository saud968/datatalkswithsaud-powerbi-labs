# Exercise: Can the sales total be trusted?

You have received `data/sales_dirty.csv` for an October 2026 sales report. Before presenting revenue to a manager, investigate its data quality.

## Required tasks
1. Profile the input: count rows, find duplicate records, identify blank quantities, blank customer names and blank payment methods.
2. Remove **exact duplicates**. Preserve all distinct orders.
3. Standardize Region using trimmed/case-normalized values (`North`, `South`, `East`, `West`).
4. Parse `OrderDate` in both `yyyy-MM-dd` and `dd/MM/yyyy` formats.
5. Convert `UnitPrice` to decimal INR by stripping `₹` and thousands separators.
6. Resolve missing CustomerName as `Unknown Customer` and missing PaymentMethod as `Not Provided` **for this exercise only**.
7. **Do not invent missing Quantity**. Keep such rows in a separate exceptions query; exclude them from reportable sales.
8. Calculate `LineTotal = Quantity * UnitPrice` for reportable rows.
9. Create a Sales Snapshot with Total Sales, Orders, AOV, Sales by Region and Product.
10. Explain whether a different missing-quantity business rule would change your answer.

## Acceptance criteria
- CSV has 125 input rows; exactly 5 are complete-row duplicates.
- 120 distinct records after removing those 5 duplicate rows.
- 4 unique rows have blank quantity; only 116 rows belong in the reportable sales calculation.
- All reportable records have valid dates, quantities and numeric unit prices.
- All reported region labels are one of the four standardized values.
- Total Sales agrees with `data/expected_summary.json` to 2 decimals.
- The 4 excluded orders are reported as exceptions, not quietly deleted from the audit trail.

## Reflection
Would blank quantity mean zero units, one unit, incomplete capture, or something else in a real company? **Do not choose a rule without owner approval.** Here, exclusion from revenue is an explicit training policy, not a universal business rule.
