#!/usr/bin/env python3
"""OpenAPI-first SDK orchestration for multi-repo releases."""

from __future__ import annotations

import argparse
import ast
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Set, Tuple
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

try:
    import yaml  # type: ignore
except ImportError:  # pragma: no cover - optional dependency for YAML specs.
    yaml = None


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST_PATH = ROOT / "config" / "sdk-manifest.json"
HTTP_METHODS = ("get", "put", "post", "delete", "options", "head", "patch", "trace")


class CLIError(RuntimeError):
    """Raised for actionable command-line failures."""


@dataclass
class ValidationResult:
    errors: List[str]
    warnings: List[str]


def log(message: str) -> None:
    print(message, file=sys.stderr)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def remove_path(path: Path) -> None:
    if path.is_dir() and not path.is_symlink():
        shutil.rmtree(path)
    elif path.exists():
        path.unlink()


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(read_text(path))


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--manifest",
        default=str(DEFAULT_MANIFEST_PATH),
        help="Path to the central SDK manifest JSON file.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    fetch_parser = subparsers.add_parser("fetch-spec", help="Fetch the canonical OpenAPI document.")
    fetch_parser.add_argument("--source-url", help="Override the spec source URL.")
    fetch_parser.add_argument("--output", help="Override the spec output path.")
    fetch_parser.add_argument(
        "--header",
        action="append",
        default=[],
        help="Extra request header in KEY=VALUE format. Repeatable.",
    )

    validate_parser = subparsers.add_parser("validate-spec", help="Validate spec structure and governance.")
    validate_parser.add_argument("--spec", help="Override the spec path.")
    validate_parser.add_argument(
        "--skip-generator-validate",
        action="store_true",
        help="Skip `openapi-generator validate`.",
    )

    examples_parser = subparsers.add_parser(
        "validate-examples",
        help="Statically validate Python examples in Markdown documentation.",
    )
    examples_parser.add_argument(
        "paths",
        nargs="*",
        help="Optional Markdown paths. Defaults to README.md and docs/**/*.md.",
    )

    breaking_parser = subparsers.add_parser("breaking-check", help="Detect breaking spec changes.")
    breaking_parser.add_argument("--base", help="Override the baseline spec path.")
    breaking_parser.add_argument("--head", help="Override the head spec path.")

    generate_parser = subparsers.add_parser("generate", help="Generate SDK workspaces for one or more languages.")
    generate_parser.add_argument("--spec", help="Override the spec path.")
    generate_parser.add_argument(
        "--languages",
        help="Comma separated language list. Defaults to all configured languages.",
    )
    generate_parser.add_argument(
        "--workspace",
        help="Override the generation workspace directory.",
    )
    generate_parser.add_argument(
        "--clean",
        action="store_true",
        help="Delete previous workspace outputs before generation.",
    )

    sync_parser = subparsers.add_parser("sync-repos", help="Sync generated SDKs into target Git repositories.")
    sync_parser.add_argument(
        "--languages",
        help="Comma separated language list. Defaults to all configured languages.",
    )
    sync_parser.add_argument(
        "--workspace",
        help="Override the generation workspace directory.",
    )
    sync_parser.add_argument("--spec", help="Override the spec path.")
    sync_parser.add_argument(
        "--repos-dir",
        help="Override the local repositories cache directory.",
    )
    sync_parser.add_argument("--push", action="store_true", help="Push commits to remotes after syncing.")
    sync_parser.add_argument("--tag", action="store_true", help="Create and push a release tag in each repo.")
    sync_parser.add_argument(
        "--github-token-env",
        default="SDK_REPO_PUSH_TOKEN",
        help="Environment variable containing a GitHub token for authenticated pushes.",
    )
    sync_parser.add_argument("--dry-run", action="store_true", help="Render actions without mutating repos.")

    return parser.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)
    manifest = load_manifest(Path(args.manifest))

    try:
        if args.command == "fetch-spec":
            fetch_spec(args, manifest)
        elif args.command == "validate-spec":
            validate_spec_command(args, manifest)
        elif args.command == "validate-examples":
            validate_examples_command(args)
        elif args.command == "breaking-check":
            breaking_check_command(args, manifest)
        elif args.command == "generate":
            generate_command(args, manifest)
        elif args.command == "sync-repos":
            sync_repos_command(args, manifest)
        else:  # pragma: no cover - argparse ensures this never happens.
            raise CLIError("Unknown command: %s" % args.command)
    except CLIError as exc:
        log("error: %s" % exc)
        return 1
    return 0


def load_manifest(path: Path) -> Dict[str, Any]:
    if not path.exists():
        raise CLIError("Manifest not found: %s" % path)
    manifest = load_json(path)
    if "languages" not in manifest or not manifest["languages"]:
        raise CLIError("Manifest must define at least one language.")
    return manifest


def resolve_path(raw_path: str) -> Path:
    path = Path(raw_path)
    if not path.is_absolute():
        path = ROOT / path
    return path


def display_path(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def resolve_spec_path(manifest: Dict[str, Any], override: Optional[str] = None) -> Path:
    raw_path = override or manifest["spec"]["path"]
    path = resolve_path(raw_path)
    if not path.exists():
        raise CLIError("Spec file not found: %s" % path)
    return path


def resolve_languages(manifest: Dict[str, Any], raw_languages: Optional[str] = None) -> List[str]:
    configured = list(manifest["languages"].keys())
    if not raw_languages:
        return configured
    requested = [item.strip() for item in raw_languages.split(",") if item.strip()]
    unknown = [name for name in requested if name not in manifest["languages"]]
    if unknown:
        raise CLIError("Unknown languages requested: %s" % ", ".join(unknown))
    return requested


def load_spec(path: Path) -> Dict[str, Any]:
    suffix = path.suffix.lower()
    content = read_text(path)

    if suffix == ".json":
        return json.loads(content)

    if suffix in (".yaml", ".yml"):
        if yaml is None:
            raise CLIError(
                "PyYAML is required to load YAML specs. Install it or switch to JSON."
            )
        data = yaml.safe_load(content)
        if not isinstance(data, dict):
            raise CLIError("Expected a mapping at the root of %s" % path)
        return data

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        if yaml is None:
            raise CLIError("Unsupported spec format for %s" % path)
        data = yaml.safe_load(content)
        if not isinstance(data, dict):
            raise CLIError("Expected a mapping at the root of %s" % path)
        return data


def spec_version(spec: Dict[str, Any]) -> str:
    version = spec.get("info", {}).get("version")
    if not version:
        raise CLIError("Spec info.version is required.")
    return str(version)


def fetch_spec(args: argparse.Namespace, manifest: Dict[str, Any]) -> None:
    source_url = args.source_url or manifest["spec"].get("source_url")
    output_path = resolve_path(args.output or manifest["spec"]["path"])
    if not source_url:
        raise CLIError("No spec source URL configured.")

    headers = parse_headers(args.header)
    api_key = os.getenv("JUSTSERPAPI_API_KEY")
    if api_key and "X-API-Key" not in headers:
        headers["X-API-Key"] = api_key

    request = Request(source_url, headers=headers)
    log("Fetching spec from %s" % source_url)
    try:
        with urlopen(request) as response:
            payload = response.read()
            content_type = response.headers.get("Content-Type", "")
    except HTTPError as exc:
        raise CLIError(
            "Unable to fetch spec from %s: HTTP %s" % (source_url, exc.code)
        ) from exc
    except URLError as exc:
        raise CLIError("Unable to fetch spec from %s: %s" % (source_url, exc)) from exc

    output_path.parent.mkdir(parents=True, exist_ok=True)
    if "json" in content_type.lower():
        try:
            parsed = json.loads(payload.decode("utf-8"))
        except json.JSONDecodeError:
            output_path.write_bytes(payload)
        else:
            write_text(output_path, json.dumps(parsed, indent=2, sort_keys=True) + "\n")
    else:
        output_path.write_bytes(payload)
    log("Saved spec to %s" % output_path)


def parse_headers(header_items: Sequence[str]) -> Dict[str, str]:
    headers: Dict[str, str] = {}
    for item in header_items:
        if "=" not in item:
            raise CLIError("Header must be KEY=VALUE: %s" % item)
        key, value = item.split("=", 1)
        headers[key.strip()] = value.strip()
    return headers


def validate_spec_command(args: argparse.Namespace, manifest: Dict[str, Any]) -> None:
    spec_path = resolve_spec_path(manifest, args.spec)
    spec = load_spec(spec_path)
    result = validate_governance(spec)
    for warning in result.warnings:
        log("warning: %s" % warning)
    if result.errors:
        for error in result.errors:
            log("error: %s" % error)
        raise CLIError("Governance validation failed for %s" % spec_path)

    if not args.skip_generator_validate:
        ensure_generator_validate(manifest, spec_path)
    log("Spec validation passed for %s" % spec_path)


def validate_examples_command(args: argparse.Namespace) -> None:
    paths = documentation_paths(args.paths)
    result = validate_examples(paths)
    for warning in result.warnings:
        log("warning: %s" % warning)
    if result.errors:
        for error in result.errors:
            log("error: %s" % error)
        raise CLIError("Documentation example validation failed.")
    log("Documentation examples passed for %s" % ", ".join(display_path(path) for path in paths))


def validate_governance(spec: Dict[str, Any]) -> ValidationResult:
    errors: List[str] = []
    warnings: List[str] = []

    openapi_version = str(spec.get("openapi", ""))
    if not openapi_version.startswith("3."):
        errors.append("OpenAPI version must be 3.x, found %r." % openapi_version)

    info = spec.get("info", {})
    if not info.get("title"):
        errors.append("info.title is required.")
    if not info.get("version"):
        errors.append("info.version is required.")

    if not spec.get("servers"):
        errors.append("At least one server entry is required.")

    paths = spec.get("paths", {})
    if not paths:
        errors.append("Spec must define at least one path.")

    security_schemes = spec.get("components", {}).get("securitySchemes", {})
    api_key_auth = security_schemes.get("ApiKeyAuth")
    if not api_key_auth:
        errors.append("components.securitySchemes.ApiKeyAuth is required.")
    else:
        if api_key_auth.get("type") != "apiKey":
            errors.append("ApiKeyAuth.type must be 'apiKey'.")
        if api_key_auth.get("in") != "header":
            errors.append("ApiKeyAuth.in must be 'header'.")
        if api_key_auth.get("name") != "X-API-Key":
            errors.append("ApiKeyAuth.name must be 'X-API-Key'.")

    seen_operation_ids: Set[str] = set()
    duplicate_operation_ids: Set[str] = set()
    normalized_operation_ids: Dict[str, str] = {}
    normalized_conflicts: Set[str] = set()
    for path, method, operation, path_item in iter_operations(spec):
        label = "%s %s" % (method.upper(), path)
        operation_id = operation.get("operationId")
        if not operation.get("tags"):
            errors.append("%s is missing tags." % label)
        if not operation_id:
            errors.append("%s is missing operationId." % label)
        elif operation_id in seen_operation_ids:
            duplicate_operation_ids.add(str(operation_id))
        else:
            seen_operation_ids.add(str(operation_id))
            normalized = normalize_operation_id(str(operation_id))
            existing = normalized_operation_ids.get(normalized)
            if existing and existing != str(operation_id):
                normalized_conflicts.add("%s <-> %s" % (existing, operation_id))
            else:
                normalized_operation_ids[normalized] = str(operation_id)

        responses = operation.get("responses", {})
        if not any(status.startswith("2") or status == "default" for status in responses):
            errors.append("%s must define at least one success response." % label)
        for status, response in responses.items():
            if str(status).startswith("2") and str(status) not in {"204", "205", "304"}:
                if not response_has_schema(response):
                    errors.append(
                        "%s success response %s must declare a response schema."
                        % (label, status)
                    )

        for required_status in ("401", "403", "500"):
            if required_status not in responses:
                warnings.append("%s should document %s responses." % (label, required_status))

        params = merged_parameters(path_item, operation)
        if not any(param.get("in") == "query" for param in params):
            warnings.append("%s has no query parameters. Double-check if the API shape is correct." % label)

    if duplicate_operation_ids:
        errors.append(
            "operationId values must be unique. Duplicates: %s"
            % ", ".join(sorted(duplicate_operation_ids))
        )
    if normalized_conflicts:
        errors.append(
            "operationId values must remain unique after Python normalization. Conflicts: %s"
            % ", ".join(sorted(normalized_conflicts))
        )

    return ValidationResult(errors=errors, warnings=warnings)


def normalize_operation_id(value: str) -> str:
    snake = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", value)
    snake = re.sub(r"[^a-zA-Z0-9]+", "_", snake)
    snake = re.sub(r"_+", "_", snake)
    return snake.strip("_").lower()


def response_has_schema(response: Any) -> bool:
    if not isinstance(response, dict):
        return False
    content = response.get("content")
    if not isinstance(content, dict):
        return False
    for media in content.values():
        if isinstance(media, dict) and isinstance(media.get("schema"), dict):
            return True
    return False


def iter_operations(spec: Dict[str, Any]) -> Iterable[Tuple[str, str, Dict[str, Any], Dict[str, Any]]]:
    for path, path_item in spec.get("paths", {}).items():
        if not isinstance(path_item, dict):
            continue
        for method in HTTP_METHODS:
            operation = path_item.get(method)
            if isinstance(operation, dict):
                yield str(path), method, operation, path_item


def merged_parameters(path_item: Dict[str, Any], operation: Dict[str, Any]) -> List[Dict[str, Any]]:
    merged: Dict[Tuple[str, str], Dict[str, Any]] = {}
    for parameters in (path_item.get("parameters", []), operation.get("parameters", [])):
        for parameter in parameters:
            if not isinstance(parameter, dict):
                continue
            location = str(parameter.get("in", ""))
            name = str(parameter.get("name", ""))
            if location and name:
                merged[(location, name)] = parameter
    return list(merged.values())


def ensure_generator_validate(manifest: Dict[str, Any], spec_path: Path) -> None:
    generator = manifest["generator"]
    jar_path = ensure_generator_cli(generator["version"], resolve_path(generator["cache_dir"]))
    run(
        ["java", "-jar", str(jar_path), "validate", "-i", str(spec_path)],
        cwd=ROOT,
    )


def ensure_generator_cli(version: str, cache_dir: Path) -> Path:
    cache_dir.mkdir(parents=True, exist_ok=True)
    jar_path = cache_dir / ("openapi-generator-cli-%s.jar" % version)
    if jar_path.exists():
        return jar_path

    url = (
        "https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/"
        "%s/openapi-generator-cli-%s.jar" % (version, version)
    )
    log("Downloading OpenAPI Generator CLI %s" % version)
    request = Request(url)
    try:
        with urlopen(request) as response:
            jar_path.write_bytes(response.read())
    except HTTPError as exc:
        raise CLIError("Unable to download OpenAPI Generator CLI %s" % version) from exc
    return jar_path


def breaking_check_command(args: argparse.Namespace, manifest: Dict[str, Any]) -> None:
    base_path = resolve_path(args.base or manifest["spec"]["baseline_path"])
    head_path = resolve_spec_path(manifest, args.head)
    if not base_path.exists():
        raise CLIError("Baseline spec not found: %s" % base_path)

    breaking = detect_breaking_changes(load_spec(base_path), load_spec(head_path))
    if breaking:
        for issue in breaking:
            log("breaking: %s" % issue)
        raise CLIError("Breaking changes detected between %s and %s" % (base_path, head_path))
    log("No breaking changes detected between %s and %s" % (base_path, head_path))


def detect_breaking_changes(base: Dict[str, Any], head: Dict[str, Any]) -> List[str]:
    issues: List[str] = []
    base_ops = operation_map(base)
    head_ops = operation_map(head)

    removed_ops = sorted(set(base_ops.keys()) - set(head_ops.keys()))
    for path, method in removed_ops:
        issues.append("Removed operation %s %s." % (method.upper(), path))

    for key, base_operation in base_ops.items():
        head_operation = head_ops.get(key)
        if not head_operation:
            continue
        base_path_item = base_operation["path_item"]
        head_path_item = head_operation["path_item"]
        base_op = base_operation["operation"]
        head_op = head_operation["operation"]
        label = "%s %s" % (key[1].upper(), key[0])

        if base_op.get("operationId") != head_op.get("operationId"):
            issues.append("%s changed operationId from %s to %s." % (
                label,
                base_op.get("operationId"),
                head_op.get("operationId"),
            ))

        base_required = {
            parameter_identity(parameter)
            for parameter in merged_parameters(base_path_item, base_op)
            if parameter.get("required")
        }
        head_required = {
            parameter_identity(parameter)
            for parameter in merged_parameters(head_path_item, head_op)
            if parameter.get("required")
        }
        for parameter in sorted(head_required - base_required):
            issues.append("%s added a newly required parameter %s." % (label, parameter))

        base_success = success_responses(base_op)
        head_success = success_responses(head_op)
        if base_success and not head_success:
            issues.append("%s removed all documented success responses." % label)

    return issues


def operation_map(spec: Dict[str, Any]) -> Dict[Tuple[str, str], Dict[str, Any]]:
    mapping: Dict[Tuple[str, str], Dict[str, Any]] = {}
    for path, method, operation, path_item in iter_operations(spec):
        mapping[(path, method)] = {"operation": operation, "path_item": path_item}
    return mapping


def parameter_identity(parameter: Dict[str, Any]) -> str:
    return "%s:%s" % (parameter.get("in"), parameter.get("name"))


def success_responses(operation: Dict[str, Any]) -> Set[str]:
    return {
        str(status)
        for status in operation.get("responses", {})
        if str(status).startswith("2") or str(status) == "default"
    }


def generate_command(args: argparse.Namespace, manifest: Dict[str, Any]) -> None:
    spec_path = resolve_spec_path(manifest, args.spec)
    spec = load_spec(spec_path)
    version = spec_version(spec)
    languages = resolve_languages(manifest, args.languages)
    workspace = resolve_path(
        args.workspace or manifest["release"].get("generated_dir", ".generated")
    )

    if args.clean and workspace.exists():
        shutil.rmtree(workspace)
    workspace.mkdir(parents=True, exist_ok=True)

    generator = manifest["generator"]
    jar_path = ensure_generator_cli(generator["version"], resolve_path(generator["cache_dir"]))

    for language in languages:
        generate_language(
            manifest=manifest,
            language=language,
            spec=spec,
            spec_path=spec_path,
            spec_version_value=version,
            workspace=workspace,
            jar_path=jar_path,
        )
    log("Generated SDK workspaces under %s" % workspace)


def generate_language(
    manifest: Dict[str, Any],
    language: str,
    spec: Dict[str, Any],
    spec_path: Path,
    spec_version_value: str,
    workspace: Path,
    jar_path: Path,
) -> None:
    language_cfg = manifest["languages"][language]
    context = build_context(
        manifest=manifest,
        language=language,
        language_cfg=language_cfg,
        spec=spec,
        spec_path=spec_path,
        spec_version_value=spec_version_value,
    )
    output_dir = workspace / language_cfg.get("output_subdir", language)
    config_template_path = resolve_path(language_cfg["config_template"])

    if output_dir.exists():
        shutil.rmtree(output_dir)

    with tempfile.TemporaryDirectory(prefix="sdkctl-") as temp_dir_name:
        temp_dir = Path(temp_dir_name)
        rendered_config_path = temp_dir / ("%s-config.json" % language)
        render_text_file(config_template_path, rendered_config_path, context)

        command = [
            "java",
            "-jar",
            str(jar_path),
            "generate",
            "-g",
            language_cfg["generator"],
            "-i",
            str(spec_path),
            "-o",
            str(output_dir),
            "-c",
            str(rendered_config_path),
        ]
        global_properties = language_cfg.get("global_properties")
        if global_properties:
            rendered_global = ",".join(
                "%s=%s" % (key, value) for key, value in sorted(global_properties.items())
            )
            command.extend(["--global-property", rendered_global])

        run(command, cwd=ROOT)

    overlay_dir = resolve_path(language_cfg["overlay_dir"])
    render_overlay_tree(overlay_dir, output_dir, context)
    write_smoke_tests(language, output_dir, context)
    write_metadata(output_dir, manifest, language, spec_path, spec_version_value)


def build_context(
    manifest: Dict[str, Any],
    language: str,
    language_cfg: Dict[str, Any],
    spec: Dict[str, Any],
    spec_path: Path,
    spec_version_value: str,
) -> Dict[str, str]:
    service = manifest["service"]
    repo = language_cfg["repo"]
    package = language_cfg["package"]
    context: Dict[str, str] = {
        "SERVICE_NAME": str(service["name"]),
        "SERVICE_DISPLAY_NAME": str(service["display_name"]),
        "SERVICE_DESCRIPTION": str(service["description"]),
        "SPEC_PATH": display_path(spec_path),
        "SPEC_VERSION": str(spec_version_value),
        "GENERATOR_VERSION": str(manifest["generator"]["version"]),
        "DEFAULT_SERVER_URL": str(service["default_server_url"]),
        "LANGUAGE": language,
        "REPO_NAME": str(repo["name"]),
        "REPO_REMOTE": str(repo["remote"]),
        "PACKAGE_NAME": str(package["name"]),
        "PACKAGE_REGISTRY": str(package["registry"]),
        "INFO_TITLE": str(spec.get("info", {}).get("title", service["display_name"])),
        "INFO_VERSION": str(spec_version_value),
    }

    for key, value in language_cfg.items():
        if isinstance(value, str):
            context[key.upper()] = value
        elif isinstance(value, dict):
            for nested_key, nested_value in value.items():
                if isinstance(nested_value, str):
                    context["%s_%s" % (key.upper(), nested_key.upper())] = nested_value
    return context


TEMPLATE_PATTERN = re.compile(r"{{\s*([A-Z0-9_]+)\s*}}")


def render_template_text(template: str, context: Dict[str, str]) -> str:
    def replace(match: re.Match[str]) -> str:
        key = match.group(1)
        if key not in context:
            raise CLIError("Missing template value for %s" % key)
        return context[key]

    return TEMPLATE_PATTERN.sub(replace, template)


def render_text_file(template_path: Path, output_path: Path, context: Dict[str, str]) -> None:
    rendered = render_template_text(read_text(template_path), context)
    write_text(output_path, rendered)


def render_overlay_tree(overlay_dir: Path, output_dir: Path, context: Dict[str, str]) -> None:
    if not overlay_dir.exists():
        return
    for source in sorted(overlay_dir.rglob("*")):
        relative = source.relative_to(overlay_dir)
        if source.is_dir():
            (output_dir / relative).mkdir(parents=True, exist_ok=True)
            continue

        target_relative = relative
        is_template = source.suffix == ".tmpl"
        if is_template:
            target_relative = relative.with_suffix("")
        target_path = output_dir / target_relative
        target_path.parent.mkdir(parents=True, exist_ok=True)

        if is_template:
            rendered = render_template_text(read_text(source), context)
            write_text(target_path, rendered)
        else:
            shutil.copy2(source, target_path)


PYTHON_SNIPPET_PATTERN = re.compile(r"```python\s*\n(.*?)```", re.DOTALL)


def documentation_paths(raw_paths: Optional[Sequence[str]] = None) -> List[Path]:
    if raw_paths:
        return [resolve_path(path) for path in raw_paths]

    paths = [ROOT / "README.md"]
    docs_dir = ROOT / "docs"
    if docs_dir.exists():
        paths.extend(sorted(docs_dir.rglob("*.md")))
    return paths


def validate_examples(paths: Sequence[Path]) -> ValidationResult:
    errors: List[str] = []
    warnings: List[str] = []

    for path in paths:
        if not path.exists():
            errors.append("Documentation file not found: %s" % path)
            continue
        snippets = extract_python_snippets(path)
        if not snippets:
            warnings.append("%s contains no Python examples." % display_path(path))
            continue
        for index, snippet in enumerate(snippets, start=1):
            label = "%s snippet %s" % (display_path(path), index)
            try:
                ast.parse(snippet, filename=str(path))
            except SyntaxError as exc:
                errors.append("%s failed to parse: %s" % (label, exc))
                continue
            if "os." in snippet and not re.search(r"^\s*(import os|from os import )", snippet, re.MULTILINE):
                errors.append("%s references os.* without importing os." % label)

    return ValidationResult(errors=errors, warnings=warnings)


def extract_python_snippets(path: Path) -> List[str]:
    content = read_text(path)
    return [match.group(1).strip() for match in PYTHON_SNIPPET_PATTERN.finditer(content)]


def write_smoke_tests(language: str, output_dir: Path, context: Dict[str, str]) -> None:
    if language == "python":
        smoke_path = output_dir / "tests" / "test_client_smoke.py"
        smoke = """import unittest

import {{PACKAGE_NAME}}


class ConfigurationSmokeTest(unittest.TestCase):
    def test_high_level_client_entrypoint(self) -> None:
        with {{PACKAGE_NAME}}.Client(api_key="test-api-key", base_url="{{DEFAULT_SERVER_URL}}") as client:
            self.assertEqual("test-api-key", client.configuration.api_key["ApiKeyAuth"])
            self.assertIsNotNone(client.configuration.retries)


if __name__ == "__main__":
    unittest.main()
"""
        write_text(smoke_path, render_template_text(smoke, context))
    elif language == "java":
        invoker_package = context["INVOKER_PACKAGE"]
        package_path = invoker_package.replace(".", "/")
        smoke_path = output_dir / "src" / "test" / "java" / package_path / "ApiClientSmokeTest.java"
        smoke = """package {{INVOKER_PACKAGE}};

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class ApiClientSmokeTest {
    @Test
    void supportsBasePathAndApiKeyConfiguration() {
        ApiClient client = new ApiClient();
        client.setBasePath("{{DEFAULT_SERVER_URL}}");
        client.setApiKey("test-api-key");
        assertEquals("{{DEFAULT_SERVER_URL}}", client.getBasePath());
    }
}
"""
        write_text(smoke_path, render_template_text(smoke, context))
    elif language == "go":
        smoke_path = output_dir / "client_smoke_test.go"
        smoke = """package {{PACKAGE_NAME}}

import "testing"

func TestClientConfigurationSmoke(t *testing.T) {
    cfg := NewConfiguration()
    if cfg == nil {
        t.Fatal("expected configuration")
    }

    client := NewAPIClient(cfg)
    if client == nil {
        t.Fatal("expected API client")
    }
}
"""
        write_text(smoke_path, render_template_text(smoke, context))


def write_metadata(
    output_dir: Path,
    manifest: Dict[str, Any],
    language: str,
    spec_path: Path,
    spec_version_value: str,
) -> None:
    metadata = {
        "generatedAt": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "language": language,
        "specPath": display_path(spec_path),
        "specVersion": spec_version_value,
        "generatorVersion": manifest["generator"]["version"],
    }
    write_text(output_dir / "sdk-origin.json", json.dumps(metadata, indent=2, sort_keys=True) + "\n")


def sync_repos_command(args: argparse.Namespace, manifest: Dict[str, Any]) -> None:
    workspace = resolve_path(
        args.workspace or manifest["release"].get("generated_dir", ".generated")
    )
    repos_dir = resolve_path(
        args.repos_dir or manifest["release"].get("repositories_dir", ".repositories")
    )
    languages = resolve_languages(manifest, args.languages)
    spec_path = resolve_spec_path(manifest, args.spec)
    version = spec_version(load_spec(spec_path))
    commit_message = render_template_text(
        manifest["release"]["commit_message"], {"SPEC_VERSION": version}
    )
    tag_name = render_template_text(manifest["release"]["tag_name"], {"SPEC_VERSION": version})

    token = os.getenv(args.github_token_env)
    for language in languages:
        language_cfg = manifest["languages"][language]
        output_dir = workspace / language_cfg.get("output_subdir", language)
        if not output_dir.exists():
            raise CLIError("Generated workspace missing for %s: %s" % (language, output_dir))

        repo_cfg = language_cfg["repo"]
        checkout_dir = repos_dir / repo_cfg["name"]
        if args.dry_run:
            log(
                "[dry-run] would sync %s -> %s (%s)"
                % (output_dir, checkout_dir, repo_cfg["remote"])
            )
            continue

        prepare_checkout(
            checkout_dir=checkout_dir,
            remote=repo_cfg["remote"],
            branch=repo_cfg.get("default_branch", "main"),
            push=args.push,
            token=token,
        )
        sync_directory(output_dir, checkout_dir)
        if not git_has_changes(checkout_dir):
            log("No repo changes for %s" % language)
            continue

        run(["git", "add", "--all"], cwd=checkout_dir)
        run(["git", "commit", "-m", commit_message], cwd=checkout_dir)

        if args.tag:
            run(["git", "tag", "-f", tag_name], cwd=checkout_dir)

        if args.push:
            run(["git", "push", "origin", repo_cfg.get("default_branch", "main")], cwd=checkout_dir)
            if args.tag:
                run(["git", "push", "--force", "origin", tag_name], cwd=checkout_dir)


def prepare_checkout(
    checkout_dir: Path,
    remote: str,
    branch: str,
    push: bool,
    token: Optional[str],
) -> None:
    if not checkout_dir.exists():
        checkout_dir.parent.mkdir(parents=True, exist_ok=True)
        clone_remote = authenticated_remote(remote, token) if push else remote
        run(["git", "clone", "--branch", branch, clone_remote, str(checkout_dir)], cwd=ROOT)
        return

    run(["git", "fetch", "origin"], cwd=checkout_dir)
    run(["git", "checkout", branch], cwd=checkout_dir)
    run(["git", "pull", "--ff-only", "origin", branch], cwd=checkout_dir)


def authenticated_remote(remote: str, token: Optional[str]) -> str:
    if not token:
        return remote
    parsed = urlparse(remote)
    if remote.startswith("git@github.com:"):
        repo_path = remote.split("git@github.com:", 1)[1]
        return "https://x-access-token:%s@github.com/%s" % (token, repo_path)
    if parsed.scheme in ("http", "https") and parsed.netloc == "github.com":
        return "https://x-access-token:%s@github.com%s" % (token, parsed.path)
    return remote


def sync_directory(source_dir: Path, target_dir: Path) -> None:
    protected = {".git"}
    for item in target_dir.iterdir():
        if item.name in protected:
            continue
        remove_path(item)

    for item in source_dir.iterdir():
        destination = target_dir / item.name
        if item.is_dir():
            shutil.copytree(item, destination)
        else:
            shutil.copy2(item, destination)


def git_has_changes(repo_dir: Path) -> bool:
    result = subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=repo_dir,
        check=True,
        capture_output=True,
        text=True,
    )
    return bool(result.stdout.strip())


def run(command: Sequence[str], cwd: Path) -> None:
    log("+ %s" % " ".join(command))
    subprocess.run(command, cwd=cwd, check=True)


if __name__ == "__main__":
    raise SystemExit(main())
