from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'landing/index.html')


def comming_soon(request):
    return render(request,'landing/comming_soon.html')