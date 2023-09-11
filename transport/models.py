import datetime

from django.db import models

class Expense(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class TransportExpenses(models.Model):
    name= models.ForeignKey(Expense, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date=models.DateField(default=datetime.date.today)
    def __str__(self):
        return f"{self.name}: {self.amount}"


class Trips(models.Model):
    starting_km = models.PositiveIntegerField()
    ending_km = models.PositiveIntegerField()
    money_collected = models.DecimalField(max_digits=10, decimal_places=2)
    is_online_payment = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=50, blank=True, null=True)
    expenses = models.DecimalField(max_digits=10, decimal_places=2)
    diesel = models.DecimalField(max_digits=8, decimal_places=2)
    date=models.DateField(default=datetime.date.today)

    def __str__(self):
        return f"Trip {self.id}: Starting KM - {self.starting_km}, Ending KM - {self.ending_km}"
