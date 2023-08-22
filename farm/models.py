from django.db import models

class Expense(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Crop(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Farm(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Season(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    starting_date = models.DateField()
    harvested_crop_amount_tons = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    harvested_crop_price_per_ton = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    first_payment = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    second_payment = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.BooleanField(default=False)

    WATER = 'Water'
    LABOR = 'Labor'
    FERTILIZERS = 'Fertilizers'
    OTHER = 'Other'
    TRACTOR = 'Tractor'
    EXPENSE_CHOICES = [
        (WATER, 'Water Related'),
        (LABOR, 'Labor Related'),
        (FERTILIZERS, 'Fertilizers Related'),
        (OTHER, 'Other Related'),
        (TRACTOR, 'Tractor Related'),
    ]
    expenses = models.ManyToManyField('Expense', through='SeasonExpense')

    def final_amount(self):
        return self.harvested_crop_amount_tons * self.harvested_crop_price_per_ton

    def __str__(self):
        return f"{self.crop.name} Season at {self.farm.name}"


class SeasonExpense(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.expense.name} for {self.season.crop.name} Season"