# This script will generate the ordered choices for the airdrop (randomly pick unused trbls) and the airdrop CSV file.
import json
from data.chainlink_results import all_request_results

data_folder = "data"
output_folder = "output"

total_random_values = 0
for result_batch in all_request_results:
    total_random_values += len(result_batch)

# First batch for 40 wallets sums up to 185 NFTs
assert total_random_values == 185

with open(f"{data_folder}/unused_trbls.json", "r") as f:
    unused_trbls = json.load(f)

# Make sure NFTs are in ascending order
assert sorted(unused_trbls) == unused_trbls

# Make sure there are 1841 NFTs left
assert len(unused_trbls) == 1841

# unwrap the all_request_results in a single list
unwrapped_randomness = [
    item for sublist in all_request_results for item in sublist]

assert len(unwrapped_randomness) == 185

# Now, let's pick 185 NFTs each time popping one from the unused_trbls list
ordered_choices = []
for i, random_value in enumerate(unwrapped_randomness, start=1):
    # Scale the random_value to the range of 0 to len(unused_trbls)
    scaled_random_value = random_value % len(unused_trbls)
    choice = unused_trbls.pop(scaled_random_value)
    # print(f"{i}: Trbl Mkr #{choice}")
    ordered_choices.append(choice)

# Now, let's assign them to the wallets
with open(f"{output_folder}/1_sol_airdrop_amounts_obscured.json", "r") as f:
    sol_airdrop_amounts_obscured = json.load(f)

# Make sure the wallets are in ascending order
assert sorted(
    list(sol_airdrop_amounts_obscured.keys())) == list(sol_airdrop_amounts_obscured.keys())

n = 0
csv_output = ""
for sol_wallet, airdrop_size in sol_airdrop_amounts_obscured.items():
    for i in range(airdrop_size):
        csv_output += f"Trbl Mkr #{ordered_choices[n]}, {sol_wallet}\n"
        n += 1
assert n == 185

with open(f"{output_folder}/2_ordered_choices.json", "w") as f:
    f.write(json.dumps(ordered_choices))

with open(f"{output_folder}/2_airdrop.csv", "w") as f:
    f.write(csv_output)