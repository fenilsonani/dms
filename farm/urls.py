from django.urls import path

from . import views

urlpatterns = [
    path('create_crop/', views.create_crop, name='create_crop'),
    path('create_expense_type/', views.create_expense_type, name='create_expense_type'),
    path('create_season/', views.create_season, name='create_season'),
    path('create_expense/', views.create_season_expense, name='create_season_expense'),
    path('create_farm/', views.create_farm, name='create_farm'),
    path('display_farms/', views.display_farm, name='display_farms'),
    path('edit_farm/<int:id>/', views.edit_farm, name='edit_farm'),
    path('delete_farm/<int:id>/', views.delete_farm, name='delete_farm'),
    path('display_crops/', views.display_crop, name='display_crops'),
    path('edit_crop/<int:id>/', views.edit_crop, name='edit_crop'),
    path('delete_crop/<int:id>/', views.delete_crop, name='delete_crop'),
    path('display_expense_type/', views.display_expense_type, name='display_expense_type'),
    path('edit_expense_type/<int:id>/', views.edit_expense_type, name='edit_expense_type'),
    path('delete_expense_type/<int:id>/', views.delete_expense_type, name='delete_expense_type'),
    path('display_season/', views.display_season, name='display_season'),
    path('edit_season/<int:id>/', views.edit_season, name='edit_season'),
    path('delete_season/<int:id>/', views.delete_season, name='delete_season'),
    path('display_expense/', views.display_season_expense, name='display_expense'),
    path('edit_expense/<int:id>/', views.edit_season_expense, name='edit_expense'),
    path('delete_expense/<int:id>/', views.delete_season_expense, name='delete_expense'),
]