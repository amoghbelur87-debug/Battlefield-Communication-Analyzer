def detect_anomaly(feature_vector: dict) -> dict:
    """
    Simple rule-based anomaly detection (baseline)
    """

    score = 0

    freq = feature_vector.get("frequency", 0)
    amp = feature_vector.get("amplitude", 0)
    strength = feature_vector.get("signal_strength", 0)

    # Basic rules (you can tune later)
    if freq > 10:
        score += 0.4

    if amp > 1 or amp < 0:
        score += 0.3

    if strength > 15:
        score += 0.3

    is_anomaly = score > 0.5

    return {
        "anomaly_score": round(score, 2),
        "is_anomaly": is_anomaly
    }