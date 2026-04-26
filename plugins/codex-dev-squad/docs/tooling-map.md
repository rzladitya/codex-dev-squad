# Tooling Map

## Default Stack

| Area | Tool |
| --- | --- |
| Product collaboration | GitHub Issues, Projects, Milestones |
| Design | Paper |
| Frontend | Next.js, React, TypeScript, Tailwind CSS, shadcn/ui |
| Backend | Python, FastAPI, Pydantic, PostgreSQL, SQLAlchemy or SQLModel, Alembic |
| API contract | OpenAPI |
| Testing | Playwright, Pytest, Vitest where applicable |
| Code quality | Ruff, ESLint, Prettier, type checks |
| DevOps | Docker, GitHub Actions |
| Operations | Logs, health checks, backups, rollback notes |

## Stack Modes

### Simple SaaS Mode

- Next.js frontend.
- FastAPI backend.
- PostgreSQL.
- Docker Compose for local development.
- GitHub Actions for lint, tests, and deploy.

### Production Growth Mode

- Separate frontend and backend services.
- PostgreSQL plus Redis when needed.
- Background jobs for long-running tasks.
- Staging and production environments.
- Monitoring and error tracking.

## Rule

Agents should follow the existing project stack when a repository already exists. This plugin's stack is the default only when the project has no established convention.

