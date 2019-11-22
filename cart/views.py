from django.shortcuts import render,reverse,redirect
from .models import CartItem
from shop.models import Product

# Create your views here.
def add_to_cart(request,product_id):
    product = Product.objects.get(pk=product_id)
    existing_cart_item = CartItem.objects.get(owner = request.user, product = product)
    
    if existing_cart_item == None:
        new_cart_item = CartItem()
        new_cart_item.product = product
        new_cart_item.owner = request.user
        new_cart_item.quantity = 1
        new_cart_item.save()
    else:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    return redirect(reverse('catalog'))
