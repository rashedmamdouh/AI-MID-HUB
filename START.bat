@echo off
echo ========================================
echo   AI Medical Hub - Starting Server
echo ========================================
echo.

cd /d "%~dp0backend"

echo Starting backend on http://localhost:8000
echo Open your browser at: http://localhost:8000
echo.
echo Press CTRL+C to stop the server.
echo.

python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload

pause
