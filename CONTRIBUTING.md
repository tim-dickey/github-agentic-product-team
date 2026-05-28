# Contributing to github-agentic-product-team

Thanks for helping improve this project.

This repository is meant to be a practical, community-maintained scaffold for GitHub agent workflows, reusable skills, evals, and safety guardrails for software product teams. Contributions are welcome across documentation, workflow examples, datasets, schemas, eval logic, policies, and community process.

## Good first contributions

Strong early contributions include:

- Clarifying confusing documentation.
- Improving examples in skills or workflows.
- Adding or tightening eval datasets.
- Fixing schema mismatches or validation gaps.
- Expanding guardrail coverage for risky behaviors.
- Improving community docs without adding unnecessary bureaucracy.

## Before you start

Please:

1. Read `README.md` for project context.
2. Read `AGENTS.md` for repository-wide guidance.
3. Check existing issues and pull requests so work does not duplicate ongoing effort.
4. Prefer discussing broad or opinionated changes in an issue before implementing them.

## Contribution principles

This project favors contributions that are:

- Small enough to review without guesswork.
- Easy to test or validate.
- Specific about the problem being solved.
- Backed by examples or evidence where possible.
- Careful about safety, especially for auth, billing, privacy, secrets, and workflow side effects.

## Pull request expectations

Each pull request should include:

- A short summary of what changed.
- Why the change is needed.
- Any tradeoffs or open questions.
- Testing or validation notes.
- Eval results when workflows, prompts, adapters, schemas, datasets, or policies change.

If tests or evals were not run, say exactly what was skipped and why.

## Specific guidance by contribution type

### Workflow changes

If a pull request changes files in `.github/workflows/`:

- Explain the intended behavior clearly.
- Document any safe-output assumptions.
- Keep permissions as narrow as practical.
- Avoid adding side effects without a strong justification.

### Skill changes

If a pull request changes files in `agent-skills/`:

- Keep `SKILL.md` focused and fast to load.
- Move deep details into `references/`.
- Put reusable templates in `assets/`.
- Prefer concrete examples over abstract advice.

### Eval changes

If a pull request changes files in `evals/`:

- Keep datasets realistic and concise.
- Add negative and adversarial cases where useful.
- Update schemas, policies, or baselines together when they are logically linked.
- Call out any expected drift or temporary baseline changes.

## Style expectations

- Use plain language.
- Prefer boring clarity over cleverness.
- Keep docs scannable.
- Do not over-engineer examples.
- Do not present speculation as fact.

## Community norms

Please be respectful, direct, and collaborative. A code of conduct helps define community standards and outline reporting paths for unacceptable behavior, which is why this project includes one and expects contributors to follow it.[cite:120]

## Reporting bugs and proposing features

When opening an issue:

- Explain the current behavior.
- Explain the expected behavior.
- Include reproduction steps when applicable.
- Include examples or failing inputs for eval or schema issues.
- Keep feature requests grounded in a real maintainer or team use case.

## Security and sensitive issues

Do not open a public issue for:

- vulnerabilities
- secrets exposure
- auth bypass behavior
- unsafe workflow side effects
- prompt-injection paths that could cause real harm

Use the process in `SECURITY.md` instead.

## License for contributions

By contributing to this repository, you agree that your contributions will be licensed under the Apache License 2.0 used by this project.
