import asyncio
import os
from importlib import import_module
from jocasta.utlis.logger import log
from jocasta.services.language import get_strings_dec
from aiogram import executor
from jocasta import dp
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from jocasta.modules import ALL_MODULES, LOADED_MODULES, MOD_HELP


# from jocasta.services.sql.afk import *

dp.middleware.setup(LoggingMiddleware())

log.info("Getting Modules.")


modules = ALL_MODULES

log.info("Modules to load: %s", str(modules))

for module_name in modules:
    log.debug(f"Importing <d><n>{module_name}</></>")
    imported_module = import_module(f"jocasta.modules.{module_name}")
    if hasattr(imported_module, "__help__"):
        if hasattr(imported_module, "__mod_name__"):
            MOD_HELP[imported_module.__mod_name__] = imported_module.__help__
        else:
            MOD_HELP[imported_module.__name__] = imported_module.__help__
    LOADED_MODULES.append(imported_module)
log.info("Modules loaded!")

loop = asyncio.get_event_loop()


executor.start_polling(
        dp,
        loop=loop,
        # on_startup=start,
        timeout=15,
        relax=0.1,
        fast=True,
        skip_updates=True,
    )