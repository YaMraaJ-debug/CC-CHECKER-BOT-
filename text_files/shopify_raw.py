import cgi
import time
import requests
import re

def find_between( data, first, last ):
    try:
        start = data.index( first ) + len( first )
        end = data.index( last, start )
        return data[start:end]
    except ValueError:
        return None

r = requests.Session()

a = r.get('https://www.edensgarden.com/collections/roll-ons/products/eucalyptus-roll-on')



b_data = {
    "items": [
        {
            "id": 27893566993,
            "quantity": 1,
            "properties": {
                "_dtstamp": 1646673282320,
                "_giftuid": 1646673282320
            }
        }
    ]
}


b = r.post('https://www.edensgarden.com/cart/add.js', json = b_data) #200
print(b.status_code)

quit()
r.get('https://www.edensgarden.com/cart')

d_post = 'quantity=1'
d = r.post('https://www.edensgarden.com/checkout', d_post)

dd = r.get(d.url)

auth_token = find_between(dd.text, 'type="hidden" name="authenticity_token" value="','"')


# r.get(d.url + '?no_cookies_from_redirect=1')
# r.get(d.url + '?cookies_blocked=1&no_cookies_from_redirect=1')
e_data = {
'_method': 'patch',
'authenticity_token': 'N6EYat_buQw3_NuOv5bOQBaiyRszptG0fldfYCruGo1LWsAa41mbZKCdsuMUjcLxG-cxq1ADF0_zxGoziZ4ddQ',
'previous_step': 'contact_information',
'step': 'shipping_method',
'checkout[email]': 'vkgfbfbftj@metalunits.com',
'checkout[buyer_accepts_marketing]': '0',
'checkout[shipping_address][first_name]': 'martin',
'checkout[shipping_address][last_name]': 'York',
'checkout[shipping_address][company]': '',
'checkout[shipping_address][address1]': '3 allen street',
'checkout[shipping_address][address2]': '',
'checkout[shipping_address][city]': 'New York',
'checkout[shipping_address][country]': 'US',
'checkout[shipping_address][province]': 'New York',
'checkout[shipping_address][zip]': '10002',
'checkout[shipping_address][phone]': '+1 02259383093',
'checkout[shipping_address][first_name]': 'martin',
'checkout[shipping_address][last_name]': 'York',
'checkout[shipping_address][company]': '',
'checkout[shipping_address][address1]': '3 allen street',
'checkout[shipping_address][address2]': '',
'checkout[shipping_address][city]': 'New York',
'checkout[shipping_address][country]': 'United States',
'checkout[shipping_address][province]': 'NY',
'checkout[shipping_address][zip]': '10002',
'checkout[shipping_address][phone]': '(225) 938-3093',
'checkout[remember_me]': '',
'checkout[remember_me]': '0',
'checkout[buyer_accepts_sms]': '0',
'checkout[sms_marketing_phone]': '',
'checkout[client_details][browser_width]': '742',
'checkout[client_details][browser_height]': '667',
'checkout[client_details][javascript_enabled]': '1',
'checkout[client_details][color_depth]': '24',
'checkout[client_details][java_enabled]': 'false',
'checkout[client_details][browser_tz]': '-330',
}

e = r.post(d.url, e_data)

# ee = r.get(d.url + '/shipping_rates?step=shipping_method')

f_data = {
'_method': 'patch',
'authenticity_token': auth_token,
'previous_step': 'shipping_method',
'step': 'payment_method',
'checkout[shipping_rate][id]': 'shopify-Free%20Shipping%20(3-8%20business%20days)-0.00',
'checkout[client_details][browser_width]': '632',
'checkout[client_details][browser_height]': '667',
'checkout[client_details][javascript_enabled]': '1',
'checkout[client_details][color_depth]': '24',
'checkout[client_details][java_enabled]': 'false',
'checkout[client_details][browser_tz]': '-330',
}


f = r.post(d.url, f_data)
with open('f.html', 'w', encoding='utf-8') as wr: wr.write(f.text)
h = r.get(f.url)
print(h.url)

payment_gateway = find_between(h.text,'data-subfields-for-gateway="','"')


print(payment_gateway)


json_four = {
    "credit_card": {
        "number": "4318 2900 9108 9652",
        "name": "Martin",
        "month": 4,
        "year": 2025,
        "verification_value": "358"
    },
    "payment_session_scope": "www.edensgarden.com"
}

four = r.post('https://deposit.us.shopifycs.com/sessions', json = json_four)

token = four.json()['id']

print(token)
g_data  = {
'_method': 'patch',
'authenticity_token': auth_token,
'previous_step': 'payment_method',
'step': '',
's': token,
'checkout[payment_gateway]': payment_gateway,
'checkout[credit_card][vault]': 'false',
'checkout[different_billing_address]': 'false',
'checkout[remember_me]': 'false',
'checkout[remember_me]': '0',
'checkout[vault_phone]': '',
'checkout[total_price]': '866',
'complete': '1',
'checkout[client_details][browser_width]': '615',
'checkout[client_details][browser_height]': '667',
'checkout[client_details][javascript_enabled]': '1',
'checkout[client_details][color_depth]': '24',
'checkout[client_details][java_enabled]': 'false',
'checkout[client_details][browser_tz]': '-330',
}

print(d.url)
g = r.post(d.url, g_data)
g_url = g.url
h = r.get(f'{g.url}?from_processing_page=1')
i = r.get(f'{h.url}&validate=true')
# print(g.status_code)


# with open('g.html', 'w', encoding='utf-8') as wr: wr.write(g.text)
# with open('h.html', 'w', encoding='utf-8') as wr: wr.write(h.text)
with open('i.html', 'w', encoding='utf-8') as wr: wr.write(i.text)


