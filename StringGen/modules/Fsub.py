from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from StringGen import Anony
import config
import random

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
                    photo=random.choice(["https://graph.org/file/77acdef881be3189ba87d.jpg", "https://telegra.ph/file/d43451736c2efb5a1c9bf.jpg", "https://telegra.ph/file/c1b2aa1904b21f0ff5a45.jpg", "https://telegra.ph/file/707ea2fb3882e409e8977.jpg", "https://telegra.ph/file/b6fe258f7ccf99bd1de07.jpg", "https://telegra.ph/file/3aed9117aa02ac59b3ba9.jpg", "https://telegra.ph/file/abe6b52efd6980f6c2d55.jpg", "https://telegra.ph/file/fa107b7f37e0c619b45cf.jpg", "https://telegra.ph/file/ab47c2266bb9fbdc82468.jpg", "https://telegra.ph/file/f58c18c34dfde407c1fbd.jpg", "https://telegra.ph/file/1a11733bb418369bc11a1.jpg", "https://telegra.ph/file/64dbed83bfb0c78e66f6a.jpg", "https://telegra.ph/file/a7db113e67cb150de9a2b.jpg", "https://telegra.ph/file/86a703358683ffed650e0.jpg", "https://telegra.ph/file/b8a99bc5cb08abfaa1d61.jpg", "https://telegra.ph/file/1e7a0a4be2df05550a65b.jpg", "https://telegra.ph/file/2c16f898ad10798d4856c.jpg", "https://telegra.ph/file/1a3275c7c5a7be58e098d.jpg", "https://te.legra.ph/file/0fb1c625e4c1661ec2fec.jpg"]),
                    caption=f"⌯ ʜᴇʏ {msg.from_user.mention} 🥀\n\n⌯ ꜰʀɪꜱᴛ ᴊᴏɪɴ [ᴄʜᴀɴɴᴇʟ](https://t.me/solotreee/141) & [ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ](https://t.me/solotree_support).\n\n⌯ ᴛʜɪꜱ ᴀᴅᴠᴀɴᴄᴇ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ʙᴏᴛ ɴᴏ ɴᴇᴇᴅᴇᴅ ꜰᴏʀ <b><u>ᴀᴘᴋ_ɪᴅ</u></b> & <b><u>ᴀᴘɪ_ʜᴀꜱʜ</b></u>, ᴘᴜᴛ ʏᴏᴜʀ ᴍᴏʙɪʟᴇ ɴᴜᴍʙᴇʀ ɢᴇᴛ ʏᴏᴜʀ ꜱᴇꜱꜱɪᴏɴ ꜰᴀꜱᴛʟʏ❄️",
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton(u"‹ ᴊᴏɪɴ ғɪʀsᴛ ›", url=link)],
                        [InlineKeyboardButton(u"ʀᴇғʀᴇsн", url=config.RESTART_BOT)]
                    ]),
                    has_spoiler=True,  # Add this line
                    protect_content=True  # Add this line
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"Promote the admin bot in the channel: @solotreee!")
