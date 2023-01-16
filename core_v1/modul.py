from pyrogram import Client, errors, types, filters

prefixes = (".", "/", "!")

app = Client("my_account")


class ModulesHelpDict(dict):
    def append(self, obj: dict):
        # convert help from old to new type
        module_name = list(obj.keys())[0]
        cmds = obj[module_name]
        commands = {}
        for cmd in cmds:
            cmd_name = list(cmd.keys())[0]
            cmd_desc = cmd[cmd_name]
            commands[cmd_name] = cmd_desc 
        self[module_name] = commands
  
  
modules_help = ModulesHelpDict()

requirements_list = []
