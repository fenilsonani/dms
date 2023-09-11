from django.db import models


class House(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class RentalPerson(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,default=0)
    amount_pending = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,default=0)
    house = models.ForeignKey(House, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class RentPayment(models.Model):
    rental_person = models.ForeignKey(RentalPerson, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    PAYMENT_METHOD_CHOICES = (
        ('cash', 'Cash'),
        ('gpay', 'GPay'),
        ('phonepe', 'PhonePe'),
        ('paytm', 'Paytm'),
    )
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    payment_id = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"Payment of {self.rental_person} on {self.date}"

    def save(self, *args, **kwargs):
        self.rental_person.amount_paid += self.amount
        self.rental_person.amount_pending -= self.amount
        self.rental_person.save()
        super().save(*args, **kwargs)
