from pyrogram import Client 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
from pyrogram.errors import MessageDeleteForbidden 
import asyncio

from config import SUPPORT_CHAT 
import time 
import config 

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
    [InlineKeyboardButton(text="ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/ibuttu")],  # Update with your developer's username
]) 

gen_key = InlineKeyboardMarkup([ 
    [ 
        InlineKeyboardButton(text="ᴩʏʀᴏɢʀᴀᴍ v1", callback_data="pyrogram1"), 
        InlineKeyboardButton(text="ᴩʏʀᴏɢʀᴀᴍ v2", callback_data="pyrogram"), 
    ], 
    [InlineKeyboardButton(text="ᴛᴇʟᴇᴛʜᴏɴ", callback_data="telethon")], 
]) 
so=["https://telegra.ph/file/1b1e1359c2e794f07ce75.mp4", "https://telegra.ph/file/f92fe8b57929dc37f2592.mp4"] 
 @app.on_callback_query(filters.regex("sour")) 
 async def sour(_, query: CallbackQuery): 
     ur=random.choice(so) 
     await query.edit_message_media( 
         media=InputMediaVideo(ur, has_spoiler=True), 
         reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="settingsback_helper")]]), 
     )
retry_key = InlineKeyboardMarkup([[InlineKeyboardButton(text="ᴛʀʏ ᴀɢᴀɪɴ", callback_data="gensession")]])
