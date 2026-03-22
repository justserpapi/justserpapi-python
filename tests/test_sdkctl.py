import json
import tempfile
import unittest
from pathlib import Path

from scripts import sdkctl


FIXTURES = Path(__file__).resolve().parent / "fixtures"


class GovernanceValidationTest(unittest.TestCase):
    def test_governance_passes_on_sample_spec(self) -> None:
        spec = sdkctl.load_spec(FIXTURES / "sample-openapi.json")
        result = sdkctl.validate_governance(spec)
        self.assertEqual([], result.errors)

    def test_governance_requires_success_schema(self) -> None:
        spec = sdkctl.load_spec(FIXTURES / "sample-openapi.json")
        spec["paths"]["/api/v1/google/search"]["get"]["responses"]["200"] = {
            "description": "Missing schema"
        }
        result = sdkctl.validate_governance(spec)
        self.assertTrue(any("must declare a response schema" in error for error in result.errors))

    def test_governance_rejects_python_operation_id_collisions(self) -> None:
        spec = sdkctl.load_spec(FIXTURES / "sample-openapi.json")
        spec["paths"]["/api/v1/google/maps/search"]["get"]["operationId"] = "search_google"
        result = sdkctl.validate_governance(spec)
        self.assertTrue(any("Python normalization" in error for error in result.errors))

    def test_breaking_change_detection_flags_removed_operation(self) -> None:
        base = sdkctl.load_spec(FIXTURES / "breaking-base-openapi.json")
        head = sdkctl.load_spec(FIXTURES / "breaking-head-openapi.json")
        issues = sdkctl.detect_breaking_changes(base, head)
        self.assertTrue(any("Removed operation GET /widgets/{widgetId}" in issue for issue in issues))

    def test_template_rendering_requires_all_values(self) -> None:
        rendered = sdkctl.render_template_text(
            "package {{PACKAGE_NAME}} version {{SPEC_VERSION}}",
            {"PACKAGE_NAME": "justserpapi", "SPEC_VERSION": "1.2.3"},
        )
        self.assertEqual("package justserpapi version 1.2.3", rendered)


class MetadataTest(unittest.TestCase):
    def test_write_metadata_file(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir_name:
            output_dir = Path(temp_dir_name)
            sdkctl.write_metadata(
                output_dir=output_dir,
                manifest={"generator": {"version": "7.20.0"}},
                language="python",
                spec_path=Path("/repo/openapi/justserpapi.openapi.json"),
                spec_version_value="1.0.0",
            )
            payload = json.loads((output_dir / "sdk-origin.json").read_text(encoding="utf-8"))
            self.assertEqual("python", payload["language"])
            self.assertEqual("1.0.0", payload["specVersion"])


if __name__ == "__main__":
    unittest.main()
