from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    peoples =[
        {'name' : 'asasd','age' : 52},
        {'name' : 'kartik','age' : 45},
        {'name' : 'sambhav','age' : 32},
        {'name' : 'sanyam','age' : 15},
        {'name' : 'aman','age' : 42},
    ]
    return render(request,"home.html",context={'peoples': peoples})
# Create your views here.

def about(request):
    return render (request,"about.html")

def base(request):
    return render(request,"base.html")
