from django.shortcuts import render
# from django.http import HttpResponse
from django.urls import path
from . import views

app_name = 'savearea'

# def index(request):
#     return HttpResponse("hi");

urlpatterns = [
    path('', views.home),
]