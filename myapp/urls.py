from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
      path('',views.index,name="index"),
      path('signup/',views.sign,name="signup"),
      path('sign/',views.sign,name="sign"),
]
