from pydantic import BaseModel
from typing import Optional, Dict, Any


class SignalInput(BaseModel):
    frequency: float
    amplitude: float
    modulation: str

    # NEW (ML-aligned fields)
    signal_strength: Optional[float] = None
    bandwidth: Optional[float] = None
    memory_usage: Optional[float] = None
    wifi_strength: Optional[float] = None

    source: Optional[str] = "unknown"
    metadata: Optional[Dict[str, Any]] = {}