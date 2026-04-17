# AI Medical Hub — Fixed Version

## How to Run (Windows)

### First time only:
1. Open **Anaconda Prompt**
2. Run: `conda activate medical_hub`
3. Navigate to this folder: `cd "path\to\ai_medical_hub_fixed"`
4. Run: `INSTALL.bat`

### Every time:
1. Place your 3 model files in `backend\models\`:
   - `screening_model.pth`
   - `infections_model.pth`
   - `tissue_model.pth`

2. Open **Anaconda Prompt**
3. Run: `conda activate medical_hub`
4. Navigate to this folder
5. Double-click **START.bat** OR run:
   ```
   cd backend
   python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

6. Open browser at: **http://localhost:8000**

## What's Fixed
- Frontend served directly from backend (no need for second terminal)
- No more "Backend not reachable" error toast
- API URL auto-detects correctly
- Chat request format fixed
- numpy install issue bypassed
