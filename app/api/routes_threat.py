from fastapi import APIRouter

router = APIRouter()

@router.get("/intel")
def get_threat_intel():
    return {"message": "Threat intelligence endpoint"}