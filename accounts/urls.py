from accounts import views
from django.urls import path
urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.authlogin, name="login"),
    path('logout/',views.logout, name='logout')

]



