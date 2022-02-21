'''
Created on Feb 18, 2022

@author: shamim
'''
from django.contrib import admin 
from Student import views
from django.urls.conf import path

urlpatterns= [
     path('admin/', admin.site.urls),  
    path('std', views.std),  
    path('show',views.show), 
     path("", views.home, name="home"),
    ]
