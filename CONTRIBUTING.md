# Contributing to DataTalksWithSaud Power BI Labs

Thanks for helping make practical Power BI learning accessible.

## Contributions welcome

- Reproducible corrections to the synthetic sales exercise.
- Clearer explanations of Power Query or DAX (state the Power BI Desktop version used for testing).
- Accessibility improvements and beginner-friendly documentation.
- New exercises using independently created synthetic data.

## Before submitting a pull request

1. Start from the latest `main` branch and keep changes focused.
2. Describe the problem, the change, and how it was tested.
3. If you modify `data/sales_dirty.csv` or `data/expected_summary.json`, run `python scripts/verify_dataset.py` and document any intended changes to the expected totals.
4. State clearly whether Power BI formulas have actually been run in Power BI Desktop or are illustrative examples.
5. Do not include private, personal, client or employer data; passwords; access tokens; non-public screenshots; paid e-books; or material you are not authorized to redistribute.

## Reporting an issue

Include the exercise step, expected result, actual result, and reproduction steps. For Power Query or DAX errors, include the exact error message and Power BI Desktop version when possible. Do not post real customer or company data in issues.

## License and attribution

Original contributions are accepted under the repository's MIT license. Retain required copyright and third-party license notices. Do not claim third-party work as your own.
