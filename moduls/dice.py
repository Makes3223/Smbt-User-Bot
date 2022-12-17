from pyrogram import Client, filters
from pyrogram.types import Message
from core_v1.modul import prefixes, app, modules_help
from core_v1.script import format_exc
import asyncio


@app.on_message(filters.command("dice", prefixes) & filters.me)
async def dice_text(client: Client, message: Message):
    try:
        value = int(message.command[1])
        if value not in range(1, 7):
            raise AssertionError
    except (ValueError, IndexError, AssertionError):
        return await message.edit("<b>Invalid value</b>")

    try:
        message.dice = type("bruh", (), {"value": 0})()
        while message.dice.value != value:
            message = (await asyncio.gather(
                message.delete(),
                client.send_dice(message.chat.id)
            ))[1]
    except Exception as e:
        await message.edit(format_exc(e))


modules_help["dice"] = {
    "dice [1-6]*": "Generate dice with specified value. Works only in groups"
}
