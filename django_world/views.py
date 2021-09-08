from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# helper function to return text or other primitive types to caller
def index(request):
    return HttpResponse("Hello from Django!!!")
