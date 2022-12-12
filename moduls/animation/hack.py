import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message
from core_v1.modul import prefixes, app, modules_help

@app.on_message(filters.command("hack", prefixes) & filters.me)
async def ding(client: Client, message: Message):
    animation_interval = 0.9
    animation_ttl = range(0, 14)
    animation_chars = [
    "<b>HACKING YOUR PHONE</b>", 
    "<b><i>Loading...</i></b>",
    "10%  █▒▒▒▒▒▒▒▒▒▒▒▒",
    "30%  ███▒▒▒▒▒▒▒▒▒▒",
    "50%  █████▒▒▒▒▒▒▒▒",
    "66%  ██████▒▒▒▒▒▒▒",
    "79%  ████████▒▒▒▒▒",
    "84%  █████████▒▒▒▒",
    "89%  ██████████▒▒▒",
    "95%  ████████████▒",
    "99%  █████████████",
    "100% █████████████",
    "<b> YOUR PHONE HACKED </b>",
    "<b><i>$toner:  YOUR PHONE HAS BEEN HACKED, IF YOU DON'T WRITE @MacsimBlin, YOUR SYSTEM WILL BE DESTROID.</i></b>",
]

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit_text(animation_chars[i % 14])

modules_help["hack"] = {
    "hack": "chack YOUR PHONE"
}