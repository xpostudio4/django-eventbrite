# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-05 13:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventbrite', '0015_auto_20161005_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='start_date',
            field=models.DateTimeField(null=True),
        ),
    ]