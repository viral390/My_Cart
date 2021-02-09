from django.shortcuts import render
from django.http import HttpResponse
from .models import product, Contact
from math import ceil

# Create your views here.

def index(request):
    # products = product.objects.all()
    # print(products)
    # n = len(products)
    # nslides= n//4 + ceil((n/4)-(n//4))
    # param = {'no_of_slides': nslides,'range':range(1,nslides), 'product':products}
    # allproducts= [[products, range(1, nslides), nslides], [products, range(1, nslides), nslides]] (old list)
    allproducts = []
    catproducts = product.objects.values('category','id')
    cats = {item['category'] for item in catproducts}
    for cat in cats:
        prod =product.objects.filter(category=cat)
        n = len(prod)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        allproducts.append([prod, range(1,nslides), nslides])
    param ={'allproducts': allproducts}
    return render(request, 'shop/index.html', param)





def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    if request.method == "POST":
        name =request.POST.get("name", "")
        email =request.POST.get("email", "")
        phone =request.POST.get("phone", "")
        desc =request.POST.get("desc", "")
        print(name, email, phone, desc)
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')





def search(request):
    return render(request, 'shop/search.html')

def productviews(request,myid):
    # fetch the product using the id
    products = product.objects.filter(id=myid)

    return render(request, 'shop/productviews.html', {'product':products[0]})

def checkout(request):
    return render(request, 'shop/checkout.html')


def tracker(request):
    return render(request, 'shop/tracker.html')
