from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def pindex(request):
    return HttpResponse("Hello you are in product index")
