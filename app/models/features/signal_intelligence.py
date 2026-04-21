import pandas as pd
import numpy as np

def add_signal_intelligence(df):

    # ✅ Clean column names (VERY IMPORTANT)
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # 🔹 Signal Quality
    df["signal_quality"] = df["signal_strength"] / (df["bandwidth"] + 1)

    # 🔹 Noise Ratio
    df["noise_ratio"] = abs(df["signal_strength"]) / (df["bandwidth"] + 1)

    # 🔹 Frequency Band
    df["freq_band"] = pd.cut(
        df["frequency"],
        bins=[0, 1e7, 1e8, 1e9],
        labels=[0, 1, 2]
    ).astype(int)

    # 🔹 System Load
    df["system_load"] = df["cpu_usage"] + df["memory_usage"]

    # 🔹 Environmental Effect
    df["env_effect"] = df["humidity"] + df["precipitation"]

    # 🔹 Network Strength
    df["network_strength"] = df["wifi_strength"] + df["signal_strength"]

    return df