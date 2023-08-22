from django.urls import path

from .views import dashboard,add_user_into_system,add_normal_user

urlpatterns = [
    path('', dashboard, name='login_admin'),
    path('add_user/', add_user_into_system, name='add_user'),
    path('add_normal/', add_normal_user, name='add_normal'),
]
