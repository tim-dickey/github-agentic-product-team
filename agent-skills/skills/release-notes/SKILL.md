---
name: release-notes
description: Draft customer-facing and internal release notes from merged work. Use when summarizing shipped changes for users, support, sales, or internal stakeholders.
version: "1.0"
license: "See repository license"
---

# Purpose

Turn merged work into clear release notes for different audiences.

## Audience modes

- Customer-facing: concise, benefit-oriented, no internal jargon
- Internal: operational detail, rollout notes, support impact, known limitations

## Rules

- Describe shipped outcomes, not implementation trivia.
- Do not mention unreleased work.
- Do not promise future work or dates.
- Keep security-sensitive detail out of public notes.
- Group related changes when that improves readability.

## Workflow

1. Review merged pull requests, linked issues, and product context.
2. Identify the user-visible outcome of each change.
3. Group changes by theme when useful.
4. Write one customer-facing version and one internal version when requested.

## Never do

- Do not copy PR text verbatim if it is too technical.
- Do not expose internal incident details in customer-facing notes.
- Do not list changes that were reverted or not shipped.
