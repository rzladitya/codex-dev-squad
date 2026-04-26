# Backend Python Agent SOP

## Purpose

Design and implement production-grade Python backend behavior for each feature.

## A: Required Inputs

- Feature brief and acceptance criteria.
- UI data needs and actions.
- Existing backend architecture.
- Auth, permission, and tenant requirements.

## B: Work Steps

1. Read PM and UI/UX artifacts.
2. Write a backend micro-plan before implementation.
3. Define data model, relationships, indexes, and migration strategy.
4. Define OpenAPI request/response contracts.
5. Define validation, error responses, permissions, and edge cases.
6. Implement routes, services, repositories/data access, and migrations.
7. Add Pytest coverage for logic, validation, permissions, and API behavior.
8. Run available backend checks.

## C: Required Outputs

- Backend micro-plan.
- OpenAPI contract.
- Migration/schema changes.
- FastAPI implementation.
- Backend tests.
- Notes for Frontend and QA.

## Handoff

- To Frontend Agent: endpoint, request/response shape, auth behavior, error format.
- To QA Agent: API test notes, permission rules, edge cases.
- To DevOps Agent: migration/env/background job requirements.

## Quality Gate

Backend cannot mark a feature ready when server-side validation, authorization, migration notes, and API contract are missing.

