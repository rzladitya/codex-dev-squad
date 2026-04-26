# Production Readiness Workflow

Use this workflow before calling a SaaS product production-ready.

## Checklist

- Authentication is implemented and tested.
- Authorization is enforced server-side.
- Critical data has migrations and backup strategy.
- API contract is documented.
- Critical flows have QA coverage.
- CI runs lint/type/test checks.
- Secrets are stored outside the repo.
- Staging exists or an equivalent pre-production path is defined.
- Error logging or monitoring exists.
- Release and rollback procedures are documented.

## Decision

The squad should mark each item as pass, fail, or accepted risk before production launch.

