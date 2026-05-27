"""Tests for the mock Aave adapter — proves the scaffold shape is honored."""
import unittest

from kernel.types import Opportunity
from mocks.aave import fetch_opportunities


class TestMockAaveAdapter(unittest.TestCase):
    def test_returns_iterable_of_opportunities(self):
        opps = list(fetch_opportunities())
        self.assertGreater(len(opps), 0)
        for opp in opps:
            self.assertIsInstance(opp, Opportunity)

    def test_fields_in_valid_ranges(self):
        for opp in fetch_opportunities():
            self.assertGreaterEqual(opp.confidence, 0.0)
            self.assertLessEqual(opp.confidence, 1.0)
            self.assertGreaterEqual(opp.alignment, 0.0)
            self.assertLessEqual(opp.alignment, 1.0)
            self.assertGreaterEqual(opp.liquidity, 0.0)
            self.assertLessEqual(opp.liquidity, 1.0)
            self.assertGreaterEqual(opp.risk, 0.0)
            self.assertLessEqual(opp.risk, 1.0)
            self.assertGreaterEqual(opp.expected_return, 0.0)

    def test_ids_unique(self):
        opps = list(fetch_opportunities())
        ids = [o.id for o in opps]
        self.assertEqual(len(ids), len(set(ids)))


if __name__ == "__main__":
    unittest.main()
