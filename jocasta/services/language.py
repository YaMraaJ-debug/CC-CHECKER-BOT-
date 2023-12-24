from jocasta.utlis.logger import log
from jocasta.services.red import aioredis
import os
import yaml
from babel.core import Locale


async def get_chat_lang(chat_id: int) -> str:
    if data := await aioredis.get(f"lang_{chat_id}"):
        return data.lower()
    else:
        return "en"


log.info("Adding Lanuages")

LANGUAGES = {}
for filename in os.listdir("jocasta/languages"):
    log.debug(f"Loading language file {filename}")
    with open(f"jocasta/languages/{filename}", "r", encoding="utf8") as f:
        lang = yaml.load(f, Loader=yaml.CLoader)
        lang_code = lang["language_info"]["code"]
        log.debug(f"Importing {lang_code} Language Code.")
        lang["language_info"]["babel"] = Locale(lang_code)
        LANGUAGES[lang_code] = lang

log.debug(
    f'Languages loaded: {[language["language_info"]["babel"].display_name for language in LANGUAGES.values()]}'
)


async def change_user_lang(chat_id: int, lang: str):
    print(chat_id)
    await aioredis.set(f"bin_{chat_id}", lang.lower())
    return await aioredis.set(f"lang_{chat_id}", lang.lower())


async def get_strings(chat_id, module, mas_name="STRINGS"):
    chat_lang = await get_chat_lang(chat_id)
    if chat_lang not in LANGUAGES:
        await change_user_lang(chat_id, "en")

    class Strings:
        @staticmethod
        def get_strings(lang, mas_name, module):

            if (
                    mas_name not in LANGUAGES[lang]
                    or module not in LANGUAGES[lang][mas_name]
            ):
                return {}

            data = LANGUAGES[lang][mas_name][module]
            if mas_name == "STRINGS":
                data["language_info"] = LANGUAGES[chat_lang]["language_info"]
            return data

        def get_string(self, name):
            data = self.get_strings(chat_lang, mas_name, module)
            if name not in data:
                data = self.get_strings("en", mas_name, module)
            return data[name]

        def __getitem__(self, key):
            return self.get_string(key)

    return Strings()


def get_strings_dec(module, mas_name="STRINGS"):
    def wrapped(func):
        async def wrapped_1(*args, **kwargs):
            message = args[0]
            if hasattr(message, "chat"):
                chat_id = message.chat.id
            elif hasattr(message, "message"):
                chat_id = message.message.chat.id
            else:
                chat_id = None

            strings = await get_strings(chat_id, module, mas_name=mas_name)
            return await func(*args, strings, **kwargs)

        return wrapped_1

    return wrapped


async def get_chat_lang_info(chat_id):
    chat_lang = await get_chat_lang(chat_id)
    return LANGUAGES[chat_lang]["language_info"]
