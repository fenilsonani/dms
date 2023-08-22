from django.urls import path

from . import views

urlpatterns = [
    path('create_trip/', views.create_trip, name='create_trip'),
    path('add_expenses/', views.add_expense, name='add_expenses'),
    path('create_expense/', views.create_expense, name='create_expense'),
    path('display_trips/', views.display_trips, name='display_trips'),
    path('display_expenses_type/', views.display_expenses_type, name='display_expenses_type'),
    path('display_expenses/', views.display_expenses, name='display_expenses'),
    path('edit_expense/<int:expense_id>/', views.edit_expense, name='edit_expense'),
    path('edit_trip/<int:trip_id>/', views.edit_trip, name='edit_trip'),
    path('delete_expense/<int:expense_id>/', views.delete_expense, name='delete_expense'),
    path('delete_trip/<int:trip_id>/', views.delete_trip, name='delete_trip'),
    path('delete_expense_type/<int:expense_id>/', views.delete_expense_type, name='delete_expense_type'),
    path('edit_expense_type/<int:expense_id>/', views.edit_expense_type, name='edit_expense_type'),
]