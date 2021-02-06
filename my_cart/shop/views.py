from django.shortcuts import render
from django.http import HttpResponse
from .models import product
from math import ceil

# Create your views here.

def index(request):
    products = product.objects.all()
    print(products)
    n = len(products)
    nslides= n//4 + ceil((n/4)-(n//4))
    # param = {'no_of_slides': nslides,'range':range(1,nslides), 'product':products}
    allproducts= [[products, range(1, nslides), nslides], [products, range(1, nslides), nslides]]
    param= {'allproducts': allproducts}
    return render(request, 'shop/index.html', param)


def about(request):
    return render(request, 'shop/about.html')


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
