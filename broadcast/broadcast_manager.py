from pyrogram import Client
from pyrogram.errors import FloodWait

async def broadcast_message(client: Client, message: str, user_ids: list):
    try:
        for user_id in user_ids:
            await client.send_message(user_id, message)
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return await broadcast_message(client, message, user_ids)
    except Exception as err:
        print(f"Broadcast error: {err}")
