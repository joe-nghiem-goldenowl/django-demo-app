from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')

app = Celery('demo')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print("PING")

@app.task(bind=True)
def update_currency_rate(self):
    def get_currency_rate():
        from requests import get
        from json import loads
        from dotenv import load_dotenv
        import os

        load_dotenv()
        params = {
            'apikey': os.environ.get('CURRENCY_API_KEY'),
            'base_currency': 'USD',
            'currencies': 'VND'
        }

        res = loads(get('https://api.currencyapi.com/v3/latest', params=params).content)
        return res['data']['VND']['value']

    rate = get_currency_rate()
    obj = {
        'rate': rate,
    }
    with open('currency_rate.json', 'w') as f:
        import json
        f.write(json.dumps(obj))
        f.close()
    print("Update new rate: " + str(rate))    