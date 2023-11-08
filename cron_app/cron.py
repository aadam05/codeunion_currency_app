from django_cron import CronJobBase, Schedule
import requests
from bs4 import BeautifulSoup
from currency_info.models import Currency
from django_q.tasks import async_task


def update_currency_rates():
    url = 'http://www.nationalbank.kz/rss/rates_all.xml'
    response = requests.get(url)
    
    if response.status_code == 200:
        xml_data = response.text
        soup = BeautifulSoup(xml_data, 'lxml')

        for item in soup.find_all('item'):
            currency_code = item.find('title').get_text()
            rate = float(item.find('description').get_text())
            currency, created = Currency.objects.get_or_create(name=currency_code)
            currency.rate = rate
            currency.save()


def print_result(task):
    print(task.result)


class UpdateCurrencyRatesCronJob(CronJobBase):
    RUN_EVERY_MINS = 1

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'cron_app.UpdateCurrencyRatesCronJob'

    def do(self):
        async_task(update_currency_rates, hook=print_result)
        # update_currency_rates()
