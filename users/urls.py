from .views import login_admin, login_normal,logout_user, dashboard
from django.urls import path


# Path: users/urls.py

urlpatterns = [
    path('login_admin/', login_admin, name='login_admin'),
    path('login_normal/', login_normal, name='login_normal'),
    path('logout/', logout_user, name='logout'),
    path('dashboard/', dashboard, name='admin_dash'),
]