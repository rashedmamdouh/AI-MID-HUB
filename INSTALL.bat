@echo off
echo ========================================
echo   AI Medical Hub - Installing Packages
echo ========================================
echo.

echo Step 1: Installing numpy (pre-built)...
pip install "numpy>=1.26" --only-binary=:all:

echo.
echo Step 2: Installing core packages...
pip install fastapi==0.109.1 "uvicorn[standard]==0.27.0" python-multipart==0.0.9 pydantic==2.6.1 python-dotenv pillow scikit-learn sentencepiece

echo.
echo Step 3: Installing PyTorch (CPU)...
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu

echo.
echo Step 4: Installing AI/ML packages...
pip install transformers==4.37.2 accelerate easyocr sentence-transformers faiss-cpu albumentations

echo.
echo ========================================
echo   Installation complete!
echo   Now run START.bat to launch the app.
echo ========================================
pause

echo.
echo Step 5: Installing Anthropic SDK...
pip install anthropic
