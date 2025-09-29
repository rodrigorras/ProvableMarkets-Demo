# ProvableMarkets Demo

Simple FastAPI app with:

- `GET /ping` → responds `"pong"`
- `POST /hello` → receives `{"name":"<name>"}` and responds with a greeting + timestamp

---

## Setup & Run

```bash
# Create & activate virtual environment
python3 -m venv .venv

# macOS/Linux
source .venv/bin/activate

# Install dependencies
pip install fastapi==0.104.1 uvicorn[standard]==0.24.0

# Run the app
uvicorn main:app --reload
