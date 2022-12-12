import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message
from core_v1.modul import prefixes, app, modules_help

@app.on_message(filters.command("charge", prefixes) & filters.me)
async def timer_blankx(client: Client, message: Message):
    txt = (
        message.text[10:]
        + "\n\n<b>Tesla Wireless Charging (beta) Started...\nDevice Detected: Apple iPad 13\nBattery Percentage:</b> "
    )
    j = 10
    k = j
    for j in range(j):
        await message.edit_text(txt + str(k))
        k = k + 10
        await asyncio.sleep(1)
    await asyncio.sleep(1)
    await message.edit_text(
        "<b>Tesla Wireless Charging (beta) Completed...\nDevice Detected: Apple iPad 13\nBattery Percentage:</b> 100%"
    )

modules_help["charge"] = {
    "charge": "Apple iPad charging animation"
}