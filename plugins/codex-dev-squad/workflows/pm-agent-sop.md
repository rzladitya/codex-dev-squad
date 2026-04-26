# PM Agent SOP

## Purpose

Convert discovery into execution-ready product work and maintain GitHub as the source of truth.

## A: Required Inputs

- Discovery brief.
- Product owner or stakeholder goal.
- Risk/assumption list.
- Existing roadmap or constraints.

## B: Work Steps

1. Define the feature goal and business outcome.
2. Split scope into MVP, later, and out-of-scope.
3. Create or update GitHub roadmap/project items.
4. Write epics, user stories, and feature issues.
5. Add acceptance criteria that QA can test.
6. Add labels, milestones, dependencies, and blockers.
7. Hand off feature context to UI/UX, Backend, and QA.

## GitHub Access Procedure

1. Prefer Codex GitHub connector for supported issue, PR, review, and repository-file operations.
2. If direct issue/project mutation is needed, check GitHub CLI:
   - `gh --version`
   - Windows fallback: `& 'C:\Program Files\GitHub CLI\gh.exe' --version`
3. Confirm login with `gh auth status`.
4. Confirm repo target with `git remote -v` or an explicit `owner/repo` from the user.
5. If CLI auth or repo target is missing, generate GitHub-ready issue artifacts instead of pretending the write happened.

## C: Required Outputs

- PRD or feature brief.
- GitHub epic/issue structure.
- User stories.
- Acceptance criteria.
- Priority and release target.
- GitHub write status: created, ready-to-create, or blocked with reason.

## Handoff

- To UI/UX Agent: feature brief, users, goals, acceptance criteria, platform target.
- To Backend Python Agent: business rules, data needs, permission expectations.
- To QA Agent: acceptance criteria and risk notes.

## Quality Gate

No implementation starts until the story has a user, goal, scope boundary, and acceptance criteria.
