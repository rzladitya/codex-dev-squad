# Codex Dev Squad Installation Guide

This guide installs Codex Dev Squad as a local Codex plugin and prepares the prerequisites for GitHub and Paper workflows.

## 1. Prerequisites

- Codex desktop app is available.
- This repository contains `plugins/codex-dev-squad`.
- Python is available for the local MCP server.
- Git is available.
- GitHub CLI is installed when direct issue/project operations are needed.
- Paper MCP is available when UI/UX Agent will create designs in Paper.

## 2. Verify Plugin Files

From the repository root:

```powershell
python .\plugins\codex-dev-squad\scripts\validate_plugin.py
```

Expected output:

```text
Codex Dev Squad plugin scaffold is valid.
```

## 3. Verify GitHub CLI

If `gh` is in PATH:

```powershell
gh --version
gh auth status
```

Windows fallback when `gh` is installed but not in PATH:

```powershell
& 'C:\Program Files\GitHub CLI\gh.exe' --version
& 'C:\Program Files\GitHub CLI\gh.exe' auth status
```

If not authenticated:

```powershell
& 'C:\Program Files\GitHub CLI\gh.exe' auth login
```

## 4. Prepare Git Remote

Create a GitHub repository manually or through your normal GitHub workflow.

Then connect the local repo:

```powershell
git remote add origin https://github.com/<owner>/<repo>.git
git branch -M main
git push -u origin main
```

If the repo already has a remote:

```powershell
git remote -v
```

## 5. Install as a Local Codex Plugin

Codex local plugins are discovered from a plugin marketplace/registry entry and a Codex config marketplace registration.

For home-local development, copy the plugin to:

```text
~/plugins/codex-dev-squad
```

Then create:

```text
~/.agents/plugins/marketplace.json
```

with an entry similar to:

```json
{
  "name": "codex-dev-squad",
  "source": {
    "source": "local",
    "path": "./plugins/codex-dev-squad"
  },
  "policy": {
    "installation": "AVAILABLE",
    "authentication": "ON_INSTALL"
  },
  "category": "Productivity"
}
```

Recommended marketplace path for repo-local development:

```text
.agents/plugins/marketplace.json
```

Recommended marketplace path for home-local development:

```text
~/.agents/plugins/marketplace.json
```

Then register the marketplace and enable the plugin in:

```text
~/.codex/config.toml
```

```toml
[plugins."codex-dev-squad@local-dev"]
enabled = true

[marketplaces.local-dev]
last_updated = "2026-04-26T11:25:24Z"
source_type = "local"
source = 'C:\Users\rzladitya'
```

After adding the marketplace entry and config registration, fully restart Codex so it can discover the plugin.

## 6. Verify MCP Server

The plugin exposes a local stdio MCP server through `.mcp.json`.

Expected tools:

- `list_roles`
- `list_workflows`
- `list_templates`
- `list_role_skills`
- `list_docs`
- `get_role_skill`
- `get_workflow`
- `get_template`
- `get_doc`

## 7. Verify Paper

Before UI/UX work:

1. Open a Paper file.
2. Ask Codex to inspect Paper context.
3. UI/UX Agent should call Paper MCP guidance and `get_basic_info`.

## 8. Ready State

The plugin is ready when:

- Plugin validation passes.
- Codex can discover the plugin.
- MCP tools are visible.
- GitHub connector or GitHub CLI is authenticated.
- Local repo has a remote when direct GitHub operations are expected.
- Paper file is open when UI/UX design work is expected.
