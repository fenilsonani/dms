from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=10)

    # Add any other fields you need for customers

    def __str__(self):
        return self.name


class Delivery(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField()
    daily_ice_block_given = models.PositiveIntegerField()
    one_ice_block_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_ice_block_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    additional_transportation_charge = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_charge = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"Delivery for {self.customer} on {self.date}"

    class Meta:
        ordering = ['-date']

# You can add more fields to the models as needed.
