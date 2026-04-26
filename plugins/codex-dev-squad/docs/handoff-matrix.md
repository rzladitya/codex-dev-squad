# Handoff Matrix

This matrix is the operating contract for Codex Dev Squad. Every role must know what it receives, what it produces, and who depends on it.

| Step | Agent | A: Receives | B: Does | C: Produces | Next |
| --- | --- | --- | --- | --- | --- |
| 1 | Research | Product idea, market/user notes, stakeholder goals | Validates problem, user, alternatives, risks, and opportunity | Discovery brief, pain points, assumptions, competitor notes, recommendation | PM |
| 2 | PM | Discovery brief, stakeholder priorities | Defines scope, roadmap, GitHub issues, user stories, acceptance criteria | PRD, feature brief, backlog, GitHub issue, acceptance criteria | UI/UX, Backend, QA |
| 3 | UI/UX | PRD, feature brief, user stories, acceptance criteria | Designs flow, screens, states, and Paper handoff | User flow, Paper reference, UI handoff, screen data needs | Frontend, Backend, QA |
| 4 | Backend Python | Feature brief, UI data needs, acceptance criteria | Designs data model, API contract, auth, validation, backend plan | OpenAPI contract, schema/migration plan, backend implementation, tests | Frontend, QA |
| 5 | Frontend | UI handoff, API contract, acceptance criteria | Builds screens, components, state handling, API integration | Frontend implementation, integration notes, test notes | QA |
| 6 | QA | PRD, acceptance criteria, UI handoff, API contract, build/PR | Tests happy path, validation, permissions, regression, defects | QA report, bug reports, release sign-off or block | FE/BE for fixes, DevOps for release |
| 7 | DevOps | QA sign-off, release candidate, env/migration notes | Checks CI, secrets, deploy path, health, rollback | Staging/prod deploy, release notes, monitoring, rollback plan | PM, users |

## Block Rules

- PM cannot hand off unclear acceptance criteria.
- UI/UX cannot hand off a UI feature without screen states and data needs.
- Backend cannot hand off without API contract and permission rules.
- Frontend cannot hand off without loading, error, empty, and permission states where relevant.
- QA cannot sign off without mapping results to acceptance criteria.
- DevOps cannot deploy production without QA sign-off or explicit accepted risk.

## Feedback Loops

- QA bugs return to Frontend or Backend with reproduction steps.
- Backend API changes return to Frontend and QA for contract review.
- UI/UX flow changes return to PM for scope confirmation.
- Production incidents return to PM, QA, DevOps, and responsible engineering agent.

