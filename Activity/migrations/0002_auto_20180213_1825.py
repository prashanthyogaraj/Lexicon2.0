# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-13 12:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Activity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='comment',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='test',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
