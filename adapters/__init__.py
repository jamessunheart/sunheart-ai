"""
Chain integration adapters.

Adapters translate between on-chain reality (positions, yields, gas, slippage)
and the kernel's pure `Opportunity` / `Wallet` types. They are the boundary
where math meets execution.

House rules
-----------
- Adapters MAY import from `kernel.types` (they consume `Opportunity`/`Wallet`).
- Adapters MUST NOT modify `kernel/` itself.
- Adapters MAY have external dependencies (`web3`, `httpx`, etc) — declared in
  `requirements-adapters.txt` when it exists.
- Each adapter is one file or one subpackage. No god-objects.

See `mocks/aave/` for a reference scaffold that returns synthetic data so the
shape of the interface lands before the chain integration does.
"""
