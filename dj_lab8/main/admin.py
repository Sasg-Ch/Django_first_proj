from django.contrib import admin
from .models import Customer, Item, Storage, Sale
# Register your models here.
admin.site.register(Customer)
admin.site.register(Item)
admin.site.register(Storage)
admin.site.register(Sale)