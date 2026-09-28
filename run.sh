#!/usr/bin/env bash
# Starts backend (8000) + frontend (8501). Usage: ./run.sh
cd "$(dirname "$0")"
if [ -f venv/bin/activate ]; then source venv/bin/activate; elif [ -f venv/Scripts/activate ]; then source venv/Scripts/activate; fi
uvicorn legalEaseAPI.main:app --reload --port 8000 &
BACK=$!
trap 'kill $BACK 2>/dev/null' EXIT
sleep 2
streamlit run frontend/app.py
