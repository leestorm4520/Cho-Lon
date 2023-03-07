from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.getAllProducts, name='products'),
    path('products/<str:pk>/', views.getProduct, name='product')
]