import math
from app.db.supabase_client import supabase_instance


def calculate_distance(vec1: list, vec2: list) -> float:
    """
    Euclidean distance between two vectors
    """
    if len(vec1) != len(vec2):
        return float("inf")

    return math.sqrt(sum((a - b) ** 2 for a, b in zip(vec1, vec2)))


def get_all_threat_intel():
    response = supabase_instance.table("threat_intelligence").select("*").execute()
    
    if not response or not response.data:
        return []

    return response.data


def match_threat_intelligence(fingerprint: list) -> dict:
    """
    Compare signal fingerprint with stored intelligence
    """

    intel_data = get_all_threat_intel()

    best_match = None
    best_distance = float("inf")

    for item in intel_data:
        stored_fp = item.get("fingerprint", [])

        distance = calculate_distance(fingerprint, stored_fp)

        if distance < best_distance:
            best_distance = distance
            best_match = item

    # Threshold (tune later)
    if best_match and best_distance < 5:
        return {
            "matched": True,
            "category": best_match["category"],
            "name": best_match["name"],
            "distance": round(best_distance, 2)
        }

    return {
        "matched": False,
        "category": "Unknown",
        "name": None,
        "distance": None
    }