from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from jocasta import dp, USERNAME
from jocasta.services.addtodb import pyro_user_info_dec
from jocasta.services.language import get_strings_dec
from jocasta.modules.filters.admins_rights import is_user_admin
from jocasta.modules.filters.user_info import is_user_allowed, is_chat_allowed


class IsWarned(BoundFilter):
    key = "is_warned"

    def __init__(self, is_warned):
        self.is_warned = is_warned

    @get_strings_dec("mains")
    @pyro_user_info_dec()
    async def check(self, event, strings, user):
        if user['warn'] > 5:
            task = event.answer if hasattr(event, "message") else event.reply
            await task(strings["warned"])
            return False
        return True


class IsUserAllowed(BoundFilter):
    key = "user_allowed"

    def __init__(self, user_allowed):
        self.user_allowed = user_allowed

    @get_strings_dec("decorator_error")
    async def check(self, m: types.Message, strings) -> bool:
        data = await is_user_allowed(m)
        if data:
            return True
        elif data is False and m.chat.type == 'private':
            task = m.answer if hasattr(m, "message") else m.reply
            await task(strings["no_access"])
            return False
        elif data is False:
            if await is_chat_allowed(m.chat.id):
                return True
            task = m.answer if hasattr(m, "message") else m.reply
            await task(strings["no_groups"])
            return False
        else:
            task = m.answer if hasattr(m, "message") else m.reply
            await task(strings["no_access"])
            return False


class IsUserCallback(BoundFilter):
    key = "user_callback"

    def __init__(self, user_callback):
        self.user_callback = user_callback

    @get_strings_dec("decorator_error")
    async def check(self, message, strings) -> bool:
        if "reply_to_message" not in message.message:
            return True
        if message.from_user.id == message.message.reply_to_message.from_user.id:
            return True
        task = message.answer if hasattr(message, "message") else message.reply
        await task(strings["no_callback"])
        return False


dp.filters_factory.bind(IsUserAllowed)
dp.filters_factory.bind(IsWarned)
dp.filters_factory.bind(IsUserCallback)
