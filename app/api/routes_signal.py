from fastapi import APIRouter, HTTPException
from app.schemas.signal_schema import SignalInput
from app.schemas.response_schema import APIResponse
from app.db.queries import insert_signal
from app.utils.logger import log_event
from app.core.preprocessing import preprocess_signal
from app.core.feature_extraction import extract_features
from app.db.queries import insert_features
from app.core.ml_anomaly import ml_detect_anomaly
from app.db.queries import insert_anomaly
from app.core.classification import classify_signal
from app.db.queries import insert_classification
from app.core.decision_engine import make_decision
from app.db.queries import insert_decision
from app.intelligence.fingerprinting import generate_fingerprint
from app.intelligence.threat_engine import match_threat_intelligence
from app.db.queries import insert_fingerprint


router = APIRouter()


@router.post("/analyze", response_model=APIResponse)
def analyze_signal(signal: SignalInput):
    try:
        # Step 1: Convert input to dict
        signal_dict = signal.dict()

        # Step 2: Store signal in DB
        stored_signal = insert_signal(signal_dict)
        signal_id = stored_signal["id"]

        # Step 3: Preprocess
        processed_signal = preprocess_signal(signal_dict)
        log_event(signal_id, "PREPROCESSING", processed_signal)

        # Step 4: Feature Extraction
        features = extract_features(processed_signal)
        log_event(signal_id, "FEATURE_EXTRACTION", features)

        # Step 5: Store features
        insert_features(signal_id, features)

        # Step 6: Fingerprint Generation
        fingerprint = generate_fingerprint(features)

        log_event(signal_id, "FINGERPRINT_GENERATION", {"fingerprint": fingerprint})

        # Step 7: Store fingerprint
        insert_fingerprint(signal_id, fingerprint)

        # Step 6: Anomaly Detection
        anomaly_result = ml_detect_anomaly(features)

        log_event(signal_id, "ANOMALY_DETECTION", anomaly_result)

        # Step 7: Store anomaly
        insert_anomaly(signal_id, anomaly_result)

        # Step 8: Classification
        classification_result = classify_signal(features, anomaly_result)

        log_event(signal_id, "CLASSIFICATION", classification_result)

        # Step 9: Store classification
        insert_classification(signal_id, classification_result)

        # Step 10: Threat Intelligence Matching
        threat_intel_result = match_threat_intelligence(fingerprint)

        log_event(signal_id, "THREAT_INTELLIGENCE", threat_intel_result)

        # Step 10: Decision Engine
        decision_result = make_decision(classification_result, anomaly_result, threat_intel_result)

        log_event(signal_id, "DECISION_ENGINE", decision_result)

        # Step 11: Store decision
        insert_decision(signal_id, decision_result)

        print("Received signal:", signal_dict)
        print("Stored signal:", stored_signal)

        # ✅ CRITICAL FIX: RETURN RESPONSE
        return APIResponse(
            status="success",
            message="Signal processed successfully",
            data={
                "signal_id": signal_id,
                "features": features,
                "anomaly": anomaly_result,
                "classification": classification_result,
                "threat_intelligence": threat_intel_result,
                "decision": decision_result
            }
        )

    except Exception as e:
        print("[ROUTE ERROR]:", e)

        return APIResponse(
            status="error",
            message=f"Signal processing failed: {str(e)}",
            data=None
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{signal_id}", response_model=APIResponse)
def get_signal(signal_id: str):
    return APIResponse(
        status="success",
        message="Fetch logic not implemented yet",
        data={"signal_id": signal_id}
    )