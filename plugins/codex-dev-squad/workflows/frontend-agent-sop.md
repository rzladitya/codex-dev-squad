# Frontend Agent SOP

## Purpose

Build user-facing product features from UI/UX handoff and backend API contract.

## A: Required Inputs

- UI handoff and Paper reference.
- API contract.
- Acceptance criteria.
- Existing frontend patterns and design system.

## B: Work Steps

1. Read UI/UX, PM, and API artifacts.
2. Write a frontend micro-plan before implementation.
3. Identify routes, pages, components, forms, tables, and state boundaries.
4. Implement UI with existing project conventions.
5. Integrate APIs according to the contract.
6. Handle loading, empty, error, success, validation, and permission states.
7. Add or update relevant frontend tests.
8. Run available lint/type/test checks.

## C: Required Outputs

- Frontend micro-plan.
- Routes/pages/components.
- API integration.
- UI state handling.
- Frontend test notes.

## Handoff

- To QA Agent: testable build, implemented flows, known limitations.
- To Backend Python Agent: contract mismatch reports if found.
- To DevOps Agent: frontend build/env notes if changed.

## Quality Gate

Frontend cannot mark a feature ready without handling critical states and confirming API contract compatibility.

