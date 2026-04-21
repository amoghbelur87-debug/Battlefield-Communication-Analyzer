def extract_features(processed_signal: dict) -> dict:

    freq = processed_signal.get("frequency", 0)
    amp = processed_signal.get("amplitude_normalized", 0)
    strength = processed_signal.get("signal_strength", -50)
    bandwidth = processed_signal.get("bandwidth", 50000)
    memory = processed_signal.get("memory_usage", 40)
    wifi = processed_signal.get("wifi_strength", -60)

    features = {
        "frequency": freq,
        "amplitude": amp,
        "signal_strength": strength,
        "bandwidth": bandwidth,
        "memory_usage": memory,
        "wifi_strength": wifi
    }

    # -----------------------------
    # ML ENGINEERED FEATURES (subset)
    # -----------------------------

    # Signal quality
    features["signal_quality"] = strength / (bandwidth + 1)

    # Frequency band
    if freq < 1e7:
        features["freq_band"] = 0
    elif freq < 1e8:
        features["freq_band"] = 1
    else:
        features["freq_band"] = 2

    # System load
    features["system_load"] = memory

    # Network strength
    features["network_strength"] = wifi + strength

    # Existing feature (keep)
    features["signal_strength_score"] = freq * amp

    return features