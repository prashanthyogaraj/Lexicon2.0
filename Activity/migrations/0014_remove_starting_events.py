# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-20 12:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Activity', '0013_starting_events'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='starting',
            name='events',
        ),
    ]
