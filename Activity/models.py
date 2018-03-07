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

class other_testcases(models.Model):
    engineer = models.CharField(max_length=20)
    label = models.CharField(max_length=100,blank=True)
    comments = models.CharField(max_length=5000,blank=True,null=True)
    effort = models.CharField(max_length=10,null=True)
    event = models.DateTimeField(auto_now=True,editable=True)

    def __str__(self):
        return self.label + '_'+ self.engineer