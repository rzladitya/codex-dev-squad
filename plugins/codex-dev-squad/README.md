# Codex Dev Squad

Codex Dev Squad is a Codex plugin blueprint for a small but production-minded software team. It treats each function as a role-based skill and coordinates the work through feature-sized workflows and shared artifacts.

## Default Team

- Research Agent: validates user problems, market context, risks, and opportunities.
- PM Agent: turns discovery into roadmap, GitHub issues, user stories, and acceptance criteria.
- UI/UX Agent: designs flows and handoff specs in Paper.
- Frontend Agent: builds Next.js, React, TypeScript user interfaces.
- Backend Python Agent: builds FastAPI, PostgreSQL, OpenAPI, auth, business logic, and tests.
- QA Agent: verifies acceptance criteria with Playwright, Pytest, and structured bug reports.
- DevOps Agent: handles Docker, GitHub Actions, environments, deployment, monitoring, and rollback.

## Default Stack

- Collaboration: GitHub Issues, Projects, Pull Requests, Releases.
- Design: Paper.
- Frontend: Next.js, React, TypeScript, Tailwind CSS, shadcn/ui.
- Backend: Python, FastAPI, Pydantic, SQLAlchemy/SQLModel, Alembic, PostgreSQL.
- API Contract: OpenAPI plus shared validation notes.
- QA: Playwright, Pytest, Ruff, type checks.
- DevOps: Docker, GitHub Actions, staging, production, backups, monitoring.

## Working Principle

Small feature, clear contract, short loop.

Every feature should move through:

1. Discovery and product framing.
2. PM requirement and acceptance criteria.
3. UI/UX handoff.
4. API contract and backend plan.
5. Frontend plan and implementation.
6. QA verification.
7. Release and monitoring.

## Agent Contract

Each agent follows the same A/B/C contract:

- A: required inputs before the agent starts.
- B: role-specific SOP and quality checks.
- C: required outputs and handoff targets.

The detailed cross-agent handoff is documented in `docs/handoff-matrix.md`, and each role has a dedicated SOP under `workflows/*-agent-sop.md`.

## Codex Tool Usage

The squad should use existing Codex integrations before inventing custom glue:

- PM and engineering agents use the GitHub connector for issues, PRs, repository files, and reviews where supported.
- UI/UX Agent uses Paper MCP for live design work and Paper handoff.
- Connector limitations are documented in `docs/codex-tool-integrations.md`.

## Install and Use

- Installation guide: `docs/installation-guide.md`
- Daily usage SOP: `docs/usage-sop.md`
