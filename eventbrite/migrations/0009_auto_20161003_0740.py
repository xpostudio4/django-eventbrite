# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-03 11:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventbrite', '0008_auto_20161003_0739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='display_price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
