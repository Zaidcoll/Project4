from django.urls import path, include
from .views import add_to_cart

urlpatterns = [
    path('add_to_cart/<product_id>',add_to_cart,name='add_to_cart')
    
    
] 
