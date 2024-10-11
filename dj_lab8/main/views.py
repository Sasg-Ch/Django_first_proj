from django.shortcuts import render
from .models import Storage, Customer, Item, Sale
# Create your views here.
def index(request):
    storages = Storage.objects.all()
    customers = Customer.objects.all()
    items = Item.objects.all()
    sales = Sale.objects.all()

    context = {
        'storages': storages,
        'customers': customers,
        'items': items,
        'sales': sales
    }

    return render(request, 'main/index.html',context)