#!/usr/bin/env python3
"""Validate the repository's single Agent Skill."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "preferences-validate"
SKILL_FILE = SKILL_DIR / "SKILL.md"
PLACEHOLDER = SKILL_DIR / ".gitkeep"
MAX_LINES = 500
LINK_PATTERN = re.compile(
    r"(?<!!)\[[^\]]+\]\(\s*(?:<([^>]+)>|([^\s)]+))"
)
FRONTMATTER_KEY = re.compile(r"^([A-Za-z][A-Za-z0-9_-]*):\s*(.*?)\s*$")


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def parse_frontmatter(text: str, errors: list[str]) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        fail("SKILL.md must start with YAML frontmatter.", errors)
        return {}

    try:
        end = next(index for index, line in enumerate(lines[1:], 1) if line.strip() == "---")
    except StopIteration:
        fail("SKILL.md frontmatter must have a closing '---' line.", errors)
        return {}

    metadata: dict[str, str] = {}
    for line in lines[1:end]:
        match = FRONTMATTER_KEY.match(line)
        if match:
            metadata[match.group(1)] = match.group(2).strip("\"'")
    return metadata


def validate_links(text: str, errors: list[str]) -> None:
    skill_root = SKILL_DIR.resolve()
    for match in LINK_PATTERN.finditer(text):
        target = match.group(1) or match.group(2)
        if not target:
            continue

        parsed = urlsplit(target)
        if parsed.scheme or target.startswith(("#", "/")):
            continue

        relative_target = unquote(parsed.path)
        if not relative_target:
            continue

        candidate = (SKILL_DIR / relative_target).resolve()
        try:
            candidate.relative_to(skill_root)
        except ValueError:
            fail(f"Local reference escapes the skill directory: {target}", errors)
            continue

        if not candidate.exists():
            fail(f"Broken local reference in SKILL.md: {target}", errors)


def main() -> int:
    errors: list[str] = []

    if not SKILL_DIR.is_dir():
        fail(f"Missing skill directory: {SKILL_DIR.relative_to(ROOT)}", errors)
    elif not SKILL_FILE.exists():
        if PLACEHOLDER.exists():
            print(
                "SKILL.md is not present; the repository scaffold placeholder is "
                "still active."
            )
            return 0
        fail(f"Missing required file: {SKILL_FILE.relative_to(ROOT)}", errors)
    else:
        if PLACEHOLDER.exists():
            fail(
                "Remove skills/preferences-validate/.gitkeep after copying SKILL.md.",
                errors,
            )

        text = SKILL_FILE.read_text(encoding="utf-8")
        lines = text.splitlines()
        metadata = parse_frontmatter(text, errors)

        if len(lines) > MAX_LINES:
            fail(
                f"SKILL.md is {len(lines)} lines; the maximum is {MAX_LINES}.",
                errors,
            )
        if metadata.get("name") != "preferences-validate":
            fail(
                "SKILL.md frontmatter must set name: preferences-validate.",
                errors,
            )
        if not metadata.get("description", "").strip():
            fail("SKILL.md frontmatter must include a non-empty description.", errors)

        validate_links(text, errors)

    if errors:
        print("Skill validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Skill validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
