import html
from urllib.request import urlopen
from jocasta import LOG_CHAT, bot
from jocasta.services.python_telegram_bot import dispatcher
from jocasta.config import get_int_key, get_str_key
from jocasta.utlis.logger import log

TOKEN = get_str_key("BOT_TOKEN", True)
chat_id = get_int_key("SUPPORT_CHAT")

def channel_log(msg, info_log=True):
    if info_log:
        log.warn(msg)

    urlopen(
        f'https://api.telegram.org{TOKEN}/sendMessage?chat_id={chat_id}&text={msg}'
    )


async def send_logs(msg, info_log=True):
    if info_log:
        log.critical(msg, exc_info =True)

    await bot.send_message(
        LOG_CHAT,
        text = msg
    )


async def send_logs_doc(msg):

    await bot.send_document(
        chat_id= LOG_CHAT,
        document = msg
    )
    