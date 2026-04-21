import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib
import os

print("🚀 Training Model with Real Dataset...")

# Load dataset - use absolute path
script_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_dir, "..", "..", "data", "signals.csv")
print(f"Looking for data at: {data_path}")

df = pd.read_csv(data_path)

# 🔥 Clean column names (VERY IMPORTANT)
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Remove bad data
df = df.drop_duplicates()
df = df.fillna(df.mean(numeric_only=True))



# ==============================
# 🔥 FEATURE ENGINEERING
# ==============================

# Signal quality
df["signal_quality"] = df["signal_strength"] / (df["bandwidth"] + 1)

# Frequency band grouping
df["freq_band"] = pd.cut(
    df["frequency"],
    bins=[0, 1e7, 1e8, 1e9],
    labels=[0, 1, 2]
).fillna(0).astype(int)

# System stress
df["system_load"] = df["cpu_usage"] + df["memory_usage"]

# Environment effect
df["env_effect"] = df["humidity"] + df["precipitation"]

# Network strength
df["network_strength"] = df["wifi_strength"] + df["signal_strength"]

# ==============================
# 🔥 SELECT FEATURES
# ==============================

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

df = df[features]

# ==============================
# 🔥 TRAIN MODEL
# ==============================

model = IsolationForest(
    n_estimators=100,
    contamination=0.1,
    random_state=42
)

model.fit(df)

# Save model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_MODEL_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(LOG_MODEL_DIR, exist_ok=True)
joblib.dump(model, os.path.join(LOG_MODEL_DIR, "iso_model.pkl"))

print("✅ Model trained successfully!")