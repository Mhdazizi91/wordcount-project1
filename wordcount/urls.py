from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('countthewords/', views.count, name='count'),
    path('aboutpage/', views.about, name='about'),
]
