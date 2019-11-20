
from django.urls import path, include
from accounts.views import index, logout , login , profile , register
from .views import create_item

urlpatterns = [
    path('create',create_item, name = 'create_item')
]