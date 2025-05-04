from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, constr
from twilio.rest import Client
import os
import logging
from typing import Optional
from pydantic import BaseModel, constr
from typing import Annotated
from pydantic import BaseModel, Field

# ---------------------
# Setup logging
# ---------------------
logging.basicConfig(level=logging.INFO)

# ---------------------
# FastAPI App Instance
# ---------------------
app = FastAPI(
    title="WhatsApp Sender API",
    version="1.0.0",
    description="An API to send WhatsApp messages using Twilio."
)

# ---------------------
# Twilio Client Holder (Lazy Initialization)
# ---------------------
client: Optional[Client] = None

def get_twilio_client() -> Client:
    """
    Lazily initializes and returns a Twilio Client instance.
    """
    global client
    if client is None:
        account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        if not account_sid or not auth_token:
            raise RuntimeError("Twilio credentials are missing in environment variables.")
        client = Client(account_sid, auth_token)
        logging.info("Twilio client initialized.")
    return client
# twilio BPT2UQ3HXVH5P2BAPGJ9NECV recover code
# ---------------------
# Pydantic Model for Input Validation
# ---------------------

class WhatsAppMessage(BaseModel):
    to: Annotated[
        str,
        Field(pattern=r"^\+\d{10,15}$")
    ]
    message: Annotated[
        str,
        Field(min_length=1, max_length=4096)
    ]

# ---------------------
# API Endpoint
# ---------------------
@app.post("/send-whatsapp", summary="Send a WhatsApp Message")
async def send_whatsapp(msg: WhatsAppMessage):
    """
    Sends a WhatsApp message using Twilio's API.
    """
    twilio_client = get_twilio_client()
    from_whatsapp = os.getenv("TWILIO_WHATSAPP_FROM")
    
    if not from_whatsapp:
        raise HTTPException(status_code=500, detail="Twilio WhatsApp sender number not configured.")

    try:
        logging.info(f"Sending WhatsApp message to {msg.to}")
        message = twilio_client.messages.create(
            body=msg.message,
            from_=from_whatsapp,
            to=f"whatsapp:{msg.to}"
        )
        logging.info(f"Message sent successfully. SID: {message.sid}")
        return {"status": "success", "sid": message.sid}
    except Exception as e:
        logging.error(f"Failed to send WhatsApp message: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))  # SHOW Twilio's error message

