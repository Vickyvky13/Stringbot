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
COOWNER_ID = int(getenv("COOWNER_ID", 5903371502))

so = ["https://telegra.ph/file/1b1e1359c2e794f07ce75.mp4", "https://telegra.ph/file/f92fe8b57929dc37f2592.mp4"]

SOURCE_IMG_URL = random.choice(so)

load_dotenv()