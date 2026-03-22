import tempfile
import unittest
from pathlib import Path

from scripts import sdkctl


class ExampleValidationTest(unittest.TestCase):
    def test_repository_examples_parse(self) -> None:
        result = sdkctl.validate_examples(
            [
                Path("README.md"),
                Path("docs/GoogleAPIApi.md"),
            ]
        )
        self.assertEqual([], result.errors)

    def test_example_validation_reports_missing_os_import(self) -> None:
        markdown = """# Example

```python
print(os.environ["API_KEY"])
```
"""
        with tempfile.TemporaryDirectory() as temp_dir_name:
            path = Path(temp_dir_name) / "README.md"
            path.write_text(markdown, encoding="utf-8")
            result = sdkctl.validate_examples([path])
            self.assertTrue(any("without importing os" in error for error in result.errors))


if __name__ == "__main__":
    unittest.main()
