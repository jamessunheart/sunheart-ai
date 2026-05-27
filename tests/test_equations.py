"""
Property + example tests for kernel.equations.

Run: `python -m pytest tests/` (requires pytest)
    or: `python -m unittest tests/test_equations.py`
"""

import math
import unittest

from kernel import (
    power,
    treasury_efficiency,
    cay,
    optimal_allocation,
    velocity_value,
    recursive_intelligence,
)
from kernel.types import Opportunity


class TestPowerEquation(unittest.TestCase):
    """① Power = Money × Velocity × Coherence."""

    def test_idle_capital_has_zero_power(self):
        self.assertEqual(power(1_000_000, 0, 1.0), 0.0)
        self.assertEqual(power(100, 0, 2.0), 0.0)

    def test_baseline_circulation(self):
        self.assertEqual(power(100, 1, 1.0), 100.0)

    def test_velocity_compounds(self):
        # doubling velocity doubles power
        baseline = power(100, 1, 1.0)
        doubled = power(100, 2, 1.0)
        self.assertEqual(doubled, 2 * baseline)

    def test_coherence_compounds(self):
        # 1.5x coherence = 1.5x power
        baseline = power(100, 1, 1.0)
        higher = power(100, 1, 1.5)
        self.assertAlmostEqual(higher, 1.5 * baseline)

    def test_one_dollar_intelligent_beats_ten_dollar_idle(self):
        # Core claim from MATHEMATICS.md: $1 moving > $10 idle
        intelligent = power(1, 1, 1.0)
        idle = power(10, 0, 1.0)
        self.assertGreater(intelligent, idle)


class TestCAY(unittest.TestCase):
    """③ CAY = Yield × Coherence × Sustainability."""

    def test_regenerative_beats_extractive_long_arc(self):
        regenerative = cay(0.05, 1.0, 1.5)
        extractive = cay(0.15, 1.0, 0.3)
        self.assertGreater(regenerative, extractive)

    def test_neutral_sustainability_passes_yield_through(self):
        self.assertAlmostEqual(cay(0.10, 1.0, 1.0), 0.10)

    def test_zero_coherence_zeros_yield(self):
        self.assertEqual(cay(0.20, 0.0, 1.0), 0.0)


class TestTreasuryEfficiency(unittest.TestCase):
    """② Efficiency = Productive Flow ÷ Entropy."""

    def test_high_flow_low_entropy_high_efficiency(self):
        self.assertEqual(treasury_efficiency(100, 10), 10.0)

    def test_zero_entropy_infinite_efficiency(self):
        self.assertTrue(math.isinf(treasury_efficiency(100, 0)))

    def test_more_entropy_lower_efficiency(self):
        low_entropy = treasury_efficiency(100, 5)
        high_entropy = treasury_efficiency(100, 50)
        self.assertGreater(low_entropy, high_entropy)


class TestOptimalAllocation(unittest.TestCase):
    """④ Optimal Allocation = (R × C × A × L) ÷ (Risk × Complexity)."""

    def _opp(self, **overrides):
        defaults = dict(
            id="test",
            name="Test Opp",
            expected_return=0.10,
            confidence=0.8,
            alignment=0.9,
            liquidity=1.0,
            risk=0.5,
            complexity=0.5,
        )
        defaults.update(overrides)
        return Opportunity(**defaults)

    def test_high_return_high_alignment_scores_high(self):
        good = self._opp(expected_return=0.20, alignment=1.0)
        bad = self._opp(expected_return=0.05, alignment=0.2)
        self.assertGreater(optimal_allocation(good), optimal_allocation(bad))

    def test_high_risk_demotes_score(self):
        safe = self._opp(risk=0.1)
        risky = self._opp(risk=0.9)
        self.assertGreater(optimal_allocation(safe), optimal_allocation(risky))

    def test_locked_capital_demotes_score(self):
        liquid = self._opp(liquidity=1.0)
        locked = self._opp(liquidity=0.1)
        self.assertGreater(optimal_allocation(liquid), optimal_allocation(locked))


class TestVelocityValue(unittest.TestCase):
    """⑤ Velocity Value = Economic Flow × Coherence Density."""

    def test_zero_flow_zero_value(self):
        self.assertEqual(velocity_value(0, 1.0), 0.0)

    def test_zero_coherence_density_zero_value(self):
        # high circulation in a misaligned system yields nothing
        self.assertEqual(velocity_value(1000, 0.0), 0.0)


class TestRecursiveIntelligenceBaseline(unittest.TestCase):
    """⑥ Intelligence(t+1) = Intelligence(t) + Verified Learning."""

    def test_identity_with_zero_learning(self):
        self.assertEqual(recursive_intelligence(10.0, 0.0), 10.0)

    def test_learning_accumulates(self):
        self.assertEqual(recursive_intelligence(10.0, 5.0), 15.0)

    def test_learning_rate_scales(self):
        self.assertEqual(recursive_intelligence(10.0, 5.0, learning_rate=0.5), 12.5)


if __name__ == "__main__":
    unittest.main()
