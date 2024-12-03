from pyrogram.enums import ParseMode
from config import LOG_CHANNEL_ID, JOIN_REQUEST_LOG_CHANNEL_ID

def get_greeting():
    """Return a greeting message based on the time of day."""
    from datetime import datetime
    current_hour = datetime.now().hour
    if current_hour < 12:
        return "Good Morning"
    elif 12 <= current_hour < 18:
        return "Good Afternoon"
    else:
        return "Good Evening"

def log_user_start(user, client):
    """Log user start interaction to the log channel."""
    text = (
        f"👤 **User Started Bot**\n\n"
        f"**ID:** `{user.id}`\n"
        f"**Name:** {user.first_name} {user.last_name or ''}\n"
        f"**Username:** @{user.username or 'N/A'}\n"
        f"**Language:** {user.language_code or 'N/A'}\n"
    )
    client.send_message(LOG_CHANNEL_ID, text, parse_mode=ParseMode.MARKDOWN)

def log_join_request(user, chat, client):
    """Log join request approval to the join request log channel."""
    text = (
        f"✅ **Join Request Approved**\n\n"
        f"👤 **User ID:** `{user.id}`\n"
        f"**Name:** {user.first_name} {user.last_name or ''}\n"
        f"**Chat Title:** {chat.title}\n"
        f"**Chat ID:** `{chat.id}`\n"
    )
    client.send_message(JOIN_REQUEST_LOG_CHANNEL_ID, text, parse_mode=ParseMode.MARKDOWN)
