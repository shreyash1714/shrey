from django.shortcuts import render
from django.shortcuts import redirect,render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello index from customer")
