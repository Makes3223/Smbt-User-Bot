import asyncio

from collections import deque
from pyrogram import Client, filters
from pyrogram.types import Message
from core_v1.modul import prefixes, app, modules_help

@app.on_message(filters.command("stars", prefixes) & filters.me)
async def stars(client: Client, message: Message):
    deq = deque(list("🦋✨🦋✨🦋✨‍"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await message.edit_text("".join(deq))
        deq.rotate(1)

modules_help["stars"] = {
    "stars": "Fun animation try yourself to know more"
}