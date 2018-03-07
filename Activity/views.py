# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.views.decorators.cache import cache_control
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.template import loader
from models import other_testcases
from login.models import Login
from Activity import login_server
from django.conf import settings
import django.contrib.sessions
from  django.contrib.sessions.backends.db import *
import time

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def landing(request):
    if request.method== "POST":
        print "POST"
        uname1 = request.POST.get("uname")
        passwd = request.POST.get("pswd")
        request.session['uname'] = uname1

        print "Hey session of u1 is",uname1
        user_database = Login.objects.filter(user__startswith=str(uname1))
        context = {
            'user_database': user_database

        }
        ua = request.session['uname']
        if not user_database:
            return render(request,'nouser.html')
        else:
            for user in user_database:
                if passwd ==user.pswd:
                    print 'user name is',user,'and passwd is',passwd,'adn it matched'

                    return render(request,'landing.html',context)
                else:
                    return render(request, 'login_pswd.html')
    elif request.method == "GET":
        return render(request, 'error404.html')

# def activity(request):
#     return render(request,'landing.html')
def save_othertestcase(request):
    print 'inside save_othertestcase'
    uname = request.session['uname']
    user_database = Login.objects.filter(user__startswith=str(uname))
    context = {
        'user_database' : user_database
    }

    if not user_database:
        return render(request, 'nouser.html')

    elif request.method=='POST' and user_database:
        engineer = uname
        other_testcases_obj = other_testcases()
        print 'engineer is',engineer
        txtarea  =request.POST.getlist('txtareanam')
        efrt = request.POST.getlist('effortname')
        labl = request.POST.getlist('labl')
        save_zip = zip(txtarea,efrt,labl)
        for textarea,effort,label in save_zip:
            other_testcases_obj = other_testcases()
            print 'textarea is',textarea,'effort is',effort,'lable is',label
            other_testcases_obj.label=label
            other_testcases_obj.comments=textarea
            other_testcases_obj.effort=effort
            other_testcases_obj.engineer = engineer
            other_testcases_obj.save()

    return render(request,'landing.html',context)

def Review(request):

    name = request.POST.getlist("ip")
    cmt = request.POST.getlist("pass")
    zipped = zip(name,cmt)

    for n,c in zipped:
        # te = starting()
        print 'cmt is',c
        print 'name is',n
        # te.comment=c
        # te.name=n
        # te.save()
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
    detail = login_server.get_adapter_detail(ip, password)
    context = {
        'li' : li,
    }
    print 'detail is',detail
    return HttpResponse(detail)
    # return render(request,'Activity.html',context)

