# Security Policy

## Supported versions

| Version | Status |
|---------|--------|
| v0.1.x  | active development · receives security fixes |

The project is in early-substrate phase (v0.1, Day 1 as of 2026-05-27). The supported-version table will expand as releases tag.

## Reporting a vulnerability

If you discover a security issue — in the kernel, in any agent contract, in the build/deploy pipeline, or in any infrastructure described in this repository — please **do not open a public GitHub issue**.

Instead, email:

**[james@fullpotential.com](mailto:james@fullpotential.com)**

Use subject line: `[sunheart-ai SECURITY] <one-line summary>`

Include:
- Affected file or commit
- Steps to reproduce (or proof-of-concept)
- Suggested fix, if you have one
- Your preferred attribution name (or "anonymous")

You should receive an acknowledgement within 48 hours. We'll work with you on disclosure timing.

## Scope

In scope:
- `kernel/` — pure-function math layer
- `tests/` — test suite
- `examples/` — demo scripts
- `fixtures/` — sample data
- `.devcontainer/` — development environment config

Out of scope (until later phases land):
- Treasury execution paths (Phase 3+ · not yet built)
- On-chain integrations (Phase 2 · not yet built)
- Agent execution permissions (Phase 2-3 · not yet built)

## Responsible disclosure principles

- Coordinated disclosure preferred
- 90-day default disclosure window
- Earlier disclosure if exploitation is in the wild
- Credit to reporter in CHANGELOG.md unless they prefer anonymity

## What this project will NOT do

- Pay bug bounties at v0.1 (no treasury exists)
- Sue or threaten reporters acting in good faith
- Demand NDAs

If something is broken, we want to know. Refinement is the whole point.

---

*Last reviewed: 2026-05-27*
