from django.contrib import admin
from .models import Trips, Expense,TransportExpenses
# Register your models here.

admin.site.register(Trips)
admin.site.register(Expense)
admin.site.register(TransportExpenses)