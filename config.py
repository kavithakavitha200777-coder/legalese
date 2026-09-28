"""Central configuration for LegalEase (loaded from .env)."""
import os
from pathlib import Path

from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parent
load_dotenv(ROOT_DIR / ".env")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-flash-latest").strip()
# Tried in order if the primary model is unavailable / retired
GEMINI_FALLBACK_MODELS = ["gemini-flash-latest", "gemini-2.5-flash"]

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000").rstrip("/")
MOCK_MODE = os.getenv("MOCK_MODE", "false").strip().lower() in {"1", "true", "yes"}

IMAGE_DIR = ROOT_DIR / "Image"
LOGO_PATH = str(IMAGE_DIR / "Logo.png")               # light background (DOCX / PDF)
WEB_LOGO_PATH = str(IMAGE_DIR / "inverseLogo.png")    # dark background (web UI)

APP_NAME = "LegalEase"
FOOTER_TEXT = "LegalEase | AI-generated draft - review with a qualified legal professional"
