# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, serializers, filters

from .models import Merchant, PaymentForm
from .serializers import MerchantSignUpSerializer, CreatePaymentFormSerializer, MerchantProfileActionsSerializer

# Create your views here.


class MerchantSignUpView(generics.CreateAPIView):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSignUpSerializer
    permission_classes = []


class MerchantProfileActionsView(generics.RetrieveUpdateAPIView):
    queryset = Merchant.objects.all()
    serializer_class = MerchantProfileActionsSerializer
    permission_classes = (IsAuthenticated, )

    def get_object(self):
        user = self.request.user
        user_profile = Merchant.objects.get(pk=user.pk)
        return user_profile


class CreatePaymentFormView(generics.CreateAPIView):
    queryset = PaymentForm.objects.all()
    serializer_class = CreatePaymentFormSerializer
    # TODO : v
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        return serializer.create(serializer.validated_data)
