# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-11-11 21:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventbrite', '0016_auto_20161005_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='include_fee',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='max',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='min',
            field=models.IntegerField(),
        ),
    ]