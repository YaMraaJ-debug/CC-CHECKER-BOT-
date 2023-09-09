from telethon import TelegramClient
from jocasta.utlis.logger import log
from jocasta.config import get_str_key, get_int_key


TOKEN = get_str_key("BOT_TOKEN", True)
NAME = TOKEN.split(':')[0]

tbot = TelegramClient(
    NAME,
    get_int_key("API_ID",1),
    get_str_key("API_HASH",1),
)

log.info("STARTED TELETHON..")

tbot.start(bot_token=TOKEN)