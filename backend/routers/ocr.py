"""
OCR Router — EasyOCR text extraction → free LLM structured report
"""

import os, re, json, requests
import cv2
import numpy as np
from PIL import Image
from io import BytesIO
from typing import List, Optional

from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()
ocr_router = APIRouter()

HF_API_KEY   = os.getenv("HF_API_KEY", "")
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")

_HF_HEADERS = {"Content-Type": "application/json"}
if HF_API_KEY:
    _HF_HEADERS["Authorization"] = f"Bearer {HF_API_KEY}"

_HF_MODEL   = "mistralai/Mistral-7B-Instruct-v0.3"
_GROQ_MODEL = "llama-3.1-8b-instant"   # free on Groq

_easy_ocr = None


def _load_easy():
    global _easy_ocr
    if _easy_ocr is None:
        import easyocr
        print("[OCR] Loading EasyOCR ...")
        _easy_ocr = easyocr.Reader(["en"], gpu=False, verbose=False)
        print("[OCR] ✓ EasyOCR ready")
    return _easy_ocr


# ─── Response Model ────────────────────────────────────────────────────────
class OCRResponse(BaseModel):
    raw_text: str
    summary: str
    patient_info: List[str]
    chief_complaint: str
    medical_history: List[str]
    diagnoses: List[str]
    medications: List[str]
    test_results: List[str]
    recommendations: List[str]
    follow_up_actions: List[str]
    doctor_info: str
    urgency_level: str
    urgency_explanation: str
    key_findings: List[str]
    diagnosis_explanation: str
    detailed_advice: str
    medication_explanation: str
    test_interpretation: str
    lifestyle_modifications: str
    warning_signs: str


# ─── Image preprocessing ──────────────────────────────────────────────────
def _preprocess(img_bytes: bytes) -> np.ndarray:
    arr = np.frombuffer(img_bytes, dtype=np.uint8)
    img = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    if img is None:
        pil = Image.open(BytesIO(img_bytes)).convert("RGB")
        img = cv2.cvtColor(np.array(pil), cv2.COLOR_RGB2BGR)

    # Upscale small images for better OCR accuracy
    h, w = img.shape[:2]
    if w < 1400:
        scale = 2000 / w
        img = cv2.resize(img, None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)

    # Convert to grayscale → denoise → sharpen
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.fastNlMeansDenoising(gray, h=10)
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    gray = cv2.filter2D(gray, -1, kernel)
    # Back to BGR so EasyOCR accepts it
    return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)


# ─── EasyOCR text extraction ───────────────────────────────────────────────
def extract_text(img_bytes: bytes) -> str:
    img  = _preprocess(img_bytes)
    easy = _load_easy()

    results = easy.readtext(img, detail=1, paragraph=False)
    if not results:
        raise ValueError("No text detected. Please use a clear, well-lit scan.")

    # Group words that are on the same line (within 12px vertically)
    results.sort(key=lambda r: r[0][0][1])   # sort by top-left Y

    lines, current_line, last_y = [], [], -999
    for box, text, conf in results:
        if conf < 0.25 or len(text.strip()) < 2:
            continue
        y = box[0][1]
        if abs(y - last_y) > 12 and current_line:
            current_line.sort(key=lambda i: i[0])   # sort by X within line
            lines.append(" ".join(t for _, t in current_line))
            current_line = []
        current_line.append((box[0][0], text.strip()))
        last_y = y

    if current_line:
        current_line.sort(key=lambda i: i[0])
        lines.append(" ".join(t for _, t in current_line))

    raw = "\n".join(l for l in lines if l.strip())
    if len(raw) < 30:
        raise ValueError("Could not extract sufficient text. Please use a clear, well-lit scan.")

    print(f"[OCR] EasyOCR extracted {len(raw)} chars")
    return _clean(raw)


def _clean(text: str) -> str:
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)
    text = re.sub(r'[ \t]{3,}', '  ', text)
    text = re.sub(r'\n{4,}', '\n\n', text)
    return text.strip()


# ─── LLM structured report ─────────────────────────────────────────────────
_PROMPT = """\
<s>[INST] You are a medical document analyst. The following text was extracted via OCR from a medical report image and may contain minor noise or formatting errors.

Your task is to read it carefully and return a single valid JSON object with EXACTLY these keys. Follow the field definitions strictly.

FIELD DEFINITIONS:
- summary: 2-3 sentence plain-English overview of the entire report.
- patient_info: list of strings for patient demographics only (name, age, gender, DOB, ID, report date). Example: ["Patient: John Doe", "Age: 45", "Gender: Male"]
- chief_complaint: the patient's main reason for the visit (string).
- medical_history: list of past or chronic conditions mentioned. Example: ["Hypertension since 2018", "Type 2 Diabetes"]
- diagnoses: list of current diagnoses or clinical impressions only. Example: ["Community-Acquired Pneumonia", "Type 2 Diabetes Mellitus"]
- medications: list of drug prescriptions ONLY — each must include drug name + dose + frequency. Example: ["Amoxicillin 500mg twice daily for 7 days", "Metformin 1000mg BID"]. Do NOT include doctor names, lifestyle advice, or follow-up instructions here.
- test_results: list of lab or physical examination findings with values. Example: ["WBC: 11,000/μL (elevated)", "SpO2: 94%", "Blood pressure: 140/90 mmHg"]
- recommendations: list of medical recommendations from the doctor. Example: ["Increase fluid intake", "Avoid strenuous activity for 2 weeks"]
- follow_up_actions: list of scheduled follow-up steps only. Example: ["Return visit in 7 days", "Repeat chest X-ray in 4 weeks"]
- doctor_info: doctor name and credentials only (string). Example: "Dr. Mona Khaled, MD — License No. 12345"
- urgency_level: exactly one of: "High", "Moderate", or "Low".
- urgency_explanation: one sentence explaining the urgency level.
- key_findings: list of the 3-5 most important clinical findings.
- diagnosis_explanation: plain-language explanation of the diagnoses for the patient.
- detailed_advice: comprehensive patient advice based on the report.
- medication_explanation: plain-language explanation of each prescribed medication and why it was given.
- test_interpretation: plain-language interpretation of the lab/test results.
- lifestyle_modifications: specific lifestyle changes recommended (diet, exercise, sleep, etc.).
- warning_signs: symptoms that should prompt the patient to seek immediate care.

RULES:
- Every list field must be a JSON array of strings.
- Every string field must be a plain string.
- urgency_level must be exactly "High", "Moderate", or "Low" — nothing else.
- Do NOT put doctor names, lifestyle advice, or follow-up text inside the medications list.
- Return ONLY the JSON object. No markdown, no explanation, no extra text outside the JSON.

OCR TEXT:
{raw_text}
[/INST]"""


def _extract_json(text: str) -> dict | None:
    match = re.search(r'\{.*\}', text, re.DOTALL)
    if not match:
        return None
    return json.loads(match.group())


def _llm_parse_groq(raw_text: str) -> dict | None:
    """Primary: Groq free API (llama-3.1-8b-instant) — fast and reliable."""
    if not GROQ_API_KEY:
        return None
    try:
        resp = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {GROQ_API_KEY}",
            },
            json={
                "model": _GROQ_MODEL,
                "messages": [{"role": "user", "content": _PROMPT.format(raw_text=raw_text[:3500])}],
                "temperature": 0.1,
                "max_tokens": 1500,
            },
            timeout=30,
        )
        if resp.status_code != 200:
            print(f"[OCR-LLM/Groq] HTTP {resp.status_code}: {resp.text[:200]}")
            return None
        text = resp.json()["choices"][0]["message"]["content"]
        parsed = _extract_json(text)
        if parsed:
            print("[OCR-LLM] ✓ Groq structured report OK")
        else:
            print("[OCR-LLM/Groq] No JSON in response")
        return parsed
    except json.JSONDecodeError as e:
        print(f"[OCR-LLM/Groq] JSON parse error: {e}")
    except requests.Timeout:
        print("[OCR-LLM/Groq] Timeout")
    except Exception as e:
        print(f"[OCR-LLM/Groq] Error: {e}")
    return None


def _llm_parse_hf(raw_text: str) -> dict | None:
    """Fallback: HuggingFace Inference Router (requires token with Inference Providers permission)."""
    if not HF_API_KEY:
        return None
    try:
        resp = requests.post(
            f"https://router.huggingface.co/hf-inference/models/{_HF_MODEL}",
            headers=_HF_HEADERS,
            json={
                "inputs": _PROMPT.format(raw_text=raw_text[:3500]),
                "parameters": {"max_new_tokens": 1000, "temperature": 0.1, "return_full_text": False},
            },
            timeout=60,
        )
        if resp.status_code != 200:
            print(f"[OCR-LLM/HF] HTTP {resp.status_code}: {resp.text[:200]}")
            return None
        data = resp.json()
        text = (data[0].get("generated_text", "") if isinstance(data, list) else data.get("generated_text", ""))
        parsed = _extract_json(text)
        if parsed:
            print("[OCR-LLM] ✓ HF structured report OK")
        else:
            print("[OCR-LLM/HF] No JSON in response")
        return parsed
    except json.JSONDecodeError as e:
        print(f"[OCR-LLM/HF] JSON parse error: {e}")
    except requests.Timeout:
        print("[OCR-LLM/HF] Timeout")
    except Exception as e:
        print(f"[OCR-LLM/HF] Error: {e}")
    return None


def _llm_parse(raw_text: str) -> dict | None:
    return _llm_parse_groq(raw_text) or _llm_parse_hf(raw_text)


def _build_response(raw_text: str, llm: dict) -> dict:
    """Safely map LLM output to response fields, filling blanks with safe defaults."""
    def lst(key, default=None):
        v = llm.get(key)
        if isinstance(v, list):
            return [str(i) for i in v if str(i).strip()]
        if isinstance(v, str) and v.strip():
            return [v.strip()]
        return default or []

    def s(key, default=""):
        v = llm.get(key)
        return str(v).strip() if v else default

    urgency = s("urgency_level")
    if urgency not in ("High", "Moderate", "Low"):
        urgency = "Low"

    return dict(
        raw_text=raw_text,
        summary=s("summary", "Medical report processed."),
        patient_info=lst("patient_info"),
        chief_complaint=s("chief_complaint"),
        medical_history=lst("medical_history"),
        diagnoses=lst("diagnoses", ["No diagnoses identified."]),
        medications=lst("medications", ["No medications identified."]),
        test_results=lst("test_results", ["No test results identified."]),
        recommendations=lst("recommendations", ["Follow physician's instructions."]),
        follow_up_actions=lst("follow_up_actions", ["Consult your physician for follow-up schedule."]),
        doctor_info=s("doctor_info"),
        urgency_level=urgency,
        urgency_explanation=s("urgency_explanation", "No critical findings detected."),
        key_findings=lst("key_findings"),
        diagnosis_explanation=s("diagnosis_explanation", "Please consult your physician for a full explanation."),
        detailed_advice=s("detailed_advice", "Follow all instructions in the report and consult your physician."),
        medication_explanation=s("medication_explanation", "Take all medications exactly as prescribed."),
        test_interpretation=s("test_interpretation", "Consult your physician for interpretation of test results."),
        lifestyle_modifications=s("lifestyle_modifications", "Follow any lifestyle advice provided by your physician."),
        warning_signs=s("warning_signs", "Seek immediate care if symptoms worsen or new symptoms develop."),
    )


# ─── Endpoint ──────────────────────────────────────────────────────────────
@ocr_router.post("/analyze", response_model=OCRResponse)
async def analyze_report(file: UploadFile = File(...)):
    img_bytes = await file.read()
    if not img_bytes:
        raise HTTPException(400, "Empty file uploaded.")

    try:
        raw_text = extract_text(img_bytes)
    except ValueError as e:
        raise HTTPException(422, str(e))
    except Exception as e:
        print(f"[OCR] Error: {e}")
        raise HTTPException(500, f"OCR failed: {str(e)}")

    llm_result = _llm_parse(raw_text)
    if not llm_result:
        raise HTTPException(503, "LLM report generation failed. Please try again or check your HF_API_KEY.")

    result = _build_response(raw_text, llm_result)
    return OCRResponse(**result)
