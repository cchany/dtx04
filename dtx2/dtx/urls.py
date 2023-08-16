from turtle import home
from django.urls import path
from . import views


app_name = 'dtx'

urlpatterns = [
    path('main/', views.Main),]
