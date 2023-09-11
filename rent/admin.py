from django.contrib import admin
from .models import House, RentalPerson,RentPayment


# Register your models here.
admin.site.register(House)
admin.site.register(RentalPerson)
admin.site.register(RentPayment)
