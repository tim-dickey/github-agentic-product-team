# Agent evaluation harness

This directory contains the evaluation and testing harness for workflows, skills, and guardrails.

## What is new in this version

- Pass^k support for high-risk consistency gating
- Adversarial and prompt-injection datasets
- Trace IDs, run IDs, tool IDs, and per-run cost accounting
- Loop/stall detection
- Expanded schemas for richer observability

## Why pass^k matters

Pass@k asks whether at least one of many attempts succeeds.
Pass^k asks whether all repeated attempts succeed.
For high-risk agent actions, pass^k is a better reliability bar because consistency matters more than lucky wins.

## Usage

Validate a dataset:

```bash
python evals/tools/validate_dataset.py \
  --schema evals/schemas/eval_case.schema.json \
  --dataset evals/datasets/prompt-injection-negative.jsonl
```

Run the full suite:

```bash
python evals/tools/run_suite.py --config evals/config.yaml --adapter local-agent
```

## Adapter contract

Your adapter should normalize agent output to:

- `selected_labels`
- `comment`
- `escalate_to_human`
- `actions`
- `trace`
- `meta`

The harness validates that object.
Only validated outputs should be allowed to trigger side effects.
