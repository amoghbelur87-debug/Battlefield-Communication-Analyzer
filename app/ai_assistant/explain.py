def explain_decision(signal_data: dict) -> dict:
    """
    Generate explanation based on pipeline outputs
    """

    classification = signal_data.get("classification", {})
    anomaly = signal_data.get("anomaly", {})
    decision = signal_data.get("decision", {})
    threat_intel = signal_data.get("threat_intelligence", {})

    explanation = []

    # Classification explanation
    explanation.append(
        f"Signal classified as {classification.get('label')} "
        f"with confidence {classification.get('confidence')}"
    )

    # Anomaly explanation
    if anomaly.get("is_anomaly"):
        explanation.append(
            f"High anomaly score detected ({anomaly.get('anomaly_score')})"
        )

    # Threat intelligence
    if threat_intel.get("matched"):
        explanation.append(
            f"Matched known {threat_intel.get('category')} signal ({threat_intel.get('name')})"
        )

    # Final decision
    explanation.append(
        f"Final decision: {decision.get('final_label')} "
        f"(Threat Score: {decision.get('threat_score')})"
    )

    return {
        "explanation": explanation
    }