import asyncio
from pyrogram import Client

lang_dict = {
"en": {
"text_first": "Your api_id and api_hash in https://my.telegram.org/",
"text_api": "Enter your api_id: ",
"text_hash": "Enter your api_hash: ",
"text_app": "Greetings from @MacsimBlin, now you can have fun!",
"text_app_second": "I congratulate you on the installation of the bot, to see the commands, write '.help'",
"text_end": "Great, now go to Favorites and read commands, or write a command .moduls or .m",
"text_phone": "Enter your phone_number: "
},
"ua": {
"text_first": "Ваш api_id та api_hash у https://my.telegram.org/",
"text_api": "Введіть api_id: ",
"text_hash": "Введіть api_hash: ",
"text_app": "Вітання від @MacsimBlin, тепер ви можете веселитися!",
"text_app_second": "Вітаю з установкою бота, для перегляду команд напишіть '.help'",
"text_end": "Чудово, тепер перейдіть до вибраного та прочитайте команди або напишіть команду .moduls або .m",
"text_phone": "Введіть свій номер телефону: "
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
    text_phone = lang_dict[lang]["text_phone"]

print(text_first)

apiid = input(text_api)
apihash = input(text_hash)
phone = input(text_phone)

if apiid == "" or apihash == "":
    print("Telegram API_ID/API_HASH error!")
else:
    async def main():
        async with Client("my_account", api_id = apiid, api_hash = apihash, phone_number = phone) as app:
            await app.send_message("me", text_app)
            await asyncio.sleep(0.5)
            await app.send_message("me", text_app_second)
asyncio.run(main())
print(text_end)