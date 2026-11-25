import os
from google import genai
from google.genai import types
from app.schemas.report import ReportAnalysisResponse

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_PROMPT = """
You are a compassionate, accurate clinical communication assistant.
Translate the provided medical or lab report into clear, calm, jargon-free language for a patient.
Rules:
1. Never diagnose a disease or prescribe medication.
2. Highlight out-of-range values objectively based on the report's reference ranges.
3. If values appear critically abnormal, set urgency_flag to 'prompt_attention' and advise contacting a doctor promptly without causing panic.
4. Adapt explanations to the requested target language while keeping standard medical test names recognizable.
"""

def analyze_medical_text(report_text: str, target_language: str = "English") -> ReportAnalysisResponse:
    prompt = f"Target Language: {target_language}\n\nMedical Report Text:\n{report_text}"

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            response_mime_type="application/json",
            response_schema=ReportAnalysisResponse,
            temperature=0.2,
        ),
    )
    return ReportAnalysisResponse.model_validate_json(response.text)