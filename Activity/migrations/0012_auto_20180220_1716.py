# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-20 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Activity', '0011_auto_20180220_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='starting',
            name='event',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
