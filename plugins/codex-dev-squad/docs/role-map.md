# Role Map

| Role | Primary Question | Main Artifact | Handoff To |
| --- | --- | --- | --- |
| Research | Why should we build this, and for whom? | Discovery brief | PM |
| PM | What should be built first, and how do we know it is done? | PRD, user stories, acceptance criteria | UI/UX, Backend, QA |
| UI/UX | How should users complete the task? | Paper design, UI handoff | Frontend, Backend |
| Backend Python | What data, API, rules, and security make this work? | API contract, schema, service code | Frontend, QA |
| Frontend | How does the user use the feature? | Pages, components, API integration | QA |
| QA | Does the feature satisfy the agreed criteria? | Test plan, bug report, sign-off | DevOps, FE/BE |
| DevOps | Can this be released and operated safely? | Deployment, release note, rollback plan | Users, PM |

## Gate Rules

- PM gates scope.
- UI/UX gates usability and design handoff.
- Backend gates API contract and data integrity.
- Frontend gates user-facing completeness.
- QA gates release readiness.
- DevOps gates production rollout.

