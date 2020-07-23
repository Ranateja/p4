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
def urls_data(request,name):
    return HttpResponse("<h1>{}</h1>".format(name))
'''def ab(request,ab):
    a=ab.split(' ')
    sum=int(a[0])+int(a[1])
    return HttpResponse(str(sum))'''

def ab(request,a,b):
    sum=int(a)+int(b)
    return HttpResponse(str(sum))

def cd(request,cd):
    e=cd.split(' ')
    if int(e[0]) > int(e[1]):
        return HttpResponse(str(e[0]))
    else:
        return HttpResponse(str(e[1]))

def xy(request,x,y,z):
    if int(x > y) and int(x > z):
        return HttpResponse('The greatest value is {}'.format(x))
    elif int(y > x) and (y > z):
        return HttpResponse('The greatest value is {}'.format(y))
    else:
        return HttpResponse('The greatest value is {}'.format(z))

def rv(request,str):
    r='aeiouAEIOU'
    vowels=0
    consonants=0
    for i in str:
        if i in r:
            vowels+=1
        else:
            consonants+=1
        return render(request,"directory/sample6.html",{'string':str,'vowels': vowels,'consonants':consonants})

