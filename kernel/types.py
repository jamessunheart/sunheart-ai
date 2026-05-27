"""
Domain types for the Sunheart AI kernel.

Kept minimal and stdlib-only for v0.1. No pydantic, no SQLAlchemy.
Future versions may evolve these into validated dataclasses, but
the first contract should be readable by humans AND AIs cold.
"""

from dataclasses import dataclass, field
from typing import Optional


@dataclass(frozen=True)
class Opportunity:
    """A deployable capital opportunity (yield strategy, allocation target, etc)."""
    id: str
    name: str
    expected_return: float        # annualized, 0.0–1.0+ (e.g. 0.06 = 6% APY)
    confidence: float             # 0.0–1.0 (how sure are we the return materializes)
    alignment: float              # 0.0–1.0 (how well does this match Sunheart principles)
    liquidity: float              # 0.0–1.0 (1 = instant exit, 0 = locked forever)
    risk: float                   # 0.0–1.0 (higher = more risk)
    complexity: float             # 0.0–1.0 (higher = harder to operate)
    sustainability: float = 1.0   # 0.0–2.0+ (regenerative > 1, extractive < 1)
    coherence_multiplier: float = 1.0  # 0.0–2.0+ (community/externality bonus)


@dataclass(frozen=True)
class Wallet:
    """Treasury state at a point in time."""
    total_usd: float              # everything denominated in USD for v0
    idle_usd: float               # not in any yield position
    productive_usd: float         # currently in yield-bearing positions
    fragmentation_count: int = 1  # number of separate accounts/wallets/chains
    cognitive_load: float = 0.0   # 0.0–1.0 (decision burden on operator)


@dataclass(frozen=True)
class Allocation:
    """A scored allocation recommendation."""
    opportunity: Opportunity
    score: float                  # output of optimal_allocation()
    cay: float                    # output of cay() for this opp
    rationale: str = ""           # human-readable explanation


@dataclass(frozen=True)
class CoherenceScore:
    """Composite score for treasury-state quality."""
    power: float                  # M × V × C
    efficiency: float             # productive_flow / entropy
    velocity_value: float         # flow × density
    composite: float              # weighted blend
    components: dict = field(default_factory=dict)
