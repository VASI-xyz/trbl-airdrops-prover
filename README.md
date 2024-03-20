# trbl-airdrops-prover
Chainlink VRF code for TRBLTWN

## How it works
Make sure you have the latest Python 3.xx installed and `python3` available in your console.

Run the scripts (in this order):
- `python3 1_generate_sol_wallet_to_particlon_balance.py`

- `python3 2_generate_ordered_choices_airdrop.py`

Optional
- `python3 3_generate_cm_cache.py`

Based on the randomness given in `data/chainlink_results.py`, this will randomly pick unused Trblmkrs and assign them to the sol wallets, which are ordered alphabetically in ascending order.

The random results can be verified on-chain: https://polygonscan.com/address/0x01E035926A4E5aE088DBb764a1F607510798cEA8.