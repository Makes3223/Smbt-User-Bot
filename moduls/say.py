from pyrogram import Client, filters
from pyrogram.types import Message
from core_v1.modul import prefixes, app
from core_v1.modul import modules_help


@app.on_message(filters.command(["say", "s"], prefixes) & filters.me)
async def say(_, message: Message):
    if len(message.command) == 1:
        return
    command = " ".join(message.command[1:])
    await message.edit(f"<code>{command}</code>")


modules_help["say"] = {
    "say [command]*": "Send message that won't be interpreted by userbot",
}
