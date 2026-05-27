"""
Mock adapters.

Same shape as `adapters/` but return synthetic data. Useful for:
- Testing the kernel against realistic opportunity shapes
- Onboarding new adapter writers (copy the mock, swap in chain calls)
- CI runs that must be deterministic and offline

Every real adapter in `adapters/` should have a mirror mock here. The mock
is the contract; the real adapter is the implementation.
"""
