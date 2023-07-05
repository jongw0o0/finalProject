from django.shortcuts import render
from django.urls import path
from . import views

app_name = 'tourresult'

urlpatterns = [
    path('', views.tourdetail), # 상세피이지 필요
]
