from telegram import Update, Chat, ChatMember, ParseMode, ChatMemberUpdated
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackContext,
    ChatMemberHandler,
)

from jocasta.config import get_str_key

TOKEN = get_str_key("BOT_TOKEN", True)

updater = Updater(TOKEN)

dispatcher = updater.dispatcher

