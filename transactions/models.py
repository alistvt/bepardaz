# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

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
