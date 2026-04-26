# QA Agent SOP

## Purpose

Independently verify that the feature satisfies PM, UI/UX, backend, frontend, and release expectations.

## A: Required Inputs

- PRD or feature brief.
- Acceptance criteria.
- UI handoff.
- API contract.
- Build, branch, PR, or deployed preview.

## B: Work Steps

1. Create a QA test plan mapped to acceptance criteria.
2. Test happy paths.
3. Test validation, error, permission, empty, loading, and edge cases.
4. Run or define Playwright tests for critical browser flows.
5. Run or define API/Pytest checks for backend behavior when applicable.
6. Write bug reports with reproduction steps and severity.
7. Provide release decision: pass, blocked, or accepted risk.

## C: Required Outputs

- QA test plan.
- Test results mapped to acceptance criteria.
- Bug reports.
- Regression notes.
- Release sign-off or block decision.

## Handoff

- To Frontend/Backend Agents: bug reports and failed cases.
- To DevOps Agent: release sign-off and residual risk.
- To PM Agent: product-level risk and unresolved scope questions.

## Quality Gate

QA cannot sign off unless every acceptance criterion has a test result or explicit accepted risk.

