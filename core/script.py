import os
import sys
import asyncio
import subprocess
import importlib
import traceback

from pyrogram.types import Message
from pyrogram import Client, errors, types
from core.modul import modules_help, prefixes, requirements_list, app


def format_exc(e: Exception, hint: str = None):
    traceback.print_exc()
    if isinstance(e, errors.RPCError):
        return (
            f"<b>Telegram API error!</b>\n"
            f"<code>[{e.CODE} {e.ID or e.NAME}] - {e.MESSAGE}</code>"
        )
    else:
        if hint:
            hint_text = f"\n\n<b>Hint: {hint}</b>"
        else:
            hint_text = ""
        return (
            f"<b>Error!</b>\n" f"<code>{e.__class__.__name__}: {e}</code>" + hint_text
        )

def format_module_help(module_name: str):
    commands = modules_help[module_name]
  
    help_text = f"<b>Help for |{module_name}|\n\nUsage:</b>\n"
  
    for command, desc in commands.items():
        cmd = command.split(maxsplit=1)
        args = " <code>" + cmd[1] + "</code>" if len(cmd) > 1 else ""
        help_text += f"<code>{prefixes}{cmd[0]}</code>{args} — <i>{desc}</i>\n"
  
    return help_text
  
  
def format_small_module_help(module_name: str):
    commands = modules_help[module_name]
  
    help_text = f"<b>Help for |{module_name}|\n\nCommands list:\n"
    for command, desc in commands.items():
         cmd = command.split(maxsplit=1)
         args = " <code>" + cmd[1] + "</code>" if len(cmd) > 1 else ""
         help_text += f"<code>{prefixes}{cmd[0]}</code>{args}\n"
    help_text += f"\nGet full usage: <code>{prefixes}help {module_name}</code></b>"
  
    return help_text

def text(message: types.Message):
    return message.text if message.text else message.caption

def restart():
    os.execvp(sys.executable, [sys.executable, "main.py"])


def with_reply(func):
    async def wrapped(client: Client, message: types.Message):
        if not message.reply_to_message:
            await message.edit("<b>Reply to message is required</b>")
        else:
            return await func(client, message)

    return wrapped


async def interact_with(message: types.Message) -> types.Message:
    """
    Check history with bot and return bot's response
    Example:
    .. code-block:: python
        bot_msg = await interact_with(await bot.send_message("@BotFather", "/start"))
    :param message: already sent message to bot
    :return: bot's response
    """

    await asyncio.sleep(1)
    # noinspection PyProtectedMember
    response = await message._client.get_chat_history(message.chat.id, limit=1)
    seconds_waiting = 0

    while response[0].from_user.is_self:
        seconds_waiting += 1
        if seconds_waiting >= 5:
            raise RuntimeError("bot didn't answer in 5 seconds")

        await asyncio.sleep(1)
        # noinspection PyProtectedMember
        response = await message._client.get_chat_history(message.chat.id, limit=1)

    interact_with_to_delete.append(message.message_id)
    interact_with_to_delete.append(response[0].message_id)

    return response[0]


interact_with_to_delete = []

def import_library(library_name: str, package_name: str = None):
    """
    Loads a library, or installs it in ImportError case
    :param library_name: library name (import example...)
    :param package_name: package name in PyPi (pip install example)
    :return: loaded module
    """
    if package_name is None:
        package_name = library_name
    requirements_list.append(package_name)

    try:
        return importlib.import_module(library_name)
    except ImportError:
        completed = subprocess.run(["python3", "-m", "pip", "install", package_name])
        if completed.returncode != 0:
            raise AssertionError(
                f"Failed to install library {package_name} (pip exited with code {completed.returncode})"
            )
        return importlib.import_module(library_name)

async def edit_or_reply(message: Message, *args, **kwargs) -> Message:
    apa = (
        message.edit_text
        if bool(message.from_user and message.from_user.is_self or message.outgoing)
        else (message.reply_to_message or message).reply_text
    )
    return await apa(*args, **kwargs)