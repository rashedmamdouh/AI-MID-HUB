"""
X-Ray Classification Router — 3-Model Cascade
================================================
POST /api/xray/classify

Pipeline (matches your diagnose_xray_report logic exactly):
  1. Screening model  → Normal vs Abnormal
  2. If Abnormal (or low-confidence Normal):
       • Infections model → Normal / Pneumonia / COVID-19 / Tuberculosis
       • Tissue model     → Normal / Lung Cancer / Fibrosis / Effusion
  3. Primary diagnosis = highest-confidence non-Normal finding above threshold

The DiseaseClassifier class here is a direct copy of yours so it loads
your .pth weights with no architecture mismatch.
"""

import os, sys
import torch
import torch.nn as nn
import torchvision.models as models
import cv2
import numpy as np
from PIL import Image
from io import BytesIO
from datetime import datetime
from typing import List, Optional, Dict

from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel
import albumentations as A
from albumentations.pytorch import ToTensorV2
from dotenv import load_dotenv

load_dotenv()
xray_router = APIRouter()

# ─── Config (matches your Config class) ───────────────────────────────────
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
IMG_SIZE = 224
CONFIDENCE_THRESHOLD = 70.0   # same as your default

_BACKEND_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCREENING_PATH   = os.getenv("SCREENING_MODEL_PATH",   os.path.join(_BACKEND_DIR, "models", "screening_model.pth"))
INFECTIONS_PATH  = os.getenv("INFECTIONS_MODEL_PATH",  os.path.join(_BACKEND_DIR, "models", "infections_model.pth"))
TISSUE_PATH      = os.getenv("TISSUE_MODEL_PATH",      os.path.join(_BACKEND_DIR, "models", "tissue_model.pth"))

SCREENING_CLASSES  = ["Normal", "Abnormal"]
INFECTION_CLASSES  = ["Normal", "Pneumonia", "COVID-19", "Tuberculosis"]
TISSUE_CLASSES     = ["Normal", "Lung Cancer", "Fibrosis", "Effusion"]


# ─── Model Architecture (exact copy of yours) ─────────────────────────────
class DiseaseClassifier(nn.Module):
    def __init__(self, num_classes):
        super().__init__()
        self.backbone = models.efficientnet_b3(weights=None)   # weights loaded from .pth
        num_features = self.backbone.classifier[1].in_features
        self.backbone.classifier = nn.Identity()

        if num_classes == 2:
            self.classifier = nn.Sequential(
                nn.Dropout(0.3),
                nn.Linear(num_features, 256),
                nn.ReLU(),
                nn.BatchNorm1d(256),
                nn.Dropout(0.2),
                nn.Linear(256, num_classes),
            )
        else:
            self.classifier = nn.Sequential(
                nn.Dropout(0.4),
                nn.Linear(num_features, 512),
                nn.ReLU(),
                nn.BatchNorm1d(512),
                nn.Dropout(0.3),
                nn.Linear(512, 256),
                nn.ReLU(),
                nn.BatchNorm1d(256),
                nn.Dropout(0.2),
                nn.Linear(256, num_classes),
            )

    def forward(self, x):
        features = self.backbone(x)
        return self.classifier(features)


# ─── Load all 3 models once at startup ────────────────────────────────────
_models: Dict[str, Optional[nn.Module]] = {"screening": None, "infections": None, "tissue": None}


def _load_single(name: str, path: str, num_classes: int):
    if not os.path.exists(path):
        print(f"[XRAY] WARNING: {name} weights not found at '{path}'")
        return None
    m = DiseaseClassifier(num_classes=num_classes).to(DEVICE)
    m.load_state_dict(torch.load(path, map_location=DEVICE))
    m.eval()
    print(f"[XRAY] ✓ {name} model loaded")
    return m


def load_models():
    print(f"[XRAY] Looking for models in: {_BACKEND_DIR}/models/")
    print(f"[XRAY] screening path: {SCREENING_PATH}")
    _models["screening"]  = _load_single("screening",  SCREENING_PATH,  2)
    _models["infections"] = _load_single("infections", INFECTIONS_PATH, 4)
    _models["tissue"]     = _load_single("tissue",     TISSUE_PATH,     4)


_models_loaded = False


def _ensure_models():
    global _models_loaded
    if not _models_loaded:
        load_models()
        _models_loaded = True


# ─── Preprocessing (matches your preprocess_image exactly) ────────────────
_transform = A.Compose([
    A.Resize(IMG_SIZE, IMG_SIZE),
    A.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ToTensorV2(),
])


def _preprocess(image_bytes: bytes):
    """bytes → (tensor, original RGB numpy)"""
    img_pil = Image.open(BytesIO(image_bytes)).convert("RGB")
    img_np  = np.array(img_pil)
    tensor  = _transform(image=img_np)["image"].unsqueeze(0).to(DEVICE)
    return tensor, img_np


# ─── Predict helper (matches your predict() exactly) ──────────────────────
def _predict(model: nn.Module, tensor, class_names: List[str]):
    with torch.no_grad():
        logits = model(tensor)
        probs  = torch.softmax(logits, dim=1)[0]
        conf, idx = torch.max(probs, 0)

    all_probs = {
        class_names[i]: round(float(probs[i]) * 100, 2)
        for i in range(len(class_names))
    }
    return class_names[idx.item()], round(float(conf) * 100, 2), all_probs


# ─── Recommendations (exact copy of yours) ────────────────────────────────
RECOMMENDATIONS = {
    "Pneumonia": [
        "Immediate medical attention recommended",
        "Antibiotic treatment may be required",
        "Follow-up chest X-ray in 4-6 weeks",
        "Monitor for worsening symptoms",
    ],
    "COVID-19": [
        "Isolate immediately — highly contagious",
        "Seek medical evaluation for oxygen levels",
        "Contact local health authorities",
        "Monitor symptoms closely",
    ],
    "Tuberculosis": [
        "URGENT: Infectious disease specialist referral",
        "Long-term antibiotic therapy needed (6–9 months)",
        "Respiratory isolation precautions",
        "Contact tracing for recent exposures",
    ],
    "Lung Cancer": [
        "URGENT: Oncology referral required",
        "Further imaging (CT, PET scan) needed",
        "Biopsy for tissue diagnosis",
        "Multidisciplinary team consultation",
    ],
    "Fibrosis": [
        "Pulmonology referral recommended",
        "Pulmonary function tests needed",
        "May require anti-fibrotic medication",
        "Pulmonary rehabilitation program",
    ],
    "Effusion": [
        "Medical evaluation needed",
        "Thoracentesis may be required",
        "Fluid analysis to determine cause",
        "Underlying cause investigation",
    ],
}

DEFAULT_RECS = [
    "Consult with healthcare provider",
    "Additional testing may be needed",
    "Follow-up as recommended",
]


# ─── Response schemas ──────────────────────────────────────────────────────
class ModelResult(BaseModel):
    result: str
    confidence: float
    probabilities: Dict[str, float]


class FinalDiagnosis(BaseModel):
    primary: str
    confidence: float
    category: str   # "Healthy" | "Infection" | "Tissue" | "Uncertain"


class XRayReport(BaseModel):
    timestamp: str
    screening: ModelResult
    infection_analysis: Optional[ModelResult] = None
    tissue_analysis: Optional[ModelResult] = None
    final_diagnosis: FinalDiagnosis
    recommendations: List[str]


# ─── Endpoint ──────────────────────────────────────────────────────────────
@xray_router.post("/classify", response_model=XRayReport)
async def classify_xray(image: UploadFile = File(...)):
    """
    Upload a chest X-ray → full 3-model cascade diagnosis report.
    """
    # Validate
    if image.content_type not in ("image/png", "image/jpeg", "image/jpg"):
        raise HTTPException(400, "Only PNG/JPG images are accepted.")

    # Check models
    if not all(_models.values()):
        missing = [k for k, v in _models.items() if v is None]
        raise HTTPException(503, f"Models not loaded: {missing}. Check .pth file paths in .env")

    raw = await image.read()
    tensor, _ = _preprocess(raw)

    # ── Step 1: Screening ──────────────────────────────────────────────
    s_label, s_conf, s_probs = _predict(_models["screening"], tensor, SCREENING_CLASSES)

    report_screening = ModelResult(result=s_label, confidence=s_conf, probabilities=s_probs)

    # ── Step 2: If Normal with high confidence → done ─────────────────
    if s_label == "Normal" and s_conf >= CONFIDENCE_THRESHOLD:
        return XRayReport(
            timestamp=datetime.now().isoformat(),
            screening=report_screening,
            final_diagnosis=FinalDiagnosis(primary="Normal", confidence=s_conf, category="Healthy"),
            recommendations=[
                "No significant abnormalities detected",
                "Routine follow-up as scheduled",
                "Maintain healthy lifestyle",
            ],
        )

    # ── Step 3: Run Infections + Tissue in parallel (logically) ───────
    inf_label, inf_conf, inf_probs = _predict(_models["infections"], tensor, INFECTION_CLASSES)
    tis_label, tis_conf, tis_probs = _predict(_models["tissue"],     tensor, TISSUE_CLASSES)

    report_inf = ModelResult(result=inf_label, confidence=inf_conf, probabilities=inf_probs)
    report_tis = ModelResult(result=tis_label, confidence=tis_conf, probabilities=tis_probs)

    # ── Step 4: Determine primary diagnosis (your exact logic) ─────────
    findings = []
    if inf_label != "Normal" and inf_conf >= CONFIDENCE_THRESHOLD:
        findings.append(("Infection", inf_label, inf_conf))
    if tis_label != "Normal" and tis_conf >= CONFIDENCE_THRESHOLD:
        findings.append(("Tissue", tis_label, tis_conf))

    if findings:
        findings.sort(key=lambda x: x[2], reverse=True)
        category, disease, conf = findings[0]
        final = FinalDiagnosis(primary=disease, confidence=conf, category=category)
        recs  = RECOMMENDATIONS.get(disease, DEFAULT_RECS)
    else:
        final = FinalDiagnosis(primary="Indeterminate", confidence=s_conf, category="Uncertain")
        recs  = [
            "Findings are inconclusive",
            "Recommend additional imaging",
            "Consult with radiologist",
        ]

    return XRayReport(
        timestamp=datetime.now().isoformat(),
        screening=report_screening,
        infection_analysis=report_inf,
        tissue_analysis=report_tis,
        final_diagnosis=final,
        recommendations=recs,
    )
