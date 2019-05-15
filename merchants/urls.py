from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^signup/$', views.MerchantSignUpView.as_view(), name='merchant-sign-up'),
    url(r'^createpf/$', views.CreatePaymentFormView.as_view(), name='merchant-create-payment-form'),
    url(r'^profile/$', views.MerchantProfileActionsView.as_view(), name='merchant-profile-actions'),
]
