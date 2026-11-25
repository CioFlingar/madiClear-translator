from pydantic import BaseModel, Field
from typing import List, Literal

class BiomakerItem(BaseModel):
    name: str = Field(..., description="Standardized test name, e.g., Hemoglobin A1c")
    value: str = Field(..., description="Measured value with units, e.g., 6.8 %")
    reference_range: str = Field(..., description="Normal lab reference range if present")
    status: Literal["normal", "borderline", "high", "low", "unknown"]
    plain_english_meaning: str = Field(..., description="1-2 sentence explanation of what this marker measures in everyday terms")

class ReportAnalysisResponse(BaseModel):
    disclaimer: str = Field(
        default="Informational summary only. Not a medical diagnosis. Always review these results with a licensed physician."
    )
    overall_summary: str = Field(..., description="Calm, empathetic 3-4 sentence overview of the report")
    urgency_flag: Literal["routine", "discuss_soon", "prompt_attention"]
    Biomakers: List[BiomakerItem]
    questions_for_doctor: List[str] = Field(..., description="3-5 specific, high-value questions the patient should ask their doctor")
    lifestyle_context: List[str] = Field(..., description="General, non-prescriptive wellness factors commonly associated with these markers")
