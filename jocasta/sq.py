import requests
import urllib.parse 
from urllib.parse import urlencode, quote_plus
def find_between( data, first, last ):
    try:
        start = data.index( first ) + len( first )
        end = data.index( last, start )
        return data[start:end]
    except ValueError:
        return None

r = requests.Session()

a = r.get('https://square.link/u/Q6lOoHzr?src=embed')
# with open("a.html",'w', encoding = 'utf-8') as write: write.write(a.text)
# quit()
order_id = find_between(a.text, 'order: {"id":"','"')
location_id = find_between(a.text, 'location_id":"','"')
application_id = find_between(a.text, 'application_id":"','"')


b = r.get(f'https://pci-connect.squareup.com/v2/iframe?type=main&app_id={application_id}&host_name=checkout.square.site&location_id={location_id}&version=4192ac3ca7')

sess = find_between(b.text,'fi="','"')


quo = urllib.parse.quote(a.url, safe="")

c = r.get(f'https://connect.squareup.com/payments/data/frame.html?referer={quo}')
v = find_between(c.text,'version:"','"')

analytics_token = find_between(c.text,'s="','"')

po = {
    "components": "{\"user_agent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36\",\"language\":\"en-IN\",\"color_depth\":24,\"resolution\":[1366,768],\"available_resolution\":[1366,738],\"timezone_offset\":-330,\"session_storage\":1,\"local_storage\":1,\"open_database\":1,\"cpu_class\":\"unknown\",\"navigator_platform\":\"Win32\",\"do_not_track\":\"1\",\"regular_plugins\":[\"PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf\"],\"adblock\":false,\"has_lied_languages\":false,\"has_lied_resolution\":false,\"has_lied_os\":false,\"has_lied_browser\":false,\"touch_support\":[0,false,false],\"js_fonts\":[\"Arial\",\"Arial Black\",\"Arial Narrow\",\"Calibri\",\"Cambria\",\"Cambria Math\",\"Comic Sans MS\",\"Consolas\",\"Courier\",\"Courier New\",\"Georgia\",\"Helvetica\",\"Impact\",\"Lucida Console\",\"Lucida Sans Unicode\",\"Microsoft Sans Serif\",\"MS Gothic\",\"MS PGothic\",\"MS Sans Serif\",\"MS Serif\",\"Palatino Linotype\",\"Segoe Print\",\"Segoe Script\",\"Segoe UI\",\"Segoe UI Light\",\"Segoe UI Semibold\",\"Segoe UI Symbol\",\"Tahoma\",\"Times\",\"Times New Roman\",\"Trebuchet MS\",\"Verdana\",\"Wingdings\",\"Wingdings 2\",\"Wingdings 3\"]}",
    "fingerprint": "ff29402705e67d89bd1da8765894be71",
    "version": v,
    "website_url": "https://checkout.square.site/",
    "client_id": "sq0idp-w46nJ_NCNDMSOywaCY0mwA",
    "browser_fingerprint_by_version": [
        {
            "payload_json": "{\"components\":{\"user_agent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36\",\"language\":\"en-IN\",\"color_depth\":24,\"resolution\":[1366,768],\"available_resolution\":[1366,738],\"timezone_offset\":-330,\"session_storage\":1,\"local_storage\":1,\"open_database\":1,\"cpu_class\":\"unknown\",\"navigator_platform\":\"Win32\",\"do_not_track\":\"1\",\"regular_plugins\":[\"PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf\"],\"adblock\":false,\"has_lied_languages\":false,\"has_lied_resolution\":false,\"has_lied_os\":false,\"has_lied_browser\":false,\"touch_support\":[0,false,false],\"js_fonts\":[\"Arial\",\"Arial Black\",\"Arial Narrow\",\"Calibri\",\"Cambria\",\"Cambria Math\",\"Comic Sans MS\",\"Consolas\",\"Courier\",\"Courier New\",\"Georgia\",\"Helvetica\",\"Impact\",\"Lucida Console\",\"Lucida Sans Unicode\",\"Microsoft Sans Serif\",\"MS Gothic\",\"MS PGothic\",\"MS Sans Serif\",\"MS Serif\",\"Palatino Linotype\",\"Segoe Print\",\"Segoe Script\",\"Segoe UI\",\"Segoe UI Light\",\"Segoe UI Semibold\",\"Segoe UI Symbol\",\"Tahoma\",\"Times\",\"Times New Roman\",\"Trebuchet MS\",\"Verdana\",\"Wingdings\",\"Wingdings 2\",\"Wingdings 3\"]},\"fingerprint\":\"ff29402705e67d89bd1da8765894be71\"}",
            "payload_type": "fingerprint-v1"
        },
        {
            "payload_json": "{\"components\":{\"language\":\"en-IN\",\"color_depth\":24,\"resolution\":[1366,768],\"available_resolution\":[1366,738],\"timezone_offset\":-330,\"session_storage\":1,\"local_storage\":1,\"open_database\":1,\"cpu_class\":\"unknown\",\"navigator_platform\":\"Win32\",\"do_not_track\":\"1\",\"regular_plugins\":[\"PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf\"],\"adblock\":false,\"has_lied_languages\":false,\"has_lied_resolution\":false,\"has_lied_os\":false,\"has_lied_browser\":false,\"touch_support\":[0,false,false],\"js_fonts\":[\"Arial\",\"Arial Black\",\"Arial Narrow\",\"Calibri\",\"Cambria\",\"Cambria Math\",\"Comic Sans MS\",\"Consolas\",\"Courier\",\"Courier New\",\"Georgia\",\"Helvetica\",\"Impact\",\"Lucida Console\",\"Lucida Sans Unicode\",\"Microsoft Sans Serif\",\"MS Gothic\",\"MS PGothic\",\"MS Sans Serif\",\"MS Serif\",\"Palatino Linotype\",\"Segoe Print\",\"Segoe Script\",\"Segoe UI\",\"Segoe UI Light\",\"Segoe UI Semibold\",\"Segoe UI Symbol\",\"Tahoma\",\"Times\",\"Times New Roman\",\"Trebuchet MS\",\"Verdana\",\"Wingdings\",\"Wingdings 2\",\"Wingdings 3\"]},\"fingerprint\":\"fe6a54c1165838ea6882b510da7b977e\"}",
            "payload_type": "fingerprint-v1-sans-ua"
        }
    ]
}
hey = r.post('https://connect.squareup.com/v2/analytics/token', json = po)

token = hey.json()['token']

print(analytics_token, token)

obj = {
    "client_id": application_id,
    "location_id": location_id,
    "session_id": sess,
    "website_url": "https://checkout.square.site/",
    "squarejs_version": "4192ac3ca7",
    "analytics_token": token,
    "card_data": {
        "number": "4427950009858955",
        "exp_month": 9,
        "exp_year": 2024,
        "cvv": "485",
        "billing_postal_code": "10002"
    }
}

d = r.post('https://pci-connect.squareup.com/v2/card-nonce?_=1646066506059.7424&version=4192ac3ca7',json = obj)

card_nonce = d.json()['card_nonce']


e_data = {
    "browser_fingerprint_by_version": [
        {
            "payload_json": "{\"components\":{\"user_agent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36\",\"language\":\"en-IN\",\"color_depth\":24,\"resolution\":[1366,768],\"available_resolution\":[1366,738],\"timezone_offset\":-330,\"session_storage\":1,\"local_storage\":1,\"open_database\":1,\"cpu_class\":\"unknown\",\"navigator_platform\":\"Win32\",\"do_not_track\":\"1\",\"regular_plugins\":[\"PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf\"],\"adblock\":false,\"has_lied_languages\":false,\"has_lied_resolution\":false,\"has_lied_os\":false,\"has_lied_browser\":false,\"touch_support\":[0,false,false],\"js_fonts\":[\"Arial\",\"Arial Black\",\"Arial Narrow\",\"Calibri\",\"Cambria\",\"Cambria Math\",\"Comic Sans MS\",\"Consolas\",\"Courier\",\"Courier New\",\"Georgia\",\"Helvetica\",\"Impact\",\"Lucida Console\",\"Lucida Sans Unicode\",\"Microsoft Sans Serif\",\"MS Gothic\",\"MS PGothic\",\"MS Sans Serif\",\"MS Serif\",\"Palatino Linotype\",\"Segoe Print\",\"Segoe Script\",\"Segoe UI\",\"Segoe UI Light\",\"Segoe UI Semibold\",\"Segoe UI Symbol\",\"Tahoma\",\"Times\",\"Times New Roman\",\"Trebuchet MS\",\"Verdana\",\"Wingdings\",\"Wingdings 2\",\"Wingdings 3\"]},\"fingerprint\":\"ff29402705e67d89bd1da8765894be71\"}",
            "payload_type": "fingerprint-v1"
        },
        {
            "payload_json": "{\"components\":{\"language\":\"en-IN\",\"color_depth\":24,\"resolution\":[1366,768],\"available_resolution\":[1366,738],\"timezone_offset\":-330,\"session_storage\":1,\"local_storage\":1,\"open_database\":1,\"cpu_class\":\"unknown\",\"navigator_platform\":\"Win32\",\"do_not_track\":\"1\",\"regular_plugins\":[\"PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf\"],\"adblock\":false,\"has_lied_languages\":false,\"has_lied_resolution\":false,\"has_lied_os\":false,\"has_lied_browser\":false,\"touch_support\":[0,false,false],\"js_fonts\":[\"Arial\",\"Arial Black\",\"Arial Narrow\",\"Calibri\",\"Cambria\",\"Cambria Math\",\"Comic Sans MS\",\"Consolas\",\"Courier\",\"Courier New\",\"Georgia\",\"Helvetica\",\"Impact\",\"Lucida Console\",\"Lucida Sans Unicode\",\"Microsoft Sans Serif\",\"MS Gothic\",\"MS PGothic\",\"MS Sans Serif\",\"MS Serif\",\"Palatino Linotype\",\"Segoe Print\",\"Segoe Script\",\"Segoe UI\",\"Segoe UI Light\",\"Segoe UI Semibold\",\"Segoe UI Symbol\",\"Tahoma\",\"Times\",\"Times New Roman\",\"Trebuchet MS\",\"Verdana\",\"Wingdings\",\"Wingdings 2\",\"Wingdings 3\"]},\"fingerprint\":\"fe6a54c1165838ea6882b510da7b977e\"}",
            "payload_type": "fingerprint-v1-sans-ua"
        }
    ],
    "browser_profile": {
        "components": "{\"user_agent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36\",\"language\":\"en-IN\",\"color_depth\":24,\"resolution\":[1366,768],\"available_resolution\":[1366,738],\"timezone_offset\":-330,\"session_storage\":1,\"local_storage\":1,\"open_database\":1,\"cpu_class\":\"unknown\",\"navigator_platform\":\"Win32\",\"do_not_track\":\"1\",\"regular_plugins\":[\"PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf\"],\"adblock\":false,\"has_lied_languages\":false,\"has_lied_resolution\":false,\"has_lied_os\":false,\"has_lied_browser\":false,\"touch_support\":[0,false,false],\"js_fonts\":[\"Arial\",\"Arial Black\",\"Arial Narrow\",\"Calibri\",\"Cambria\",\"Cambria Math\",\"Comic Sans MS\",\"Consolas\",\"Courier\",\"Courier New\",\"Georgia\",\"Helvetica\",\"Impact\",\"Lucida Console\",\"Lucida Sans Unicode\",\"Microsoft Sans Serif\",\"MS Gothic\",\"MS PGothic\",\"MS Sans Serif\",\"MS Serif\",\"Palatino Linotype\",\"Segoe Print\",\"Segoe Script\",\"Segoe UI\",\"Segoe UI Light\",\"Segoe UI Semibold\",\"Segoe UI Symbol\",\"Tahoma\",\"Times\",\"Times New Roman\",\"Trebuchet MS\",\"Verdana\",\"Wingdings\",\"Wingdings 2\",\"Wingdings 3\"]}",
        "fingerprint": "ff29402705e67d89bd1da8765894be71",
        "version": v,
        "website_url": "https://checkout.square.site/"
    },
    "client_id": application_id,
    "payment_source": card_nonce,
    "universal_token": {
        "token": location_id,
        "type": "UNIT"
    },
    "verification_details": {
        "billing_contact": {
            "given_name": "martin",
            "postal_code": "10002"
        },
        "intent": "CHARGE",
        "total": {
            "amount": 100,
            "currency": "USD"
        }
    }
}


e = r.post('https://connect.squareup.com/v2/analytics/verifications', json= e_data)

verf = e.json()['token']


f_data = {
    "square_merchant_id": "ML9W48PYQ8KN7",
    "square_location_id": location_id,
    "nonce": card_nonce,
    "buyer_verification_token": verf,
    "buyer_email": "vkgfbfbftj@metalunits.com",
    "buyer_name": "martin York",
    "buyer_locale": "en-IN",
    "buyer_postal_code": "10002",
    "order_id": order_id,
    "order_version": 3,
    "amount": 100,
    "spos_cart": False,
    "customer_note": None,
    "phone_number": "+12259383093",
    "tip_amount": None
}

e = r.post('https://checkout.square.site/app/square-sync/published/payment', json = e_data)
print(e.text)
# 