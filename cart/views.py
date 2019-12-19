from django.shortcuts import render,reverse,redirect
from .models import CartItem
from django.conf import settings
from shop.models import Product
import stripe

def view_cart(request):
    all_cart_items = CartItem.objects.filter(owner=request.user)
    stripe_publishable_key = settings.STRIPE_PUBLISHABLE_KEY
    total_cost = 0
    for cart_item in all_cart_items:
        total_cost += cart_item.product.cost * cart_item.quantity
    return render(request,'cart/view_cart.html',{
        'all_cart_items':all_cart_items,
        'stripe_key':stripe_publishable_key,
        'amount_instripe':int(total_cost)*100,
        'total_cost':total_cost
    })
    

def add_to_cart(request,product_id):
    product = Product.objects.get(pk=product_id)
    existing_cart_item = CartItem.objects.filter(owner = request.user, product = product).first()
    
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
    

    

def remove_from_cart(request,cart_item_id):
    
    existing_cart_item=CartItem.objects.get(pk=cart_item_id)
    existing_cart_item.delete()
    return redirect(reverse('view_cart'))

