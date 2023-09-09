from telethon import TelegramClient
from jocasta.utlis.logger import log
from jocasta.config import get_str_key, get_int_key
from telethon.sessions import StringSession
from jocasta import SESSION_STRING


ubot = TelegramClient(
    StringSession(SESSION_STRING),
    get_int_key("API_ID",1),
    get_str_key("API_HASH",1),
)

log.info("STARTED TELETHON USER BOT..")

ubot.start()


# for message in ubot.get_messages('roldexverse', limit=2):
    # print(message.message)