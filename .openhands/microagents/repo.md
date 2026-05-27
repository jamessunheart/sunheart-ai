---
name: sunheart-ai
type: repo
agent: CodeActAgent
---

# Sunheart AI — repo microagent

You are contributing to **Sunheart AI**, open-source treasury intelligence.

## Boot reads (in order)
1. `README.md` — what this is
2. `AGENTS.md` — the AI contract (read this every time)
3. `MATHEMATICS.md` — the 8 kernel layers
4. `ISSUES.md` — the 5 named good-first-issues
5. `kernel/equations.py` + `tests/test_equations.py` — current implementation

## House rules
- **Pure functions only** in `kernel/`. No I/O, no chain calls, no globals.
- **Tests are the contract.** Update `tests/` for every kernel change.
- **Anchor every change to a layer.** Cite the layer number in the PR body.
- **No new dependencies** without a one-line justification in the PR body.
- **Python 3.10+ stdlib only** for the kernel. (Extras live in `adapters/` and may pull deps.)

## Verification before opening PR
```bash
python -m unittest discover tests -v
python examples/first_contribution.py
```

Both must pass on Python 3.10/3.11/3.12 (CI matrix).

## Where chain integration lands
`adapters/` and `mocks/` (when they exist) — NOT inside `kernel/`. Keep the math pure.
