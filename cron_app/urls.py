from django.urls import path
from .views import UpdateCurrencyRatesAPIView

app_name = 'cron_app'

urlpatterns = [
    path('update_currency_rates/', UpdateCurrencyRatesAPIView.as_view(), name='update_currency_rates'),
]
