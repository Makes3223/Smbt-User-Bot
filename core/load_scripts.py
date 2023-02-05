import importlib
import os

from importlib import import_module

from pyrogram import Client, filters
from pyrogram.types import Message

from core.script import restart
from core.modul import modules_help, prefixes, app


BASE_PATH = os.path.abspath(os.getcwd())
SCRIPT_DIRECTORY = os.path.join(f"{BASE_PATH}/scripts")
loaded_modules = {}

if not os.path.exists(SCRIPT_DIRECTORY):
    os.makedirs(SCRIPT_DIRECTORY)

modules = []
if os.path.exists("loaded_modules.txt"):
    with open("loaded_modules.txt", "r") as f:
        modules = f.readlines()
modules = [module.strip() for module in modules]
for module in modules:
    imported_module = import_module(f"scripts.{module.split('.')[0]}")
    loaded_modules[module] = imported_module

@app.on_message(filters.command(["loadscript", "ls"], prefixes) & filters.me)
async def load_script(client: Client, message: Message):
    if len(message.command) < 2:
        await message.edit("<b>Please specify script name to load</b>")
        return
    script_name = message.command[1]
    if not script_name.endswith(".py"):
        script_name += ".py"
    script_path = os.path.join(SCRIPT_DIRECTORY, script_name)
    if not os.path.exists(script_path):
        await message.edit(f"<b>Script <code>{script_name}</code> not found in {SCRIPT_DIRECTORY} directory</b>")
        return
    imported_module = import_module(f"scripts.{script_name.split('.')[0]}")
    loaded_modules[script_name] = imported_module
    with open("loaded_modules.txt", "w") as f:
        for module in loaded_modules:
            f.write(module + "\n")
    await message.edit(f"<b>Successfully loaded script <code>{script_name}</code> from {SCRIPT_DIRECTORY} directory</b>")

@app.on_message(filters.command(["unloadscript", "uls"], prefixes) & filters.me)
async def unload_script(client: Client, message: Message):
    if len(message.command) < 2:
        await message.edit("<b>Please specify script name to unload</b>")
        return
    script_name = message.command[1]
    if not script_name.endswith(".py"):
        script_name += ".py"
    script_path = os.path.join(SCRIPT_DIRECTORY, script_name)
    if not os.path.exists(script_path):
        await message.edit(f"<b>Script <code>{script_name}</code> not found in {SCRIPT_DIRECTORY} directory</b>")
        return
    if script_name not in loaded_modules:
        await message.edit(f"<b>Script <code>{script_name}</code> is not currently loaded</b>")
        return
    imported_module = loaded_modules.pop(script_name)
    importlib.reload(imported_module)
    with open("loaded_modules.txt", "w") as f:
        for module in loaded_modules:
            f.write(module + "\n")
    await message.edit(f"<b>Successfully unloaded script <code>{script_name}</code></b>")
    restart()

modules_help["loadscript"] = {
    "loadscript, 'ls' [module_name]*": "Download module.\n"
    "Only modules from the official custom_modules repository and proven ",
    "unloadscript,  'uls' [module_name]*": "Delete module",
}