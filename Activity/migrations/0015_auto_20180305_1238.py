# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-05 07:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Activity', '0014_remove_starting_events'),
    ]

    operations = [
        migrations.CreateModel(
            name='other_testcases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('engineer', models.CharField(max_length=20)),
                ('comments', models.CharField(blank=True, max_length=5000, null=True)),
                ('effort', models.CharField(max_length=10, null=True)),
                ('event', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='starting',
        ),
    ]
