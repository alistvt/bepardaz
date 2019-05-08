# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Merchant(User):
    # todo (ask): the best way to store phone number
    phone = models.CharField(max_length=20, verbose_name=_('phone number'))

    class Meta:
        verbose_name = _("merchant")
        verbose_name_plural = _("merchants")
        ordering = ['last_name']

    def __str__(self):
        return '{name}'.format(name=self.first_name + ' ' + self.last_name)


class PaymentForm(models.Model):
    creator = models.ForeignKey(Merchant, related_name='payment_forms', on_delete=models.CASCADE, verbose_name=_('creator'))
    title = models.CharField(max_length=255, verbose_name=_('title'))
    # todo (ask): for blank and null value
    description = models.TextField(blank=True, default='', verbose_name=_('description'))
    price = models.PositiveIntegerField(verbose_name=_('price'))
    link = models.CharField(max_length=36, verbose_name=_('link'))
    # times that link can be payed. 0 means infinitely.
    payable_times = models.PositiveSmallIntegerField(default=0, verbose_name=_('payable times'))
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Creation Date'))

    class Meta:
        verbose_name = _("payment form")
        verbose_name_plural = _("payment forms")
        ordering = ['-created_date']

    def __str__(self):
        return '{title}'.format(title=self.title)
