# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-20 10:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Activity', '0006_auto_20180220_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='starting',
            name='event',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 20, 15, 30, 42, 51000), editable=False),
        ),
    ]
