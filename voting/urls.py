from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    
    path('',SignUpView.as_view(),name="signup"),
    path('login',LoginView.as_view(),name="login"),

]
