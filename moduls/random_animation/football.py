import random

from time import sleep
from pyrogram import Client, filters
from pyrogram.types import Message
from core_v1.modul import prefixes, app, modules_help


@app.on_message(filters.command("foot", prefixes) & filters.me)
def betalove(_, msg):
    time = 0.9
    for i in range(1):
        msg.edit(f"<b>⚽️ You entered the football field, you have to score a penalty to win.</b>")  # red
        sleep(2)
        msg.edit(f"<b>⏳ Preparing for the game.</b>")  # orange
        sleep(2)
        msg.edit(f"<b>⌛ Preparing for the game..</b>")  # orange
        sleep(time)
        msg.edit(f"<b>⏳ Preparing for the game...</b>")  # red
        sleep(time)
        msg.edit(f"<b>⚽ Hit.</b>")  # orange
        sleep(time)
        msg.edit(f"<b>⚽ Hit..</b>")  # red
        sleep(time)
        msg.edit(f"<b>⚽ Hit...</b>")  # orange
        sleep(time)
        msg.edit(random.choice(foot))
        sleep(5)

foot = ["<b>❌ Unfortunately you lost..</b>", "<b>✅ You scored a goal and won the game!</b>"]

modules_help["foot"] = {
    "foot": "Check your luck",
}