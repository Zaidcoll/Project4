from django.shortcuts import render
from .models import Product
# Create your views here.

def catalog(request):
    all_products= Product.objects.all()
    return render(request,'shop/catalog.html',{
        'all_products':all_products
    })
