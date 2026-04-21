def classify_signal(feature_vector: dict, anomaly_result: dict) -> dict:
    """
    Placeholder classification logic (will be replaced by ML model later)
    """

    # If anomaly is high → unknown
    if anomaly_result["is_anomaly"]:
        return {
            "label": "Unknown",
            "confidence": 0.4
        }

    freq = feature_vector.get("frequency", 0)
    strength = feature_vector.get("signal_strength", 0)

    # Simple rules (temporary)
    if freq < 3 and strength < 5:
        return {
            "label": "Friendly",
            "confidence": 0.8
        }

    elif strength > 5:
        return {
            "label": "Hostile",
            "confidence": 0.7
        }

    else:
        return {
            "label": "Unknown",
            "confidence": 0.5
        }