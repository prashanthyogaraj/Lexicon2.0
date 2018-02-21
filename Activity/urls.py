

from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'dashboard/', views.landing,name='landing'),
    url(r'^Activity',views.activity,name='activity'),
    url(r'^Review',views.Review,name='Review'),
    url(r'^Ajax/request/',views.ajax,name='ajax'),
    url(r'^sample',views.sample,name='sample'),

]
