import asyncio
from pyrogram import Client, enums
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from database.join_reqs import JoinReqs

join_reqs = JoinReqs()

async def ForceSub(bot: Client, update: Message, file_id: str = False, mode="checksub"):
    # Logic for forced subscription
    try:
        # Check subscription status
        user = await bot.get_chat_member(chat_id="YOUR_CHANNEL_ID", user_id=update.from_user.id)
        if user.status == "kicked":
            await update.reply("You are banned.")
            return False
        return True
    except UserNotParticipant:
        invite_link = "https://t.me/YOUR_CHANNEL_ID?start"
        await update.reply(f"Please join the channel: {invite_link}")
        return False
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return await ForceSub(bot, update, file_id)
    except Exception as err:
        await update.reply("An error occurred.")
        return False
