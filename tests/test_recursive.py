"""
xfail tests for recursive_intelligence — invitations for builders to refine.

These tests SHOULD pass eventually. They currently fail because the v0.1
implementation of recursive_intelligence() uses a naive constant learning_rate
without adaptive behavior. The math layer ⑥ in MATHEMATICS.md is intentionally
underspecified.

Open issues mapped to these xfails:
- [good-first-issue] Implement adaptive learning_rate that increases on surprise
- [good-first-issue] Add decay so old learning fades naturally
- [good-first-issue] Distinguish verified-positive vs verified-negative outcomes

If you fix any of these, remove the corresponding xfail decorator and submit a PR.
"""

import unittest

from kernel import recursive_intelligence


class TestRecursiveIntelligenceAspirational(unittest.TestCase):
    """These should pass once equation ⑥ is properly specified."""

    @unittest.expectedFailure
    def test_surprise_amplifies_learning(self):
        """
        When verified outcome is unexpected (surprise > 0), the learning
        impact should be amplified. A naive identity-based recursive_intelligence
        doesn't know what 'surprise' means — that's the gap to fill.

        Builders: extend the function signature to accept `expected_outcome` and
        compute surprise = |actual - expected|, then scale learning by surprise.
        """
        # Hypothetical API: surprise should boost learning over baseline
        # For now this xfails because the surprise-aware variant doesn't exist
        baseline = recursive_intelligence(10.0, 5.0)
        # surprising = recursive_intelligence(10.0, 5.0, expected_outcome=0.0)
        # self.assertGreater(surprising, baseline)
        self.fail("Surprise-aware recursive_intelligence not yet implemented")

    @unittest.expectedFailure
    def test_old_learning_decays(self):
        """
        Treasury intelligence should weight recent verified outcomes more than
        ancient ones. Without decay, the system carries dead weight from
        outcomes that no longer reflect current conditions.

        Builders: add a `decay_rate` parameter or accept a list of timestamped
        outcomes and weight by recency.
        """
        # Hypothetical API: same total learning, but spread over time, should
        # produce lower current intelligence than a single recent learning event
        self.fail("Time-decay variant of recursive_intelligence not yet implemented")

    @unittest.expectedFailure
    def test_negative_outcomes_reduce_intelligence(self):
        """
        Verified-negative outcomes (an allocation that lost money, a rule that
        broke) should REDUCE the intelligence score, not just add as positive
        learning. The v0.1 function treats all learning as additive.

        Builders: split verified_learning into verified_positive and
        verified_negative, and let negative outcomes drive learning differently
        (e.g., higher magnitude, different decay curve).
        """
        self.fail(
            "Negative-outcome handling in recursive_intelligence not yet implemented"
        )


if __name__ == "__main__":
    unittest.main()
