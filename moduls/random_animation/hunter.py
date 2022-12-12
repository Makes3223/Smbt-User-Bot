import random
from time import sleep

from pyrogram import Client, filters
from pyrogram.types import Message
from core_v1.modul import prefixes, app, modules_help


@app.on_message(filters.command("hunter", prefixes) & filters.me)
def betalove(_, msg):
    time = 0.6
    for i in range(1):
        msg.edit(f"<b>🔪 You were ordered to kill.</b>")  # red
        sleep(3)
        msg.edit(f"<b>👀 You have a couple of seconds to hide.</b>")  # orange
        sleep(2)
        msg.edit(f"<b>⏳ [ 5s ]</b>")  # orange
        sleep(time)
        msg.edit(f"<b>⌛ [ 4s ]</b>")  # red
        sleep(time)
        msg.edit(f"<b>⏳ [ 3s ]</b>")  # orange
        sleep(time)
        msg.edit(f"<b>⌛ [ 2s ]</b>")  # red
        sleep(time)
        msg.edit(f"<b>⏳ [ 1s ]</b>")  # orange
        sleep(time)
        msg.edit(f"<b>🔪 The killer came looking for you, I hope you hid well.</b>")  # orange
        sleep(time)
        msg.edit(f"<b>👀 Search.</b>")  # orange
        sleep(time)
        msg.edit(f"<b>👀 Search..</b>")  # orange
        sleep(time)
        msg.edit(f"<b>👀 Search...</b>")  # orange
        sleep(time)
        msg.edit(f"<b>👀 Search.</b>")  # orange
        sleep(time)
        msg.edit(f"<b>👀 Search..</b>")
        sleep(time)
        msg.edit(f"<b>👀 Search...</b>")
        sleep(time)
        msg.edit(random.choice(kill))

kill = ["<b>The killer found you, unfortunately you hid badly and was killed.</b>", "<b>The killer didn't find you, you hid very well.</b>"]

modules_help["hunter"] = {
    "hunter": "Check your luck",
}