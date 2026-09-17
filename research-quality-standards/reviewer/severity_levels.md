# Severity Levels

Version: 0.2.0
Last updated: 2026-09-17

## Definitions

- `BLOCKER`: artifact must not be delivered or merged until resolved; use for unsafe, invalid, or unreviewable high-stakes conditions
- `ERROR`: defect that must be fixed or explicitly waived before advancement at `DRAFT` and `SUBMISSION`
- `WARNING`: significant issue that should be fixed before the next stage
- `STYLE`: preferred improvement that usually does not affect validity or usability

`REVIEW_UNAVAILABLE` is a review status, not a finding severity. Do not report zero findings as a completed pass when review could not run.

## Escalation Rule

Treat missing or weak items more strictly as stage rises:

- `EXPLORATORY`: note major risks, but do not expect publication-grade polish
- `ROUGH_DRAFT`: structure should exist, but incomplete items may remain
- `DRAFT`: core reproducibility, evidence, and provenance expectations apply fully
- `SUBMISSION`: reader-facing consistency and compliance should be complete

## Reporting Rule

Each issue should include:

- severity
- location
- description
- why it matters
- required fix or suggested fix
