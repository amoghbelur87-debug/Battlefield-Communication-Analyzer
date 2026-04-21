import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "logs", "iso_model.pkl")


def load_ml_model():
    try:
        print("[DEBUG] Looking for model at:", MODEL_PATH)

        if not os.path.exists(MODEL_PATH):
            print("[ERROR] Model file NOT FOUND")
            return None

        model = joblib.load(MODEL_PATH)
        print("[INFO] ML Model loaded successfully")
        return model

    except Exception as e:
        print("[ERROR] Model loading failed:", str(e))
        return None
    
# 🔥 THIS LINE IS CRITICAL
model_instance = load_ml_model()