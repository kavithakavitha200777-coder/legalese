@echo off
REM Starts backend (8000) + frontend (8501) in two windows on Windows.
cd /d "%~dp0"
start "LegalEase Backend" cmd /k "venv\Scripts\activate && uvicorn legalEaseAPI.main:app --reload --port 8000"
timeout /t 3 >nul
start "LegalEase Frontend" cmd /k "venv\Scripts\activate && streamlit run frontend/app.py"
