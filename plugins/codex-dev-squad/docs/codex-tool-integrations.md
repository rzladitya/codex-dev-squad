# Codex Tool Integrations

This document describes how Codex Dev Squad should use tools already available in Codex before adding custom integration code.

## GitHub Connector

Use the GitHub connector first for repository collaboration.

### Available Connector Actions

- Search issues.
- Fetch an issue.
- Search pull requests.
- List recent user pull requests in a repository.
- List pull request reviews.
- Create a repository file through the GitHub contents API.
- Update a repository file through the GitHub contents API.
- Create a pull request.

### PM Agent Usage

PM Agent should use GitHub as the source of truth for:

- Roadmap planning.
- Feature issues.
- Bug tracking.
- PR handoff.
- Release notes.

When direct issue or project creation is unavailable through the connector, PM Agent should:

1. Generate the issue body using `templates/github-issue.md`.
2. Save or present the GitHub-ready artifact.
3. Mark the action as needing either GitHub CLI, browser execution, or a future connector extension.

### Engineering Agent Usage

Frontend, Backend, QA, and DevOps Agents should use GitHub for:

- PR context.
- Review status.
- Linked issues.
- Release branch notes.
- Repository file updates when the connector is the safest write path.

## Paper MCP

Use Paper MCP as the primary design surface for UI/UX work.

### Available Paper Actions

- Read current file/page/artboard context.
- Create artboards.
- Write HTML/CSS into Paper nodes.
- Duplicate, rename, delete, and inspect nodes.
- Read children and basic structure.

### UI/UX Agent Usage

UI/UX Agent should:

1. Read Paper guidance before design work.
2. Inspect the active Paper file with `get_basic_info`.
3. Create or update the relevant artboard.
4. Build designs incrementally.
5. Produce `templates/ui-handoff.md`.
6. Link the design reference back to the GitHub feature issue.

## Current Local Notes

- GitHub CLI may be installed outside the active PATH. On Windows, check `C:\Program Files\GitHub CLI\gh.exe` when `gh` is not found.
- If GitHub CLI is installed but not authenticated, run `gh auth login` or the full Windows path equivalent before asking PM Agent to create issues.
- A local repository may not have a remote configured.
- Connector-first means the squad should prefer Codex app tools when available, then fall back to artifacts or local CLI only when necessary.

## GitHub CLI Operator Mode

When GitHub CLI is installed and authenticated, PM Agent can operate GitHub more directly.

### Readiness Checks

1. Locate CLI:
   - `gh --version`
   - Windows fallback: `& 'C:\Program Files\GitHub CLI\gh.exe' --version`
2. Confirm auth:
   - `gh auth status`
   - Windows fallback: `& 'C:\Program Files\GitHub CLI\gh.exe' auth status`
3. Confirm repository remote:
   - `git remote -v`

### PM Agent Actions

When authenticated and the target repo is known, PM Agent may use GitHub CLI for:

- Creating issues.
- Creating labels.
- Creating milestones.
- Listing and updating issues.
- Creating project-ready backlog artifacts.

Example:

```powershell
& 'C:\Program Files\GitHub CLI\gh.exe' issue create `
  --repo owner/repo `
  --title "Feature: User Authentication" `
  --body-file docs/issues/user-authentication.md `
  --label pm,backend,frontend,qa
```

### Fallback Rule

If `gh` is not authenticated or no repository remote exists, PM Agent should still generate GitHub-ready issue files and mark the GitHub write action as blocked.
