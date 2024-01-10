from pyrogram import filters 
 from pyrogram.types import Message 
  
 from StringGen import Anony 
 from StringGen.utils import add_served_user, keyboard 

 force_btn = InlineKeyboardMarkup([ 
     [InlineKeyboardButton(text="🍁ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ🍂", url="t.me/solotreee")], 
     [InlineKeyboardButton(text="〄╏ᴄʜᴀᴛ ɢᴘᴛ╏ᴀɪ🧞", url="t.me/Chatgptasking_bot")]]) 
  
 async def check_is_joined(message, Message, client):     
     try: 
         userid = message.from_user.id 
         user_name = message.from_user.first_name 
         status = await app.get_chat_member("solotreee", userid) 
         return True 
     except Exception: 
         await message.reply_text(f'**🚧 ғɪʀsᴛ ᴊᴏɪɴ ᴛʜᴇ ʙᴏᴛ ᴄʜᴀɴɴᴇʟ ⚠️**\n┉───┈┈╌╍╌┄┈───┉┉───┈┈╌\n⌯︙**W⃟ᴇʟᴄᴏᴍᴇ :[{message.from_user.first_name}](tg://user?id={message.from_user.id})**\n⌯︙🏝️ **ʙᴏᴛ ᴄʜᴀɴɴᴇʟ :** [S⃟ᴏʟᴏ ᴛʀᴇᴇ](https://t.me/solotreee)\n┉───┈┈╌╍╌┄┈───┉┉───┈┈╌',reply_markup=force_btn,parse_mode="markdown",disable_web_page_preview=False) 
         return False 
  
 @Anony.on_message(filters.command("start") & filters.private & filters.incoming) 
 async def f_start(_, message: Message): 
     await message.reply_text( 
         text=f"ʜᴇʏ {message.from_user.first_name},\n\n๏ ᴛʜɪs ɪs {Anony.mention},\nAɴ ᴏᴘᴇɴ sᴏᴜʀᴄᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ, ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.", 
         reply_markup=keyboard, 
         disable_web_page_preview=True, 
     ) 
     await add_served_user(message.from_user.id)