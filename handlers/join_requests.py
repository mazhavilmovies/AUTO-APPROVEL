from pyrogram import Client, InlineKeyboardButton, InlineKeyboardMarkup
from database.join_reqs import JoinReqs
from datetime import datetime

join_reqs = JoinReqs()

@Client.on_chat_join_request()
async def accept_request(client, r):
    try:
        # Send a welcome message and approve join request
        rm = InlineKeyboardMarkup([
            [InlineKeyboardButton('🎉 Add Me To Your Groups 🎉', url=f'http://t.me/{bot_username}?startgroup=true')]
        ])
        welcome_text = f"Hello {r.from_user.first_name}, welcome to {r.chat.title}!"
        await client.send_photo(
            r.from_user.id,
            "https://i.ibb.co/Q9Hm3Dg/175540848.jpg",
            welcome_text,
            reply_markup=rm
        )
        await r.approve()
        join_reqs.add_request(r.from_user.id, r.chat.id)
        logger.info(f"Request approved for {r.from_user.username} in {r.chat.title}")
    except Exception as e:
        logger.error(f"Error while processing join request: {e}")
