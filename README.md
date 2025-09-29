
<img width="876" height="188" alt="image" src="https://github.com/user-attachments/assets/96fbc93f-f889-4502-997a-8904f90be873" />



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
