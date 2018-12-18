from django.http import *
from django.shortcuts import render
from .forms import *
from django.contrib import messages

def login(request):
    if request.method=='POST':
        form=student(request.POST)
        if(form.is_valid()):
            form.save()
            return HttpResponseRedirect('/login/')
    else:
        form=student()

    return render(request,'login.html',{'form':form})


def th(request):
    return  HttpResponse("<h1> jyghvvhjvhjhj</h1>")


