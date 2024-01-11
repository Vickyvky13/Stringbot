from pyrogram import filters
from pyrogram.types import Message

from StringGen import Anony
from StringGen.utils import add_served_user, keyboard

@Anony.on_message(filters.command("start") & filters.private & filters.incoming)
async def f_start(_, message: Message):
    await message.reply_text(
        text=f"⌯ ʜᴇʏ {message.from_user.mention} 🥀\n\n⌯ ꜰʀɪꜱᴛ ᴊᴏɪɴ [ᴄʜᴀɴɴᴇʟ](https://t.me/solotreee/141) & [ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ](https://t.me/solotree_support).\n\n⌯ ᴛʜɪꜱ ɪꜱ {Anony.mention}, ᴀᴅᴠᴀɴᴄᴇ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ʙᴏᴛ ɴᴏ ɴᴇᴇᴅᴇᴅ ꜰᴏʀ ||<b><u>ᴀᴘᴋ_ɪᴅ</u></b>|| & ||<b><u>ᴀᴘɪ_ʜᴀꜱʜ</b></u>|| | ᴘᴜᴛ ʏᴏᴜʀ ᴍᴏʙɪʟᴇ ɴᴜᴍʙᴇʀ ɢᴇᴛ ʏᴏᴜʀ ꜱᴇꜱꜱɪᴏɴ ꜰᴀꜱᴛʟʏ.",
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )
    await add_served_user(message.from_user.id)
