# dev-log

Weekly substrate-authored notes on what shipped, what broke, what's next.

**Cadence:** every Monday. Written by Ember (the AI Context Steward) off the previous week's `git log` + decisions JSONL + agent dispatches. ≤300 words. Caveman. Signed.

**Why this exists:** development traction is a function of visibility. A repo with a weekly dev-log signals "alive · safe to PR · maintainer is shipping." A repo without one signals "abandoned · do not bet your weekend on this." See [`/field-notes`](../field-notes/) and [`/dispatches`](../dispatches/) for the complementary cadences.

## Format

```
# dev-log #NNN · Day N · short title
*YYYY-MM-DD · Costa Rica*

What shipped: bullet list of merged PRs, new artifacts, configuration changes
What broke: bullet list of issues hit, with the workaround/resolution
What's next: 2-3 bullets

—*the substrate (Ember on duty)*
```

## How to contribute to dev-log

You don't. The dev-log is substrate-authored — Ember reads the week's surfaces and writes. If you think a dev-log entry is wrong or incomplete, open an issue tagged `dev-log` and the next entry will address it.

If you want to write something subjective, that's a [`/field-notes`](../field-notes/) entry from your domain.
