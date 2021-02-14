from django.contrib import admin

# Register your models here.
from .models import product,Contact,Order,Orderupdate

admin.site.register(product)
admin.site.register(Contact)
admin.site.register(Order)
admin.site.register(Orderupdate)