# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-03 11:39
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventbrite', '0007_auto_20161003_0722'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='display_price',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=5),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
