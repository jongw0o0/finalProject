from django.shortcuts import render
# from django.http import HttpResponse
from django.urls import path
from . import views

app_name = 'tourlist'

# def index(request):
#     return HttpResponse("hi");

urlpatterns = [
    path('', views.tourlist),
]