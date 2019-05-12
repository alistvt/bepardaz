from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _

from merchants.models import Merchant


class MerchantCreationForm(UserCreationForm):
    """
    A form that creates a merchant, with no privileges, from the given username and
    password.
    """
    class Meta:
        model = Merchant
        fields = ('phone_number', 'email', 'password1', 'password2', 'first_name', 'last_name', )

    def save(self, commit=True):
        merchant = super().save(commit=False)
        merchant.username = None
        merchant.save()
        return merchant
