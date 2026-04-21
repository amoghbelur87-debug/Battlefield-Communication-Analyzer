def debug_pipeline(signal_data: dict) -> dict:
    """
    Identify missing or broken pipeline steps
    """

    issues = []

    if not signal_data.get("features"):
        issues.append("Feature extraction missing")

    if not signal_data.get("anomaly"):
        issues.append("Anomaly detection missing")

    if not signal_data.get("classification"):
        issues.append("Classification missing")

    if not signal_data.get("decision"):
        issues.append("Decision step missing")

    if not issues:
        return {"status": "OK", "issues": []}

    return {
        "status": "ISSUES_FOUND",
        "issues": issues
    }