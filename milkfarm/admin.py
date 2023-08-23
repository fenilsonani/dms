from django.contrib import admin
from .models import Animal, Labor, Expense, Grass,Payment, DailyProduction,Customer,DailyDelivery
# Register your models here.

admin.site.register(Animal)
admin.site.register(Labor)
admin.site.register(Expense)
admin.site.register(Grass)
admin.site.register(Payment)
admin.site.register(DailyProduction)
admin.site.register(Customer)
admin.site.register(DailyDelivery)