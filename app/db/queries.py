from app.db.supabase_client import supabase_instance
from datetime import datetime


# -------------------------------
# Insert Signal
# -------------------------------
def insert_signal(signal_data: dict):
    try:
        response = supabase_instance.table("signals").insert({
            "raw_signal": signal_data,
            "source": signal_data.get("source", "unknown"),
            "status": "received"
        }).execute()

        print("Insert signal response:", response)

        if not response or not response.data:
            raise Exception("Supabase returned empty response while inserting signal")

        return response.data[0]

    except Exception as e:
        print("[DB ERROR - insert_signal]:", e)
        raise Exception(f"Signal insert failed: {str(e)}")


# -------------------------------
# Insert Audit Log
# -------------------------------
def insert_audit_log(signal_id: str, step: str, data: dict):
    try:
        response = supabase_instance.table("audit_logs").insert({
            "signal_id": signal_id,
            "step": step,
            "data": data,
            "created_at": datetime.utcnow().isoformat()
        }).execute()

        if not response or response.data is None:
            print("[WARNING] Audit log insert returned empty")

    except Exception as e:
        print("[DB ERROR - insert_audit_log]:", e)


# -------------------------------
# Insert Features
# -------------------------------
def insert_features(signal_id: str, feature_vector: dict):
    try:
        response = supabase_instance.table("features").insert({
            "signal_id": signal_id,
            "feature_vector": feature_vector
        }).execute()

        print("Insert features response:", response)

        if not response or not response.data:
            raise Exception("Supabase returned empty response while inserting features")

        return response.data[0]

    except Exception as e:
        print("[DB ERROR - insert_features]:", e)
        raise Exception(f"Feature insert failed: {str(e)}")
    

def insert_anomaly(signal_id: str, anomaly_data: dict):
    response = supabase_instance.table("anomalies").insert({
        "signal_id": signal_id,
        "anomaly_score": anomaly_data["anomaly_score"],
        "is_anomaly": anomaly_data["is_anomaly"]
    }).execute()

    if not response or not response.data:
        raise Exception("Failed to insert anomaly data")

    return response.data[0]

def insert_classification(signal_id: str, classification: dict):
    response = supabase_instance.table("classifications").insert({
        "signal_id": signal_id,
        "label": classification["label"],
        "confidence": classification["confidence"],
        "model_version": "v1_rule_based"
    }).execute()

    if not response or not response.data:
        raise Exception("Failed to insert classification")

    return response.data[0]

def insert_decision(signal_id: str, decision: dict):
    response = supabase_instance.table("decisions").insert({
        "signal_id": signal_id,
        "final_label": decision["final_label"],
        "threat_score": decision["threat_score"],
        "confidence": decision["confidence"],
        "reason": decision["reason"]
    }).execute()

    if not response or not response.data:
        raise Exception("Failed to insert decision")

    return response.data[0]

def insert_fingerprint(signal_id: str, fingerprint: list):
    response = supabase_instance.table("fingerprints").insert({
        "signal_id": signal_id,
        "fingerprint_vector": fingerprint
    }).execute()

    if not response or not response.data:
        raise Exception("Failed to insert fingerprint")

    return response.data[0]