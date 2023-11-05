from django.test import TestCase
from currency_info.models import Currency
from currency_info.management.commands import create_currency
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User


# Сути не меняет если мы переведем в строку rate и сделаем assert со строкой,
# однако можем избежать потенциальных ошибок с типами
class CurrencyModelTestCase(TestCase):
  def test_create_currency_whole_number(self):
    currency = Currency.objects.create(name='USD', rate=400)
    currency.save()

    saved_currency = Currency.objects.all().first()
    self.assertEqual(saved_currency.name, 'USD')
    self.assertEqual(str(saved_currency.rate), '400.00')

  def test_create_currency_decimal_number(self):
    currency = Currency.objects.create(name='USD', rate=1.50)
    currency.save()

    saved_currency = Currency.objects.all().first()
    self.assertEqual(saved_currency.name, 'USD')
    self.assertEqual(str(saved_currency.rate), '1.50')


# Сути не меняет если мы переведем в строку rate и сделаем assert со строкой,
# однако можем избежать потенциальных ошибок с типами
class UpdateCurrencyCommandTestCase(TestCase):
  def test_update_currency_command(self):
    cmd = create_currency.Command()
    cmd.handle(currency='USD', value=1.20)

    currency = Currency.objects.get(name='USD')
    self.assertEqual(str(currency.rate), '1.20')


class UserRegistrationTests(APITestCase):

  def test_user_registration(self):
    url = '/currency_info/registration/'
    data = {'username': 'testuser', 'password': 'testpassword'}
    response = self.client.post(url, data)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class UserLoginTests(APITestCase):
  def setUp(self):
    self.user = User.objects.create_user(username='testuser', password='testpassword')

  def test_user_login(self):
    url = '/currency_info/login/'
    data = {'username': 'testuser', 'password': 'testpassword'}
    response = self.client.post(url, data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertIn('token', response.data)


class CurrencyListTests(APITestCase):
  def test_currency_list(self):
    url = '/currency_info/currencies/'
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)


class CurrencyDetailTests(APITestCase):
  def test_currency_detail(self):
    currency = Currency.objects.create(name='USD', rate=400)
    url = f'/currency_info/currency/{currency.id}/'
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
