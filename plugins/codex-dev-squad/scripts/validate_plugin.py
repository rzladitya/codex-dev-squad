#!/usr/bin/env python
from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    ".codex-plugin/plugin.json",
    ".mcp.json",
    "README.md",
    "docs/installation-guide.md",
    "docs/usage-sop.md",
    "docs/role-map.md",
    "docs/github-paper-integration.md",
    "docs/handoff-matrix.md",
    "docs/codex-tool-integrations.md",
    "docs/tooling-map.md",
    "skills/research/SKILL.md",
    "skills/pm/SKILL.md",
    "skills/uiux/SKILL.md",
    "skills/frontend/SKILL.md",
    "skills/backend-python/SKILL.md",
    "skills/qa/SKILL.md",
    "skills/devops/SKILL.md",
    "workflows/feature-development.md",
    "workflows/research-agent-sop.md",
    "workflows/pm-agent-sop.md",
    "workflows/uiux-agent-sop.md",
    "workflows/backend-python-agent-sop.md",
    "workflows/frontend-agent-sop.md",
    "workflows/qa-agent-sop.md",
    "workflows/devops-agent-sop.md",
    "workflows/bugfix.md",
    "workflows/release.md",
    "templates/prd.md",
    "templates/github-issue.md",
    "templates/handoff-record.md",
    "templates/api-contract.openapi.yaml",
    "templates/qa-test-plan.md",
]


def main() -> None:
    for json_file in [ROOT / ".codex-plugin/plugin.json", ROOT / ".mcp.json", ROOT / ".app.json"]:
        json.loads(json_file.read_text(encoding="utf-8"))

    missing = [path for path in REQUIRED if not (ROOT / path).exists()]
    if missing:
        raise SystemExit("Missing required files:\n" + "\n".join(missing))

    print("Codex Dev Squad plugin scaffold is valid.")


if __name__ == "__main__":
    main()
