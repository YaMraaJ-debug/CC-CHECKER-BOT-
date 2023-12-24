import time
import importlib
from jocasta.utlis.logger import log
from aiogram import types
from jocasta import USERNAME as BOT_USERNAME, dp
from aiogram.dispatcher.handler import SkipHandler
from jocasta.utlis.filters import ALL_FILTERS
from importlib import import_module
# ALLOW_FORWARDS_COMMANDS= False
# ALLOW_EXCEL= False

REGISTRED_COMMANDS  = []
COMMANDS_ALIASES = {}


log.info("Filters to load: %s", str(ALL_FILTERS))
for module_name in ALL_FILTERS:
    log.info(f"Importing {module_name}")
    imported_module = import_module(f"jocasta.utlis.filters.{module_name}")
log.info("Filters loaded!")


def register(*args, cmds=None, f=None, allow_edited=True, allow_kwargs=False, **kwargs):
    if cmds and type(cmds) is str:
        cmds = [cmds]

    register_kwargs = {}

    if cmds and not f:
        regex = r"\A^{}(".format("[!/.]")

        for idx, cmd in enumerate(cmds):
            if cmd in REGISTRED_COMMANDS:
                log.warn(f"Duplication of /{cmd} command")
            REGISTRED_COMMANDS.append(cmd)
            regex += cmd

            if idx != len(cmds) - 1:
                if cmds[0] not in COMMANDS_ALIASES:
                    COMMANDS_ALIASES[cmds[0]] = [cmds[idx + 1]]
                else:
                    COMMANDS_ALIASES[cmds[0]].append(cmds[idx + 1])
                regex += "|"

        if "disable_args" in kwargs:
            del kwargs["disable_args"]
            regex += f")($|@{BOT_USERNAME}$)"
        else:
            regex += f")(|@{BOT_USERNAME})(:? |$)"

        register_kwargs["regexp"] = regex

    elif f == "text":
        register_kwargs["content_types"] = types.ContentTypes.TEXT

    elif f == "welcome":
        register_kwargs["content_types"] = types.ContentTypes.NEW_CHAT_MEMBERS

    elif f == "leave":
        register_kwargs["content_types"] = types.ContentTypes.LEFT_CHAT_MEMBER

    elif f == "service":
        register_kwargs["content_types"] = types.ContentTypes.NEW_CHAT_MEMBERS
    elif f == "any":
        register_kwargs["content_types"] = types.ContentTypes.ANY

    log.debug(f"Registered new handler: <d><n>{register_kwargs}</></>")

    register_kwargs.update(kwargs)

    def decorator(func):
        async def new_func(*def_args, **def_kwargs):
            message = def_args[0]

            if cmds:
                message.conf["cmds"] = cmds

            if allow_kwargs is False:
                def_kwargs = dict()

            await func(*def_args, **def_kwargs)
            raise SkipHandler()

        if f == "cb":
            dp.register_callback_query_handler(new_func, *args, **register_kwargs)
        else:
            dp.register_message_handler(new_func, *args, **register_kwargs)
            if allow_edited is True:
                dp.register_edited_message_handler(new_func, *args, **register_kwargs)

    return decorator

