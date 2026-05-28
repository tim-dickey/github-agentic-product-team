---
name: issue-triage
description: Review new product, bug, support, and docs issues. Use when classifying GitHub issues, assigning labels, and deciding whether more information is required.
version: "1.0"
license: "See repository license"
---

# Purpose

Help the product team route incoming issues quickly and consistently.

## Inputs

You may inspect:
- Issue title
- Issue body
- Template fields
- Existing labels
- Linked pull requests or docs
- Nearby code or docs context when available

## Required outputs

For each issue:
1. One `type:*` label
2. One `area:*` label
3. One `severity:*` label
4. A concise follow-up comment only if action is blocked by missing information

## Type labels

Choose one:
- `type:bug`
- `type:feature`
- `type:support`
- `type:docs`
- `type:duplicate`

## Area labels

Choose one:
- `area:web`
- `area:admin`
- `area:api`
- `area:auth`
- `area:billing`
- `area:notifications`
- `area:analytics`
- `area:docs`

## Severity labels

Choose one:
- `severity:critical` - outage, security risk, data loss, billing breakage, or blocked core workflow for many users
- `severity:high` - major feature broken and no reliable workaround
- `severity:medium` - meaningful defect with limited scope or workaround available
- `severity:low` - minor issue, edge case, cosmetic problem, or low-impact docs gap

## Actionability test

An issue is actionable if it contains enough information to begin investigation.

Usually sufficient:
- clear summary
- expected behavior
- actual behavior
- reproduction steps or a credible scenario
- environment details when relevant

If the issue is not actionable, ask for only the minimum missing detail.

## Duplicate policy

Apply `type:duplicate` only when a clear canonical issue exists and the symptom strongly matches.

When uncertain, do not mark as duplicate.

## Comment style

When more information is needed:
- thank the reporter briefly
- ask one compact question or one short bullet list
- explain why that detail matters
- do not overwhelm the reporter

## Never do

- Do not promise dates.
- Do not close the issue unless explicitly allowed.
- Do not speculate about root cause as if it is confirmed.
- Do not downgrade security, billing, auth, or data integrity issues to cosmetic severity.
