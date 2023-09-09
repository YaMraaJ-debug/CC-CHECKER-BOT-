from contextlib import suppress
from jocasta import bot
from jocasta.services.antispam_dec import get_spam_dec
from jocasta.services.language import get_strings_dec
from jocasta.services.gate_on_off import gate_info_dec
from jocasta.services.addtodb import user_info_dec
from jocasta.dec import register
import time
import re
from jocasta.services.user_allowed import only_premium
from jocasta.utlis.logger import log
from jocasta.services.red import aioredis
from jocasta.utlis.send_log import send_logs
from jocasta.modules.filters.bin_info import get_bin_info
from jocasta.modules.filters.get_card_details import get_cards
from .func.sho import *
from aiogram.utils.exceptions import MessageNotModified



@register(cmds="bin", is_text=True)
@user_info_dec()
@get_strings_dec("bin")
@only_premium()
async def chk(message, user_info, lang):
    try:
        start_time = time.time()
        await bot.send_chat_action(chat_id=message.chat.id, action='typing')
        msg = await message.reply(lang['bin_banned'])
        res = re.findall(r"[0-9]+", message.text)
        assert len(res) > 0, lang['error']
        assert len(res[0]) > 5, lang['error']
        bin_info = await get_bin_info(res[0][:6],message.from_user.id)
        assert bin_info, lang['']
        with suppress(MessageNotModified):
            await msg.edit_text(lang['bin'].format(
            bin_name= res[0][:6],
            bank_name= bin_info['bank_name'],
            country= bin_info['country'],
            flag= bin_info['flag'],
            iso= bin_info['iso'],
            level= bin_info['level'],
            vendor= bin_info['vendor'],
            type= bin_info['type'],
            prepaid= bin_info['prepaid'],
            name= message.from_user.first_name,
            id= message.from_user.id,
            role= user_info['role'],
            took = round(time.time() - start_time),
        ), disable_web_page_preview =True)
    except AssertionError as ae:
        await msg.edit_text(ae)
    except Exception as e:
        await send_logs(e)
    