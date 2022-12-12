import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message
from core_v1.modul import prefixes, app, modules_help

@app.on_message(filters.command("call", prefixes) & filters.me)
async def cell(client: Client, message: Message):

    animation_interval = 3
    animation_ttl = range(0, 18)
    await message.edit_text("Calling Pavel Durov (ceo of telegram)......")
    animation_chars = [
        "<b>Connecting To Telegram Headquarters...</b>",
        "<b>Call Connected.</b>",
        "<b>Telegram: Hello This is Telegram HQ. Who is this?</b>",
        f"<b>Me: Yo this is Dragon ,Please Connect me to my lil bro,Pavel Durov </b>",
        "<b>User Authorised.</b>",
        "<b>Calling Shivamani </b>  <code>At +916969696969</code>",
        "<b>Private  Call Connected...</b>",
        "<b>Me: Hello Sir, Please Ban This Telegram Account.</b>",
        "<b>Shivamani : May I Know Who Is This?</b>",
        f"<b>Me: Yo Brah, I Am Dragon</b>",
        "<b>Shivamani : OMG!!! Long time no see, Wassup cat...\nI'll Make Sure That Guy Account Will Get Blocked Within 24Hrs.</b>",
        "<b>Me: Thanks, See You Later Brah.</b>",
        "<b>Shivamani : Please Don't Thank Brah, Telegram Is Our's. Just Gimme A Call When You Become Free.</b>",
        "<b>Me: Is There Any Issue/Emergency???</b>",
        "<b>Shivamani : Yes Sur, There Is A Bug In Telegram v69.6.9.\nI Am Not Able To Fix It. If Possible, Please Help Fix The Bug.</b>",
        "<b>Me: Send Me The App On My Telegram Account, I Will Fix The Bug & Send You.</b>",
        "<b>Shivamani : Sure Sur \nTC Bye Bye :)</b>",
        "<b>Private Call Disconnected.</b>",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit_text(animation_chars[i % 18])

modules_help["call"] = {
    "call": "call to durov"
}