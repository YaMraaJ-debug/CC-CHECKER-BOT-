from jocasta.dec import register
from jocasta.services.addtodb import user_info_dec
from jocasta.services.language import get_strings_dec
from jocasta.services.mongo import adb
from jocasta.utlis.send_log import send_logs
from jocasta import bot
from time import time
from datetime import date, timedelta, datetime



@register(cmds = ['redeem', 'claim'], is_text = True, is_warned = True)
@get_strings_dec("redeem")
@user_info_dec()
async def redeem(message, lang, user):
    try:
        await bot.send_chat_action(chat_id = message.chat.id , action = 'typing')
        msg = await message.reply(lang['start_msg'])
        data = message.text.split(' ')
        assert len(data) == 2, lang['no_key']
        assert (len(data[1]) == 27  and "JOCASTA" in data[1]), lang['invalid_key']
        data = await adb.keys.find_one({'_id': data[1]})
        assert data is not None, lang['invalid_key']
        if user['status'] == "P":
            if data['days'] == "test":
                await msg.edit_text(lang['cant_claim_test_keys'])
            else:
                exp = int(data["days"]) * 86400 #days into seconds
                expiry = int(time()) + int(exp)
                expiry = int(user['expiry']) + int(expiry)
                expiry_days = int(user['expiry_days']) + int(data['days'])
                days_left = f"{expiry_days} Days"
                currenttime = datetime.now().strftime('%Y-%m-%d')
                a2s = data['key'] + str(expiry_days) + ' '+ ' Days ' +  currenttime
                new_dict = {
                    "$addToSet": {
                        "key": a2s,
                    },
                    '$set': {
                            "status": 'P',
                            "expiry": int(expiry),
                            "role": "Premium",
                            "expiry_days": int(expiry_days),
                            'spam-time': data['spam-time'],
                            'redeem-time': currenttime
                        },
                }
                x = await adb.users.update_one({'_id': message.from_user.id}, new_dict)
                if x:
                    text = lang['success'].format(
                        name = message.from_user.first_name,
                        id = message.from_user.id,
                        key = data['key'], 
                        antispam_time = data['spam-time'],
                        days_left = days_left,
                        exp_time = date.today()+timedelta(days=expiry_days)
                    )
                else:
                    text = lang['error']
                await msg.edit_text(text)
            await adb.keys.delete_one({"_id": data['key']})
        else:
            if data['days']  ==  "test":
                exp = 600
                expiry = int(time()) + exp
                days_left = "10 Minutes"
                expiry_days = 0
            else:
                exp = int(data["days"]) * 86400
                expiry = int(time()) + int(exp)
                expiry_days = int(data['days'])
                days_left = f"{data['days']} Days"
            currenttime = datetime.now().strftime('%Y-%m-%d')
            a2s = data['key'] + str(expiry_days) + ' '+ ' Days ' +  currenttime
            new_dict = {
                "$addToSet": {"key": a2s},
                '$set': {
                    "status": 'P',
                    "expiry": int(expiry),
                    "role": "Premium",
                    "expiry_days": expiry_days,
                    'spam-time': data['spam-time'],
                    'redeem-time': currenttime,
                },
            }
            x = await adb.users.update_one({'_id': message.from_user.id}, new_dict)
            if x:
                text = lang['success'].format(
                    name = message.from_user.first_name,
                    id = message.from_user.id,
                    key = data['key'], 
                    antispam_time = data['spam-time'],
                    days_left = days_left,
                    exp_time = date.today()+timedelta(days=expiry_days))
            else:
                text = lang['error']
            await adb.keys.delete_one({"_id": data['key']})
            await msg.edit_text(text)
    except AssertionError as t:
        await msg.edit_text(t)
        await adb.users.update_one({'_id': message.from_user.id}, {'$inc': {'warn':1}})
        await message.reply("You increased your check limit")
    except Exception as e:
        await send_logs(e)