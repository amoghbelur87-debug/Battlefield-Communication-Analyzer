from fastapi import APIRouter
from app.schemas.response_schema import APIResponse
from app.ai_assistant.explain import explain_decision
from app.ai_assistant.recommend import recommend_actions
from app.ai_assistant.debug import debug_pipeline

router = APIRouter()


@router.post("/assist")
def ai_assist(signal_data: dict):
    try:
        explanation = explain_decision(signal_data)
        recommendations = recommend_actions(signal_data)
        debug_info = debug_pipeline(signal_data)

        return APIResponse(
            status="success",
            message="AI assistance generated",
            data={
                "explanation": explanation,
                "recommendations": recommendations,
                "debug": debug_info
            }
        )

    except Exception as e:
        return APIResponse(
            status="error",
            message=str(e),
            data={}
        )