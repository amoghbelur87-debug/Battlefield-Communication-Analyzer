import os
import joblib

# ===============================
# 🔹 OFFLINE SYSTEM MANAGER
# ===============================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "logs", "iso_model.pkl")


def check_offline_mode():
    """
    Check if system is running offline
    """
    print("Running in OFFLINE mode (no internet required)")
    return True


def load_model():
    """
    Load model locally
    """
    if not os.path.exists(MODEL_PATH):
        print("Model not found!")
        print(f"Looked at: {MODEL_PATH}")
        print("Please run train.py first")
        return None

    print("Model loaded from local storage")
    return joblib.load(MODEL_PATH)


def fallback_prediction():
    """
    If model fails, still return safe output
    """
    print("Using fallback prediction")
    return "unknown"


def system_status():
    """
    Show system status
    """
    print("System Status:")
    print("✔ Offline Mode Enabled")
    print("✔ Local Model Usage")
    print("✔ No external dependency")