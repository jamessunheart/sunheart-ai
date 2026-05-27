# Adapters

Where chain integration lands. The kernel stays pure; adapters do the dirty work of talking to RPC nodes, subgraphs, REST APIs, indexers.

## Wanted (good adapter PRs)

| Protocol | Shape | Mock exists | Real adapter |
|---|---|---|---|
| Aave V3 | supply markets | [mocks/aave/](../mocks/aave/) | (open) |
| Pendle  | PT/YT positions | (open) | (open) |
| Morpho  | vaults | (open) | (open) |
| Gauntlet curated | curated vault feeds | (open) | (open) |
| Compound V3 | supply markets | (open) | (open) |

## Contract

Every adapter exposes `fetch_opportunities() -> Iterable[Opportunity]`.

That's it. The kernel's allocation math is responsible for ranking. Adapters are responsible for honest data.

## Copy-from scaffold

Start by copying [`mocks/aave/`](../mocks/aave/). Swap the synthetic data for real calls. Add a one-line note in your PR body justifying any new dependency.
