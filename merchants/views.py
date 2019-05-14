# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics, serializers, filters

from .models import Merchant
from .serializers import MerchantSignUpSerializer

# Create your views here.


class MerchantSignUpView(generics.CreateAPIView):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSignUpSerializer
    permission_classes = []
