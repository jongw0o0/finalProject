from django.shortcuts import render
from django.http import HttpResponse
# from .models import 모델이름

# Create your views here.

def home(request):
    return render(request, 'savearea/savearea.html') # html 바꿔야함

# def 모델이름(request):
#     # result_list = result.subject.order_by('-create_date')
#     result_list = result
#     context = {'result_list' : result_list}
#     return render(request, 'tourresult/tourresult.html', context)
