# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.utils.translation import ugettext_lazy as _

from merchants.models import Merchant, PaymentForm
from merchants.forms import MerchantCreationForm

# Register your models here.


@admin.register(Merchant)
class MerchantAdmin(admin.ModelAdmin):
    add_form = MerchantCreationForm
    # fields = ('name', ('first_name', 'last_name'), 'email', 'address', 'is_active', )
    fieldsets = (
        (_('merchant info'), {'fields': ('is_active', 'phone_number')}),
        (_('personal info'), {'fields': ('first_name', 'last_name', 'email')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'email', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )
    change_password_form = AdminPasswordChangeForm
    list_display = ('first_name', 'last_name', 'phone_number', 'is_active', )
    search_fields = ('first_name', 'last_name', 'phone_number', )
    list_filter = ('is_active', )
    ordering = ('last_name', )

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return super().get_fieldsets(request, obj)

    def get_form(self, request, obj=None, **kwargs):
        """
        Use special form during user creation
        """
        defaults = {}
        if obj is None:
            defaults['form'] = self.add_form
        defaults.update(kwargs)
        return super().get_form(request, obj, **defaults)


@admin.register(PaymentForm)
class PaymentFormAdmin(admin.ModelAdmin):
    # add_form = MerchantCreationForm
    # fields = ('name', ('first_name', 'last_name'), 'email', 'address', 'is_active', )
    # fieldsets = (
    #     (_('merchant info'), {'fields': ('is_active', 'phone_number')}),
    #     (_('personal info'), {'fields': ('first_name', 'last_name', 'email')}),
    # )
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('phone_number', 'email', 'first_name', 'last_name', 'password1', 'password2'),
    #     }),
    # )
    list_display = ('title', 'owner', 'payment_amount', 'link', 'times_payed', )
    search_fields = ('title', 'link', )
    # list_filter = ('times_payed', )
    ordering = ('title', )
    #
    # def get_fieldsets(self, request, obj=None):
    #     if not obj:
    #         return self.add_fieldsets
    #     return super().get_fieldsets(request, obj)
    #
    # def get_form(self, request, obj=None, **kwargs):
    #     """
    #     Use special form during user creation
    #     """
    #     defaults = {}
    #     if obj is None:
    #         defaults['form'] = self.add_form
    #     defaults.update(kwargs)
    #     return super().get_form(request, obj, **defaults)
    #
