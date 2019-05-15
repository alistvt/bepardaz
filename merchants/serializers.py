# from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

from merchants.models import Merchant, PaymentForm


class MerchantSignUpSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=200, required=True, label=_('confirm password'),
                                             help_text=_('confirm password'), write_only=True)

    class Meta:
        model = Merchant
        fields = ('phone_number', 'email', 'first_name', 'last_name', 'password', 'confirm_password', )
        extra_kwargs = {
            'phone_number': {
                'required': True,
            },
            'email': {
                'required': True,
            },
            'first_name': {
                'required': True,
            },
            'last_name': {
                'required': True,
            },
            'password': {
                'write_only': True,
            }
        }

    def validate(self, attrs):
        confirm_password = attrs.pop('confirm_password', None)
        password = attrs.get('password')
        if confirm_password != password:
            raise serializers.ValidationError(_('passwords doesn\'t match.'))
        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user


class MerchantProfileActionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = ('phone_number', 'email', 'first_name', 'last_name', )
        extra_kwargs = {
            'phone_number': {
                'read_only': True,
            },
        }


class CreatePaymentFormSerializer(serializers.ModelSerializer):
    model = PaymentForm
    fields = ('title', 'description', 'payment_amount', 'link', 'max_payments_count', )
    extra_kwargs = {
        'title': {
            'required': True,
        },
        'description': {
            'required': True,
        },
        'payment_amount': {
            'required': True,
        },
    }

    def create(self, validated_data):
        # break point to see the flow
        user = validated_data['user']
        owner = Merchant.objects.get(pk=user.pk)
