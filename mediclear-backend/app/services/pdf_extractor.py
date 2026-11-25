import re
import fitz #PyMuPDF

def extract_and_senitize_pdf(file_bytes: bytes)->str:
    doc = fitz.open(stream=file_bytes, filetype="pdf")
    raw_text = "\n".join(page.get_text("text") for page in doc)

    #Basic PII redaction before LLM inference
    sanitized = re.sub(r'\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b', '[REDACTED_EMAIL]', raw_text)
    sanitized = re.sub(r'(\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', '[REDACTED_PHONE]', sanitized)

    return sanitized.strip()