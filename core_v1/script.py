import os
import sys
import asyncio
import subprocess
import importlib

from pyrogram import Client, errors, types
from core_v1.modul import modules_help, prefixes, app, requirements_list


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