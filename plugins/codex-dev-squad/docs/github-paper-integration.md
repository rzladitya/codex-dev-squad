# GitHub and Paper Integration

Codex Dev Squad uses Codex's connected GitHub app as the execution command center and Paper MCP as the design handoff space.

For exact connector capability rules, see `docs/codex-tool-integrations.md`.

## GitHub Responsibilities

PM Agent owns the product structure in GitHub:

- Roadmap: GitHub Projects.
- Epic: parent issue or labeled issue.
- User story: issue with acceptance criteria.
- Engineering task: issue or PR checklist item.
- Bug: issue labeled `bug`.
- Sprint or release target: milestone.
- Code review: pull request.
- Release history: GitHub Releases.

## GitHub Connector-First Policy

Use Codex's GitHub connector first for:

- Fetching and summarizing issues.
- Searching issues and pull requests.
- Reading pull request review submissions.
- Creating or updating repository files.
- Creating pull requests after a branch exists.

If a needed GitHub write is not exposed by the connector, such as direct issue creation or project-board mutation, PM Agent should produce a ready-to-paste GitHub issue or project artifact from `templates/github-issue.md` and record that the action needs a GitHub CLI, browser, or future connector tool.

When GitHub CLI is available and authenticated, PM Agent may use it for direct issue, label, and milestone operations. On Windows, check `C:\Program Files\GitHub CLI\gh.exe` if `gh` is not available in `PATH`.

## Required Labels

- `research`
- `pm`
- `uiux`
- `frontend`
- `backend`
- `qa`
- `devops`
- `release`
- `bug`
- `blocked`

## Paper Responsibilities

UI/UX Agent owns Paper artifacts:

- User flow.
- Screen inventory.
- Wireframe or visual design.
- Component notes.
- Form and table behavior.
- Empty, loading, error, permission, and success states.
- Data needs for backend and frontend.

## Paper MCP Policy

Use Paper MCP directly when a Paper file is open:

- Call `get_guide` for Paper instructions before mutating design.
- Call `get_basic_info` to inspect the active file.
- Create or update artboards incrementally.
- Write UI in small visual groups.
- Produce a UI handoff that links the Paper artifact to GitHub issue work.

If no Paper file is open, UI/UX Agent should still produce `templates/ui-handoff.md` and mark Paper design as blocked.

## Handoff Rule

Every feature issue should link to:

- The PRD or feature brief.
- Paper design reference when UI is involved.
- API contract when backend/frontend integration is involved.
- QA test plan before release.
