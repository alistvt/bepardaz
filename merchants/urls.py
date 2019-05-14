from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^signup/$', views.MerchantSignUpView, name='merchant-sign-up'),
    url(r'^createpf/$', views.MerchantSignUpView, name='merchant-create-payment-form'),
]
