# Review Report Schema

Version: 0.2.0
Last updated: 2026-09-17

Reviewer outputs should follow this structure.

## Header

- Artifact name
- Declared or inferred genre
- Declared or inferred stage
- Reviewer identity
- Standards files applied

## Sections

1. `Verdict`
   One of:
   - `PASS`
   - `PASS_WITH_WARNINGS` (no BLOCKER or ERROR findings)
   - `REVISIONS_REQUIRED` (one or more ERROR findings, no BLOCKER)
   - `BLOCKED` (one or more BLOCKER findings)
   - `REVIEW_UNAVAILABLE` (review could not be completed; not a pass)

2. `Counts`
   - number of `BLOCKER`s
   - number of `ERROR`s
   - number of `WARNING`s
   - number of `STYLE` items

3. `Blocking Issues`
   `BLOCKER` and `ERROR` findings. Each should include location and repair instruction.

4. `Warnings`
   Material issues that should be corrected before the next stage.

5. `Style`
   Non-blocking suggestions.

6. `Missing Information`
   Items the reviewer could not verify because required context or provenance was absent.

7. `Suggested Repair Instructions`
   Short, actionable instructions aimed at the author or repairing agent.

8. `Human Cautions`
   Brief summary of any residual risks or judgment calls a PI should see.

For `REVIEW_UNAVAILABLE`, give the cause, inputs or access needed, and which deterministic checks remain possible. Do not fabricate finding counts.

Use `templates/operations/referee_report_template.md`. The severity definitions are in `severity_levels.md` and reviewer conduct is in `review_contract.md`.
