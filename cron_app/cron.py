from django_cron import CronJobBase, Schedule
import requests
from bs4 import BeautifulSoup
from currency_info.models import Currency


class UpdateCurrencyRatesCronJob(CronJobBase):
  RUN_EVERY_MINS = 60

  schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
  code = 'cron_app.update_currency_rates_cron_job'

  def do(self):
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