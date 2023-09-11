from django.urls import path

from . import views

urlpatterns = [
    path('create_customer_icechip/', views.create_customer, name='create_customer_icechip'),
    path('create_delivery_icechip/', views.create_delivery, name='create_delivery_icechip'),
    path('display_customer_icechip/', views.display_customer, name='display_customer_icechip'),
    path('display_delivery_icechip/', views.display_delivery, name='display_delivery_icechip'),
    path('edit_customer_icechip/<int:id>/', views.edit_customer, name='edit_customer_icechip'),
    path('edit_delivery_icechip/<int:id>/', views.edit_delivery, name='edit_delivery_icechip'),
    path('delete_customer_icechip/<int:id>/', views.delete_customer, name='delete_customer_icechip'),
    path('delete_delivery_icechip/<int:id>/', views.delete_delivery, name='delete_delivery_icechip'),
]
