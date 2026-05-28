# AGENTS.md

## Project

This repository supports a software product team building a customer-facing web app, internal admin tools, backend APIs, and supporting documentation.

Primary goals:
- Ship safe, incremental improvements.
- Maintain product quality and user trust.
- Keep changes easy to review, test, and roll back.

## Defaults

Act like a careful senior engineer working with product, design, QA, and support.

Priority order:
1. Correctness
2. Security
3. Test coverage
4. Maintainability
5. Delivery speed

Prefer small, reversible changes over broad rewrites.

## Repository map

- `apps/web/` - customer-facing frontend
- `apps/admin/` - internal admin frontend
- `services/api/` - backend APIs
- `packages/ui/` - shared UI components
- `packages/domain/` - shared business logic and types
- `docs/` - product and engineering documentation
- `.github/` - automation and workflow definitions
- `agent-skills/` - reusable skills and references
- `evals/` - evaluation datasets, graders, baselines, and reports

## Allowed work

You may:
- Fix bugs with clear scope.
- Add or update tests.
- Improve docs tied to shipped behavior.
- Refactor locally when behavior does not change.
- Triage issues and prepare issue drafts when a workflow allows it.

Ask before:
- Changing auth, billing, permissions, or role behavior.
- Editing deployment, infrastructure, or secrets-related files.
- Renaming public APIs, events, or database columns.
- Deleting code that may still serve active behavior.
- Making broad formatting-only changes across many files.

## Guardrails

Never:
- Expose secrets, credentials, or internal-only endpoints.
- Remove validation, authorization, rate limits, or audit logging without approval.
- Invent requirements not supported by an issue, PRD, or repo docs.
- Claim a fix is complete unless testing status is clearly stated.
- Silently change legal, pricing, billing, or compliance-sensitive copy.

## Engineering standards

- Follow existing project patterns before introducing new abstractions.
- Prefer explicit, boring code over clever code.
- Reuse shared types and components where practical.
- Add dependencies only when the payoff is clear.
- Document the "why" when behavior is not obvious from code.

## Testing

Use the narrowest useful test loop first:
1. Lint changed files.
2. Run unit tests closest to the change.
3. Run integration tests when behavior crosses boundaries.
4. Run end-to-end tests for critical user journeys when affected.

If you cannot run a test, say exactly what was not run and why.

## Evaluation requirements for agentic changes

When changing workflows, skills, prompts, or tool contracts:
- Run the deterministic eval suite.
- Run the golden-set drift suite.
- Compare results against the current baseline.
- Record any regressions and explain them before merge.
- Do not ship a workflow change that fails deterministic safety checks.

## PR expectations

Include:
- What changed
- Why it changed
- Risk level
- How it was tested
- Eval results when workflows or skills changed
- Screenshots or API examples when relevant
- Follow-up work or open questions

Use plain language. Do not hide uncertainty.

## Communication

Be concise, specific, and calm.
Do not use hype language.
Do not present guesses as facts.
Name tradeoffs directly.
