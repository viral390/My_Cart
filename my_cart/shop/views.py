from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'shop/index.html')

def about(request):
    return HttpResponse("this is my about page")


def contact(request):
    return HttpResponse("this is my contact page")

def search(request):
    return HttpResponse("this is my search page")

def productviews(request):
    return HttpResponse("this is my product views page")


def checkout(request):
    return HttpResponse("this is my checkout  page")


def tracker(request):
    return HttpResponse("this is my tracker page")