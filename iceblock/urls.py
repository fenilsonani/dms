from django.urls import path

from . import views

urlpatterns = [
    path('create_customer_iceb/', views.create_customer, name='create_customer_iceb'),
    path('create_deliver_iceb/', views.create_delivery, name='create_delivery_iceb'),
    path('display_customer_iceb/', views.display_customer, name='display_customer_iceb'),
    path('display_delivery_iceb/', views.display_delivery, name='display_delivery_iceb'),
    path('edit_customer_iceb/<int:id>/', views.edit_customer, name='edit_customer_iceb'),
    path('edit_delivery_iceb/<int:id>/', views.edit_delivery, name='edit_delivery_iceb'),
    path('delete_customer_iceb/<int:id>/', views.delete_customer, name='delete_customer_iceb'),
    path('delete_delivery_iceb/<int:id>/', views.delete_delivery, name='delete_delivery_iceb'),
]
