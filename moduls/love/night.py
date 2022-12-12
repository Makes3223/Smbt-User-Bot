import os
import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message
from core_v1.modul import prefixes, app, modules_help

@app.on_message(filters.command("night", prefixes) & filters.me)
async def stupid(client: Client, message: Message):
    animation_interval = 0.5
    animation_ttl = range(0, 14)
    await message.edit_text("<b>i love you</b>")
    text1 = [
        "<b>Good night bunny 💚</b>", 
        "<b>Good night sunshine 💛</b>",
        "<b>Goodnight kitten ❤</b>",
        "<b>Good night flower 💙</b>",
        "<b>Good night little angel 💜</b>",
        "<b>Good night princess 💓</b>",
        "<b>Good night beauty 💕</b>",
        "<b>Good night sweetie 💖</b>",
        "<b>Good night cute 💗</b> <b>Good night bead 💘</b>",
        "<b>I</b>",
        "<b>💚 you 💚</b>",
        "<b>💙 very  💙</b>",
        "<b>💛 strongly 💛</b>",
        "<b>💜 Love💜</b>",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await message.edit_text(text1[i % 14])

modules_help["night"] = {
    "night": "Surprise your significant other"
}