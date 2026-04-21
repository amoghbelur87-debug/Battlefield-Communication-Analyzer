def preprocess_signal(signal: dict) -> dict:
    processed = signal.copy()

    # Normalize amplitude
    amp = processed.get("amplitude", 0)
    processed["amplitude_normalized"] = min(max(amp, 0), 1)

    # Fill missing ML fields with defaults
    processed["signal_strength"] = processed.get("signal_strength", -50)
    processed["bandwidth"] = processed.get("bandwidth", 50000)
    processed["memory_usage"] = processed.get("memory_usage", 40)
    processed["wifi_strength"] = processed.get("wifi_strength", -60)

    processed["noise_reduced"] = True

    return processed