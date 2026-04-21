def make_decision(classification: dict, anomaly: dict, threat_intel: dict) -> dict:

    label = classification["label"]
    confidence = classification["confidence"]
    anomaly_score = anomaly["anomaly_score"]

    threat_score = 0

    # Classification contribution
    if label == "Hostile":
        threat_score += 60
    elif label == "Unknown":
        threat_score += 40
    elif label == "Friendly":
        threat_score += 10

    # Anomaly contribution
    threat_score += int(anomaly_score * 40)

    # Threat intelligence override
    if threat_intel["matched"]:
        if threat_intel["category"] == "hostile":
            threat_score += 30
            label = "Hostile"
        elif threat_intel["category"] == "friendly":
            label = "Friendly"

    threat_score = min(threat_score, 100)

    return {
        "final_label": label,
        "threat_score": threat_score,
        "confidence": confidence,
        "reason": f"ML={classification['label']}, Anomaly={anomaly_score}, Intel={threat_intel['category']}"
    }