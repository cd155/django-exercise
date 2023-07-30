from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def homepage(request): 
    return HttpResponse("Hello, world. Demoapp.") 

def drinks(request, drink):
    return HttpResponse(f'My drinks is {drink}.') 
