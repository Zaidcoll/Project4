from django.urls import path
from .views import payments,ask

urlpatterns = [
    path('ask',ask,name = 'ask'),
    path('payments',payments,name = 'payments')
]