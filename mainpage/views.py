from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Board

# Create your views here.
def home(request):
    return render(request, 'base.html')

# def signup(request):
#     return render(request, 'signup.html')

# def login(request):
#     return render(request, 'login.html')