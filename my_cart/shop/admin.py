from django.contrib import admin

# Register your models here.
from .models import product,Contact,orders

admin.site.register(product)
admin.site.register(Contact)
admin.site.register(orders)