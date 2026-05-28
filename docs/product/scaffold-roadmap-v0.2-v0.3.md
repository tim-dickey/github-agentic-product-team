# Scaffold roadmap: v0.2 and v0.3

## Goal

Evolve `github-agentic-product-team` from a strong static scaffold into a community-maintained reference repository with better contributor pathways, stronger eval discipline, and more realistic workflow examples.

## v0.2 priorities

### 1. Community contribution maturity

Target outcome:
- Make it easier for outside contributors to propose useful changes without guessing repository norms.

Planned work:
- Add issue forms for bugs and feature requests.
- Add a pull request template aligned with workflow, skill, and eval changes.
- Add starter labels and triage guidance in docs.
- Add a maintainer section that explains how issues move from idea to merge.

Success signals:
- Fewer vague issues.
- More PRs with enough context to review quickly.
- Clearer routing of sensitive reports to `SECURITY.md`.

### 2. Workflow refinement

Target outcome:
- Make the sample workflows feel more realistic and less placeholder-like.

Planned work:
- Improve `new-issue-triage.md` with clearer success criteria, escalation rules, and comment restraint.
- Add one more workflow example, such as documentation-change review or release-note drafting.
- Document the expected contract between workflow outputs and adapter validation.

Success signals:
- Workflow files become easier to remix.
- Contributors can reason about safe outputs without reading every file in the repo.

### 3. Eval coverage improvement

Target outcome:
- Increase confidence that example workflows fail safely under ambiguous, adversarial, or incomplete inputs.

Planned work:
- Expand issue-triage goldens with better low-context and edge-case issues.
- Add more prompt-injection and policy-violation cases.
- Add expected failure notes for intentionally weak stub behavior.
- Document baseline update procedure.

Success signals:
- Better visibility into regressions.
- Clearer distinction between happy-path and abuse-case performance.

### 4. Scaffold-to-real-repo documentation

Target outcome:
- Help teams adapt this scaffold into their own repo structure.

Planned work:
- Add a guide for forking and customizing labels, policies, and skill names.
- Add a migration guide for replacing the stub adapter with a real one.
- Add examples of how to trim unused folders for smaller teams.

Success signals:
- New adopters can get value faster.
- Fewer questions about which parts are placeholders versus required patterns.

## v0.3 priorities

### 1. Reference implementation depth

Target outcome:
- Move from scaffold-only examples to more end-to-end examples that feel deployable.

Planned work:
- Add at least one better-developed reference workflow with adapter expectations and example outputs.
- Add example issue labels, sample triage comments, and a sample baseline-review workflow.
- Add richer report examples in `evals/reports/` documentation.

Success signals:
- The repo becomes a stronger teaching artifact.
- Community contributors can compare ideas against a more realistic baseline.

### 2. Governance and maintenance model

Target outcome:
- Make community maintenance sustainable.

Planned work:
- Define contribution tiers such as docs-only, eval-only, and workflow-shape changes.
- Add maintainer guidelines for accepting breaking changes.
- Define versioning expectations for scaffold milestones.
- Add a changelog or release-note pattern for project evolution.

Success signals:
- Fewer ambiguous maintainer decisions.
- Better continuity as more contributors participate.

### 3. Evaluation reporting and observability

Target outcome:
- Improve the usefulness of eval outputs for maintainers.

Planned work:
- Add machine-readable summary output for CI.
- Add better markdown reports with suite-level failure explanations.
- Document how to compare run cost, variance, and failure modes over time.
- Add examples of loop/stall debugging guidance.

Success signals:
- Easier review of agent behavior changes.
- Faster diagnosis when a workflow regresses.

### 4. Expanded skill library

Target outcome:
- Broaden the scaffold beyond the initial three skills without turning it into a junk drawer.

Candidate additions:
- docs-change-review
- support-escalation-routing
- release-checklist-prep
- roadmap-slice-planning

Success signals:
- More reusable patterns.
- Clear evidence that the repo can scale without losing structure.

## Out of scope for now

The following are intentionally not required for v0.2 or v0.3:
- shipping a production SaaS app from the placeholder directories
- supporting every agent framework
- guaranteeing production-grade security by default
- maintaining broad CI/CD infrastructure beyond scaffold needs

## Milestone framing

### v0.2

Theme: contributor-ready scaffold

A good v0.2 makes the repository easier to understand, safer to extend, and more consistent to contribute to.

### v0.3

Theme: reference-quality community baseline

A good v0.3 makes the repository not just a starter scaffold, but a stronger shared reference for real product-team agent workflow design.
