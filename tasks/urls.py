
from django.urls import path, include
from accounts.views import index, logout , login , profile , register
from .views import create_item, show_item

urlpatterns = [
    path('create',create_item, name = 'create_item'),
    path('', show_item, name='show_item')
]