import os
from fastapi import APIRouter
from ..models.model_loader import model_instance, MODEL_PATH

router = APIRouter()

@router.get("/status")
def model_status():
    if model_instance is None:
        status = "Model not loaded"
        detail = {
            "loaded": False,
            "path": MODEL_PATH,
            "exists": os.path.exists(MODEL_PATH)
        }
    else:
        status = "Model loaded"
        detail = {
            "loaded": True,
            "path": MODEL_PATH,
            "exists": True
        }

    return {"status": status, "detail": detail}