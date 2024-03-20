# This script generates the cache.json file for the sugar tool
import json
COLLECTION_MINT = "4ehoUfmayqVNapjYQGsLhijudSk7zQq8p6eLyAwJW9YN"

output_folder = "output"

with open(f"{output_folder}/2_ordered_choices.json", "r") as f:
    ordered_choices = json.load(f)

assert len(ordered_choices) == 185


cache_dict = {
    "program": {
        "candyMachine": "",
        "candyGuard": "",
        "candyMachineCreator": "",
        "collectionMint": COLLECTION_MINT
    },
    "items": {
        "-1": {
            "name": "Trbl Mkrs",
            "image_hash": "",
            "image_link": "https://nftstorage.link/ipfs/bafkreiehkcovygmcjbvej3tkjp4cmh43pnwye6noubk4skubkxi6lz2fgq",
            "metadata_hash": "",
            "metadata_link": "https://nftstorage.link/ipfs/bafkreiefta4xi4spspzg4zvc5f62utdizi7t5jsr5jt3faqv5bf6dtqpty",
            "onChain": True
        },
    }
}

for i in range(185):
    trbl_id = ordered_choices[i]
    cache_dict["items"][str(i)] = {
        "name": f"Trbl Mkr #{trbl_id}",
        "image_hash": "",
        "image_link": f"https://www.arweave.net/T8i2jKBhvHzfNImuykk6GbLDDzue221xPqNPHee1gEI/TrblMkr_{trbl_id}.jpg?ext=jpeg",
        "metadata_hash": "",
        "metadata_link": f"https://bafybeibuqdmzwwvp2edrddybzmkyxjikkoced635wcnkdudy4w2p7oug2u.ipfs.nftstorage.link/{trbl_id}.json",
        "onChain": False
    }

# For actual usage with the sugar tool, remove the 3_ prefix
with open(f"{output_folder}/3_cache.json", "w") as f:
    json.dump(cache_dict, f, indent=4)
