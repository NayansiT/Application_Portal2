from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from applications import views

urlpatterns = [
    path('', include('applications.urls')),
]