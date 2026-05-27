"""
The mathematical layers from MATHEMATICS.md, expressed as pure functions.

Every equation here MUST:
1. Be a pure function (no side effects, no I/O)
2. Be documented with its formal expression (matches MATHEMATICS.md exactly)
3. Have a property-based or example-based test in tests/
4. Be referenced by a line in MATHEMATICS.md

When adding a new equation:
- Append the equation to MATHEMATICS.md FIRST (the math is the contract)
- Add the function here second
- Write the test third
- Open a PR referencing the equation ID (① through ⑧)
"""

from typing import Optional
from kernel.types import Opportunity, Wallet


def power(money: float, velocity: float, coherence: float) -> float:
    """
    ① The Core Equation.

        Power = Money × Velocity × Coherence

    $1 moving intelligently outperforms $10 sitting idle.
    Velocity: turnovers per unit time (annualized).
    Coherence: 0.0 (chaotic/extractive) – 2.0+ (aligned/regenerative).

    >>> power(100, 0, 1.0)     # idle capital → zero power
    0.0
    >>> power(100, 1, 1.0)     # baseline circulation
    100.0
    >>> power(50, 4, 1.5)      # less capital, higher velocity + alignment
    300.0
    """
    return money * velocity * coherence


def treasury_efficiency(
    productive_flow: float,
    entropy: float,
) -> float:
    """
    ② Treasury Entropy Mathematics.

        Treasury Efficiency = Productive Flow ÷ Entropy

    Productive Flow = yield + build_capacity + opportunity_generation + resilience
    Entropy = fragmentation + idle_capital + cognitive_load + coordination_drag

    Both sides denominated consistently (USD-equivalent or normalized 0–1).
    Returns infinity if entropy approaches zero (perfect treasury — unreachable).
    """
    if entropy <= 0:
        return float("inf")
    return productive_flow / entropy


def cay(
    financial_yield: float,
    coherence_multiplier: float,
    sustainability_factor: float,
) -> float:
    """
    ③ Coherence-Adjusted Yield.

        CAY = Financial Yield × Coherence Multiplier × Sustainability Factor

    A 5% regenerative yield (sustainability=1.5) can beat a 15% extractive
    yield (sustainability=0.3) on a long-arc CAY basis.

    >>> cay(0.05, 1.0, 1.5)   # regenerative 5%
    0.075
    >>> cay(0.15, 1.0, 0.3)   # extractive 15%
    0.045
    """
    return financial_yield * coherence_multiplier * sustainability_factor


def optimal_allocation(opp: Opportunity) -> float:
    """
    ④ Intelligence Routing Mathematics (Bayesian treasury allocation).

        Optimal Allocation = (Expected Return × Confidence × Alignment × Liquidity)
                             ÷ (Risk × Complexity)

    Higher score → more capital should flow here.
    Score is unitless; rank opportunities by relative score.
    """
    numerator = (
        opp.expected_return
        * opp.confidence
        * opp.alignment
        * opp.liquidity
    )
    denominator = opp.risk * opp.complexity
    if denominator <= 0:
        # zero-risk + zero-complexity is theoretically infinite leverage;
        # we cap by adding a tiny epsilon so the routing stays comparable
        denominator = 1e-9
    return numerator / denominator


def velocity_value(
    economic_flow: float,
    coherence_density: float,
) -> float:
    """
    ⑤ Velocity Mathematics.

        Velocity Value = Economic Flow × Coherence Density

    High-frequency aligned circulation compounds exponentially.
    Coherence density: how well the circulating capital is aligned per unit moved.
    """
    return economic_flow * coherence_density


def recursive_intelligence(
    current_intelligence: float,
    verified_learning: float,
    learning_rate: float = 1.0,
) -> float:
    """
    ⑥ Recursive Intelligence Mathematics.

        Treasury Intelligence(t+1) = Treasury Intelligence(t) + Verified Outcome Learning

    The treasury becomes smarter through verified outcomes (allocations that paid off,
    rules that survived, principles that held under stress).

    Learning rate gates how aggressively new evidence updates the score.
    A naive identity learning_rate=1.0 is the simplest case. Builders are encouraged
    to propose adaptive learning rates (see tests/test_recursive.py xfail tests).

    NOTE: This is intentionally underspecified at v0.1. The exact functional form of
    'verified_learning' (how do we measure it, what's the decay, how do we weight
    surprise vs. expected outcomes) is an OPEN PROBLEM that builders are invited to
    refine. See [good-first-issue] tagged in ISSUES.md.
    """
    return current_intelligence + (learning_rate * verified_learning)
