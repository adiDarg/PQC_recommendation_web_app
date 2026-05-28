import json
import os

EXPLANATIONS_FILE = os.path.join("dataset", "algorithm_data.json")

with open(EXPLANATIONS_FILE, "r") as f:
    ALGO_DATA = json.load(f)


# 2. Extraction function
def get_algorithm_explanation(variant_name: str) -> dict:
    """
    Matches a specific variant name (e.g., 'ML-KEM-512' or 'Classic-McEliece-460896(f)')
    to its base algorithm family and returns the explanation dictionary.
    """
    # Iterate through the base keys in the JSON (e.g., "ML-KEM", "Classic-McEliece")
    for base_family in ALGO_DATA.keys():
        if variant_name.startswith(base_family):
            return ALGO_DATA[base_family]

    # Fallback if no match is found
    return {
        "name": variant_name,
        "category": "Unknown",
        "description": "No explanation available for this algorithm variant."
    }