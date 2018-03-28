# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime

# Create your models here.

# class starting(models.Model):
#     comment = models.CharField(max_length=500,blank=True,null=True)
#     name = models.CharField(max_length=200,blank=True,null=True)
#     # event = models.DateTimeField(auto_now_add=True, blank=True)
#     event = models.DateTimeField(auto_now=True,editable=True)
#     # events = models.DateField(auto_now_add=True, editable=True)
#     def __str__(self):
#         return self.name
class testbed_config(models.Model):
    engineer = models.CharField(max_length=20)
    Tims_id = models.CharField(max_length=50)
    adapter_name = models.CharField(max_length=9999)
    osname = models.CharField(max_length=100)
    boot_method = models.CharField(max_length=100)
    boot_adapter= models.CharField(max_length=100)
    event = models.DateTimeField(auto_now=True, editable=True)

    def __str__(self):
        return self.Tims_id

class other_testcases(models.Model):
    engineer = models.CharField(max_length=20)
    label = models.CharField(max_length=100,blank=True)
    comments = models.CharField(max_length=5000,blank=True,null=True)
    effort = models.CharField(max_length=10,null=True)
    event = models.DateTimeField(auto_now=True,editable=True)

    def __str__(self):
        return self.label + '_'+ self.engineer