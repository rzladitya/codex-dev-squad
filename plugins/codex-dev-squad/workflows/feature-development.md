# Feature Development Workflow

Use this workflow for every production feature.

## Principle

Small feature, clear contract, short loop.

## Steps

1. PM Agent creates the feature brief, user story, scope, and acceptance criteria.
2. UI/UX Agent creates the user flow, screen inventory, state list, and Paper handoff.
3. Backend Python Agent creates the backend micro-plan, API contract, data model, permission rules, and test plan.
4. Frontend Agent creates the frontend micro-plan based on UI handoff and API contract.
5. Backend and Frontend Agents implement in coordinated branches or PRs.
6. QA Agent tests against acceptance criteria, UI handoff, and API contract.
7. DevOps Agent releases after QA sign-off.

## Gates

- Gate 1: PM requirement approved.
- Gate 2: UI/UX handoff complete.
- Gate 3: API contract agreed by backend, frontend, and QA.
- Gate 4: Backend and frontend implementation complete.
- Gate 5: QA pass or accepted risk.
- Gate 6: DevOps release checklist complete.

## Handoff Rule

No agent should execute a large feature as a single one-shot task. Each agent writes a short micro-plan before implementation.

