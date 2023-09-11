from django.db import models


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=10)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    pending_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)

    # Add any other fields you need for customers

    def __str__(self):
        return self.name


class Delivery(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField()
    daily_ice_block_given = models.PositiveIntegerField()
    one_ice_chip_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_ice_chip_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    additional_transportation_charge = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_charge = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"Delivery to {self.customer} on {self.date}"

    def save(self, *args, **kwargs):
        self.total_ice_chip_price = self.daily_ice_block_given * self.one_ice_chip_price
        self.total_charge = self.total_ice_chip_price + self.additional_transportation_charge
        self.customer.pending_amount += self.total_charge
        self.customer.save()
        super().save(*args, **kwargs)

    def update(self, *args, **kwargs):
        self.total_ice_chip_price = self.daily_ice_block_given * self.one_ice_chip_price
        self.total_charge = self.total_ice_chip_price + self.additional_transportation_charge
        self.customer.pending_amount += self.total_charge
        self.customer.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.customer.pending_amount -= self.total_charge
        self.customer.save()
        super().delete(*args, **kwargs)
