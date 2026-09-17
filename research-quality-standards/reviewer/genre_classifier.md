# Genre Classifier

Version: 0.2.0
Last updated: 2026-09-17

Use this classifier before review. If multiple genres apply, choose `mixed` and load `standards/general.md` plus no more than three specific standards files.

## Allowed Genres

- `readme`
- `software_code`
- `stats_code`
- `statistical_results`
- `writing`
- `interviews`
- `llm_agent_work`
- `data_cleaning`
- `security`
- `testing`
- `standards_package`
- `mixed`

## Decision Rules

- Use `readme` for project onboarding documents whose main job is to explain setup, execution, dependencies, inputs, outputs, and workflow.
- Use `software_code` for general scripts, utilities, application logic, and automation code.
- Use `stats_code` for code that cleans data, constructs variables, estimates models, or generates statistical outputs.
- Use `statistical_results` for reader-facing tables, regression outputs, simulation results, and empirical summaries.
- Use `writing` for manuscripts, memos, policy briefs, reports, and structured prose.
- Use `interviews` for interview notes, summaries, transcripts, and qualitative field materials.
- Add `llm_agent_work` whenever an LLM or agent produced a material part of the artifact.
- Add `data_cleaning` for raw-to-analysis transformations, merge pipelines, and recoding workflows.
- Add `security` when credentials, permissions, sensitive data, external services, or deployment are in scope.
- Add `testing` for executable changes and verification plans.
- Use `standards_package` for repositories whose primary output is standards, templates, review guidance, or validators.

## Reviewer Loading Rule

Always load:

- `standards/general.md`

Then load:

- one primary genre standard
- optional `standards/llm_agent_work.md` if applicable
- up to two more specific standards files only if clearly necessary

Safety, privacy, correctness, and reproducibility rules override genre or format preferences. If two standards still conflict on one of those dimensions, stop and surface the conflict rather than choosing silently.
