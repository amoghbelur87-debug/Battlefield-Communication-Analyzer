def generate_fingerprint(feature_vector: dict) -> list:
    return [
        feature_vector.get("frequency", 0),
        feature_vector.get("signal_strength", 0),
        feature_vector.get("bandwidth", 0),
        feature_vector.get("signal_quality", 0),
        feature_vector.get("network_strength", 0)
    ]