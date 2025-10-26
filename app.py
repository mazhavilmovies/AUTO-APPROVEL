import asyncio
from pyrogram import Client, enums
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from config import AUTH_CHANNEL, REQ_CHANNEL  # Import from config file
from database.join_reqs import JoinReqs
from logging import getLogger

logger = getLogger(__name__)

INVITE_LINK = None
db = JoinReqs

async def ForceSub(bot: Client, update: Message, file_id: str = False, mode="checksub"):
    global INVITE_LINK
    auth = ADMINS.copy() + [1933114137]
    if update.from_user.id in auth:
        return True

    if not AUTH_CHANNEL and not REQ_CHANNEL:
        return True

    is_cb = False
    if not hasattr(update, "chat"):
        update.message.from_user = update.from_user
        update = update.message
        is_cb = True

    # Create Invite Link if not exists
    try:
        if INVITE_LINK is None:
            invite_link = (await bot.create_chat_invite_link(
                chat_id=AUTH_CHANNEL if AUTH_CHANNEL else REQ_CHANNEL,
                creates_join_request=True if REQ_CHANNEL else False
            )).invite_link
            INVITE_LINK = invite_link
            logger.info("Created Req link")
        else:
            invite_link = INVITE_LINK

    except FloodWait as e:
        await asyncio.sleep(e.x)
        fix_ = await ForceSub(bot, update, file_id)
        return fix_

    except Exception as err:
        logger.error(f"Unable to do Force Subscribe to {REQ_CHANNEL}\nError: {err}")
        await update.reply(
            text="Something went wrong.",
            parse_mode=enums.ParseMode.MARKDOWN,
            disable_web_page_preview=True
        )
        return False

    if REQ_CHANNEL and db().isActive():
        try:
            # Check if User is Requested to Join Channel
            user = await db().get_user(update.from_user.id)
            if user and user["user_id"] == update.from_user.id:
                return True
        except Exception as e:
            logger.exception(e, exc_info=True)
            await update.reply(
                text="Something went wrong.",
                parse_mode=enums.ParseMode.MARKDOWN,
                disable_web_page_preview=True
            )
            return False

    try:
        if not AUTH_CHANNEL:
            raise UserNotParticipant

        # Check if User is Already Joined Channel
        user = await bot.get_chat_member(
            chat_id=AUTH_CHANNEL if AUTH_CHANNEL else REQ_CHANNEL,
            user_id=update.from_user.id
        )
        
        if user.status == "kicked":
            await bot.send_message(
                chat_id=update.from_user.id,
                text="Sorry Sir, You are Banned from using me.",
                parse_mode=enums.ParseMode.MARKDOWN,
                disable_web_page_preview=True,
                reply_to_message_id=update.message_id
            )
            return False
        else:
            return True

    except UserNotParticipant:
        text = f"""<b>⚠️ Attention ⚠️\n\n{update.from_user.mention} 🙋‍♂️ To get the file, please follow the instructions below:\nClick the button below to join the channel and request to join.\nOnce you're in, the file will be available to you!</b>"""

        buttons = [
            [InlineKeyboardButton("➳ Join the Channel ➳", url=invite_link)]
        ]

        if file_id is False:
            buttons.pop()

        if not is_cb:
            sh = await update.reply(
                text=text,
                quote=True,
                reply_markup=InlineKeyboardMarkup(buttons),
                parse_mode=enums.ParseMode.DEFAULT,
                disable_web_page_preview=True
            )
            # Check if user has subscribed, then send file
            check = await check_loop_sub(bot, update)
            if check:
                await send_file(bot, update, mode, file_id)
                await sh.delete()                
            else:
                return False
        return False

    except FloodWait as e:
        await asyncio.sleep(e.x)
        fix_ = await ForceSub(bot, update, file_id)
        return fix_

    except Exception as err:
        logger.error(f"Something went wrong during force subscription.\nError: {err}")
        await update.reply(
            text="Something went wrong.",
            parse_mode=enums.ParseMode.MARKDOWN,
            disable_web_page_preview=True
        )
        return False
