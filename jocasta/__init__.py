import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from jocasta.config import get_int_key, get_list_key, get_str_key
from jocasta.utlis.logger import log, logger

__version__ = '1.0'

logo = """

░░░░░██╗░█████╗░░█████╗░░█████╗░░██████╗████████╗░█████╗░
░░░░░██║██╔══██╗██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔══██╗
░░░░░██║██║░░██║██║░░╚═╝███████║╚█████╗░░░░██║░░░███████║
██╗░░██║██║░░██║██║░░██╗██╔══██║░╚═══██╗░░░██║░░░██╔══██║
╚█████╔╝╚█████╔╝╚█████╔╝██║░░██║██████╔╝░░░██║░░░██║░░██║
░╚════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝
                A Tᴇʟᴇɢʀᴀᴍ Bᴏᴛ                          
"""

print(logo)

log.setLevel(logging.DEBUG)

if sys.version_info[0] < 3 and sys.version_info[1] > 5:
    log.critical("Your Python Version Is Not Compatible For This Bot.")
    sys.exit(1)

# if get_int_key("DEBUG"):
#     log.setLevel("debug")


BOT_TOKEN = get_str_key("BOT_TOKEN", 1)

ADMINS = []

OWNER_ID = get_int_key("OWNER_ID", 1)
ADMINS.append(OWNER_ID)
LOG_CHAT = get_int_key("LOG_CHAT")
SUPPORT_CHAT = get_str_key("SUPPORT_CHAT")
SESSION_STRING = get_str_key("STRING_SESSION", 1)
API_TOKEN = get_str_key("BOT_TOKEN", 1)

bot = Bot(token=API_TOKEN, parse_mode='html')

# storage = RedisStorage2(
#     get_str_key("BOT_REDIS"),
#     get_int_key("BOT_REDIS_PORT"),
#     password=get_str_key("BOT_REDIS_PASS")
# )
CROSS = '❌'
TICK = '✅'

dp = Dispatcher(bot)  # storage=storage
log.info("Starting Bot.")

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
log.info("Getting Bot Info.")

bot_info = loop.run_until_complete(bot.get_me())

USERNAME = bot_info.username
BOT_ID = bot_info.id
BOT_NAME = bot_info.first_name

log.info("Username: @%s" % USERNAME)
log.info("Id: %s" % BOT_ID)
log.info("First name: %s" % BOT_NAME)
