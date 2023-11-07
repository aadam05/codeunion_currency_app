from django.urls import path
from .views import UserRegistration, UserLogin, CurrencyList, CurrencyDetail

app_name = 'currency_info'

urlpatterns = [
    path('registration/', UserRegistration.as_view(), name='registration'),
    path('login/', UserLogin.as_view(), name='login'),
    path('currencies/', CurrencyList.as_view(), name='currencies'),
    path('currency/<int:pk>/', CurrencyDetail.as_view(), name='currency_detail'),
]
