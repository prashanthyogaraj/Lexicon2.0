# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Login(models.Model):
    user = models.CharField(max_length=250)
    pswd = models.CharField(max_length=250)
    nickname = models.CharField(max_length=20)

    def __str__(self):
        return self.nickname
# Create your models here.
