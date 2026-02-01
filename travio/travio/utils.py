import random

import string

from twilio.rest import Client

from decouple import config

def generate_password():

    password = ''.join(random.choices(string.ascii_letters+string.digits,k=8))

    return password


def generate_otp():

    otp = ''.join(random.choices(string.digits,k=4))

    return otp


def send_otp(phone_num,otp):

    account_sid = config('TWILIO_ACCOUNT_SID')
    auth_token = config('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    from_=config('TWILIO_NUMBER'),
    to=config('MY_NUMBER'),
    body=f'OTP for Verification : {otp}'
    
    )
