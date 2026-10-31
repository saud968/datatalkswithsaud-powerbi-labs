# Answer key: verified sales breakdowns

**For learners who have completed the [challenge](../exercises/challenge.md).**

These results were independently calculated from the repository's fictional `data/sales_dirty.csv` on **31 October 2026**. They help you check your own Power BI report. They are **not evidence that a PBIX report or the DAX measures have been executed in Power BI Desktop**.

## The business rules behind these numbers

1. Compare all **eight original CSV columns** when removing exact duplicates; don't deduplicate by `OrderID` alone.
2. Keep a separate exception list for rows with blank `Quantity` after deduplication. Don't treat a missing quantity as 0 or 1.
3. Only the remaining reportable rows contribute to revenue.
4. Trim and standardize `Region` to `East`, `North`, `South`, or `West`.
5. Parse both `yyyy-MM-dd` and `dd/MM/yyyy` as **October 2026** dates.
6. Strip `₹` and thousands separators from `UnitPrice`, convert it to numeric, and calculate `LineTotal = Quantity × UnitPrice`.

## Overall reconciliation

| Check | Expected |
|---|---:|
| Raw CSV rows | 125 |
| Exact duplicate rows | 5 |
| Unique rows after deduplication | 120 |
| Unique rows with missing Quantity (exceptions) | 4 |
| Reportable rows | **116** |
| Distinct reportable OrderIDs | **116** |
| Reportable revenue | **₹3,29,570.00** |
| Average order value (revenue / 116 orders) | **₹2,841.12** |
| Unique rows with blank CustomerName | 6 |
| Unique rows with blank PaymentMethod | 3 |

**Note:** The blank CustomerName/PaymentMethod counts use all **120 unique rows**, including exception rows. They are data-quality indicators, not necessarily the counts after filtering to the 116 reportable rows.

## Reconcile by region

| Standardized region | Reportable orders | Revenue (INR) |
|---|---:|---:|
| East | 28 | ₹63,316.00 |
| North | 41 | ₹1,45,637.00 |
| South | 18 | ₹59,024.00 |
| West | 29 | ₹61,593.00 |
| **Total** | **116** | **₹3,29,570.00** |

## Reconcile by product

| Product | Reportable orders | Revenue (INR) |
|---|---:|---:|
| Desk Lamp | 13 | ₹35,024.00 |
| Laptop Stand | 22 | ₹65,823.00 |
| Monitor Riser | 20 | ₹59,219.00 |
| Notebook | 18 | ₹70,269.00 |
| USB Hub | 22 | ₹46,340.00 |
| Wireless Mouse | 21 | ₹52,895.00 |
| **Total** | **116** | **₹3,29,570.00** |

Your total orders and revenue must reconcile independently across both breakdowns.

## Missing-quantity exceptions

The following **synthetic** OrderIDs have blank Quantity after removing exact duplicates. Exclude them from the reported revenue **but show that they were excluded**:

- `DTS-0007`
- `DTS-0030`
- `DTS-0061`
- `DTS-0099`

You can create a separate exceptions table with the OrderID, date, region, product, and reason `Missing Quantity`.

## Debugging a mismatch

| Symptom | First check |
|---|---|
| More than 116 reportable rows | Exact duplicates were not removed, or blank Quantity was included |
| Region totals don't reconcile | Leading/trailing spaces or inconsistent capitalization in Region |
| Product totals don't reconcile | Revenue uses the wrong row set or UnitPrice remained text |
| Revenue differs but counts match | Currency symbol, comma, Quantity conversion, or the `LineTotal` formula |
| Dates appear outside October | `dd/MM/yyyy` parsed as `MM/dd/yyyy` |
| Average order value differs | Confirm the denominator is 116 distinct reportable orders, not 125 raw records |

## What to present to a stakeholder

> For this **fictional training dataset**, reported October sales total **₹3,29,570** across **116 reportable orders**. We removed five exact duplicates, retained four missing-quantity rows in an exceptions list, and excluded those four from reported revenue under the exercise's stated policy. A real business owner would need to approve the missing-quantity treatment before applying it to production reporting.

Continue with the [guided walkthrough](../docs/START_HERE.md), [Power Query solution](power_query_steps.md), and [DAX examples](dax_measures.md). For automated dataset-level checks, run `python scripts/verify_dataset.py` from the repository root.
