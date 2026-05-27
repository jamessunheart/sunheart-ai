"""
Sunheart AI · kernel — the executable thesis.

Eight mathematical layers from MATHEMATICS.md, expressed as pure functions.
Six are implemented here. Two (civilization-scale coordination, flourishing-
efficiency objective) are conceptual layers without single-line equations —
they manifest through the routing and scoring of the other six.

Import surface:
    from kernel import power, cay, treasury_efficiency, optimal_allocation
    from kernel import velocity_value, recursive_intelligence
    from kernel.types import Allocation, Opportunity, Wallet, CoherenceScore
"""

from kernel.equations import (
    power,
    treasury_efficiency,
    cay,
    optimal_allocation,
    velocity_value,
    recursive_intelligence,
)
from kernel.types import (
    Allocation,
    Opportunity,
    Wallet,
    CoherenceScore,
)

__version__ = "0.1.0"

__all__ = [
    "power",
    "treasury_efficiency",
    "cay",
    "optimal_allocation",
    "velocity_value",
    "recursive_intelligence",
    "Allocation",
    "Opportunity",
    "Wallet",
    "CoherenceScore",
]
