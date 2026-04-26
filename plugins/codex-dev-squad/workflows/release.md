# Release Workflow

Use this workflow to move a tested feature or batch of features to production.

## Steps

1. PM confirms scope included in the release.
2. QA confirms pass/fail status and residual risk.
3. DevOps checks CI, environment variables, migrations, backups, and rollback.
4. DevOps deploys to staging and validates smoke tests.
5. Product owner or PM approves production release.
6. DevOps deploys production and monitors health.
7. PM publishes release note.

## Release Gates

- CI green.
- QA sign-off complete.
- No unresolved blocker bugs.
- Migration plan reviewed.
- Rollback plan documented.
- Production health check passes.

