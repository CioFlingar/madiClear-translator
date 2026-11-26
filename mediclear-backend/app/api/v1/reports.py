from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile, status
from sqlalchemy.orm import Session


from app.db.models import ReportRecord, User
from app.db.session import get_db
from app.schemas.report import ReportAnalysisResponse
from app.services.ai_translator import analyze_medical_text
from app.services.pdf_extractor import extract_and_sanitize_pdf

router = APIRouter(prefix="/reports", tags=["Reports"])