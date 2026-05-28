# github-agentic-product-team

A community scaffold for GitHub Agentic Workflows, skills, evals, and guardrails for software product teams.

This repository is an open starter kit for teams experimenting with agent-driven GitHub automation in a product engineering context. It combines workflow definitions, reusable skills, evaluation tooling, and community health files so contributors can evolve the project in the open.[web:175][web:141]

## What is in this repo

Today, this repository includes:

- Markdown-authored GitHub workflow definitions and placeholder compiled workflow files in `.github/workflows/`
- A repo-level agent note in `.github/agents/repo-maintainer.md`
- Reusable skills in `agent-skills/skills/` for:
  - `issue-triage`
  - `prd-to-issues`
  - `release-notes`
- Supporting skill guidance in `references/` and reusable templates in `assets/`
- An evaluation harness in `evals/` with:
  - datasets
  - schemas
  - policies
  - rubrics
  - baselines
  - tools
  - report output directory
- Documentation stubs in `docs/product/` and `docs/engineering/`
- Placeholder monorepo-style directories for future implementation work in:
  - `apps/web`
  - `apps/admin`
  - `services/api`
  - `packages/ui`
  - `packages/domain`

## Repository structure

```text
.github/
  agents/
    repo-maintainer.md
  workflows/
    new-issue-triage.md
    new-issue-triage.lock.yml
    weekly-backlog-hygiene.md
    weekly-backlog-hygiene.lock.yml

agent-skills/
  AGENTS.md
  skills/
    issue-triage/
      SKILL.md
      assets/
      references/
    prd-to-issues/
      SKILL.md
      assets/
      references/
    release-notes/
      SKILL.md
      assets/
      references/

docs/
  engineering/
    architecture.md
    testing-strategy.md
  product/
    roadmap.md

evals/
  baselines/current/
  datasets/
  policies/
  reports/
  rubrics/
  schemas/
  tools/
  config.yaml
  README.md
  requirements.txt

apps/
  admin/
  web/

services/
  api/

packages/
  domain/
  ui/

AGENTS.md
APACHE-2.0-LICENSE.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
README.md
SECURITY.md
```

## Current focus

The repository is currently strongest as a **pattern library and scaffold** for:

- GitHub issue triage workflows
- backlog hygiene workflows
- reusable skill organization
- evaluation-driven workflow safety
- prompt-injection and adversarial test coverage
- community-driven iteration on agent guardrails

The `apps`, `services`, and `packages` directories are present as placeholders for future example implementation work, not as finished application code today.

## Why this project exists

Agentic workflows are more useful when teams can review the instructions, constrain the outputs, and test risky behavior before enabling side effects. This repository is structured around that idea: workflows define intent, skills capture reusable operating knowledge, and evals check whether outputs stay inside acceptable boundaries.[web:141]

It is also meant to be a community-maintained reference repo. GitHub recommends including a README and other community health files so people can understand a project and contribute more effectively, which is why this repository includes contribution, conduct, and security docs alongside the workflow and eval artifacts.[web:141][web:185]

## Quick start

### 1. Clone the repository

```bash
git clone https://github.com/tim-dickey/github-agentic-product-team.git
cd github-agentic-product-team
```

### 2. Explore the key entry points

Start here:

- `AGENTS.md`
- `.github/workflows/`
- `agent-skills/AGENTS.md`
- `agent-skills/skills/`
- `evals/README.md`

### 3. Install eval dependencies

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r evals/requirements.txt
```

On PowerShell:

```powershell
python -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
pip install -r evals/requirements.txt
```

### 4. Validate a dataset

```bash
python evals/tools/validate_dataset.py \
  --schema evals/schemas/eval_case.schema.json \
  --dataset evals/datasets/issue-triage-golden.jsonl
```

### 5. Run the sample eval suite

```bash
python evals/tools/run_suite.py --config evals/config.yaml --adapter local-agent
```

## How to contribute

Useful contributions include:

- improving workflow instructions
- tightening schemas and policies
- adding stronger negative test cases
- improving documentation and examples
- refining skill structure and references
- expanding guardrails for real-world product team use cases

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

## Community standards

This is intended to be a community effort. Please read:

- [CONTRIBUTING.md](CONTRIBUTING.md)
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)
- [SECURITY.md](SECURITY.md)

## License

This repository is currently distributed with an Apache 2.0 license file. For best GitHub license detection, it is usually better to rename `APACHE-2.0-LICENSE.md` to `LICENSE` while keeping the same license text.[web:141]