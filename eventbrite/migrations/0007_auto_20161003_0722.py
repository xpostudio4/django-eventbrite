# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-03 11:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventbrite', '0006_auto_20161002_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]