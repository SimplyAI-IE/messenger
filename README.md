# 📬 WhatsApp Sender API

A production-ready FastAPI microservice that sends WhatsApp messages using the Twilio API.  
Built with Python, Docker, and Pydantic v2. Fully compatible with Twilio Sandbox and deployable anywhere.

## 🚀 Features
- FastAPI backend with Swagger UI at `/docs`
- Input validation using Pydantic 2.x
- WhatsApp message sending via Twilio's API
- Dockerized for easy deployment
- `.env`-based configuration (no secrets in code)

## 🧪 Local Development

```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
Access the app at http://localhost:8000/docs

🐳 Docker
bash
Copy
Edit
docker build -t whatsapp-sender-api .
docker run -p 8000:8000 --env-file .env whatsapp-sender-api
🛠 .env Format
env
Copy
Edit
TWILIO_ACCOUNT_SID=ACXXXXXXXXXXXXXXXXXXXXXXXXXXXX
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_WHATSAPP_FROM=whatsapp:+14155238886
📜 License
MIT © 2025 Jason Cooke

yaml
Copy
Edit

✅ Then **Save** the file.

---

# ✅ After That:

1. Run:

```bash
git add README.md
git commit -m "Add README.md"
Push if your remote is set up:

bash
Copy
Edit
git push origin main