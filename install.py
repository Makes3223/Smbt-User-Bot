import time
import asyncio
from pyrogram import Client

print ("select language:")
lang = input ("ua, ru or en: ")

if lang == 'en':

    print("Your api_id and api_hash in https://my.telegram.org/")
    time.sleep(1.0)

    api_id_en = input("enter you api_id: $ ")
    api_hash_en = input("enter you api_hash: $ ")

    async def main():
        async with Client("my_account", api_id_en, api_hash_en) as app:
            await app.send_message("me", "Greetings from **@MacsimBlin**, now you can have fun!")

            time.sleep(0.5)
            await app.send_message("me", "I congratulate you on the installation of the bot, to see the commands, write '.help'")

    asyncio.run(main())

    print("great, now go to Favorites and read commands, or write a command .moduls or .m")

elif lang == 'ua':
    
    print("Ваш api_id та api_hash у https://my.telegram.org/")
    time.sleep(1.0)

    api_id_ua = input("введіть api_id: $ ")
    api_hash_ua = input("введіть api_hash: $ ")

    async def main():
        async with Client("my_account", api_id_ua, api_hash_ua) as app:
            await app.send_message("me", "Вітання від **@MacsimBlin**, тепер ви можете веселитися!")

            time.sleep(0.5)
            await app.send_message("me", "Вітаю з установкою бота, для перегляду команд напишіть '.help'")

    asyncio.run(main())

    print("чудово, тепер перейдіть до вибраного та прочитайте команди або напишіть команду .moduls або .m")

elif lang == 'ru':

    print("Ваш api_id и api_hash в https://my.telegram.org/")
    time.sleep(1.0)

    api_id_ua = input("введите api_id: $ ")
    api_hash_ua = input("введите api_hash: $ ")

    async def main():
        async with Client("my_account", api_id_ua, api_hash_ua) as app:
            await app.send_message("me", "Приветствие от **@MacsimBlin**, теперь вы можете веселиться!")

            time.sleep(0.5)
            await app.send_message("me", "Поздравляю с установкой бота, для просмотра команд напишите '.help'")

    asyncio.run(main())

    print("отлично, теперь перейдите к избранному и прочтите команды или напишите команду .moduls или .m")
