"""
first_contribution.py — your first sunheart-ai run.

Runs the v0.1 kernel against the sample fixtures and prints CoherenceScores
+ ranked Allocations. This is the demo every builder should run first.

Usage:
    python examples/first_contribution.py

Expected output: a ranked table of opportunities sorted by optimal_allocation()
score, with each row annotated by CAY (long-arc adjusted yield).

If you can read this output and the math feels intuitive, you understand the
v0.1 kernel. Now look at ISSUES.md and pick a good-first-issue.
"""

import json
import sys
from pathlib import Path

# Make the kernel importable when running from repo root
sys.path.insert(0, str(Path(__file__).parent.parent))

from kernel import (
    power,
    treasury_efficiency,
    cay,
    optimal_allocation,
    velocity_value,
)
from kernel.types import Opportunity, Wallet


def load_fixtures():
    root = Path(__file__).parent.parent / "fixtures"
    with open(root / "sample_wallet.json") as f:
        wallet_data = json.load(f)
    with open(root / "sample_opportunities.json") as f:
        opps_data = json.load(f)

    wallet = Wallet(
        total_usd=wallet_data["total_usd"],
        idle_usd=wallet_data["idle_usd"],
        productive_usd=wallet_data["productive_usd"],
        fragmentation_count=wallet_data["fragmentation_count"],
        cognitive_load=wallet_data["cognitive_load"],
    )
    opportunities = [Opportunity(**o) for o in opps_data]
    return wallet, opportunities


def main():
    print("☉ Sunheart AI · kernel v0.1 demo\n" + "=" * 60)
    wallet, opportunities = load_fixtures()

    # Treasury state diagnostics
    productive_flow = wallet.productive_usd * 0.06  # crude annualized
    entropy_estimate = (
        wallet.fragmentation_count * 1000
        + wallet.idle_usd * 0.02
        + wallet.cognitive_load * 5000
    )
    efficiency = treasury_efficiency(productive_flow, entropy_estimate)

    # Power proxy: assume current annual velocity = productive/total
    current_velocity = wallet.productive_usd / max(wallet.total_usd, 1)
    current_coherence = 1.0  # baseline — no scoring yet
    p = power(wallet.total_usd, current_velocity, current_coherence)

    print(f"\nTreasury state:")
    print(f"  Total:           ${wallet.total_usd:>12,.2f}")
    print(f"  Idle:            ${wallet.idle_usd:>12,.2f}  ← {wallet.idle_usd/wallet.total_usd:.0%} of treasury")
    print(f"  Productive:      ${wallet.productive_usd:>12,.2f}")
    print(f"  Fragmentation:    {wallet.fragmentation_count:>12} accounts/chains")
    print(f"  Cognitive load:   {wallet.cognitive_load:>12.2f}  (0=clear, 1=overwhelmed)")
    print(f"\nDerived metrics:")
    print(f"  ① Power (M × V × C):       {p:>16,.2f}")
    print(f"  ② Treasury Efficiency:     {efficiency:>16.2f}  (productive flow ÷ entropy)")
    print(f"  ⑤ Velocity Value:          {velocity_value(productive_flow, current_coherence):>16,.2f}")

    # Score + rank opportunities
    print("\n" + "=" * 60)
    print("Opportunities ranked by ④ Optimal Allocation score:\n")
    print(f"  {'Rank':<5}{'ID':<30}{'Score':>12}{'CAY':>10}")
    print("  " + "-" * 57)

    scored = []
    for opp in opportunities:
        score = optimal_allocation(opp)
        coh_yield = cay(opp.expected_return, opp.coherence_multiplier, opp.sustainability)
        scored.append((score, coh_yield, opp))

    scored.sort(key=lambda t: t[0], reverse=True)
    for rank, (score, coh_yield, opp) in enumerate(scored, 1):
        print(f"  {rank:<5}{opp.id:<30}{score:>12.4f}{coh_yield:>10.4f}")

    # The reveal
    print("\n" + "=" * 60)
    top = scored[0][2]
    bottom = scored[-1][2]
    print(f"\nIn this sample fixture, '{top.name}' ranks first by the kernel's score.")
    print(f"Its raw yield ({top.expected_return:.1%}) may not be the highest available")
    print(f"— but its allocation score is, because Risk, Alignment, and Liquidity matter.\n")
    print(f"Conversely: '{bottom.name}' shows a {bottom.expected_return:.1%} yield")
    print(f"but ranks last — high risk + low alignment + extractive sustainability.\n")
    print("This is the thesis: intelligence-directed capital ≠ chase highest APY.\n")
    print("(This is a math demonstration on synthetic data. Not financial advice.")
    print(" See DISCLAIMER.md.)\n")
    print("Next: open ISSUES.md, pick a [good-first-issue], submit a PR.")
    print("=" * 60)


if __name__ == "__main__":
    main()
