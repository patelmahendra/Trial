from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Homepage(request):
    return HttpResponse("Hello")

def Indexpage(request):
    return render(request,'Login/index.html')

def Index(request):
    return HttpResponse("Index Page")