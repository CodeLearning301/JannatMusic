from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "990"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/6195e56b47a1042e59c3e.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/b7e66d431a9ac55342712.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+hTILedqSqOo4MzI1")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/JannatUpdate")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))


FAILED = "https://telegra.ph/file/c1311d536ba91323c4c12.jpg"
