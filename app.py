import logging
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_TOKEN, API_ID, API_HASH, LOG_CHANNEL_ID, JOIN_REQUEST_LOG_CHANNEL_ID
from utils.db import MongoDB
from utils.helpers import get_greeting, log_user_start, log_join_request

# Setup logging
logging.basicConfig(level=logging.INFO, filename="logs/bot.log", format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Initialize the bot
bot = Client("mn-bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
db = MongoDB()

@bot.on_message(filters.command("start"))
async def start(client, message):
    user = message.from_user
    log_user_start(user, client)
    await message.reply(
        f"Hello {user.mention}! Welcome to MN Bot 🎉.\nUse /help to get started.",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Join Updates", url="https://t.me/new_ott_movies3")]]
        )
    )

@bot.on_chat_join_request()
async def approve_join_request(client, request):
    user = request.from_user
    chat = request.chat
    await client.approve_chat_join_request(chat.id, user.id)
    log_join_request(user, chat, client)

if __name__ == "__main__":
    bot.run()
