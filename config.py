import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
LOG_CHANNEL_ID = int(os.getenv("LOG_CHANNEL_ID"))
JOIN_REQUEST_LOG_CHANNEL_ID = int(os.getenv("JOIN_REQUEST_LOG_CHANNEL_ID"))
MONGO_URI = os.getenv("MONGO_URI")
AUTH_CHANNEL = os.getenv("AUTH_CHANNEL")
REQ_CHANNEL = os.getenv("REQ_CHANNEL")

