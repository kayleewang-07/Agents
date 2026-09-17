import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


class RepositoryIntegrityTests(unittest.TestCase):
    def test_required_workflow_assets_exist(self) -> None:
        required = (
            "docs/AGENT_EXPERIENCE_LOG.md",
            "reviewer/review_contract.md",
            "templates/operations/agent_experience_log_entry.md",
            "templates/operations/final_report_template.md",
            "templates/operations/progress_log_template.md",
            "templates/operations/referee_report_template.md",
        )
        missing = [path for path in required if not (REPO_ROOT / path).exists()]
        self.assertEqual([], missing)

    def test_critical_markdown_links_resolve(self) -> None:
        documents = (
            "docs/workflows/review_workflow.md",
            "docs/workflows/context_sync.md",
            "standards/INDEX.md",
            "templates/INDEX.md",
        )
        missing = []
        for relative_document in documents:
            document = REPO_ROOT / relative_document
            for target in MARKDOWN_LINK.findall(document.read_text(encoding="utf-8")):
                if target.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                resolved = (document.parent / target.split("#", 1)[0]).resolve()
                if not resolved.exists():
                    missing.append(f"{relative_document}: {target}")
        self.assertEqual([], missing)

    def test_reviewer_contract_uses_one_vocabulary(self) -> None:
        required_severities = {"BLOCKER", "ERROR", "WARNING", "STYLE"}
        required_verdicts = {
            "PASS",
            "PASS_WITH_WARNINGS",
            "REVISIONS_REQUIRED",
            "BLOCKED",
            "REVIEW_UNAVAILABLE",
        }
        severity_text = (REPO_ROOT / "reviewer/severity_levels.md").read_text(encoding="utf-8")
        schema_text = (REPO_ROOT / "reviewer/review_report_schema.md").read_text(encoding="utf-8")
        template_text = (REPO_ROOT / "templates/operations/referee_report_template.md").read_text(encoding="utf-8")
        for token in required_severities:
            self.assertIn(token, severity_text)
            self.assertIn(token, template_text)
        for token in required_verdicts:
            self.assertIn(token, schema_text)
            self.assertIn(token, template_text)

        obsolete = ("PASS WITH MINOR ISSUES", "NEEDS REVISION", "SERIOUS PROBLEMS")
        governed_files = (
            "reviewer/review_contract.md",
            "reviewer/review_report_schema.md",
            "standards/formats/python/reviewer_prompt.md",
            "standards/formats/python_stats/reviewer_prompt.md",
            "templates/operations/referee_report_template.md",
        )
        for relative_path in governed_files:
            text = (REPO_ROOT / relative_path).read_text(encoding="utf-8")
            for token in obsolete:
                self.assertNotIn(token, text, relative_path)

    def test_legacy_interview_template_points_to_canonical_template(self) -> None:
        legacy = REPO_ROOT / "templates/interviews/interview_notes_template.md"
        canonical = REPO_ROOT / "templates/surveys/interview_notes_template.md"
        self.assertTrue(canonical.exists())
        self.assertIn("../surveys/interview_notes_template.md", legacy.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
