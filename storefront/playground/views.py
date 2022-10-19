from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# A view functions is a function that takes a request
# and returns a response
# this is commonly known as a request handler

def say_hello(request):
    return HttpResponse('Hello World!')