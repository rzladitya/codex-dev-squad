# Bugfix Workflow

Use this workflow when a defect is reported.

## Steps

1. PM or QA Agent triages severity, priority, affected users, and reproduction steps.
2. QA Agent confirms the bug and writes expected vs actual behavior.
3. Backend or Frontend Agent identifies root cause and writes a fix plan.
4. The responsible agent implements the fix and adds or updates tests.
5. QA Agent verifies the fix and runs targeted regression.
6. DevOps Agent releases the fix when needed.

## Required Outputs

- Bug report.
- Root cause note.
- Fix PR.
- Regression result.
- Release note for user-visible fixes.

