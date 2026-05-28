# Severity examples

## severity:critical

Use when:
- users cannot log in at scale
- payment failures charge users incorrectly
- data is lost or corrupted
- a security risk or auth bypass is reported
- a core workflow is broadly unavailable

## severity:high

Use when:
- a major feature is broken for many users
- no reasonable workaround exists
- admin operations are blocked for the support team

## severity:medium

Use when:
- the issue is real and user-facing
- scope is limited
- a workaround exists, or only part of the workflow is affected

## severity:low

Use when:
- impact is cosmetic or narrow
- it affects edge cases only
- it is a small docs gap
- it is annoying but not operationally risky

## Bias rules

If the issue involves billing, auth, privacy, or data integrity, bias upward rather than downward.
