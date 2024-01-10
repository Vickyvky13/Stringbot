# must_join.py

from StringGen import Anony, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden

def combined_filter(message):
    # Implement the logic to combine incoming and private filters
    return filters.incoming(message) and filters.private(message)

@Anony.on_message(combined_filter, group=-1)
async def must_join_channel(bot, msg):
    MUST_JOIN = "your_channel_or_group_here"  # Replace this with your channel or group ID
    
    if not MUST_JOIN:  # Not compulsory
        return
    
    try:
        try:
            await bot.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await bot.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f"🚧 ғɪʀsᴛ ᴊᴏɪɴ ᴛʜᴇ ʙᴏᴛ ᴄʜᴀɴɴᴇʟ ⚠️\n┉───┈┈╌╍╌┄┈───┉┉───┈┈╌\n⌯︙🏝️ **ʙᴏᴛ ᴄʜᴀɴɴᴇʟ :** ||[S⃟ᴏʟᴏ ᴛʀᴇᴇ]({link})||\n┉───┈┈╌╍╌┄┈───┉┉───┈┈╌\nᴛᴏ ᴜsᴇ ᴍᴇ. Aғᴛᴇʀ ᴊᴏɪɴɪɴɢ ᴛʀʏ ᴀɢᴀɪɴ !!",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("✨ Join Channel ✨", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"I'm not admin in the MUST_JOIN chat : {MUST_JOIN} !")
