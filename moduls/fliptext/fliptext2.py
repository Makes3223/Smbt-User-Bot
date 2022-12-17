import asyncio
from pyrogram import Client, filters
from pyrogram.raw import functions
from pyrogram.types import Message
from core_v1.modul import app, prefixes,modules_help 
from core_v1.script import format_exc


REPLACEMEN_MAP = {
    "a": '卂',
    "b": '乃',
    "c": '匚',
    "d": '刀',
    "e": '乇',
    "f": '下',
    "g": '厶',
    "h": '卄',
    "i": '工',
    "j": '丁',
    "k": '长',
    "l": '乚',
    "m": '从',
    "n": '𠘨',
    "o": '口',
    "p": '尸',
    "q": '㔿',
    "r": '尺',
    "s": '丂',
    "t": '丅',
    "u": '凵',
    "v": 'リ',
    "w": '山',
    "x": '乂',
    "y": '丫',
    "z": '乙',
    "A": '卂',
    "B": '乃',
    "C": '匚',
    "D": '刀',
    "E": '乇',
    "F": '下',
    "G": '厶',
    "H": '卄',
    "I": '工',
    "J": '丁',
    "K": '长',
    "L": '乚',
    "M": '从',
    "N": '𠘨',
    "O": '口',
    "P": '尸',
    "Q": '㔿',
    "R": '尺',
    "S": '丂',
    "T": '丅',
    "U": '凵',
    "V": 'リ',
    "W": '山',
    "X": '乂',
    "Y": '丫',
    "Z": '乙',
}


@app.on_message(filters.command("fliper", prefixes) & filters.me)
async def flip(client: Client, message: Message):
    text = " ".join(message.command[1:])
    final_str = ""
    for char in text:
        if char in REPLACEMEN_MAP.keys():
            new_char = REPLACEMEN_MAP[char]
        else:
            new_char = char
        final_str += new_char
    if text != final_str:
        await message.edit(final_str)
    else:
        await message.edit(text)


modules_help["fliptext"] = {

    "flip [amount]*": "flip text"
}