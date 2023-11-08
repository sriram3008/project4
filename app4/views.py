from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def itachi(request):
    return HttpResponse("<h1> ITACHI UCHIHA </h1>")

def gengutsu(request):
    return HttpResponse("<h1><marquee> u r already under in my gengutsu</h1></marquee>")
    
