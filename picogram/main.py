import requests

from pprint import pprint


class Bot:

    def __init__(self, token):
        self.api_url = 'https://api.telegram.org/bot'
        self.token = token
        self.handlers = []

    def run_polling(self):
        offset = -2
        update_id = None
        while True:
            updates = requests.get(f'{self.api_url}{self.token}/getUpdates?offset={offset + 1}').json()
            if updates['result']:
                last_update_id = updates['result'][-1]['update_id']
                if last_update_id != update_id:
                    pprint(updates)
                    update_id = last_update_id
                    for handler in self.handlers:
                        handler(message=updates['result'][-1]['message'])

    def message(self):
        def decorator(fn):
            self.handlers.append(fn)
            return fn

        return decorator

    def send_message(self, chat_id, text):
        requests.get(f'{self.api_url}{self.token}/sendMessage?chat_id={chat_id}&text={text}')
