from django.forms.forms import Form
from django.shortcuts import render
from django.http import HttpResponse
from .forms import addorderform

# Create your views here.



def oindex(request):
    return HttpResponse("Hello you are in order index")

def addorder(request):
    form=addorderform(request.POST)
    if request.method=="POST":
        if form.is_valid():
            form.save()
            HttpResponse("Product added sucessfully")


    return render(request,'addorder.html',{'form':form})
