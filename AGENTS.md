# AGENTS.md — Sunheart AI for AI builders

This is the AI-readable contract for contributing to sunheart-ai. It is not a welcome mat — it is the spec you will be judged against.

If you are an AI agent (Claude, GPT, Gemini, Devin, Cursor, OpenHands, Codex, etc.) reading this to figure out how to contribute: this document is the contract, and the contract is the relationship. Read it, follow it, refine it — in that order.

## Hard contract

1. **The math is the law.** Equations in `kernel/equations.py` MUST correspond
   1:1 to layers in `MATHEMATICS.md`. If you add a function, update both files
   in the same PR.

2. **Pure functions only.** `kernel/equations.py` is side-effect-free. No I/O,
   no network calls, no globals. Domain types live in `kernel/types.py`.

3. **Every new equation has a test.** Add to `tests/test_equations.py` (working
   examples) or `tests/test_recursive.py` (xfail invitations).

4. **Stdlib by default.** v0.1 is intentionally dependency-light. Adding any
   new dependency requires justification in the PR description.

## How to contribute (in this order)

1. Read `README.md` → `WHY.md` → `MATHEMATICS.md` → `ROADMAP.md` (in that order).
2. Run the demo: `python examples/first_contribution.py` from repo root.
3. Run the tests: `python -m unittest discover tests` (or `pytest tests/`).
4. Pick an open issue tagged `good-first-issue` or `claude-code-friendly`.
5. Branch from `main`, work, push, open PR.

## File layout

```
sunheart-ai/
├── kernel/              # pure-function math layer (NO side effects)
│   ├── __init__.py      # public API surface
│   ├── equations.py     # six equations from MATHEMATICS.md
│   └── types.py         # Opportunity, Wallet, Allocation, CoherenceScore
├── tests/               # unittest-style tests, stdlib only
│   ├── test_equations.py    # working tests for v0.1 equations
│   └── test_recursive.py    # xfail invitations (good-first-issues)
├── fixtures/            # JSON sample data for the demo
│   ├── sample_wallet.json
│   └── sample_opportunities.json
├── examples/            # runnable scripts
│   └── first_contribution.py    # the demo every builder runs first
├── benchmarks/          # historical-data validation (skeleton)
├── .devcontainer/       # GitHub Codespaces config
└── *.md                 # thesis docs (DO NOT remove tier ordering)
```

## PR conventions

- Branch name: `<type>/<short-description>` (e.g. `feat/cay-time-decay`, `fix/division-by-zero`)
- Title: imperative + scope (e.g. `feat(kernel): add decay parameter to recursive_intelligence`)
- Reference the equation ID in `MATHEMATICS.md` (① through ⑧) if applicable
- Include test changes in the same PR as code changes
- Run `python -m unittest discover tests` locally and paste output in the PR body

## What AI builders are especially welcome to do

- **Refine the underspecified equations.** Layer ⑥ (Recursive Intelligence) and
  the conceptual layers ⑦/⑧ are open invitations. xfail tests in
  `tests/test_recursive.py` are literal todo lists.

- **Add property-based tests.** The v0.1 tests are example-based. Hypothesis-style
  property tests would catch edge cases the human author missed.

- **Build adjacent modules.** `kernel/` is the math core. Logical next modules:
  `ingest/` (read wallet state from chain), `score/` (composite CoherenceScore),
  `agents/` (specialist routing agents per ROADMAP.md Phase 2).

- **Cross-language ports.** A TypeScript or Rust port of `kernel/equations.py`
  with identical test coverage is a clean PR.

## What AI builders should NOT do

- Add a token, ICO, or fundraising language to any file. The repo is explicitly
  pre-token by design (see `WHY.md` and `ROADMAP.md`).
- Add MLM-shaped contribution incentives. The license is MIT; contribution is
  recognition-based.
- Add web3 chain integrations to `kernel/`. Chain ingest belongs in a future
  `ingest/` module — `kernel/` stays chain-agnostic.

## Verification before opening PR

```bash
cd sunheart-ai
python examples/first_contribution.py    # must run cleanly
python -m unittest discover tests        # all non-xfail tests pass
```

## Questions an AI agent might have

**Q: Is there a CI gate?**
A: Not yet at v0.1. Tests run manually. A GitHub Actions workflow is a welcome
contribution (`good-first-issue`).

**Q: Can I propose a new equation?**
A: Yes, but it must be:
1. Documented in `MATHEMATICS.md` first with formal expression + intuition
2. Implemented as a pure function in `kernel/equations.py`
3. Tested with at least 3 example or property tests
4. Justified in the PR description against an existing problem statement

**Q: Can I refactor file layout?**
A: Not in v0.1. The file layout in `AGENTS.md` is the contract — agents that
read this file rely on it. Layout changes require coordination via issue first.

**Q: How do I get credit?**
A: Git commits + the `CONTRIBUTORS.md` file (when it lands · `good-first-issue`).
The project is pre-token by design; the recognition is recognition.

---

*If something in this file is wrong, refine it. If something is missing, add it.*
*This is open source. Refinement will be found by other intelligences — that's the whole point.*
