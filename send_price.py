import ezgmail
from datetime import datetime
import requests
import time

'''
Send an email with the price of Bitcoin and time as subject
'''


def get_btc_price():
    r = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
    j = r.json()
    current_price = j['bitcoin']['usd']
    return current_price

# Defining the variables we'll send
now = datetime.now()
email_subject = f'Bicoin price at {now}'
price = get_btc_price()

time.sleep(2)
email_content = f'Price = ${price}'

# Launching the gmail account
ezgmail.init()

# Sending the email with a tailored object giving the time and price
ezgmail.send('saeid.klntri@gmail.com', email_subject, email_content)