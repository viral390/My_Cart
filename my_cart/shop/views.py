from django.shortcuts import render
from django.http import HttpResponse
from .models import product, Contact , Order , Orderupdate
from math import ceil

# Create your views here.

def index(request):
    allproducts = []
    catproducts = product.objects.values('category','id')
    cats = {item['category'] for item in catproducts}
    for cat in cats:
        prod =product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allproducts.append([prod, range(1, nSlides), nSlides])
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
    if request.method == "POST":
        items_json = request.POST.get("items_json","")
        name =request.POST.get("name", "")
        email =request.POST.get("email", "")
        mobile =request.POST.get("mobile", "")
        add1 =request.POST.get("add1", "")
        add2 =request.POST.get("add2", "")
        city =request.POST.get("city", "")
        state =request.POST.get("state", "")
        zip_code =request.POST.get("zip_code", "")
        print(items_json,name, email, mobile, add1, add2, city, state, zip_code)
        order = Order(items_json=items_json,name=name, email=email, mobile=mobile, add1=add1, add2=add2, city=city, state=state, zip_code=zip_code )
        order.save()
        update=Orderupdate(order_id=order.Order_id, update_desc="order has been placed")
        update.save()
        thank = True
        id = order.Order_id
        return render(request, 'shop/checkout.html',{'thank':thank, 'id':id})
    return render(request , 'shop/checkout.html')


def tracker(request):
    return render(request, 'shop/tracker.html')
