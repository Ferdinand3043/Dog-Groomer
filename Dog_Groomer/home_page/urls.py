from django.contrib import admin
from django.urls import path
from . import views
from .views import information



urlpatterns = [

    path('information/', views.information, name='AboutUs'),
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),

]
