---
on:
  issues:
    types: [opened, edited]

permissions:
  contents: read
  issues: write
  pull-requests: read

tools:
  - search
  - labels
  - comments

safe-outputs:
  issue_labels:
    allowed:
      - type:bug
      - type:feature
      - type:support
      - type:docs
      - type:duplicate
      - area:web
      - area:admin
      - area:api
      - area:auth
      - area:billing
      - area:notifications
      - area:analytics
      - area:docs
      - severity:critical
      - severity:high
      - severity:medium
      - severity:low
  issue_comment: {}

agent:
  skill-hints:
    - issue-triage
---

# Goal

Classify newly opened or edited issues for the product team.

## Success conditions

A run is successful if:
- exactly one `type:*` label is selected
- exactly one `area:*` label is selected
- exactly one `severity:*` label is selected
- no forbidden labels are used
- a follow-up comment is added only when action is blocked by missing information

## Failure conditions

Stop and declare failure if:
- the issue content is unavailable
- no allowed label can reasonably fit
- the task would require closing the issue or taking an action outside the allowed outputs

## Instructions

1. Read the issue title, body, and any template fields.
2. Apply exactly one `type:*` label, one `area:*` label, and one `severity:*` label.
3. If the issue is actionable, do not ask extra questions.
4. If key details are missing, leave one concise follow-up comment.
5. Never close the issue.
6. Never speculate about root cause as if confirmed.
7. Never mention internal systems, secrets, or implementation guesses.
8. Use a calm, concise tone.
