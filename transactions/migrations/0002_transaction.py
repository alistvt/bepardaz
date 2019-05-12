# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-08 13:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('merchants', '0004_auto_20190508_1346'),
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField(verbose_name='price')),
                ('status', models.IntegerField(null=True)),
                ('started_date', models.DateTimeField(auto_now_add=True, verbose_name='creation date')),
                ('ended_date', models.DateTimeField(auto_now_add=True, verbose_name='end date')),
                ('payer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='transactions', to='transactions.Payer', verbose_name='payer')),
                ('payment_form', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='transactions', to='merchants.PaymentForm', verbose_name='payment form')),
            ],
            options={
                'verbose_name': 'transaction',
                'verbose_name_plural': 'transactions',
                'ordering': ['-started_date'],
            },
        ),
    ]