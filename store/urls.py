from django.urls import path
from . import views

urlpatterns = [
    path('product-list/', views.product_list, name='product_list'),
    path('add/', views.add_products, name='add_product'),
   
]
