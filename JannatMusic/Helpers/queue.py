from JannatMusic import jannatdb


async def put(
    chat_id,
    title,
    duration,
    videoid,
    file_path,
    ruser,
    user_id,
):
    put_j = {
        "title": title,
        "duration": duration,
        "file_path": file_path,
        "videoid": videoid,
        "req": ruser,
        "user_id": user_id,
    }
    get = jannatdb.get(chat_id)
    if get:
        jannatdb[chat_id].append(put_j)
    else:
        jannatdb[chat_id] = []
        jannatdb[chat_id].append(put_j)
