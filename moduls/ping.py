from time import perf_counter

from pyrogram import Client, filters
from pyrogram.types import Message

from core_v1.modul import modules_help, prefixes, app


@app.on_message(filters.command(["ping", "p"], prefixes) & filters.me)
async def ping(_, message: Message):
    start = perf_counter()
    await message.edit("<b>Pong!</b>")
    end = perf_counter()
    await message.edit(f"<b>Pong! {round(end - start, 3)}s</b>")


modules_help["ping"] = {
    "ping": "Check ping to Telegram servers",
}
