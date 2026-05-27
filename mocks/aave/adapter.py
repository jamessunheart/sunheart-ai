"""
Mock Aave V3 adapter.

Returns synthetic `Opportunity` objects shaped like real Aave supply positions.
The shape is the contract — a real adapter in `adapters/aave/` would replace
the synthetic data with calls to an Aave subgraph or RPC node, keeping the
same return signature.

This file exists so that AI builders writing the real adapter have a copy-able
scaffold. The math layer (`kernel/`) should not know whether the data came
from a mock or a chain.
"""
from __future__ import annotations

from typing import Iterable

from kernel.types import Opportunity


# Synthetic snapshot — roughly representative of Aave V3 ETH mainnet, May 2026.
_MOCK_SUPPLY_MARKETS: list[dict] = [
    {
        "id": "aave-v3-eth-usdc",
        "name": "Aave V3 USDC (ETH mainnet)",
        "expected_return": 0.045,
        "confidence": 0.95,
        "alignment": 0.55,
        "liquidity": 0.99,
        "risk": 0.10,
        "complexity": 0.20,
        "sustainability": 1.0,
        "coherence_multiplier": 1.0,
    },
    {
        "id": "aave-v3-eth-usdt",
        "name": "Aave V3 USDT (ETH mainnet)",
        "expected_return": 0.048,
        "confidence": 0.92,
        "alignment": 0.40,
        "liquidity": 0.99,
        "risk": 0.15,
        "complexity": 0.20,
        "sustainability": 1.0,
        "coherence_multiplier": 1.0,
    },
    {
        "id": "aave-v3-base-usdc",
        "name": "Aave V3 USDC (Base)",
        "expected_return": 0.052,
        "confidence": 0.90,
        "alignment": 0.65,
        "liquidity": 0.97,
        "risk": 0.12,
        "complexity": 0.25,
        "sustainability": 1.0,
        "coherence_multiplier": 1.05,
    },
]


def fetch_opportunities() -> Iterable[Opportunity]:
    """Return synthetic Aave supply opportunities as kernel `Opportunity` objects.

    A real `adapters/aave/` implementation would replace this with subgraph
    or RPC calls but MUST keep the same return type.
    """
    return [Opportunity(**row) for row in _MOCK_SUPPLY_MARKETS]


if __name__ == "__main__":
    for opp in fetch_opportunities():
        print(opp)
