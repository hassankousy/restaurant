import imp
from django.shortcuts import render

from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

def index(request):
    return render (request,'restaurant\index.html')
