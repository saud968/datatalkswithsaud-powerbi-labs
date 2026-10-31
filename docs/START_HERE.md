# Start Here: Your First Power BI Data Quality Challenge

**Audience:** New or intermediate Power BI Desktop learners  
**Estimated scope:** One focused practice project (work at your own pace)  
**Tools:** Power BI Desktop; Python 3 is optional for checking the supplied dataset

## The business scenario

Your manager asks: **"What was our sales revenue in October 2026?"**

You are given [a deliberately messy fictional sales export](../data/sales_dirty.csv). A number in a chart is not trustworthy until you establish how it was calculated and what was excluded. The goal is to build a one-page Sales Snapshot *and* explain the evidence behind it.

## Try it yourself before reading the solutions

1. **Import:** In Power BI Desktop choose **Get data → Text/CSV**, select `data/sales_dirty.csv`, then **Transform Data**.
2. **Profile first:** Record original row count, full-row duplicates, blanks in Quantity/CustomerName/PaymentMethod, inconsistent Region values, and date formats.
3. **Define rules:** Remove *exact* duplicates across the eight original columns. Keep records with missing Quantity in a **separate exceptions query**; do not guess that a blank means 0 or 1.
4. **Clean:** Normalize Region to North/South/East/West; parse both `yyyy-MM-dd` and `dd/MM/yyyy`; remove currency symbols and commas from UnitPrice before making it numeric.
5. **Calculate:** On reportable rows only, compute `LineTotal = Quantity * UnitPrice`. Create measures for total sales, distinct orders, and average order value.
6. **Build the report:** Add KPI cards for sales, order count, and average order value; a region chart; a product chart; and a prominently labeled count of excluded orders.
7. **Reconcile:** Use the [expected summary](../data/expected_summary.json) to validate calculations. If totals disagree, find the cause instead of adjusting the target.
8. **Explain the decision:** Write 3–5 sentences covering what the number represents, what was excluded, and which missing-Quantity rule would require a business owner's decision.

## Acceptance checklist

- [ ] Raw input: **125 records**.
- [ ] Exact duplicate records: **5**.
- [ ] Distinct records after removing full-row duplicates: **120**.
- [ ] Distinct records missing Quantity: **4**, retained for exceptions reporting.
- [ ] Reportable orders: **116**.
- [ ] Total reportable sales: **₹3,29,570.00**.
- [ ] All reportable dates and prices are valid, and the four region labels are standardized.
- [ ] Region/product breakdowns reconcile to the overall reportable sales total.
- [ ] Report notes disclose that these are **synthetic data**, with a training-specific exclusion rule.

## Why the exceptions count matters

The raw export contains orders without a Quantity. Automatically filling those gaps with 0 or 1 could misstate revenue. In this exercise, such rows are **excluded from reportable revenue but not erased from the audit trail**. In a real project, the data owner would need to approve that policy.

## Resources and answer key

- [Full exercise](../exercises/challenge.md)
- [Power Query steps](../solutions/power_query_steps.md) — UI instructions, not a validated M script
- [Starter DAX measures](../solutions/dax_measures.md) — illustrative; not yet executed in Power BI Desktop
- [Validation script](../scripts/verify_dataset.py) — run `python scripts/verify_dataset.py` from the repository root
- [Expected results](../data/expected_summary.json)
- [Verified region/product answer key](../solutions/verified_breakdowns.md) — check your final breakdowns and missing-quantity exceptions **after** attempting the exercise

## Share your learning, not private data

You can recreate this exercise and describe your approach. Attribute the project to DataTalksWithSaud where appropriate, follow the [license](../LICENSE), and never substitute client/employer records for synthetic examples. Please [report reproducible documentation problems](https://github.com/saud968/datatalkswithsaud-powerbi-labs/issues).

> **Project status:** The published CSV and summary have been programmatically reconciled. A finished `.pbix` report and Power BI Desktop execution evidence are not yet included.
