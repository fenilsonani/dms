from django.urls import path

from . import views

urlpatterns = [
    path('create_trip/', views.create_trip, name='create_trip'),
    path('add_expenses_transport/', views.add_expense, name='add_expense_transport'),
    path('create_expense_transport/', views.create_expense, name='create_expense_transport'),
    path('display_trips/', views.display_trips, name='display_trips'),
    path('display_expenses_transport_type/', views.display_expenses_type, name='display_expenses_transport_type'),
    path('display_expenses_transport/', views.display_expenses, name='display_expenses_transport'),
    path('edit_expense_transport/<int:expense_id>/', views.edit_expense, name='edit_expense_transport'),
    path('edit_trip/<int:trip_id>/', views.edit_trip, name='edit_trip'),
    path('delete_expense_transport/<int:expense_id>/', views.delete_expense, name='delete_expense_transport'),
    path('delete_trip/<int:trip_id>/', views.delete_trip, name='delete_trip'),
    path('delete_expense_type_transport/<int:expense_id>/', views.delete_expense_type, name='delete_expense_type_transport'),
    path('edit_expense_type_transport/<int:expense_id>/', views.edit_expense_type, name='edit_expense_type_transport'),
]