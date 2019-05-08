# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Merchant(User):
    pass

    class Meta:
        verbose_name = _("Merchant")
        verbose_name_plural = _("Merchants")
        ordering = ['last_name']

    def __str__(self):
        return '{name}'.format(name=self.first_name + ' ' + self.last_name)
