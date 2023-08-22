from django.contrib import admin
from .models import Business, AdminUser, NormalUser
# Register your models here.

admin.site.register(Business)
admin.site.register(AdminUser)
admin.site.register(NormalUser)