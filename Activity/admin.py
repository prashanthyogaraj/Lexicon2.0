# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import other_testcases,testbed_config
from django.contrib import admin

# Register your models here.
# admin.site.register(starting)
# field = ('event',)
# readonly_fields = ('event',)

class check(admin.ModelAdmin):
    readonly_fields = ('event',)
    # readonly_fields = ('events',)
admin.site.register(other_testcases,check)
admin.site.register(testbed_config,check)

