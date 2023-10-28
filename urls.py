"""
Definition of urls for DjangoFA.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('bodyshape/', views.bodyshape_view, name='bodyshape'),
    path('skintype/', views.skintype_view, name='skintype'),
]
    
