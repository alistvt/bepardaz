# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from zeep import Client

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from .forms import PayerForm
from .models import Transaction
from merchants.models import PaymentForm

MERCHANT = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
amount = 1000  # Toman / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
email = 'email@example.com'  # Optional
mobile = '09123456789'  # Optional
callback_url = 'http://localhost:8000/verify/' # Important: need to edit for realy server.

# Create your views here.


def payment_form_view(request, link):
    payment_form = PaymentForm.objects.get(link=link)
    if request.POST:
        payer_form = PayerForm(request.POST)
        if payer_form.is_valid():
            result = client.service.PaymentRequest(MERCHANT, payer_form.payment_amount, description, email, mobile, callback_url)

            if result.Status == 100:
                return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
                # todo
                payer = PayerForm.save()
                transaction = Transaction.create(payer=payer,
                                                 payer_form=payer_form,
                                                 payment_amount=payer_form.payment_amount,
                                                 authority=str(result.Authority))

            else:
                return HttpResponse('Error code: ' + str(result.Status))

    else:
        return render(request, 'payment_form.html', {'pf': payment_form})


def verify_payment_view(request):
    if request.GET.get('Status') == 'OK':
        result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], amount)
        if result.Status == 100:
            # todo
            return HttpResponse('Transaction success.\nRefID: ' + str(result.RefID))
        elif result.Status == 101:
            return HttpResponse('Transaction submitted : ' + str(result.Status))
        else:
            return HttpResponse('Transaction failed.\nStatus: ' + str(result.Status))
    else:
        return HttpResponse('Transaction failed or canceled by user')
