from django.shortcuts import render
from django.http import HttpResponse, Http404
import datetime as dt

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to django')

# def news_of_day(request):
