import time
import asyncio
from pyrogram import Client

print("Your api_id and api_hash in https://my.telegram.org/")
time.sleep(1.0)

api_id = input("enter you api_id: $ ")
api_hash = input("enter you api_hash: $ ")

async def main():
    async with Client("my_account", api_id, api_hash) as app:
        await app.send_message("me", "Greetings from **@MacsimBlin**, now you can have fun!")

        time.sleep(0.5)
        await app.send_message("me", "I congratulate you on the installation of the bot, to see the commands, write '.help'")

asyncio.run(main())

print("great, now go to Favorites and read commands, or write a command .moduls or .m")