import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message
from core_v1.modul import prefixes, app, modules_help

@app.on_message(filters.command("kill", prefixes) & filters.me)
async def kill(client: Client, message: Message):
    animation_interval = 0.3
    animation_ttl = range(0, 103)
    animation_chars = [
        "Ｆｉｉｉｉｉｒｅ",
        "(　･ิω･ิ)︻デ═一-->",
        "------>;(^。^)ノ",
        "(￣ー￣) DED",
        "<b>Target killed successfully (°̥̥̥̥̥̥̥̥•̀.̫•́°̥̥̥̥̥̥̥)</b>",
    ]

    await message.edit_text("You're goonnaa diieeeee!")
    await asyncio.sleep(3)
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit_text(animation_chars[i % 6])

modules_help["kill"] = {
    "kill": "fireee animation = target killed ~_- "
}