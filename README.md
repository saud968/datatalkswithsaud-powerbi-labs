# Sales Data Quality Challenge — Power BI Desktop

**DataTalksWithSaud | A free, beginner-friendly, independent learning exercise**

Turn a fictional, deliberately messy sales CSV into an explainable, trustworthy Power BI report. This challenge is **not** a completed PBIX dashboard and **does not require Power BI Service**.

## Start here — free hands-on challenge

**New to Power BI?** Follow the [guided learner walkthrough](docs/START_HERE.md), which takes you from a messy CSV through an auditable Sales Snapshot and a reconciliation checklist. Try the [exercise](exercises/challenge.md) first; use the solution notes only after your own attempt.

Changes to the CSV or validation script are checked automatically by [GitHub Actions](.github/workflows/validate-dataset.yml). This checks the *synthetic data and its expected totals*, not whether the Power BI Desktop report has been built or tested.

## Learning outcomes
- Import CSV into Power BI Desktop and inspect data-quality issues.
- Remove exact duplicate rows without silently merging distinct orders.
- Normalize inconsistent region labels and mixed-format dates.
- Convert prices to numbers and calculate revenue.
- Handle missing quantity using an explicit reporting policy.
- Build an auditable summary and DAX measures.

## Contents
- `data/sales_dirty.csv`: **125 synthetic rows**, including 5 exact duplicates.
- `data/expected_summary.json`: independently calculated checks for the published cleaning policy.
- `exercises/challenge.md`: exercise and acceptance criteria.
- `solutions/power_query_steps.md`: suggested Power Query transformation logic.
- `solutions/dax_measures.md`: starter DAX and reporting checks.
- [`solutions/verified_breakdowns.md`](solutions/verified_breakdowns.md): independently checked sales totals by region and product, missing-quantity exceptions, and troubleshooting tips.
- `scripts/verify_dataset.py`: dependency-free validation script.

## Getting started
1. Install Power BI Desktop from Microsoft.
2. Open the CSV using **Get Data → Text/CSV** and select **Transform Data**.
3. Follow `exercises/challenge.md` **before** looking at the solutions.
4. Compare your final results with `data/expected_summary.json`.
5. To verify the packaged CSV independently, run `python scripts/verify_dataset.py` from the repository root.

**Important:** Price is per unit in Indian rupees (INR). All products, customers, and transactions are invented. This is a training scenario, not business data. No Power BI report file is included, and the Power Query steps are provided for guided implementation rather than as a tested, downloadable M script.

## Recommended report
Create a one-page Sales Snapshot with Total Sales, Reportable Orders, average order value, sales by region, sales by product, and a visual indicating excluded missing-quantity rows.

## Attribution and reuse
Original example data and learning content © 2026 Saud Ansari / DataTalksWithSaud. Licensed under MIT (see `LICENSE`). Power BI is a Microsoft product; this independent tutorial is not affiliated with Microsoft.

## More free practice

Want to practise SQL as well? Try **[DataTalksWithSaud SQL Labs](https://github.com/saud968/datatalkswithsaud-sql-labs)**: 12 tested SQLite exercises using fictional customers and orders, with answer keys and automated checks. No paid database required.

## About the author
[GitHub — saud968](https://github.com/saud968) · [LinkedIn](https://www.linkedin.com/in/saud-ansari968/) · [DataTalksWithSaud on Topmate](https://topmate.io/saud_ansari)
