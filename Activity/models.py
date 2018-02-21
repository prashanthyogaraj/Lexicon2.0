# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime

# Create your models here.

class starting(models.Model):
    comment = models.CharField(max_length=500,blank=True,null=True)
    name = models.CharField(max_length=200,blank=True,null=True)
    # event = models.DateTimeField(auto_now_add=True, blank=True)
    event = models.DateTimeField(auto_now=True,editable=True)
    # events = models.DateField(auto_now_add=True, editable=True)
    def __str__(self):
        return self.name