# Testing and Verification Standards

Version: 0.1.0
Last updated: 2026-09-17

Use for code and substantial computational artifacts.

## Required practices

- Do not introduce new failures. When a baseline already fails, distinguish pre-existing failures from regressions.
- Discover project commands from repository instructions, test configuration, package metadata, workflows, and conventional language tooling.
- Run relevant tests, syntax checks, linters, validators, and a focused smoke test before claiming completion.
- Never silently skip verification or claim a check ran when it did not.
- If verification is unavailable, state why, what remains uncertain, and the residual risk.
- Do not weaken tests merely to make a change pass unless the behavior change is intentional and documented.

For high-risk changes that cannot be verified enough to act safely, stop and request human review.
