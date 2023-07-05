from django.shortcuts import render
from django.http import HttpResponse
from .models import result

# Create your views here.
def result(request):
    # result_list = result.subject.order_by('-create_date')
    result_list = result
    context = {'result_list' : result_list}
    return render(request, 'tourresult/tourresult.html', context)
