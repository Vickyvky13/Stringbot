from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from StringGen import Anony
from StringGen.utils import add_served_user, keyboard

# Your InlineKeyboardMarkup for force subscription
force_btn = InlineKeyboardMarkup([
    [InlineKeyboardButton(text="🍁ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ🍂", url="t.me/solotreee")],
    [InlineKeyboardButton(text="〄╏ᴄʜᴀᴛ ɢᴘᴛ╏ᴀɪ🧞", url="t.me/Chatgptasking_bot")]
])

# Function to check if user has joined specific channels
async def check_is_joined(message, client):
    try:
        # Extract user information
        userid = message.from_user.id
        user_name = message.from_user.first_name
        
        # Check membership status in "solotreee" channel
        status_solotreee = await client.get_chat_member("solotreee", userid)
        
        # Check membership status in "Chatgptasking_bot" channel
        status_chatgpt = await client.get_chat_member("Chatgptasking_bot", userid)
        
        # Check if the user is a member of both channels
        if status_solotreee.status == "member" and status_chatgpt.status == "member":
            return True
        else:
            await message.reply_text(
                f'**🚧 ғɪʀsᴛ ᴊᴏɪɴ ᴛʜᴇ ʙᴏᴛ ᴄʜᴀɴɴᴇʟ ⚠️**\n'
                f'┉───┈┈╌╍╌┄┈───┉┉───┈┈╌\n'
                f'⌯︙**W⃟ᴇʟᴄᴏᴍᴇ :[{user_name}](tg://user?id={userid})**\n'
                f'⌯︙🏝️ **ʙᴏᴛ ᴄʜᴀɴɴᴇʟ :** [S⃟ᴏʟᴏ ᴛʀᴇᴇ](https://t.me/solotreee)\n'
                f'┉───┈┈╌╍╌┄┈───┉┉───┈┈╌',
                reply_markup=force_btn,
                parse_mode="markdown",
                disable_web_page_preview=False
            )
            return False
    except Exception as e:
        # Print the exception for debugging
        print(f"Exception in checking subscription: {e}")
        await message.reply_text(f'An error occurred while checking your subscription status: {e}')
        return False

# Handle /start command in private chat
@Anony.on_message(filters.command("start") & filters.private & filters.incoming)
async def f_start(_, message: Message):
    await message.reply_text(
        text=f"ʜᴇʏ {message.from_user.first_name},\n\n๏ ᴛʜɪs ɪs {Anony.mention},\nAɴ ᴏᴘᴇɴ sᴏᴜʀᴄᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ, ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.",
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )
    await add_served_user(message.from_user.id)
