from pyrogram import Client, filters
from pyrogram.types import Message
from core_v1.modul import prefixes, app, modules_help
from core_v1.script import format_exc

@app.on_message(filters.command(["block"], prefixes) & filters.me)
async def block_True(client: Client, message: Message):
    try:
        user_id = (
            message.command[1]
            if len(message.command) > 1
            else message.reply_to_message.from_user.id
        )
        await client.block_user(user_id)
        await message.edit(
            f"<b>🤡 The <a href='tg://user?id={user_id}'>user</a> is now blacklisted!</b>"
        )
    except Exception as e:
        await message.edit(format_exc(e))


@app.on_message(filters.command(["unblock"], prefixes) & filters.me)
async def unblock(client: Client, message: Message):
    try:
        user_id = (
            message.command[1]
            if len(message.command) > 1
            else message.reply_to_message.from_user.id
        )
        await client.unblock_user(user_id)
        await message.edit(
            f"<b>☺️ <a href='tg://user?id={user_id}'>User</a> removed from the blacklist!</b>"
        )
    except Exception as e:
        await message.edit(format_exc(e))


modules_help["blacklist"] = {
    "block [id|reply]*": "block user",
    "unblock [id|reply]*": "unblock user",
}