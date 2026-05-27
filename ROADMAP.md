# Roadmap

Five phases. Each one ships real value. None require the next to be worth using.

## Phase 1 — Clarity Engine (0-3 months)

**Aggregate all assets, cashflows, positions. Build the ultimate treasury dashboard.**

- Unified visibility across wallets, exchanges, and protocols
- Inflow / outflow tracking with intelligent categorization
- Idle capital surfacing
- Runway projection
- Single source of truth for treasury state

Status: ☉ **kernel landed 2026-05-27** · 6 of 8 mathematical layers implemented as pure functions in `kernel/equations.py` · demo runs cleanly · 22 tests pass · 3 xfail invitations open (`tests/test_recursive.py`). Still ahead: chain ingest (`ingest/` module), composite scoring (`score/`), dashboard front-end.

## Phase 2 — Intelligence & Recommendations (3-6 months)

**AI agents analyze, score opportunities, simulate outcomes, recommend allocations.**

- Yield Optimizer agent
- Risk Guardian agent
- Opportunity Detector agent
- Scenario Simulator
- Coherence-adjusted yield scoring (CAY)

Status: 🌱 specifying

## Phase 3 — Execution With Guardrails (6-12 months)

**Automated execution for low-risk strategies. Human approval for higher-risk.**

- Reversible-only automated execution
- Tiered approval flows
- Hard guardrails (principles, risk limits, kill switches)
- Append-only decision log
- Full audit trail

Status: ☉ scaffolding

## Phase 4 — Coherence & Impact Layer (12-18 months)

**Coherence scoring, impact tracking, regenerative metrics.**

- CAY as a measurable metric
- Externality scoring
- Regeneration multipliers
- Impact attribution
- Coherence dashboards

Status: 📐 envisioning

## Phase 5 — Civilization Infrastructure (18+ months)

**Deploy capital into real-world nodes — Zen Village, OneBPO, Full Potential OS, CORA, education, health, environment.**

- Multi-node treasury coordination
- Network-state-grade governance integration
- Real-world asset deployment with on-chain accountability
- Cross-treasury intelligence sharing
- The flourishing-efficiency objective live

Status: 🌌 horizon

---

## Principles that shape every phase

- **Reversibility before automation** — automate what can be undone first.
- **Open before closed** — every component built in the open by default.
- **Useful before token** — usefulness earns participation; we don't sell it.
- **Human-in-the-loop where it matters** — guardrails on direction, AI on execution.
- **Measurement humility** — we measure outcomes, not theater.
