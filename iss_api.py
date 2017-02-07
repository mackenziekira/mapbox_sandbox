# code built based on blog: https://www.twilio.com/blog/2015/11/international-space-station-notifications-with-python-redis-queue-and-twilio-copilot.html

import requests
from datetime import datetime
import pytz

def get_next_pass(lat, lon):
    iss_url = 'http://api.open-notify.org/iss-pass.json'
    location = {'lat': lat, 'lon': lon}
    response = requests.get(iss_url, params=location.json())

    if 'response' in response:
        next_pass = response['response'][0]['risetime']
        next_pass_datetime = datetime.fromtimestamp(next_pass, tz=pytz.utc)
        print('next pass for {}, {} is: {}'.format(lat, lon, next_pass_datetime))
        return next_pass_datetime
    else:
        print('no response for {}, {}'.format(lat, lon))
