# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-12 13:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('merchants', '0006_auto_20190512_1253'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paymentform',
            options={'ordering': ['-creation_date'], 'verbose_name': 'payment form', 'verbose_name_plural': 'payment forms'},
        ),
        migrations.RenameField(
            model_name='paymentform',
            old_name='created_date',
            new_name='creation_date',
        ),
        migrations.AlterField(
            model_name='paymentform',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_forms', to='merchants.Merchant', verbose_name='owner'),
        ),
        migrations.AlterField(
            model_name='paymentform',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='paymentform',
            name='payable_times',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='payable count'),
        ),
        migrations.AlterField(
            model_name='paymentform',
            name='price',
            field=models.PositiveIntegerField(verbose_name='payment amount'),
        ),
    ]
