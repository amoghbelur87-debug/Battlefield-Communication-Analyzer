import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

try:
    from ..models.model_loader import model_instance
except Exception as e:
    print("[IMPORT ERROR]:", e)
    model_instance = None
    
def ml_detect_anomaly(features: dict) -> dict:
    try:
        if model_instance is None:
            return {
                "anomaly_score": 0.0,
                "is_anomaly": False,
                "source": "fallback"
            }

        # SAFE feature construction
        input_data = {
            "frequency": features.get("frequency", 0),
            "signal_strength": features.get("signal_strength", -50),
            "bandwidth": features.get("bandwidth", 50000),

            "humidity": 50,
            "wind_speed": 10,
            "precipitation": 5,

            "cpu_usage": 30,
            "memory_usage": features.get("memory_usage", 40),
            "wifi_strength": features.get("wifi_strength", -60),
            "disk_usage": 20,

            "signal_quality": features.get("signal_quality", 0),
            "freq_band": features.get("freq_band", 0),
            "system_load": features.get("system_load", 40),

            # 🔥 IMPORTANT FIX
            "env_effect": 55,

            "network_strength": features.get("network_strength", -100)
        }

        import pandas as pd
        df = pd.DataFrame([input_data])

        pred = model_instance.predict(df)[0]

        is_anomaly = True if pred == -1 else False

        return {
            "anomaly_score": 1.0 if is_anomaly else 0.0,
            "is_anomaly": is_anomaly,
            "source": "ml"
        }

    except Exception as e:
        print("[ML ERROR]:", e)

        return {
            "anomaly_score": 0.0,
            "is_anomaly": False,
            "source": "error"
        }