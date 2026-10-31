#!/usr/bin/env python3
"""Validate DataTalksWithSaud's synthetic Power BI sales challenge."""
from pathlib import Path
import csv
from collections import Counter
from decimal import Decimal
from datetime import datetime
import json

ROOT = Path(__file__).resolve().parents[1]
FIELDS = ['OrderID', 'OrderDate', 'Region', 'Product', 'Quantity', 'UnitPrice', 'CustomerName', 'PaymentMethod']
with (ROOT / 'data/sales_dirty.csv').open(encoding='utf-8-sig', newline='') as f:
    reader = csv.DictReader(f)
    assert reader.fieldnames == FIELDS, f"Unexpected fields: {reader.fieldnames}"
    raw = list(reader)
seen = set()
unique = []
for row in raw:
    key = tuple(row[c] for c in FIELDS)
    if key not in seen:
        seen.add(key)
        unique.append(row)
missing = [r for r in unique if not r['Quantity'].strip()]
reportable = [r for r in unique if r['Quantity'].strip()]
revenue = Decimal('0')
regions = Counter()
for row in reportable:
    s = row['OrderDate']
    if '-' in s:
        dt = datetime.strptime(s, '%Y-%m-%d')
    else:
        dt = datetime.strptime(s, '%d/%m/%Y')
    assert dt.year == 2026 and dt.month == 10
    region = row['Region'].strip().title()
    assert region in {'North','South','East','West'}
    regions[region] += 1
    price = Decimal(row['UnitPrice'].replace('₹','').replace(',',''))
    revenue += Decimal(row['Quantity']) * price
out = {
    'raw_rows': len(raw),
    'exact_duplicates': len(raw) - len(unique),
    'rows_after_deduplication': len(unique),
    'missing_quantity_unique_rows': len(missing),
    'blank_customer_unique_rows': sum(not x['CustomerName'].strip() for x in unique),
    'blank_payment_method_unique_rows': sum(not x['PaymentMethod'].strip() for x in unique),
    'reportable_rows': len(reportable),
    'total_sales_inr': f'{revenue:.2f}',
    'distinct_reportable_orders': len({r['OrderID'] for r in reportable}),
}
expected = json.loads((ROOT / 'data/expected_summary.json').read_text(encoding='utf-8'))
assert out == expected, f'Expected: {expected}; Actual: {out}'
print('PASS: synthetic CSV and expected_summary.json match.')
print(json.dumps(out, indent=2))
