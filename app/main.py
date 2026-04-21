from fastapi import FastAPI
from app.api import routes_signal, routes_model, routes_threat, routes_ai

app = FastAPI(
    title="Battlefield Communication Analyzer",
    description="AI-powered RF Signal Intelligence Backend",
    version="1.0.0"
)

# Root check
@app.get("/")
def root():
    return {"message": "Backend is running"}

# Include routers
app.include_router(routes_signal.router, prefix="/signal", tags=["Signal"])
app.include_router(routes_model.router, prefix="/model", tags=["Model"])
app.include_router(routes_threat.router, prefix="/threat", tags=["Threat"])
app.include_router(routes_ai.router, prefix="/ai", tags=["AI Assistant"])