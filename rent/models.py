from django.db import models

class House(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Rental(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    rent_paid = models.BooleanField(default=False)
    tenant_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)

    def __str__(self):
        return f"Rental for {self.house.name} - {self.tenant_name}"