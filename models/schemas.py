from pydantic import BaseModel


class FaceComparisonResult(BaseModel):
    verified: bool
    distance: float
    threshold: float
    confidence: float
    model: str