import csv
import os
from datetime import datetime

# ===============================
# 🔹 AUDIT LOGGER SYSTEM
# ===============================

LOG_FILE = "logs/audit_log.csv"


def initialize_logger():
    """
    Create log file if not exists
    """
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, mode="w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                "Timestamp",
                "Frequency",
                "Signal Strength",
                "Bandwidth",
                "Prediction",
                "Threat Level"
            ])

        print("Audit log initialized")


def log_event(signal, prediction):
    """
    Save each signal event or error
    """
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    initialize_logger()

    # Simple threat logic
    if prediction == -1 or signal == "Error":
        threat = "HIGH"
    else:
        threat = "LOW"

    with open(LOG_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)

        if isinstance(signal, dict):
            # Case: signal is a dictionary of features
            writer.writerow([
                datetime.now(),
                signal.get("frequency", "N/A"),
                signal.get("signal_strength", "N/A"),
                signal.get("bandwidth", "N/A"),
                prediction,
                threat
            ])
        else:
            # Case: signal is a category/message (like "Error" or "Prediction")
            writer.writerow([
                datetime.now(),
                signal,
                "N/A",
                "N/A",
                prediction,
                threat
            ])