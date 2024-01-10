from pyrogram import Client, filters 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message 
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden 
from StringGen import Anony 
  
@Anony.on_message(filters.incoming & filters.private, group=-1) 
async def must_join_channel(bot: Client, msg: Message): 
    if not "https://t.me/solotreee":  # Not compulsory 
        return 
    try: 
        try: 
            await bot.get_chat_member("solotreee", msg.from_user.id) 
        except UserNotParticipant: 
            if "https://t.me/solotreee".isalpha(): 
                link = "https://t.me/solotreee" 
            else: 
                chat_info = await bot.get_chat("solotreee") 
                link = chat_info.invite_link 
            try: 
                await bot.send_photo( 
                    chat_id=msg.chat.id, 
                    photo="https://graph.org/file/77acdef881be3189ba87d.jpg", 
                    caption=f"⌯︙🌳 W⃟ᴇʟᴄᴏᴍᴇ : {msg.from_user.mention}\n⌯︙🏝️ ʙᴏᴛ ᴄʜᴀɴɴᴇʟ @solotreee\n⌯︙🍃 ꜱᴜʙꜱᴄʀɪʙᴇ ᴛᴏ ᴊᴏɪɴ ㅤㅤㅤㅤㅤㅤㅤᴛʜᴇ ʙᴏᴛ ᴄʜᴀɴɴᴇʟ ᴘʟᴇᴀꜱᴇ!!.\n┉───┈┈╌╍╌┄┈───┉┉───┈┈╌", 
                    reply_markup=InlineKeyboardMarkup([ 
                        [InlineKeyboardButton(u"‹ Solo tree ›", url=link)],
                        [InlineKeyboardButton(u"Start Bot", url="https://t.me/Solostringsession_bot?start=help")]
                    ]) 
                ) 
                await msg.stop_propagation() 
            except ChatWriteForbidden: 
                pass 
    except ChatAdminRequired: 
        print(f"Promote the admin bot in the channel: @solotreee!")
