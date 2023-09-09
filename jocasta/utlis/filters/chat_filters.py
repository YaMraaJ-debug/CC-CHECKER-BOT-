from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from jocasta import ADMINS, dp, USERNAME
from jocasta.services.addtodb import pyro_user_info_dec, user_info_dec
from jocasta.services.language import get_strings_dec
from jocasta.modules.filters.admins_rights import is_user_admin


class OnlyPM(BoundFilter):
    key = "only_pm"
    
    def __init__(self, only_pm):
        self.only_pm = only_pm

    async def check(self, message: types.Message) -> bool:
        return bool(message.from_user.id == message.chat.id)


class OnlyGP(BoundFilter):
    key = "only_gp"
    
    def __init__(self, only_gp):
        self.only_gp = only_gp

    async def check(self, message: types.Message) -> bool:
        if not message.from_user.id == message.chat.id:
            return True

class IsAdmin(BoundFilter):
    key = "is_admin"

    def __init__(self, is_admin):
        self.is_admin = is_admin

    @get_strings_dec("global")
    async def check(self, event, strings):

        if hasattr(event, "message"):
            chat_id = event.message.chat.id
        else:
            chat_id = event.chat.id

        if not await is_user_admin(chat_id, event.from_user.id):
            task = event.answer if hasattr(event, "message") else event.reply
            await task(strings["u_not_admin"])
            return False
        return True



class only_admins(BoundFilter):
    key = "only_admins"
    
    def __init__(self, only_admins):
        self.only_admins = only_admins

    async def check(self, message: types.Message) -> bool:
        if message.from_user.id in ADMINS:
            return True

class OnlyBot(BoundFilter):
    key = "only_bot"
    
    def __init__(self, only_bot):
        self.only_bot = only_bot

    async def check(self, m: types.Message) -> bool:
        return bool(m.from_user and m.from_user.is_bot)


class is_text(BoundFilter):
    key = "is_text"
    
    def __init__(self, is_text):
        self.is_text = is_text

    async def check(self, m: types.Message):
        if "text" in m:
            return True


class is_replied(BoundFilter):
    key = "is_replied"
    
    def __init__(self, is_replied):
        self.is_replied = is_replied

    async def check(self, m: types.Message) -> bool:
        return bool(m.reply_to_message)

class is_edited(BoundFilter):
    key = "is_edited"
    
    def __init__(self, is_edited):
        self.is_edited = is_edited

    async def check(self, m: types.Message) -> bool:
        return bool(m.edit_date)


class is_audio(BoundFilter):
    key = "is_audio"
    
    def __init__(self, is_audio):
        self.is_audio = is_audio

    async def check(self, m: types.Message) -> bool:
        return bool(m.is_audio)

class is_document(BoundFilter):
    key = "is_document"
    
    def __init__(self, is_document):
        self.is_document = is_document

    async def check(self, m: types.Message) -> bool:
        return bool(m.is_document)


class is_photo(BoundFilter):
    key = "is_photo"
    
    def __init__(self, is_photo):
        self.is_photo = is_photo

    async def check(self, m: types.Message) -> bool:
        return bool(m.is_photo)

class is_sticker(BoundFilter):
    key = "is_sticker"
    
    def __init__(self, is_sticker):
        self.is_sticker = is_sticker

    async def check(self, m: types.Message) -> bool:
        return bool(m.is_sticker)

class is_animation(BoundFilter):
    key = "is_animation"
    
    def __init__(self, is_animation):
        self.is_animation = is_animation

    async def check(self, m: types.Message) -> bool:
        return bool(m.is_animation)

class is_group(BoundFilter):
    key = "is_group"
    
    def __init__(self, is_group):
        self.is_group = is_group

    async def check(self, m: types.Message) -> bool:
        return bool(m.chat and m.chat.type in ["is_group", "supergroup"])

class new_chat_participant(BoundFilter):
    key = "new_chat_participant"
    
    def __init__(self, new_chat_participant):
        self.new_chat_participant = new_chat_participant

    async def check(self, m: types.Message) -> bool:
        if "new_chat_participant" in m:
            return True
        else:
            return False


class left_chat_participant(BoundFilter):
    key = "left_chat_participant"
    
    def __init__(self, left_chat_participant):
        self.left_chat_participant = left_chat_participant

    async def check(self, m: types.Message) -> bool:
        if "left_chat_members" in m:
            return True
        else:
            return False




dp.filters_factory.bind(OnlyPM)
dp.filters_factory.bind(OnlyGP)
dp.filters_factory.bind(IsAdmin)
dp.filters_factory.bind(OnlyBot)
dp.filters_factory.bind(is_text)
dp.filters_factory.bind(is_replied)
dp.filters_factory.bind(is_edited)
dp.filters_factory.bind(is_audio)
dp.filters_factory.bind(is_document)
dp.filters_factory.bind(is_photo)
dp.filters_factory.bind(is_sticker)
dp.filters_factory.bind(is_animation)
dp.filters_factory.bind(is_group)
dp.filters_factory.bind(new_chat_participant)
dp.filters_factory.bind(left_chat_participant)
dp.filters_factory.bind(only_admins)


