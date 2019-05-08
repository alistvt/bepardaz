# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from merchants.models import PaymentForm

# Create your models here.


class Payer(User):
    # todo (ask): the best way to store phone number
    phone = models.CharField(max_length=20, verbose_name=_('phone number'))

    class Meta:
        verbose_name = _("payer")
        verbose_name_plural = _("payers")
        ordering = ['last_name']

    def __str__(self):
        return '{name}'.format(name=self.first_name + ' ' + self.last_name)


class Transaction(models.Model):
    payer = models.ForeignKey(Payer, related_name='transactions', on_delete=models.DO_NOTHING, verbose_name=_('payer'))
    payment_form = models.ForeignKey(PaymentForm, related_name='transactions',
                                     on_delete=models.DO_NOTHING, verbose_name=_('payment form'))
    price = models.PositiveIntegerField(verbose_name=_('price'))
    status = models.IntegerField(null=True)
    started_date = models.DateTimeField(auto_now_add=True, verbose_name=_('creation date'))
    ended_date = models.DateTimeField(auto_now_add=True, verbose_name=_('end date'))

    class Meta:
        verbose_name = _("transaction")
        verbose_name_plural = _("transactions")
        ordering = ['-started_date']

    def __str__(self):
        return '{payer} - {payment_form}'.format(payer=self.payer, payment_form=self.payment_form)
