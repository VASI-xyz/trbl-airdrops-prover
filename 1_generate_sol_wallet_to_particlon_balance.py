# This script generates a JSON file that maps Solana wallet addresses to the number of Particlons they will receive in the airdrop.
import os
import json

data_folder = "data"
output_folder = "output"

with open(f"{data_folder}/particlon_snapshot_obscured.json", "r") as f:
    snapshot = json.load(f)

snapshot_values = list(snapshot.values())

with open(f"{data_folder}/wallets_obscured.json", "r") as f:
    wallets = json.loads(f.read())

sol_airdrop_promises = {}
for eth_wallet, sol_wallet in wallets.items():
    particlon_balance = snapshot_values.count(eth_wallet)
    sol_airdrop_promises[sol_wallet] = particlon_balance

# Now, sort the airdrop amounts by sol address in ascending order
sol_airdrop_promises = dict(
    sorted(sol_airdrop_promises.items(), key=lambda item: item[0]))

# And save it to a file
if output_folder not in os.listdir():
    os.mkdir(output_folder)

with open(f"{output_folder}/1_sol_airdrop_amounts_obscured.json", "w") as f:
    json.dump(sol_airdrop_promises, f, indent=4)
