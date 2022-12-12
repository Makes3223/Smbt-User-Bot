import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message
from core_v1.modul import prefixes, app, modules_help


@app.on_message(filters.command(["leave_chat", "lc"], prefixes) & filters.me)
async def leave_chat(_, message: Message):
    if message.chat.type != "private":
        await message.edit("<b>Goodbye...</b>")
        await asyncio.sleep(3)
        await message.chat.leave()
    else:
        await message.edit("<b>Not supported in private chats</b>")


modules_help["leave"] = {
    "leave_chat": "Quit chat",
}
