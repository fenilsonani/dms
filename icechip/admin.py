from django.contrib import admin

# Register your models here.
from .models import Customer,Delivery

admin.site.register(Customer)
admin.site.register(Delivery)