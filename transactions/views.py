# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from merchants.models import PaymentForm

# Create your views here.

def payment_form_view(request, link):
    payment_form =  PaymentForm.objects.get(link=link)
    return render(request, 'payment_form.html', {'pf': payment_form})