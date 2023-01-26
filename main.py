print('''
                            v0.1
 ____            _     _        _   _                 ____        _
/ ___| _ __ ___ | |__ | |_     | | | |___  ___ _ __  | __ )  ___ | |_
\___ \| '_ ` _ \| '_ \| __|____| | | / __|/ _ \ '__| |  _ \ / _ \| __|
 ___) | | | | | | |_) | ||_____| |_| \__ \  __/ |    | |_) | (_) | |_
|____/|_| |_| |_|_.__/ \__|     \___/|___/\___|_|    |____/ \___/ \__|
''')

print("Loading")

from pyrogram import Client, filters
from core_v1.modul import prefixes, app
from core_v1.modul import modules_help
from core_v1 import helpp

from core_v1 import loader as loader
from core_v1 import load_scripts as load_scripts


print("-" * 19)
print("loading successfully")
app.run()