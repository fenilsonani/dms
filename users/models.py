from django.db import models
from django.contrib.auth.models import User

class Business(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class AdminUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=True)
    def __str__(self):
        return self.user.username

class NormalUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username