from django.contrib import admin
from .models import Farm,Expense,Season,SeasonExpense,Crop
# Register your models here.

admin.site.register(Farm)
admin.site.register(Expense)
admin.site.register(Season)
admin.site.register(SeasonExpense)
admin.site.register(Crop)
