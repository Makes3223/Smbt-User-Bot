import time
import asyncio
from pyrogram import Client

print ("select language:")
lang = input ("en, ua or ru: ")

if lang == "":
    print("Error!!!")
    
elif lang == "en":
    text_first = "Your api_id and api_hash in https://my.telegram.org/"

    text_api = "enter you api_id: $ "
    text_hash = "enter you api_hash: $ "

    text_app = "me", "Greetings from **@MacsimBlin**, now you can have fun!"
    text_app_second = "me", "I congratulate you on the installation of the bot, to see the commands, write '.help'"

    text_end = "great, now go to Favorites and read commands, or write a command .moduls or .m"

elif lang == "ua":
    text_first = "Ваш api_id та api_hash у https://my.telegram.org/"
    text_api = "введіть api_id: $ "
    text_hash = "введіть api_hash: $ "

    text_app = "me", "Вітання від **@MacsimBlin**, тепер ви можете веселитися!"
    text_app_second = "me", "Вітаю з установкою бота, для перегляду команд напишіть '.help'"

    text_end = "чудово, тепер перейдіть до вибраного та прочитайте команди або напишіть команду .moduls або .m"

elif lang == "ru":

    text_first = "Ваш api_id и api_hash в https://my.telegram.org/"

    text_api = "введите api_id: $ "
    text_hash = "введите api_hash: $ "

    text_app = "me", "Приветствие от **@MacsimBlin**, теперь вы можете веселиться!"

    text_app_second = "me", "Поздравляю с установкой бота, для просмотра команд напишите '.help'"

    text_end = "отлично, теперь перейдите к избранному и прочтите команды или напишите команду .moduls или .m"

print(text_first)
time.sleep(1.0)

api_id = input(text_api)
api_hash = input(text_hash)

if api_id == "":
    print("Telegram API_ID error!")
elif api_hash == "":
    print("Telegram API_HASH error!")
else:
    async def main():
        async with Client("my_account", api_id, api_hash) as app:
            await app.send_message(text_app)

            time.sleep(0.5)
            await app.send_message(text_app_second)

    asyncio.run(main())

    print(text_end)