from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from .serializers import UserSerialzier, UserVerifySerializer
from .models import User
from random import randint
from django.core.cache import cache
from rest_framework import viewsets, status


class LoginView(APIView):
    def post(self, request):
        srz_data = UserSerialzier(data=request.data)
        if srz_data.is_valid():  # shouldn't check the phone is unique
            the_code = randint(1, 9)
            phone = srz_data.validated_data["phone_number"]
            cache.set(the_code, phone)
            print(the_code)
            return Response(data=srz_data.data, status=status.HTTP_200_OK)
        return Response(data=srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class UserVerifyView(APIView):
    def post(self, request):
        srz_data = UserVerifySerializer(data=request.data)
        if srz_data.is_valid():
            phone = srz_data.validated_data["code"]  # validated data return the phone
            try:
                user = User.objects.get(phone_number=phone)
            except User.DoesNotExist:
                rand_password = User.get_random_string()
                user = User.objects.create_user(
                    phone_number=phone, password=rand_password)

            tokens = user.get_tokens_for_user()
            return Response(data=tokens)
        return Response(data=srz_data.errors, status=status.HTTP_400_BAD_REQUEST)
