from pyrogram import Client
import pyrogram.filters
from jocasta.config import get_str_key, get_int_key
import logging
from jocasta.utlis.logger import log

TOKEN = get_str_key("BOT_TOKEN", True)
NAME = TOKEN.split(':')[0]

pbot = Client(
    NAME,
    get_int_key("API_ID",1),
    get_str_key("API_HASH", 1),
    bot_token= TOKEN
)

logging.getLogger("pyrogram").setLevel(level=logging.ERROR)

log.info("STARTED PYROGRAM..")

pbot.start()