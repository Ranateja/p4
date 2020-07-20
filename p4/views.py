from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return HttpResponse("<marquee>Welcome To The Project</marquee>")
def home(request):
    return render(request,"sample1.html")
def second(request):
    return render(request,"directory/sample2.html")