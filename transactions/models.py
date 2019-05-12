# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _

from merchants.models import PaymentForm

# Create your models here.


class Payer(User):
    phone_number = models.CharField(max_length=20,
                                    verbose_name=_('phone number'),
                                    validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                                               message=_("entered phone number is invalid."))])

    class Meta:
        verbose_name = _("payer")
        verbose_name_plural = _("payers")
        ordering = ['last_name']

    def __str__(self):
        return '{first_name} {last_name}'.format(first_name=self.first_name, last_name=self.last_name)


class Transaction(models.Model):
    payer = models.ForeignKey(Payer, related_name='transactions', on_delete=models.DO_NOTHING, verbose_name=_('payer'))
    payment_form = models.ForeignKey(PaymentForm, related_name='transactions',
                                     on_delete=models.DO_NOTHING, verbose_name=_('payment form'))
    payment_amount = models.PositiveIntegerField(verbose_name=_('payment amount'))
    status_code = models.IntegerField(null=True, verbose_name=_("status code"))
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name=_('creation date'))

    class Meta:
        verbose_name = _("transaction")
        verbose_name_plural = _("transactions")
        ordering = ['-creation_date']

    def __str__(self):
        return '{payer} - {payment_form}'.format(payer=self.payer, payment_form=self.payment_form)
