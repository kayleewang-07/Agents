# Standards Package Standards

Version: 0.1.0
Last updated: 2026-09-17

Use for repositories whose main products are standards, workflows, templates, reviewer instructions, or validation helpers.

## Required practices

- Explain what the package governs, who should use it, and what remains outside its scope.
- Distinguish normative rules from examples, starter tools, and planned capabilities.
- Give one preferred verification path and its expected success signal.
- Identify deterministic checks, external-review dependencies, and decisions that still require human judgment.
- Keep indexes, counterpart links, reviewer contracts, and referenced templates synchronized in the same change.
- Record known limitations instead of implying complete automation.

Use `BLOCKER` when the package creates unsafe confidence, such as claiming verification that cannot run. Use `ERROR` when required navigation or the documented verification path is broken.

Related template: [standards package README](../templates/README/standards_package_readme_template.md)
