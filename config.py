from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN")
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

OWNER_ID = int(getenv("OWNER_ID", 1356469075))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/solotree_support")
MUST_JOIN= getenv("MUST_JOIN","https://t.me/solotreee")
RESTART_BOT= getenv("RESTART_BOT", "https://t.me/Solostringsession_bot?start=help")
COOWNER_ID = int(getenv("COOWNER_ID", "5903371502"))