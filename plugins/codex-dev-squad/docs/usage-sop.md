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

## Full Use Case: User Authentication

This example shows one complete feature moving through the whole squad.

### Feature Brief

```text
Feature: User Authentication
Goal: Allow users to register, log in, log out, and access protected SaaS pages.
Target users: SaaS account users and admins.
Platform: Web app.
Repo: rzladitya/codex-dev-squad or the active product repo.
Design surface: Paper.
Backend stack: FastAPI, PostgreSQL, Pydantic, SQLAlchemy/SQLModel, Alembic.
Frontend stack: Next.js, React, TypeScript, Tailwind CSS.
```

### Step 1: Research Agent

Prompt:

```text
Use Codex Dev Squad Research Agent to create a discovery brief for User Authentication in a small SaaS product.

Focus on:
- user expectations
- security expectations
- common SaaS auth flows
- MVP vs later features
- risks and assumptions
```

Expected Research output:

```text
Discovery Brief

Target users:
- New SaaS users creating accounts.
- Returning users accessing private dashboard pages.
- Admins managing protected areas.

Pain points:
- Users need a fast and familiar login flow.
- Users need clear error messages when credentials are wrong.
- Product needs protected pages that cannot be accessed anonymously.

MVP recommendation:
- Email/password registration.
- Email/password login.
- Logout.
- Protected route/session check.
- Basic password reset placeholder or later-phase story.

Risks:
- Weak password handling.
- Missing server-side authorization.
- Leaking whether an email exists.
- Poor session expiration behavior.
```

Handoff to PM:

```text
Research recommends authentication as a foundational MVP feature.
PM should split this into small stories: register, login, logout, protected route, reset password later.
```

### Step 2: PM Agent

Prompt:

```text
Use Codex Dev Squad PM Agent to turn the User Authentication discovery brief into GitHub-ready epics, issues, user stories, and acceptance criteria.

Use GitHub connector first. If direct issue creation is unavailable, generate GitHub-ready issue bodies.
```

Expected PM output:

```text
Epic: Authentication Module

Story 1: User can register with email and password
Labels: pm, frontend, backend, qa

Acceptance criteria:
- Given a new user, when they submit valid email and password, then an account is created.
- Given an existing email, when registration is attempted, then the request fails safely.
- Given invalid input, when submitted, then validation messages are shown.

Story 2: User can log in
Acceptance criteria:
- Given valid credentials, login succeeds and the user reaches the dashboard.
- Given invalid credentials, login fails with a safe error message.
- Given an unauthenticated user, protected pages redirect to login.

Story 3: User can log out
Acceptance criteria:
- Given an authenticated user, logout ends the session.
- Given a logged-out user, protected pages are no longer accessible.
```

PM handoff:

```text
To UI/UX:
- Design registration, login, logout state, protected-route redirect, form validation states.

To Backend:
- Provide endpoints for register, login, logout/me/session check.
- Enforce password hashing and server-side auth.

To QA:
- Test each acceptance criterion, including invalid credentials and protected routes.
```

### Step 3: UI/UX Agent

Prompt:

```text
Use Codex Dev Squad UI/UX Agent to create the Paper design and UI handoff for User Authentication.

Design screens:
- Login
- Register
- Forgot password placeholder
- Protected dashboard empty state after login
- Error/loading/success states
```

Expected UI/UX output:

```text
Paper reference:
- Authentication Flow artboard

Screens:
- /login
- /register
- /forgot-password
- /dashboard

Fields:
- email
- password
- confirm_password for registration

States:
- loading submit
- invalid email
- wrong credentials
- existing email
- session expired
- logged out

Data needs:
- current user
- auth token/session status
- validation errors
```

UI/UX handoff:

```text
To Frontend:
- Build auth pages and dashboard redirect behavior.
- Use accessible form labels and visible validation.

To Backend:
- Frontend needs register/login/logout/session endpoints.
- Error responses must support field-level validation and safe auth errors.
```

### Step 4: Backend Python Agent

Prompt:

```text
Use Codex Dev Squad Backend Python Agent to create the backend micro-plan and OpenAPI contract for User Authentication.

Assume FastAPI, PostgreSQL, Pydantic, SQLAlchemy/SQLModel, Alembic, and Pytest.
```

Expected backend micro-plan:

```text
Data model:
- users
  - id
  - email unique indexed
  - password_hash
  - role
  - is_active
  - created_at
  - updated_at

Endpoints:
- POST /auth/register
- POST /auth/login
- POST /auth/logout
- GET /auth/me

Security:
- Hash passwords with a strong password hashing algorithm.
- Do not return password_hash.
- Use safe error messages.
- Enforce protected routes server-side.

Tests:
- register valid user
- reject duplicate email
- reject invalid password
- login valid credentials
- reject invalid credentials
- /auth/me requires auth
```

Expected OpenAPI excerpt:

```yaml
paths:
  /auth/register:
    post:
      summary: Register user
  /auth/login:
    post:
      summary: Login user
  /auth/logout:
    post:
      summary: Logout user
  /auth/me:
    get:
      summary: Get current user
```

Backend handoff:

```text
To Frontend:
- Use POST /auth/register and POST /auth/login.
- Use GET /auth/me for session bootstrap.
- Treat 401 as unauthenticated and redirect to login.

To QA:
- Test auth errors, duplicate registration, and protected endpoint access.

To DevOps:
- Requires AUTH_SECRET or equivalent session/token secret.
- Requires database migration for users table.
```

### Step 5: Frontend Agent

Prompt:

```text
Use Codex Dev Squad Frontend Agent to implement User Authentication from the UI handoff and API contract.

Build Next.js pages, forms, API integration, validation, and protected dashboard routing.
```

Expected frontend plan:

```text
Routes:
- /login
- /register
- /forgot-password
- /dashboard

Components:
- AuthLayout
- LoginForm
- RegisterForm
- PasswordField
- AuthErrorMessage
- ProtectedRoute or middleware/session guard

Behavior:
- Validate email format and required password.
- Show loading state on submit.
- Show safe error messages.
- Redirect to dashboard after login.
- Redirect unauthenticated dashboard access to login.
```

Frontend handoff:

```text
To QA:
- Test register/login/logout flows.
- Test protected route redirect.
- Test validation and API error states.

To Backend:
- Report any API contract mismatch.
```

### Step 6: QA Agent

Prompt:

```text
Use Codex Dev Squad QA Agent to create and run a QA test plan for User Authentication.

Map every result to the PM acceptance criteria.
```

Expected QA test plan:

```text
Happy path:
- Register with valid email/password.
- Login with registered account.
- Access dashboard after login.
- Logout and confirm dashboard is blocked.

Validation:
- Invalid email fails.
- Missing password fails.
- Duplicate email fails safely.
- Wrong password fails safely.

Permission:
- Anonymous user cannot access dashboard.
- /auth/me returns 401 without auth.

Regression:
- Auth pages render on desktop and mobile.
- Form errors do not break layout.
```

QA release decision:

```text
Pass:
- All acceptance criteria pass.

Blocked:
- Any critical auth, session, or protected route failure.

Accepted risk:
- Forgot password deferred if explicitly out of MVP scope.
```

### Step 7: DevOps Agent

Prompt:

```text
Use Codex Dev Squad DevOps Agent to prepare release checklist, environment variables, deployment notes, health checks, and rollback plan for User Authentication.
```

Expected DevOps output:

```text
Environment variables:
- DATABASE_URL
- AUTH_SECRET
- APP_URL

Pre-release:
- CI green.
- Database migration reviewed.
- QA sign-off attached.
- Secrets configured outside repository.

Smoke tests:
- /login loads.
- /register loads.
- user can log in.
- /dashboard requires auth.

Rollback:
- Revert auth feature PR.
- Roll back users migration only if no production user data depends on it.
- Disable protected routes only through an approved emergency change.
```

Release note:

```text
Added User Authentication:
- Users can register, log in, log out, and access protected dashboard pages.
- Authenticated routes now require a valid session.
- Password reset remains planned for a later release.
```

### End-to-End Handoff Summary

```text
Research -> PM:
Problem, risks, MVP recommendation.

PM -> UI/UX:
Stories, scope, acceptance criteria.

UI/UX -> Backend:
Data needs, screens, actions, states.

Backend -> Frontend:
API contract, auth rules, error format.

Frontend -> QA:
Implemented flows and known limitations.

QA -> DevOps:
Pass/fail report and residual risk.

DevOps -> PM/User:
Release status, URL, release note, rollback plan.
```

### One-Prompt End-to-End Test

Use this when testing whether the squad can plan the full workflow:

```text
Use Codex Dev Squad to run an end-to-end feature-development plan for User Authentication.

Do not implement code yet.
Produce:
- Research discovery brief
- PM GitHub-ready issues
- UI/UX Paper handoff plan
- Backend Python API contract
- Frontend implementation plan
- QA test plan
- DevOps release checklist
- Handoff records between all agents
```
