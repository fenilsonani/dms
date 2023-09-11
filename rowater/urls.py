from django.urls import path

from . import views

urlpatterns = [
    path('create_customer_rowater/', views.create_customer, name='create_customer_rowater'),
    path('create_delivery_rowater/', views.create_delivery, name='create_delivery_rowater'),
    path('display_customer_rowater/', views.display_customer, name='display_customer_rowater'),
    path('display_delivery_rowater/', views.display_delivery, name='display_delivery_rowater'),
    path('edit_customer_rowater/<int:id>/', views.edit_customer, name='edit_customer_rowater'),
    path('edit_delivery_rowater/<int:id>/', views.edit_delivery, name='edit_delivery_rowater'),
    path('delete_customer_rowater/<int:id>/', views.delete_customer, name='delete_customer_rowater'),
    path('delete_delivery_rowater/<int:id>/', views.delete_delivery, name='delete_delivery_rowater'),
]
