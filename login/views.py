# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from django.views.decorators.cache import cache_control
from . models import Login
# Create your views here.

def login_extra(request):
    return render(request, 'login.html')

def logout_extra(request):
    del request.session['uname']
    return render(request, 'login.html')


def admin_signout(request):
    return redirect('/')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def validate(request):
    if request.method == 'POST':

        uname = request.POST.get('uname')
        pswd = request.POST.get('pswd')
        user_existence = Login.objects.filter(user__startswith=str(uname))
        print str(uname)
        print user_existence
        if not user_existence:
            return render(request, 'nouser.html')
        else:
            for username in user_existence:
                if pswd == username.pswd:
                    context = {
                        'user_existance': user_existence
                    }
                    return render(request, 'newhtml1.html', context)
                else:
                    return render(request, 'login_pswd.html')
    elif request.method == 'GET':

        return render(request, 'error404.html')


def admin_home(request):
    uname = request.POST['uname']
    pswd = request.POST['pswd']

    user = authenticate(username=uname, password=pswd)
    print "User obj is ", user
    if user is not None:
        if user.is_active:
            login(request, user)
            print 'redirecting page'
            return redirect('/admin/')

    return render(request, 'error404.html')