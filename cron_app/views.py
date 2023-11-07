from rest_framework.views import APIView
from rest_framework.response import Response
from .cron import UpdateCurrencyRatesCronJob


class UpdateCurrencyRatesAPIView(APIView):
    def get(self, request):
        cron_job = UpdateCurrencyRatesCronJob()
        cron_job.do()
        return Response({'message': 'CRON job executed successfully'})
