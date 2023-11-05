from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status, generics
from rest_framework.authtoken.models import Token
from currency_info.serializers import CurrencySerializer
from currency_info.models import Currency
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class UserRegistration(APIView):
  @swagger_auto_schema(
    manual_parameters=[
      openapi.Parameter('username', in_=openapi.IN_QUERY, description='Username', type=openapi.TYPE_STRING),
      openapi.Parameter('password', in_=openapi.IN_QUERY, description='Password', type=openapi.TYPE_STRING),
    ],
    responses={
      200: openapi.Response('Successful response'),
      400: 'Bad Request',
      401: 'Unauthorized',
    }
  )
  def post(self, request):
    username = request.query_params.get('username') or request.data.get('username')
    password = request.query_params.get('password') or request.data.get('password')

    if not username or not password:
      return Response({'error': 'Username, password and name are required.'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, password=password)
    user.save()

    return Response({'message': 'User registered successfully.'}, status=status.HTTP_201_CREATED)


class UserLogin(APIView):
  @swagger_auto_schema(
    manual_parameters=[
      openapi.Parameter('username', in_=openapi.IN_QUERY, description='Username', type=openapi.TYPE_STRING),
      openapi.Parameter('password', in_=openapi.IN_QUERY, description='Password', type=openapi.TYPE_STRING),
    ],
    responses={
      200: openapi.Response('Successful response'),
      400: 'Bad Request',
      401: 'Unauthorized',
    }
  )
  def post(self, request):
    username = request.query_params.get('username') or request.data.get('username')
    password = request.query_params.get('password') or request.data.get('password')

    user = authenticate(request, username=username, password=password)

    if user:
      token = Token.objects.create(user=user)
      return Response({'token': token.key}, status=status.HTTP_200_OK)
    else:
      return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
    

class CurrencyList(generics.ListCreateAPIView):
  queryset = Currency.objects.all()
  serializer_class = CurrencySerializer

class CurrencyDetail(generics.RetrieveAPIView):
  queryset = Currency.objects.all()
  serializer_class = CurrencySerializer
