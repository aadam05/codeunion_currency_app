from django.core.management.base import BaseCommand
from currency_info.models import Currency


class Command(BaseCommand):
    help = 'Update or view currency data'

    def add_arguments(self, parser):
        parser.add_argument('--currency', type=str, help='Currency name')
        parser.add_argument('--value', type=float, help='Currency value')

    def handle(self, *args, **options):
        currency_name = options['currency']
        currency_rate = options['value']

        if currency_name and currency_rate:
            currency, created = Currency.objects.get_or_create(name=currency_name)
            currency.rate = currency_rate
            currency.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully updated {currency_name} with value {currency_rate}'))
        elif currency_name:
            try:
                currency = Currency.objects.get(name=currency_name)
                self.stdout.write(self.style.SUCCESS(f'Currency: {currency_name}, Value: {currency.rate}'))
            except Currency.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'Currency {currency_name} not found'))
        else:
            self.stdout.write(self.style.ERROR('Please provide currency name and/or value'))
