from contextlib import suppress
import pprint
from jocasta import bot
from jocasta.services.language import get_strings_dec
from jocasta.services.mongo import adb
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



@register(cmds="lives", is_text=True)
@user_info_dec()
@get_strings_dec("lives")
@only_premium()
async def chk(message, user_info, lang):
    try:
        await message.answer_chat_action('typing')
        msg = await message.reply(lang['start_msg'])
        assert 'cards' in user_info, lang['no_ccs']
        assert len(user_info['cards']) > 0, lang['no_ccs']
        keys = [f'`{str(i)}`' for i in user_info['cards']]
        assert len(keys) > 0, lang['no_ccs']
        await msg.edit_text(lang['msg'].format(cards='\n'.join(keys), name = message.from_user.first_name, id = message.from_user.id, role =user_info['role']), disable_web_page_preview= True)
        if len(keys) > 20:
            await adb.update_one({'_id': message.from_user.id}, {'$set': {'cards': []}})
    except AssertionError as ae:
        await msg.edit_text(ae)
    except Exception as e:
        await send_logs(e)
