<p align="center">
    <br>
    <h3><b>Smbt-Userbot</b></h>
    <br>
    <a href='https://github.com/Makes3223/Smbt-User-Bot#installation'>
        Installation
    </a>
</p>

<h1>About</h1>
<p>Bot name is a Telegram userbot (in case you didn't know, selfbot/userbot are used to automate user accounts). So how does it work? It works in a very simple way, using the pyrogram library, a python script connects to your account (creating a new session) and catches your commands.

Using selfbot/userbot is against Telegram's Terms of Service, and you may get banned for using it if you're not careful.

The developers are not responsible for any consequences you may encounter when using bot name. We are also not responsible for any damage to chat rooms caused by using this userbot</p>

<h1>Requirements</h1>

| Platform| Supported  |
|:-------------|:-------------|
| Android | ✅ |
| IOS     | ❌ |
| MacOS   | ❌ |
| Windows [only wsl]| ✅ |
| Windows | ❌ |
| Linux   | ✅ |
<h1>Installation</h1>


<h2>Linux, Termux (use <a href='https://f-droid.org/en/packages/com.termux/'>f-droid</a> version) and Windows [only wsl]</h2>

<pre><code>apt-get upgrade -y && apt-get update && apt install git && git clone https://github.com/Makes3223/Smbt-User-Bot.git
</code></pre>

First launch:

<pre><code>cd Smbt-User Bot</code></pre>

<pre><code>pip3 -r install requirements.txt</code></pre>

<pre><code>python3 install.py</code></pre>

Subsequent launch:

<pre><code>python3 main.py</code></pre>


<h1>Custom modules</h1>


```python3
import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message

from core_v1.modul import prefixes, app, modules_help
from core_v1.script import with_reply, restart, format_exc

@app.on_message(filters.command("example_edit", prefixes) & filters.me)
async def example_edit(client: Client, message: Message):
    await message.edit("<code>This is an example module</code>")


@app.on_message(filters.command("example_send", prefixes) & filters.me)
async def example_send(client: Client, message: Message):
    await client.send_message(message.chat.id, "<b>This is an example module</b>")
```

<h2>Groups and support</h2>


<h2>Credits</h2>


Written on <a href='https://github.com/pyrogram/pyrogram'>Pyrogram❤️</a></h4>
