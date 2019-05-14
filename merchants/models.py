# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Merchant(User):
    phone_number = models.CharField(unique=True, max_length=20,
                                    verbose_name=_('phone number'),
                                    validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                                               message=_("entered phone number is invalid."))])

    class Meta:
        verbose_name = _("merchant")
        verbose_name_plural = _("merchants")
        ordering = ['last_name']

    def save(self, *args, **kwargs):
        if not self.username:
            if self.email:
                self.username = self.email
            else:
                self.username = self.phone_number

        super().save(*args, **kwargs)

    def __str__(self):
        return '{first_name} {last_name}'.format(first_name=self.first_name, last_name=self.last_name)


class PaymentForm(models.Model):
    creator = models.ForeignKey(Merchant, related_name='payment_forms', on_delete=models.CASCADE, verbose_name=_('owner'))
    title = models.CharField(max_length=255, verbose_name=_('title'))
    description = models.TextField(blank=True, null=True, verbose_name=_('description'))
    payment_amount = models.PositiveIntegerField(verbose_name=_('payment amount'))
    link = models.CharField(max_length=36, verbose_name=_('link'))
    # times that link can be payed. 0 means infinitely.
    max_payments_count = models.PositiveSmallIntegerField(default=0, verbose_name=_('maximum payments count'))
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name=_('creation cate'))

    class Meta:
        verbose_name = _("payment form")
        verbose_name_plural = _("payment forms")
        ordering = ['-creation_date']

    def __str__(self):
        return '{title}'.format(title=self.title)
