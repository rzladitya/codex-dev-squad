# Codex Dev Squad

Codex Dev Squad is a local Codex plugin that packages a small production software team into role-based skills, SOPs, workflows, templates, and a lightweight MCP server.

It is designed for building small SaaS products with a clear end-to-end flow:

```text
Research -> PM -> UI/UX -> Backend Python -> Frontend -> QA -> DevOps
```

## What Is Included

- 7 role skills:
  - Research Agent
  - PM Agent
  - UI/UX Agent
  - Backend Python Agent
  - Frontend Agent
  - QA Agent
  - DevOps Agent
- Feature workflows and agent SOPs.
- GitHub and Paper integration guidance.
- Templates for PRDs, GitHub issues, UI handoff, API contracts, QA plans, bug reports, and release notes.
- A local MCP server that exposes role, workflow, template, and documentation lookup tools.

## Default Stack

- Collaboration: GitHub Issues, Projects, Pull Requests, Releases.
- Design: Paper MCP.
- Frontend: Next.js, React, TypeScript, Tailwind CSS, shadcn/ui.
- Backend: Python, FastAPI, Pydantic, PostgreSQL, SQLAlchemy/SQLModel, Alembic.
- API Contract: OpenAPI.
- QA: Playwright, Pytest.
- DevOps: Docker, GitHub Actions.

## Repository Structure

```text
.
|-- .agents/plugins/marketplace.json
`-- plugins/codex-dev-squad
    |-- .codex-plugin/plugin.json
    |-- .mcp.json
    |-- skills/
    |-- workflows/
    |-- templates/
    |-- docs/
    |-- assets/
    `-- scripts/
```

## Install Locally in Codex

The plugin is designed to be installed as a local Codex plugin.

Detailed instructions:

[Installation Guide](plugins/codex-dev-squad/docs/installation-guide.md)

Short version:

1. Copy or keep the plugin at `~/plugins/codex-dev-squad`.
2. Register a local marketplace at `~/.agents/plugins/marketplace.json`.
3. Add the marketplace and plugin enablement to `~/.codex/config.toml`.
4. Restart Codex Desktop.
5. Search for `Codex Dev Squad` in the plugin marketplace.

## Usage SOP

Daily operating guide:

[Usage SOP](plugins/codex-dev-squad/docs/usage-sop.md)

Example prompt:

```text
Use Codex Dev Squad PM Agent to create a GitHub-ready feature brief and issue plan for Feature: User Authentication.
```

## MCP Tools

The plugin MCP server exposes:

- `list_roles`
- `list_workflows`
- `list_templates`
- `list_role_skills`
- `list_docs`
- `get_role_skill`
- `get_workflow`
- `get_template`
- `get_doc`

Validate locally:

```powershell
python .\plugins\codex-dev-squad\scripts\validate_plugin.py
```

Expected output:

```text
Codex Dev Squad plugin scaffold is valid.
```

## GitHub Publishing Notes

To publish this repository to a personal GitHub account:

```powershell
& 'C:\Program Files\GitHub CLI\gh.exe' auth login
& 'C:\Program Files\GitHub CLI\gh.exe' repo create codex-dev-squad --private --source . --remote origin --push
```

Use `--public` instead of `--private` if this should be visible publicly.

## License

MIT
