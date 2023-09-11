from django.urls import path
from . import views

urlpatterns = [
    path('create_house/', views.create_house, name='create_house'),
    path('create_rental/', views.create_rental, name='create_rental'),
    path('display_house/', views.display_house, name='display_house'),
    path('display_rental/', views.display_rental, name='display_rental'),
    path('edit_house/<int:id>/', views.edit_house, name='edit_house'),
    path('edit_rental/<int:id>/', views.edit_rental, name='edit_rental'),
    path('delete_house/<int:id>/', views.delete_house, name='delete_house'),
    path('delete_rental/<int:id>/', views.delete_rental, name='delete_rental'),
    path('create_payment_rent/', views.add_rent_payment, name='create_payment_rent'),
    path('display_payment_rent/', views.display_rent_payment, name='display_payment_rent'),
    path('edit_payment_rent/<int:id>/', views.edit_rent_payment, name='edit_payment_rent'),
    path('delete_payment_rent/<int:id>/', views.delete_rent_payment, name='delete_payment_rent'),
]