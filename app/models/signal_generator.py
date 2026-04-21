import random
import time
import pandas as pd

# 🔥 Import features
from features.signal_intelligence import add_signal_intelligence
from features.offline_mode import load_model, fallback_prediction
from features.audit_logger import log_event


# ==============================
# 🔥 GENERATE RAW SIGNAL
# ==============================
def generate_signal():
    return {
        "Frequency": random.uniform(1e7, 1e9),
        "Signal_Strength": random.uniform(-100, -20),
        "Bandwidth": random.randint(1000, 100000),
        "Humidity": random.randint(20, 90),
        "Wind_Speed": random.randint(0, 20),
        "Precipitation": random.randint(0, 50),
        "CPU_Usage": random.randint(0, 100),
        "Memory_Usage": random.randint(0, 100),
        "WiFi_Strength": random.uniform(-90, -30),
        "Disk_Usage": random.randint(0, 100)
    }


# ==============================
# 🧠 DECISION ENGINE
# ==============================
def intelligent_decision(pred, data):

    if pred == -1 and data["Signal_Strength"] < -80:
        return "hostile 🚨"

    if data["Bandwidth"] > 80000 and data["Signal_Strength"] < -70:
        return "jamming attack ⚠"

    if data["Humidity"] > 80 and data["Precipitation"] > 40:
        return "environmental interference 🌧"

    return "friendly ✅"


# ==============================
# 🚀 CONTINUOUS SCANNING SYSTEM
# ==============================
def run_scanner():

    print("📡 RF Scanner Started...\n")

    model = load_model()

    while True:

        # 🔹 Generate signal
        signal = generate_signal()
        df = pd.DataFrame([signal])

        try:
            # 🔥 Add intelligence features
            df = add_signal_intelligence(df)

            # 🔥 Select features
            features = [
                "Frequency",
                "Signal_Strength",
                "Bandwidth",
                "signal_quality",
                "noise_ratio",
                "freq_band",
                "instability",
                "strength_level",
                "bandwidth_efficiency",
                "interference_score"
            ]

            X = df[features]

            # 🔥 Predict
            if model is not None:
                pred = model.predict(X)[0]
                decision = intelligent_decision(pred, df.iloc[0])
            else:
                decision = fallback_prediction()

            # 🔥 Output
            print("📡 Signal:", signal)
            print("🧠 Decision:", decision)
            print("-" * 50)

            # 🔥 Logging
            log_event("Scan", f"{signal} -> {decision}")

        except Exception as e:
            print("❌ Error:", e)
            log_event("Error", str(e))

        time.sleep(2)


# ==============================
# ▶ RUN
# ==============================
if __name__ == "__main__":
    run_scanner()