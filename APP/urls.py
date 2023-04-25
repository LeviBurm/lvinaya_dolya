from django.urls import path
from .views import *

urlpatterns = [
    path('', prochee),
    path('products/', products_view, name = 'products'),
    path('products/<int:id>/', product_view, name = 'product')
]