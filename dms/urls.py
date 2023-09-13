"""
URL configuration for dms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('secre/dev/admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', views.index, name='index'),
    path('dashboard/', include('dashboard.urls')),
    path('dashboard/farm/', include('farm.urls')),
    path('dashboard/transport/', include('transport.urls')),
    path('dashboard/iceblock/', include('iceblock.urls')),
    path('dashboard/rent/', include('rent.urls')),
    path('dashboard/milk/', include('milkfarm.urls')),
    path('dashboard/icechip/', include('icechip.urls')),
    path('dashboard/rowater/', include('rowater.urls')),
    path('comming_soon/', views.comming_soon, name='comming_soon'),
]