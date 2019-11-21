from django.shortcuts import render ,HttpResponse
from django.conf import settings
import stripe

# Create your views here.

def ask(request):
    return render(request,'payments/ask.html')
    
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