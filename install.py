import asyncio
from pyrogram import Client

lang_dict = {
"en": {
"text_first": "Your api_id and api_hash in https://my.telegram.org/",
"text_api": "Enter your api_id: ",
"text_hash": "Enter your api_hash: ",
"text_app": "Greetings from @MacsimBlin, now you can have fun!",
"text_app_second": "I congratulate you on the installation of the bot, to see the commands, write '.help'",
"text_end": "Great, now go to Favorites and read commands, or write a command .moduls or .m"
},
"ua": {
"text_first": "Ваш api_id та api_hash у https://my.telegram.org/",
"text_api": "Введіть api_id: ",
"text_hash": "Введіть api_hash: ",
"text_app": "Вітання від @MacsimBlin, тепер ви можете веселитися!",
"text_app_second": "Вітаю з установкою бота, для перегляду команд напишіть '.help'",
"text_end": "Чудово, тепер перейдіть до вибраного та прочитайте команди або напишіть команду .moduls або .m"
},
"ru": {
"text_first": "Ваш api_id и api_hash в https://my.telegram.org/",
"text_api": "Введите api_id: ",
"text_hash": "Введите api_hash: ",
"text_app": "Приветствие от @MacsimBlin, теперь вы можете веселиться!",
"text_app_second": "Поздравляю с установкой бота, для просмотра команд напишите '.help'",
"text_end": "отлично, теперь перейдите к избранному и прочтите команды или напишите команду .moduls или .m"
}
}

print ("select language:")
lang = input ("en, ua or ru: ")

if lang not in lang_dict:
    print("Error!!!")
else:
    text_first = lang_dict[lang]["text_first"]
    text_api = lang_dict[lang]["text_api"]
    text_hash = lang_dict[lang]["text_hash"]
    text_app = lang_dict[lang]["text_app"]
    text_app_second = lang_dict[lang]["text_app_second"]
    text_end = lang_dict[lang]["text_end"]

print(text_first)

api_id = input(text_api)
api_hash = input(text_hash)

if api_id == "" or api_hash == "":
    print("Telegram API_ID/API_HASH error!")
else:
    async def main():
        async with Client("my_account", api_id, api_hash) as app:
            await app.send_message("me", text_app)
            await asyncio.sleep(0.5)
            await app.send_message("me", text_app_second)
asyncio.run(main())
print(text_end)