# Benchmarks

How CAY-adjusted scoring compares to naive APY-chasing on historical data.

## Status — v0.1 skeleton

This directory holds the scaffold for empirical validation of the kernel. The
core question: does the kernel's coherence-adjusted scoring actually outperform
naive APY-chasing over multi-year windows?

**This is an open invitation.** The current state is a directory + this README.
A real benchmark suite is a `[good-first-issue]` waiting for a builder.

## What a real benchmark needs

1. **Historical opportunity data** — at minimum, 24 months of Aave/Compound/Pendle
   APYs + risk events (depegs, hacks, governance failures)
2. **Two strategies** — `apy_max` (sort by raw expected_return) vs `cay_ranked`
   (sort by `optimal_allocation()` score from `kernel/equations.py`)
3. **Outcome metrics** — final treasury value, drawdown depth, days-in-drawdown,
   number of strategies switched
4. **Reproducible run** — `python benchmarks/run.py --start 2024-01-01 --end 2026-01-01`
5. **CSV output** — versioned in this directory for transparency

## Proposed file structure

```
benchmarks/
├── README.md (this file)
├── run.py                    # entry point, takes --start/--end flags
├── data/
│   ├── aave_v3_apys.csv      # daily APY snapshots
│   ├── pendle_pt_yields.csv
│   └── risk_events.csv       # depegs, hacks, governance fails
├── strategies/
│   ├── apy_max.py            # baseline: chase highest APY
│   ├── cay_ranked.py         # uses kernel.optimal_allocation
│   └── coherence_only.py     # uses kernel.cay
└── results/
    └── 2024-01_to_2026-01.csv
```

## Why this matters

The thesis claim from `WHY.md` is "5% regenerative yield may outperform 15%
extractive yield long-term." This benchmark is how the claim earns or loses
credibility. Until it runs against real data, the math is theory.

## How to contribute

If you have access to historical DeFi APY data:
1. Open an issue describing the data source + license
2. Land a PR with `benchmarks/data/<source>.csv` + a fetch script
3. Implement at least one strategy file
4. Run `python benchmarks/run.py` and commit the result CSV

If you don't have data: the harness itself (run.py + strategy interface) can be
built against synthetic data first. That's a clean v0 PR.

## Reference for AI builders

The strategies must call into `kernel.equations` — do not reimplement the math.
That keeps `kernel/` as the single source of truth for the equations and the
benchmarks as the empirical validator.

```python
from kernel import optimal_allocation, cay
from kernel.types import Opportunity

# given a list of Opportunity objects per day, sort by optimal_allocation
ranked = sorted(opps_today, key=optimal_allocation, reverse=True)
chosen = ranked[0]
```
