# Data Cleaning Standards

Version: 0.1.0
Last updated: 2026-09-17

Use for code or documentation that transforms raw data into analysis-ready files. Apply alongside the relevant language and statistical-code standards.

## Required practices

- Never overwrite raw data; write cleaned and derived outputs separately.
- Document inputs, outputs, merge keys, row drops, renames, recodes, missingness rules, duplicate handling, and manual corrections.
- Log row counts around major filters, merges, deduplication, and aggregation.
- Check expected key uniqueness, merge success, missingness in key variables, ranges, duplicates, and impossible dates or values.
- Keep outputs traceable to source inputs and generation code, with a version or date and a data dictionary for derived variables.

## Review severity

Use `BLOCKER` when a workflow risks corrupting raw data or produces an untraceable high-stakes output. Use `ERROR` for unchecked merge failures, unexplained row loss, or undocumented key-variable construction that must be repaired before use.
