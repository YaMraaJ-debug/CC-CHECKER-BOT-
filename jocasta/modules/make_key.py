from jocasta.modules.filters.checker_defs import Helper
from jocasta.dec import register
from jocasta.services.addtodb import user_info_dec
from jocasta.services.language import get_strings_dec
from jocasta.services.mongo import adb
from jocasta.utlis.send_log import send_logs
from jocasta import bot
from  random import randint


@register(cmds = 'make_key', is_text = True, only_admins = True,is_warned = True)
@get_strings_dec("make_key")
@user_info_dec()
async def make_key(message, lang, user):
    try:
        await bot.send_chat_action(chat_id = message.chat.id , action = 'typing')
        msg = await message.reply(lang['start_msg'])
        data = message.text.split(' ')
        assert len(data) < 4, lang['no_days']
        assert (data[1].isdigit() or data[1].lower() == "test") and data[1] != "0",lang['no_days']
        # assert len(data) > 3 and data[2] < 30,lang['no_days']
        key = 'JOCASTA-' + str(randint(3000,5000)) +'-'+ str(randint(1000,9999)) +'-'+ str(randint(1000,9999)) +'-'+ str(randint(1000,9999))
        antispam_time = int(data[2]) if len(data) == 3 and data[2].isdigit() else 30
        post_data = {
        '_id': key,
        'key': key,
        'days': data[1],
        'spam-time': antispam_time,
            }
        set = await adb.keys.insert_one(post_data)
        if set:
            text = f"""
<b>{lang['key_redeemed']}</b>:-
<b>{lang['key']}</b>: `{key}`
<b>{lang['days']}</b>: <b>{data[1]} Days</b>
<b>{lang['antispam_time']}</b>: <b>{antispam_time}</b>
<b>{lang['gen_by']}</b>: [{message.from_user.first_name}](tg://user?id={message.from_user.id}) [{user['role']} User]
<b>{lang['notes'].format(key = key)}</b>
"""

            await msg.edit_text(text)
        else:
            await msg.edit_text(lang['error'])
    except AssertionError as t:
        await msg.edit_text(t)
    except Exception as e:
        await send_logs(e)