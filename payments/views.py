from django.shortcuts import render ,HttpResponse
from django.conf import settings
from cart.models import CartItem
import stripe

# Create your views here.

def ask(request):
    all_cart_items= CartItem.objects.filter(owner=request.user)
    total_cost = 0
    for cart_item in all_cart_items:
        total_cost += cart_item.product.cost * cart_item.quantity
    return render(request,'payments/ask.html',{
        'total_cost':total_cost
    })
    
def payments(request):
    if request.method == 'GET':
        amount = request.GET['amount']
        stripe_publishable_key = settings.STRIPE_PUBLISHABLE_KEY
        return render(request,'payments/payments.html',{
            'stripe_key': stripe_publishable_key,
            'amount_dollars':amount,
            'amount':int(amount)*100
        })
    else:
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe_token = request.POST['stripeToken']
        charge = stripe.Charge.create(amount=request.POST['amount'],
        currency='sgd',
        source=stripe_token)
        return HttpResponse("Thank you for your purchase!")