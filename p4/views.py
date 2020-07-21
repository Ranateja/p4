from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return HttpResponse("<marquee>Welcome To The Project</marquee>")
def home(request):
    return render(request,"sample1.html")
def second(request):
    return render(request,"directory/sample2.html")
def third(request):
    return render(request,"directory/sample3.html",context={'data':'Rana','name':'Ranateja'})
def fourth(request):
    fruits=['apple','mango','banana','pineapple','avacado']
    return render(request,"directory/sample4.html",{'fruits':fruits})
def fifth(request):
    return render(request,"directory/sample5.html",{'a':10,'b':20})