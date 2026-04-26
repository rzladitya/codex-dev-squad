#!/usr/bin/env python
"""Minimal stdio MCP server for Codex Dev Squad.

This intentionally avoids external dependencies so the plugin can expose its
role/workflow/template knowledge immediately. It implements the small subset of
JSON-RPC/MCP methods needed for tool discovery and tool calls.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PROTOCOL_VERSION = "2024-11-05"

ROLES = {
    "research": "Discovery, user problems, competitor context, assumptions, and opportunity framing.",
    "pm": "Roadmap, GitHub backlog, user stories, acceptance criteria, and scope control.",
    "uiux": "Paper-based user flows, wireframes, UI specs, and design handoff.",
    "frontend": "Next.js, React, TypeScript UI implementation and API integration.",
    "backend-python": "FastAPI, PostgreSQL, OpenAPI, auth, services, migrations, and backend tests.",
    "qa": "Acceptance testing, Playwright/Pytest coverage, bug reports, and release sign-off.",
    "devops": "Docker, GitHub Actions, environments, deployment, monitoring, backup, and rollback.",
}


def read_message() -> dict[str, Any] | None:
    headers: dict[str, str] = {}
    while True:
        line = sys.stdin.buffer.readline()
        if line == b"":
            return None
        if line in (b"\r\n", b"\n"):
            break
        key, _, value = line.decode("utf-8").partition(":")
        headers[key.lower()] = value.strip()

    length = int(headers.get("content-length", "0"))
    if length <= 0:
        return None
    body = sys.stdin.buffer.read(length)
    return json.loads(body.decode("utf-8"))


def write_message(payload: dict[str, Any]) -> None:
    body = json.dumps(payload, separators=(",", ":")).encode("utf-8")
    sys.stdout.buffer.write(f"Content-Length: {len(body)}\r\n\r\n".encode("ascii"))
    sys.stdout.buffer.write(body)
    sys.stdout.buffer.flush()


def list_files(folder: str, suffix: str) -> list[str]:
    path = ROOT / folder
    if not path.exists():
        return []
    return sorted(file.name for file in path.glob(f"*{suffix}") if file.is_file())


def list_nested_skill_files() -> list[str]:
    path = ROOT / "skills"
    if not path.exists():
        return []
    return sorted(str(file.relative_to(path)).replace("\\", "/") for file in path.glob("*/SKILL.md"))


def read_named_file(folder: str, name: str, suffixes: tuple[str, ...]) -> str:
    safe_name = Path(name).name
    candidates = [ROOT / folder / safe_name]
    for suffix in suffixes:
        if not safe_name.endswith(suffix):
            candidates.append(ROOT / folder / f"{safe_name}{suffix}")

    for candidate in candidates:
        if candidate.exists() and candidate.is_file():
            return candidate.read_text(encoding="utf-8")
    available = ", ".join(list_files(folder, "")) or "none"
    raise ValueError(f"File not found: {name}. Available: {available}")


def tool_definitions() -> list[dict[str, Any]]:
    return [
        {
            "name": "list_roles",
            "description": "List Codex Dev Squad roles and their responsibilities.",
            "inputSchema": {"type": "object", "properties": {}, "additionalProperties": False},
        },
        {
            "name": "list_workflows",
            "description": "List available Codex Dev Squad workflows.",
            "inputSchema": {"type": "object", "properties": {}, "additionalProperties": False},
        },
        {
            "name": "list_templates",
            "description": "List available Codex Dev Squad artifact templates.",
            "inputSchema": {"type": "object", "properties": {}, "additionalProperties": False},
        },
        {
            "name": "list_role_skills",
            "description": "List available Codex Dev Squad role skill files.",
            "inputSchema": {"type": "object", "properties": {}, "additionalProperties": False},
        },
        {
            "name": "list_docs",
            "description": "List available Codex Dev Squad integration and operating documents.",
            "inputSchema": {"type": "object", "properties": {}, "additionalProperties": False},
        },
        {
            "name": "get_role_skill",
            "description": "Read a role skill by role name, for example backend-python or pm.",
            "inputSchema": {
                "type": "object",
                "properties": {"role": {"type": "string"}},
                "required": ["role"],
                "additionalProperties": False,
            },
        },
        {
            "name": "get_workflow",
            "description": "Read a workflow by filename, for example feature-development.md.",
            "inputSchema": {
                "type": "object",
                "properties": {"name": {"type": "string"}},
                "required": ["name"],
                "additionalProperties": False,
            },
        },
        {
            "name": "get_template",
            "description": "Read an artifact template by filename, for example prd.md.",
            "inputSchema": {
                "type": "object",
                "properties": {"name": {"type": "string"}},
                "required": ["name"],
                "additionalProperties": False,
            },
        },
        {
            "name": "get_doc",
            "description": "Read an integration or operating document by filename, for example codex-tool-integrations.md.",
            "inputSchema": {
                "type": "object",
                "properties": {"name": {"type": "string"}},
                "required": ["name"],
                "additionalProperties": False,
            },
        },
    ]


def call_tool(name: str, arguments: dict[str, Any]) -> str:
    if name == "list_roles":
        return "\n".join(f"- {role}: {summary}" for role, summary in ROLES.items())
    if name == "list_workflows":
        return "\n".join(f"- {file}" for file in list_files("workflows", ".md"))
    if name == "list_templates":
        return "\n".join(f"- {file}" for file in list_files("templates", ""))
    if name == "list_role_skills":
        return "\n".join(f"- {file}" for file in list_nested_skill_files())
    if name == "list_docs":
        return "\n".join(f"- {file}" for file in list_files("docs", ".md"))
    if name == "get_role_skill":
        role = Path(arguments["role"]).name
        skill_file = ROOT / "skills" / role / "SKILL.md"
        if not skill_file.exists():
            available = ", ".join(ROLES) or "none"
            raise ValueError(f"Role skill not found: {role}. Available roles: {available}")
        return skill_file.read_text(encoding="utf-8")
    if name == "get_workflow":
        return read_named_file("workflows", arguments["name"], (".md",))
    if name == "get_template":
        return read_named_file("templates", arguments["name"], (".md", ".yaml", ".yml", ".json"))
    if name == "get_doc":
        return read_named_file("docs", arguments["name"], (".md",))
    raise ValueError(f"Unknown tool: {name}")


def handle(request: dict[str, Any]) -> dict[str, Any] | None:
    method = request.get("method")
    request_id = request.get("id")

    if method == "notifications/initialized":
        return None

    try:
        if method == "initialize":
            result = {
                "protocolVersion": PROTOCOL_VERSION,
                "capabilities": {"tools": {"listChanged": False}},
                "serverInfo": {"name": "codex-dev-squad", "version": "0.1.0"},
            }
        elif method == "ping":
            result = {}
        elif method == "tools/list":
            result = {"tools": tool_definitions()}
        elif method == "tools/call":
            params = request.get("params", {})
            text = call_tool(params.get("name", ""), params.get("arguments", {}) or {})
            result = {"content": [{"type": "text", "text": text}], "isError": False}
        else:
            return {
                "jsonrpc": "2.0",
                "id": request_id,
                "error": {"code": -32601, "message": f"Method not found: {method}"},
            }
        return {"jsonrpc": "2.0", "id": request_id, "result": result}
    except Exception as exc:
        return {
            "jsonrpc": "2.0",
            "id": request_id,
            "error": {"code": -32000, "message": str(exc)},
        }


def main() -> None:
    while True:
        request = read_message()
        if request is None:
            break
        response = handle(request)
        if response is not None and "id" in request:
            write_message(response)


if __name__ == "__main__":
    main()
