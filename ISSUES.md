# Open contribution surfaces

Five concrete issues land in GitHub at https://github.com/jamessunheart/sunheart-ai/issues
when the substrate-sprint (this commit) lands. They are mirrored here so this file
serves as the canonical record even if GitHub goes offline.

## [good-first-issue] 1. Surprise-aware Recursive Intelligence

**File:** `kernel/equations.py` · `recursive_intelligence()`
**Test:** `tests/test_recursive.py::test_surprise_amplifies_learning` (currently xfail)

The v0.1 implementation treats all verified outcomes as equal-weight additive
learning. The math layer ⑥ should weight surprising outcomes more heavily.

**Acceptance:**
- Add `expected_outcome` parameter (default 0.0 for backward-compat)
- Compute `surprise = abs(verified_learning - expected_outcome)`
- Scale learning impact by `(1 + surprise)`
- xfail decorator removed; test passes
- Update MATHEMATICS.md ⑥ section with the refined formal expression

**Tags:** `good-first-issue` · `kernel` · `math` · `claude-code-friendly`

## [good-first-issue] 2. Time-decay on Recursive Intelligence

**File:** `kernel/equations.py`
**Test:** `tests/test_recursive.py::test_old_learning_decays` (currently xfail)

Old verified outcomes should fade. Without decay, the treasury intelligence
carries dead weight from outcomes that no longer reflect current conditions.

**Acceptance:**
- Accept a list of `(timestamp, learning)` tuples instead of a single scalar
- Add `half_life_days` parameter (default 90)
- Apply exponential decay based on timestamp distance from now
- xfail removed; test passes

**Tags:** `good-first-issue` · `kernel` · `math` · `claude-code-friendly`

## [good-first-issue] 3. Property-based tests via Hypothesis

**File:** new `tests/test_properties.py`

The current tests are example-based. Hypothesis-style property tests would catch
edge cases (negative inputs, NaN, infinity) the human author missed.

**Acceptance:**
- Add `hypothesis` to a `requirements-dev.txt` (kernel/ stays stdlib-only)
- Property test for `power()`: doubling money always doubles power
- Property test for `cay()`: zero coherence always zeroes the score
- Property test for `optimal_allocation()`: increasing risk monotonically reduces score
- All pass on `pytest tests/`

**Tags:** `good-first-issue` · `tests` · `claude-code-friendly`

## [good-first-issue] 4. CLI: `sunheart score`

**File:** new `cli/sunheart.py` + entry point in `pyproject.toml`

A command-line interface that wraps `examples/first_contribution.py`:
```
sunheart score --wallet path/to/wallet.json --opportunities path/to/opps.json
```

Outputs JSON to stdout for piping into other tools.

**Acceptance:**
- `pip install -e .` installs `sunheart` on PATH
- Accepts `--wallet` and `--opportunities` flags
- Outputs JSON: `{"power": float, "efficiency": float, "ranked": [{"id": str, "score": float, "cay": float}, ...]}`
- `--help` shows usage
- Tests cover the CLI parsing

**Tags:** `good-first-issue` · `cli` · `human-friendly`

## [claude-code-friendly] 5. Benchmark harness (skeleton → working)

**File:** `benchmarks/run.py` + `benchmarks/strategies/*.py`

See `benchmarks/README.md` for the full spec. The skeleton exists; what's
needed is the actual harness + at least one strategy (`apy_max` baseline) +
synthetic data fixtures to start.

**Acceptance:**
- `python benchmarks/run.py --start 2024-01-01 --end 2026-01-01` runs without error
- Two strategies implemented: `apy_max` (raw return) and `cay_ranked` (kernel-driven)
- CSV output in `benchmarks/results/` with final-value + drawdown columns
- README updated with results table

**Tags:** `claude-code-friendly` · `benchmarks` · `kernel`

---

## How to claim an issue

1. Comment on the GitHub issue: "claiming"
2. Branch from `main`: `git checkout -b <type>/<short-description>`
3. Open a draft PR within 48 hours so others know it's active
4. If you stall, comment "unclaiming" and someone else picks up

## How to propose a new issue

Open an issue with:
- The equation or layer from MATHEMATICS.md it touches (or names a new one)
- An acceptance test (concrete, runnable)
- A scope estimate (<2hrs, <half-day, etc.)
