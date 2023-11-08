from rest_framework.views import APIView
from rest_framework.response import Response
from .cron import update_currency_rates_cron_job


class UpdateCurrencyRatesAPIView(APIView):
    def get(self, request):
        update_currency_rates_cron_job()
        return Response({'message': 'CRON job executed successfully'})
