from JannatMusic import jannatdb
from JannatMusic.Helpers import remove_active_chat


async def _clear_(chat_id):
    try:
        jannatdb[chat_id] = []
        await remove_active_chat(chat_id)
    except:
        return
