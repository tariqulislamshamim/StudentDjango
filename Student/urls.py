'''
Created on Feb 18, 2022

@author: shamim
'''
from django.contrib import admin 
from Student import views
from django.urls.conf import path

urlpatterns= [ 
    path('std', views.std, name='addstd'),  
    path('show',views.show, name="show"), 
     path("", views.home, name="home"),
     path("absent/",views.absent,name='absent'),
     path("base",views.base),
    ]
