import pandas as pd
import joblib
import os
import sys

# Import features
from features.signal_intelligence import add_signal_intelligence
from features.offline_mode import load_model, fallback_prediction
from features.audit_logger import log_event


# ===============================
# 🚀 PREDICT FUNCTION
# ===============================
def predict_signal(frequency, signal_strength, bandwidth, modulation_type):

    # Load model
    model = load_model()

    if model is None:
        result = fallback_prediction()
        log_event("Prediction", f"Fallback used -> {result}")
        print(result)
        return

    try:
        # ===============================
        # 🔥 CREATE INPUT DATA (FIXED)
        # ===============================
        data = {
            "frequency": frequency,
            "signal_strength": signal_strength,
            "bandwidth": bandwidth,
            "humidity": 50,
            "wind_speed": 10,
            "precipitation": 5,
            "cpu_usage": 30,
            "memory_usage": 40,
            "wifi_strength": 60,
            "disk_usage": 20
        }

        df = pd.DataFrame([data])

        # ✅ VERY IMPORTANT (fix column mismatch)
        df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

        # ===============================
        # 🔥 ADD INTELLIGENCE FEATURES
        # ===============================
        df = add_signal_intelligence(df) 

        # 🔍 DEBUG PRINT (ADD HERE)
        print("\n Engineered Features:")
        print(df[[
            "signal_quality",
            "freq_band",
            "system_load",
            "env_effect",
            "network_strength"
        ]])

        # ===============================
        # 🔥 SELECT FEATURES (FIXED)
        # ===============================
        features = [
            "frequency",
            "signal_strength",
            "bandwidth",
            "humidity",
            "wind_speed",
            "precipitation",
            "cpu_usage",
            "memory_usage",
            "wifi_strength",
            "disk_usage",
            "signal_quality",
            "freq_band",
            "system_load",
            "env_effect",
            "network_strength"
        ]

        X = df[features]

        # ===============================
        # 🔥 MODEL PREDICTION
        # ===============================
        pred = model.predict(X)[0]

        # ===============================
        # 🧠 INTELLIGENT DECISION
        # ===============================
        result = intelligent_decision(pred, df.iloc[0])

        print(f"Final Decision: {result}")

        # Logging structured data
        log_event(data, result)

    except Exception as e:
        print(f"Error: {e}")
        log_event("Error", str(e))


# ===============================
# 🧠 DECISION LOGIC (FIXED)
# ===============================
def intelligent_decision(pred, data):

    # Rule 1: Strong anomaly
    if pred == -1:
        if data["signal_strength"] < -80:
            return "hostile"

    # Rule 2: Jamming detection
    if data["bandwidth"] > 80000 and data["signal_strength"] < -70:
        return "jamming attack"

    # Rule 3: Environmental interference
    if data["humidity"] > 80 and data["precipitation"] > 40:
        return "environmental interference"

    return "friendly"


# ===============================
# ▶ CLI RUN
# ===============================
if __name__ == "__main__":

    if len(sys.argv) < 5:
        print("Usage: python predict.py <frequency> <signal_strength> <bandwidth> <modulation>")
        print("Example: python predict.py 120000000 -45 50000 QAM")

    else:
        freq = float(sys.argv[1])
        strength = float(sys.argv[2])
        bw = float(sys.argv[3])
        mod = sys.argv[4]

        predict_signal(freq, strength, bw, mod)