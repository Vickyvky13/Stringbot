from pyrogram import filters
from pyrogram.types import Message

from StringGen import Anony
from StringGen.utils import add_served_user, keyboard

# Function to check if the user is a member of the channel
async def is_channel_member(user_id):
    # Add your logic here to check if the user is a member of the channel
    # You can use the pyrogram method to check channel membership
    channel_id = "-1001979606304"  # Replace with your channel ID
    try:
        member = await Anony.get_chat_member(chat_id=channel_id, user_id=user_id)
        return member.status in ["member", "administrator", "creator"]
    except Exception as e:
        print(f"Error checking channel membership: {e}")
        return False


@Anony.on_message(filters.command("start") & filters.private & filters.incoming)
async def f_start(_, message: Message):
    user_id = message.from_user.id
    if await is_channel_member(user_id):
        await message.reply_text(
            text=f"ʜᴇʏ {message.from_user.first_name},\n\n๏ ᴛʜɪs ɪs {Anony.mention},\nAɴ ᴏᴘᴇɴ sᴏᴜʀᴄᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ, ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.",
            reply_markup=keyboard,
            disable_web_page_preview=True,
        )
        await add_served_user(user_id)
    else:
        channel_link = "https://t.me/solotreee"  # Replace with your channel link
        await message.reply_text(
            f"You need to join our channel to use this bot.\nJoin here: {channel_link}"
        )