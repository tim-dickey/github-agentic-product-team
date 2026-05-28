# github-agentic-product-team

A community scaffold for GitHub Agentic Workflows, skills, evals, and guardrails for software product teams.

This repository is a starter kit for teams that want to build and maintain agent-driven GitHub automation with clearer safety boundaries, reusable instructions, and evaluation discipline. It is designed for software product teams working across issues, workflows, planning, release communication, and operational guardrails.

## What this repo includes

- GitHub workflow authoring examples for issue triage and backlog hygiene.
- Reusable agent skills for issue triage, PRD-to-issue breakdowns, and release-note drafting.
- Evaluation harness files for deterministic checks, drift checks, adversarial suites, prompt-injection tests, and pass^k reliability gating.
- Policies, schemas, datasets, and baseline examples to help teams validate outputs before allowing side effects.
- Repository conventions for maintainable community contribution.

## Why this exists

Modern agentic workflows are powerful, but they can also become chaotic if prompts, tool usage, and side effects are mixed together without structure. GitHub’s repository guidance recommends clear README documentation for helping people understand and navigate a project, GitHub topics for discoverability, and community health files such as a code of conduct to support contributions.[cite:141][cite:118][cite:120]

This scaffold takes that idea further by treating workflows, reusable skills, and evals as first-class artifacts that can be reviewed, tested, and improved by a community over time. GitHub’s repository-topic guidance explicitly recommends using topics that describe a repository’s purpose and subject area, while its code-of-conduct guidance emphasizes making collaboration standards visible to contributors.[cite:118][cite:120]

## Who this is for

This repository is aimed at:

- Product engineering teams experimenting with GitHub Agentic Workflows.
- Maintainers who want reusable agent skills rather than one-off prompt files.
- Teams that need stronger guardrails around issue classification, workflow outputs, and evaluation quality.
- Contributors who want to help shape community patterns for safe and useful software-team automation.

## Repository layout

```text
.github/
  workflows/         Markdown-authored workflow definitions and compiled placeholders
  agents/            Repo-level agent role notes
agent-skills/
  skills/            Reusable skills with SKILL.md, references, and assets
apps/
  web/               Example application space
  admin/             Example internal admin space
services/
  api/               Example backend service space
docs/
  product/           Product planning and roadmap docs
  engineering/       Architecture and testing docs
evals/
  datasets/          Golden, safety, adversarial, and prompt-injection cases
  schemas/           Output, trace, baseline, and dataset schemas
  policies/          Label policy and forbidden-action policy
  rubrics/           Quality and safety scoring guidance
  baselines/         Approved baseline summaries for drift comparison
  tools/             Validation and suite-running scripts
```

## Guiding principles

- Normalize agent outputs before side effects.
- Keep instructions modular and reviewable.
- Prefer deterministic checks for safety-critical behavior.
- Use adversarial and prompt-injection evals, not only happy-path tests.
- Treat observability, traceability, and cost metadata as part of product quality.
- Keep community contribution lightweight but structured.

## Quick start

### 1. Clone the repository

```bash
git clone https://github.com/tim-dickey/github-agentic-product-team.git
cd github-agentic-product-team
```

### 2. Review the repo-level guidance

Start with:

- `AGENTS.md`
- `.github/workflows/`
- `agent-skills/`
- `evals/README.md`

### 3. Install eval dependencies

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r evals/requirements.txt
```

### 4. Validate the sample datasets

```bash
python evals/tools/validate_dataset.py \
  --schema evals/schemas/eval_case.schema.json \
  --dataset evals/datasets/issue-triage-golden.jsonl
```

### 5. Run the sample evaluation suite

```bash
python evals/tools/run_suite.py --config evals/config.yaml --adapter local-agent
```

## How to use this scaffold

There are several good ways to use this repository:

- Fork it and adapt the workflows, skills, and datasets to a real product team.
- Borrow only the eval harness and plug in a custom adapter.
- Reuse the skills structure and references layout for a different domain.
- Contribute improved policies, datasets, or workflow examples back to the project.

## Community direction

This repository is intended to be maintained as a community effort. The goal is not to declare one perfect workflow pattern for all teams, but to provide a useful, evolving baseline that teams can test, critique, and improve together.

Community-ready repositories benefit from visible contribution norms and conduct standards, which is why this project includes dedicated contribution and conduct files alongside the code and docs.[cite:141][cite:120]

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request. For community behavior expectations, read [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). For sensitive vulnerabilities or unsafe workflow concerns, use the process in [SECURITY.md](SECURITY.md).[cite:120]

## License

This project is licensed under the Apache License 2.0.
