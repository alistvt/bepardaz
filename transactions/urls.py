from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^(?P<link>[\w\-]+)/$', views.payment_form_view, name='payment-form'),
    url(r'^verify/$', views.verify_payment_view, name='payment-verification'),
]
