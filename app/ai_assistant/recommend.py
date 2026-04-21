def recommend_actions(signal_data: dict) -> dict:
    """
    Suggest improvements or actions
    """

    anomaly = signal_data.get("anomaly", {})
    features = signal_data.get("features", {})

    recommendations = []

    # Noise / anomaly suggestions
    if anomaly.get("is_anomaly"):
        recommendations.append(
            "Signal appears anomalous. Consider applying stronger filtering."
        )

    # Weak signal
    if features.get("amplitude", 0) < 0.2:
        recommendations.append(
            "Low amplitude detected. Signal may be weak or degraded."
        )

    # Frequency warning
    if features.get("frequency", 0) > 10:
        recommendations.append(
            "High frequency signal detected. Verify if expected in environment."
        )

    if not recommendations:
        recommendations.append("Signal appears normal. No action required.")

    return {
        "recommendations": recommendations
    }