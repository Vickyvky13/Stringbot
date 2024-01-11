from pyrogram import Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import MessageDeleteForbidden
import asyncio

from config import SUPPORT_CHAT, COOWNER 
import time

async def delete_message_after_2min(client, message):
    time.sleep(120)  # Wait for 2 minutes
    try:
        await message.delete()
    except MessageDeleteForbidden:
        # Handle case where the bot doesn't have permission to delete messages
        pass

# Assuming you have an async function to handle your inline queries
@Client.on_callback_query()
async def on_callback_query(client, query):
    # Your existing callback query handling logic here

    # Add the delete_message_after_2min task
    asyncio.ensure_future(delete_message_after_2min(client, query.message))

# Your existing code for inline keyboards
keyboard = InlineKeyboardMarkup([
    [InlineKeyboardButton(text="ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ", callback_data="gensession")],
    [
        InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", url=SUPPORT_CHAT),
        InlineKeyboardButton(
            text="ᴄʜᴀɴɴᴇʟ", url="https://t.me/solotreee"
        ),
    ],
        [InlineKeyboardButton(text="ᴅᴇᴠᴇʟᴏᴘᴇʀ", user_id=config.COOWNER)],
])

gen_key = InlineKeyboardMarkup([
    [
        InlineKeyboardButton(text="ᴩʏʀᴏɢʀᴀᴍ v1", callback_data="pyrogram1"),
        InlineKeyboardButton(text="ᴩʏʀᴏɢʀᴀᴍ v2", callback_data="pyrogram"),
    ],
    [InlineKeyboardButton(text="ᴛᴇʟᴇᴛʜᴏɴ", callback_data="telethon")],
])

retry_key = InlineKeyboardMarkup([[InlineKeyboardButton(text="ᴛʀʏ ᴀɢᴀɪɴ", callback_data="gensession")]])
