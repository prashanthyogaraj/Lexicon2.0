# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.views.decorators.cache import cache_control
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.template import loader
from models import starting
from Activity import login
import time


def landing(request):
    if request.method== "POST":
        print "POST"
    return render(request,'landing.html')

def activity(request):
    return render(request,'landing.html')

def Review(request):

    name = request.POST.getlist("eng")
    cmt = request.POST.getlist("area")
    zipped = zip(name,cmt)

    for n,c in zipped:
        te = starting()
        print 'cmt is',c
        print 'name is',n
        te.comment=c
        te.name=n
        te.save()
    # te = test(name=name,comment=cmt)
    # te.comment=cmt
    # te.name=name
    # te.save()
    return render(request,'Activity.html')

def ajax(request):
    li= ['hey','u','come','here']
    print "inisde ajax"
    ip=request.POST.get("ip")
    password = request.POST.get("pass")
    print 'ip is',ip,'and pass is',password
    detail = login.get_adapter_detail(ip,password)
    context = {
        'li' : li,
    }
    print 'detail is',detail
    return HttpResponse(detail)
    # return render(request,'Activity.html',context)

def sample(request):
    lis = ['hey', 'u', 'come', 'here']
    context = {
        'lis': lis,
    }
    return render(request,'sample.html',context)