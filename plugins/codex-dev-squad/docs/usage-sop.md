# Codex Dev Squad Usage SOP

Use this SOP to operate Codex Dev Squad from product idea to release.

## Operating Principle

Small feature, clear contract, short loop.

Every feature must move through:

1. Research.
2. PM.
3. UI/UX.
4. Backend Python.
5. Frontend.
6. QA.
7. DevOps.

## Standard Prompt Pattern

Use prompts like:

```text
Use Codex Dev Squad to run the feature-development workflow for:

Feature: <feature name>
Goal: <business/user goal>
Target users: <users>
Platform: <web/mobile/iOS/etc>
Repo: <owner/repo or local repo>
Design surface: Paper
```

## 1. Product Discovery

Use when the idea is still vague.

Prompt:

```text
Use Codex Dev Squad Research Agent to create a discovery brief for this SaaS idea: <idea>.
```

Expected output:

- Discovery brief.
- User segment.
- Pain points.
- Assumptions.
- Risks.
- Recommendation.

## 2. PM Planning

Use after discovery is clear.

Prompt:

```text
Use Codex Dev Squad PM Agent to turn this discovery brief into GitHub-ready roadmap, epic, user stories, and acceptance criteria.
```

PM Agent should:

- Use GitHub connector first where supported.
- Use GitHub CLI when authenticated and repo target is known.
- Generate GitHub-ready issue artifacts when direct GitHub write is blocked.

Expected output:

- PRD.
- GitHub issue bodies.
- Labels.
- Milestones.
- Acceptance criteria.
- Handoff to UI/UX, Backend, and QA.

## 3. UI/UX Design

Use after PM defines feature scope.

Prompt:

```text
Use Codex Dev Squad UI/UX Agent to design the Paper handoff for this feature.
```

UI/UX Agent should:

- Read Paper MCP guidance.
- Inspect active Paper file.
- Create or update artboard.
- Produce UI handoff.

Expected output:

- Paper design reference.
- User flow.
- Screen inventory.
- UI states.
- Data needs.

## 4. Backend Planning and Build

Use after UI data needs and PM criteria are clear.

Prompt:

```text
Use Codex Dev Squad Backend Python Agent to create the backend micro-plan and API contract for this feature.
```

Expected output:

- Backend micro-plan.
- OpenAPI contract.
- Data model.
- Auth/permission rules.
- Tests.

## 5. Frontend Planning and Build

Use after UI handoff and API contract are available.

Prompt:

```text
Use Codex Dev Squad Frontend Agent to implement this feature from the UI handoff and API contract.
```

Expected output:

- Frontend micro-plan.
- Pages/components.
- API integration.
- UI state handling.
- Test notes.

## 6. QA

Use when the feature build is ready.

Prompt:

```text
Use Codex Dev Squad QA Agent to test this feature against the acceptance criteria and API/UI handoff.
```

Expected output:

- QA test plan.
- Test results.
- Bug reports.
- Release decision.

## 7. DevOps Release

Use after QA pass or accepted risk.

Prompt:

```text
Use Codex Dev Squad DevOps Agent to prepare release checklist, deploy notes, and rollback plan.
```

Expected output:

- Release note.
- Deployment checklist.
- Health check plan.
- Rollback plan.

## Handoff Rule

Every agent must fill a handoff record when passing work to another agent:

- Inputs received.
- Work completed.
- Outputs delivered.
- Decisions made.
- Open questions.
- Blockers.
- Links to GitHub, Paper, PR, or API contract.

Use `templates/handoff-record.md`.

## Block Rules

- Do not start implementation without acceptance criteria.
- Do not start frontend implementation without UI handoff and API contract for integrated features.
- Do not mark backend ready without validation, authorization, and API contract.
- Do not sign off QA without mapping tests to acceptance criteria.
- Do not deploy production without QA sign-off or explicit accepted risk.

