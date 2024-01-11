from pyrogram import Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaVideo
from pyrogram.errors import MessageDeleteForbidden
import asyncio
import random
from config import SUPPORT_CHAT
from pyrogram import filters

async def delete_message_after_2min(client, message):
    time.sleep(120)
    try:
        await message.delete()
    except MessageDeleteForbidden:
        pass

@Client.on_callback_query()
async def on_callback_query(client, query):
    asyncio.ensure_future(delete_message_after_2min(client, query.message))

keyboard = InlineKeyboardMarkup([
    [InlineKeyboardButton(text="ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ", callback_data="gensession")],
    [
        InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", url=SUPPORT_CHAT),
        InlineKeyboardButton(
            text="ᴄʜᴀɴɴᴇʟ", callback_data="sour"
        ),
    ],
    [InlineKeyboardButton(text="ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/ibuttu")],
])

gen_key = InlineKeyboardMarkup([
    [
        InlineKeyboardButton(text="ᴩʏʀᴏɢʀᴀᴍ v1", callback_data="pyrogram1"),
        InlineKeyboardButton(text="ᴩʏʀᴏɢʀᴀᴍ v2", callback_data="pyrogram"),
    ],
    [InlineKeyboardButton(text="ᴛᴇʟᴇᴛʜᴏɴ", callback_data="telethon")],
])

so = ["https://telegra.ph/file/1b1e1359c2e794f07ce75.mp4", "https://telegra.ph/file/f92fe8b57929dc37f2592.mp4"]

@Client.on_callback_query(filters.regex("sour"))
async def sour(_, query: CallbackQuery):
    ur = random.choice(so)
    await query.edit_message_media(
        media=InputMediaVideo(ur, has_spoiler=True),
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="settingsback_helper")]])
    )

retry_key = InlineKeyboardMarkup([[InlineKeyboardButton(text="ᴛʀʏ ᴀɢᴀɪɴ", callback_data="gensession")]])
