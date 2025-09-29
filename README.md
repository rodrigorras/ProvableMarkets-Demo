
<img width="540" height="169" alt="image" src="https://github.com/user-attachments/assets/7634e9cb-7c22-41c7-ba16-1e15d260acd4" />


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
pip install -r requirements.txt

# Run the app
uvicorn main:app --reload
