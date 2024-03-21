from pprint import pprint

import requests
import time

API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = 'your_token_here'
TEXT = 'Update!'
MAX_COUNTER = 200

offset = -2
counter = 0
chat_id: int

while counter < MAX_COUNTER:

    print('attempt =', counter)

    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()
    pprint(updates)

    if updates['result']:
        print("Something is here", counter)
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')

    time.sleep(0.5)
    counter += 1
