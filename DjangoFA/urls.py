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
    path('figurefit/', views.figurefit, name='figurefit'),
    path('customerRev/', views.customerRev, name='customerRev'),
    path('advisor/', views.advisor, name='advisor'),
    path('signup/', views.signup_view, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout_view, name='signout'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    
]
    
