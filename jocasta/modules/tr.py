from contextlib import suppress
from aiogram.utils.exceptions import MessageNotModified
from googletrans import LANGCODES, LANGUAGES, Translator
from jocasta import bot
from jocasta.dec import register
from jocasta.services.addtodb import user_info_dec
from jocasta.services.language import get_strings_dec
from jocasta.services.red import aioredis
from jocasta.services.user_allowed import only_premium
from jocasta.utlis.logger import log
from jocasta.utlis.send_log import send_logs



@register(cmds="tr", is_text=True)
@user_info_dec()
@get_strings_dec("tr")
@only_premium()
async def chk(message, user_info, lang):
    try:
        await bot.send_chat_action(chat_id=message.chat.id, action='typing')
        msg = await message.reply(lang['start_msg'])
        splited_msg = message.text.split(' ',2)
        # assert len(splited_msg) > 0, lang['lang_text_not_found']
        language = splited_msg[1] if len(splited_msg) > 1  else "en"
        # assert len(language) > 1, lang['lang_not_found']
        if len(splited_msg) == 3:
            t_text = splited_msg[2]
        elif 'reply_to_message' in message and hasattr(message.reply_to_message, 'text'):
            t_text = message.reply_to_message.text 
        else: raise AssertionError(lang['text_not_found'])
        if len(language) == 2 and language not in LANGUAGES or len(language) != 2 and language not in LANGCODES: 
            t_lang = "auto"
        else: t_lang= language
        translator = Translator()
        tr = translator.translate(t_text, dest= t_lang)
        with suppress(MessageNotModified):
            await msg.edit_text(lang['tr'].format(
                name = message.from_user.first_name,
                id = message.from_user.id, role = user_info['role'],
                src = tr.src, dest= tr.dest, t_text = t_text, f_text = tr.text
            ), disable_web_page_preview =True)
    except AssertionError as ae:
        await msg.edit_text(ae)
    except Exception as e:
        await send_logs(e)
