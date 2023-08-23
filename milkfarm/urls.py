from django.urls import path

from . import views

urlpatterns = [
    path('create_animal/', views.create_animal, name='create_animal'),
    path('create_labor/', views.create_labor, name='create_labor'),
    path('create_expense/', views.create_expense, name='create_expense'),
    path('create_grass/', views.create_grass, name='create_grass'),
    path('edit_animal/<int:animal_id>/', views.update_animal, name='edit_animal'),
    path('edit_labor/<int:labor_id>/', views.update_labor, name='edit_labor'),
    path('edit_milk_expense/<int:expense_id>/', views.update_expense, name='edit_expense'),
    path('edit_grass/<int:grass_id>/', views.update_grass, name='edit_grass'),
    path('delete_animal/<int:animal_id>/', views.delete_animal, name='delete_animal'),
    path('delete_labor/<int:labor_id>/', views.delete_labor, name='delete_labor'),
    path('delete_milk_expense/<int:expense_id>/', views.delete_expense, name='delete_expense'),
    path('delete_grass/<int:grass_id>/', views.delete_grass, name='delete_grass'),
    path('create_payment/', views.create_payment, name='create_payment'),
    path('create_daily_production/', views.create_daily_production, name='create_daily_production'),
    path('create_customer/', views.create_customer, name='create_customer'),
    path('edit_payment/<int:payment_id>/', views.update_payment, name='edit_payment'),
    path('edit_daily_production/<int:daily_production_id>/', views.update_daily_production,
            name='edit_daily_production'),
    path('edit_customer/<int:customer_id>/', views.update_customer, name='edit_customer'),
    path('delete_payment/<int:payment_id>/', views.delete_payment, name='delete_payment'),
    path('delete_daily_production/<int:daily_production_id>/', views.delete_daily_production,
            name='delete_daily_production'),
    path('delete_customer/<int:customer_id>/', views.delete_customer, name='delete_customer'),
    path('create_daily_delivery/', views.create_daily_delivery, name='create_daily_delivery'),
    path('edit_daily_delivery/<int:daily_delivery_id>/', views.update_daily_delivery,
            name='edit_daily_delivery'),
    path('delete_daily_delivery/<int:daily_delivery_id>/', views.delete_daily_delivery,
            name='delete_daily_delivery'),
]
