# LegalEase - AI-Powered Legal Document Generator

FastAPI backend + Streamlit frontend + Google Gemini. Generates legal documents from
document type, parties, terms and dates; preview, edit, and export as TXT / DOCX / PDF.

```
LegalEase/
├── ai_core/            gemini_generator.py (Gemini calls) · generator.py (sanitize, DOCX, PDF, HTML)
├── frontend/app.py     Streamlit UI
├── legalEaseAPI/       main.py (FastAPI app) · routes.py (POST /generate)
├── Image/              Logo.png · inverseLogo.png (replace with your own branding)
├── tests/test_app.py   offline tests
├── config.py  .env  requirements.txt  run.sh  run.bat  make_logo.py
```

## Setup (VS Code)
1. Install Python 3.10+ and open the `LegalEase` folder in VS Code (`File > Open Folder`).
2. Open a terminal (`Ctrl+` `) and create + activate a virtual environment:
   - Windows: `python -m venv venv` then `venv\Scripts\activate`
   - macOS/Linux: `python3 -m venv venv` then `source venv/bin/activate`
   - In VS Code choose `Python: Select Interpreter` > the `venv` one.
3. `pip install -r requirements.txt`
4. Put your Gemini key in `.env` (free key: https://aistudio.google.com/app/apikey):
   `GEMINI_API_KEY=your_key`

## Run
Two terminals (both with the venv active), from the project root:

    uvicorn legalEaseAPI.main:app --reload          # backend  -> http://localhost:8000/docs
    streamlit run frontend/app.py                   # frontend -> http://localhost:8501

Or one command: `./run.sh` (macOS/Linux/Git Bash) or double-click `run.bat` (Windows).

## Test
- No API key yet? Set `MOCK_MODE=true` in `.env`, restart the backend, and use the whole UI with a built-in template.
- Automated: `pytest -v`
- Manual: open http://localhost:8000/health (should show `"api_key_configured": true`), then in the UI enter
  Document Type `Freelance Work Contract`, Parties `Jane Doe (Service Provider), TechNova Inc. (Client)`,
  Terms `Work delivered by May 15, 2025; Payment within 7 days; Either party may terminate with 15 days notice`,
  Date `April 15, 2025` -> Generate -> Edit -> download TXT/DOCX/PDF.

## Troubleshooting
| Problem | Fix |
|---|---|
| "Cannot reach the backend" | Start uvicorn first; check `BACKEND_URL` in `.env` |
| "GEMINI_API_KEY is missing" / key rejected | Check `.env`, restart the backend (env is read at startup) |
| Model not found | Set `GEMINI_MODEL` in `.env` (see https://ai.google.dev/gemini-api/docs/models) |
| `ModuleNotFoundError: fpdf` | `pip install fpdf2` (if old `fpdf` is installed: `pip uninstall fpdf` first) |
| Port in use | `uvicorn ... --port 8001` and set `BACKEND_URL=http://localhost:8001` |

*AI-generated drafts are not legal advice - have a qualified professional review them.*
