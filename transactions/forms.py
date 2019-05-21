from django import forms

from .models import Payer


class PayerForm(forms.ModelForm):
    class Meta:
        model = Payer
        fields = ('first_name', 'last_name', 'email', 'phone_number')