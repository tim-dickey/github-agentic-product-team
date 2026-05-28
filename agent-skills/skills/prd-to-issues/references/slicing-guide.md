# Slicing guide

## Preferred order

Break work into slices in this order:
1. user journey slice
2. admin/support slice
3. platform or API support
4. observability and follow-up hardening

## Good slice tests

A good slice:
- has one clear outcome
- can be reviewed in one sitting
- has acceptance criteria that describe observable behavior
- can be tested independently

## Smells

A slice is too broad if:
- it spans many systems without a single visible outcome
- it needs many follow-up tickets just to be testable
- it sounds like a project phase rather than a deliverable
