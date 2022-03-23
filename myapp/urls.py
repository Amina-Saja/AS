from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
      path('',views.index,name="index"),
      path('signup/',views.sign,name="signup"),
      path('home/',views.sign,name="home"),
      path('sign/',views.signin,name="sign"),
      path('login/',views.login,name="login"),
]
