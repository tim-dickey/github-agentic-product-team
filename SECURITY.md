# Security Policy

## Scope

This repository contains workflow definitions, reusable agent skills, eval datasets, schemas, and guardrail patterns for software product teams. Security concerns may include classic software vulnerabilities, but they may also include unsafe workflow behavior, prompt-injection paths, secrets exposure, overly broad permissions, or output-validation gaps.

## Please report privately

Please do **not** open a public issue for any of the following:

- credential or secret exposure
- prompt-injection paths that could trigger unsafe side effects
- permission or auth bypass issues
- unsafe workflow actions that could modify, delete, or disclose sensitive data
- insecure defaults that could cause harm if copied into a live repository
- vulnerabilities in validation logic that could allow untrusted outputs to bypass checks

Instead, use GitHub’s private vulnerability reporting process for the repository if it is enabled, or contact the maintainer privately through the available repository security contact path. GitHub’s community and repository-health guidance supports having clear project policies and health files so contributors know how to participate and where to report issues appropriately.[cite:126][cite:141]

## What to include in a report

Please include as much of the following as you can:

- a short summary of the issue
- affected files or directories
- steps to reproduce
- example inputs or prompts
- expected behavior
- actual behavior
- severity estimate and potential impact
- any suggested mitigation if known

## Preferred handling for agent-specific issues

For unsafe agent or workflow behavior, include:

- the workflow or skill involved
- the adapter or model context if relevant
- whether the issue bypasses schema validation, policy checks, or human escalation
- whether the behavior depends on prompt injection, malformed tool output, or repeated retries
- whether the issue can cause side effects or only incorrect evaluation results

## Response goals

The goal is to:

- acknowledge a valid report promptly
- understand impact and reproducibility
- contain unsafe patterns where needed
- patch the issue responsibly
- document learnings when disclosure is appropriate

## Coordinated disclosure

Please give the maintainer a reasonable opportunity to investigate and respond before disclosing details publicly. Once the issue is understood and fixed, a public summary or advisory may be added when appropriate.

## Supported fixes

Because this is a community scaffold, supported fixes may include:

- changing default workflow permissions
- tightening schemas or policies
- improving eval coverage
- adjusting examples to avoid unsafe patterns
- documenting safer implementation guidance

## No security guarantees

This repository provides examples, scaffolds, and evaluation patterns, not production security guarantees. Teams adopting these materials remain responsible for validating them in their own environments before enabling real side effects.
