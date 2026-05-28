---
name: prd-to-issues
description: Convert a product requirements document into small, independently executable engineering issues. Use when a PM, designer, or engineer wants implementation work broken into delivery slices.
version: "1.0"
license: "See repository license"
---

# Purpose

Translate a PRD into delivery-ready engineering issues for a product team.

## Principles

- Prefer vertical slices over layer-based tickets.
- Separate user-visible value from enabling work.
- Keep issues reviewable and testable.
- Surface uncertainty early.

## Workflow

1. Read the PRD carefully.
2. Identify the user journey, business goal, and acceptance criteria.
3. Split the work into slices that can be built and validated independently.
4. Create enabling tasks only when they unblock multiple slices or reduce meaningful risk.
5. Keep dependency chains shallow.
6. Flag open questions explicitly.

## Good issue characteristics

Each issue should include:
- outcome
- scope
- acceptance criteria
- risks or unknowns
- likely owner discipline if obvious

## Slice rules

Prefer:
- "User can reset password from login screen"
- "Admin can filter invoices by status"
- "API records an audit event for refund actions"

Avoid:
- "Build backend for password reset"
- "Create frontend screens"
- "Implement database changes"

## Never do

- Do not create a single mega-issue for a large feature.
- Do not invent requirements without labeling them as assumptions.
- Do not split work so finely that no issue delivers meaningful progress.
- Do not hide major unknowns inside vague implementation notes.
