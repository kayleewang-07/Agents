# Agent Experience Log

Use [the entry template](../templates/operations/agent_experience_log_entry.md) to record Tier 2 sessions, reviewed Tier 1 sessions, and review behavior that yields a reusable lesson.

## 2026-05-06: Reviewer calibration

- Task: tightened deployment policy, added experience logging, and refined Python helpers after external review.
- Review: Claude; 0 BLOCKER, 1 ERROR, 13 WARNING, 1 STYLE.
- Outcome: adopted 7 findings, partly adopted 2, rejected 5.
- Lesson: the reviewer found useful missing fallback and logging expectations, but misclassified an existing nonzero exit path and sometimes demanded production-grade behavior from intentionally scoped starter tools.
- Guardrail: reviewers must distinguish true defects, documented limitations, and scope-expanding overreach.

## 2026-05-13: Maintenance follow-through

- Task: tuned reviewer and template guidance using the prior calibration entry.
- Review: external review unavailable; deterministic verification used and disclosed.
- Outcome: adopted 3 improvements and rejected a broad rewrite unsupported by one experience.
- Lesson: no review is better than fabricated review, and one experience should produce targeted calibration rather than wholesale standards changes.
- Guardrail: use `REVIEW_UNAVAILABLE` explicitly and preserve deterministic verification and human-review cautions.
