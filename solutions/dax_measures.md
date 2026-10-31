# Suggested DAX measures

Assume the cleaned, reportable table is named `Sales_Reportable` and includes numeric `LineTotal` and a unique text `OrderID` per row. **These measures have not been executed inside Power BI Desktop in this package.**

```DAX
Total Sales = SUM ( Sales_Reportable[LineTotal] )

Reportable Orders = DISTINCTCOUNT ( Sales_Reportable[OrderID] )

Average Order Value = DIVIDE ( [Total Sales], [Reportable Orders] )
```

Format Total Sales and Average Order Value as INR currency. Add these to cards and slice them by `Region` and `Product`.

**Audit visual:** include a small table or card reporting 4 excluded orders due to missing Quantity. Its data source should be the exceptions query, **not** `Sales_Reportable`.

Expected total sales and counts are in `data/expected_summary.json`. For a region or product breakdown, validate that segment totals add up to the overall total.
