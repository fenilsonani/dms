from django.urls import path
from . import views

urlpatterns = [
    path('create_customer/', views.create_customer, name='create_customer'),
    path('create_delivery/', views.create_delivery, name='create_delivery'),
    path('display_customer/', views.display_customer, name='display_customer'),
    path('display_delivery/', views.display_delivery, name='display_delivery'),
    path('edit_customer/<int:id>/', views.edit_customer, name='edit_customer'),
    path('edit_delivery/<int:id>/', views.edit_delivery, name='edit_delivery'),
    path('delete_customer/<int:id>/', views.delete_customer, name='delete_customer'),
    path('delete_delivery/<int:id>/', views.delete_delivery, name='delete_delivery'),
]