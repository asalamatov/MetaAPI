from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def RatingView(request):
    return HttpResponse("Hello World")