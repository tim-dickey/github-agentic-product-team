---
on:
  schedule:
    - cron: "0 15 * * 1"
  workflow_dispatch:

permissions:
  contents: read
  issues: write
  pull-requests: read

tools:
  - search
  - labels
  - comments

safe-outputs:
  issue_comment: {}
  issue_labels:
    allowed:
      - status:needs-info
      - status:ready-for-refinement
      - status:stale-candidate
      - status:blocked
      - priority:p1
      - priority:p2
      - priority:p3
---

# Goal

Review open issues and improve backlog quality for the product team.

## Success conditions

A run is successful if:
- only allowed labels are applied
- comments are short and action-oriented
- no issue is closed automatically
- high-risk issues are escalated rather than improvised on

## Instructions

1. Find open issues with missing labels, unclear next steps, or outdated status.
2. Add only labels from the allowed list.
3. Leave a short comment only when it clarifies the next action.
4. Do not close issues automatically.
5. Do not relabel issues that were updated recently unless the current labels are clearly wrong.
6. Escalate billing, auth, privacy, and security concerns by leaving them untouched for human review unless explicitly instructed otherwise.
