from django.db import models


class Animal(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)  # Assuming "Surat" or "Mahesana"

    def __str__(self):
        return self.name


class Labor(models.Model):
    LABOR_TYPE_CHOICES = (
        ('monthly', 'Monthly'),
        ('daily', 'Daily'),
    )
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15, null=True, blank=True)
    labor_type = models.CharField(max_length=20, choices=LABOR_TYPE_CHOICES)
    payment_to_be_paid = models.DecimalField(max_digits=10, decimal_places=2)
    credit = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.get_labor_type_display()} Labor"


class Expense(models.Model):
    EXPENSES_TYPE_CHOICES = (
        ('food', 'Food'),
        ('medicine', 'Medicine'),
        ('grass', 'Grass'),
        ('other', 'Other'),
    )
    expenses_type = models.CharField(max_length=20, choices=EXPENSES_TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.get_expenses_type_display()} Expenses"


class Grass(models.Model):
    location = models.CharField(max_length=50)
    owner_name = models.CharField(max_length=100)
    owner_mobile = models.CharField(max_length=15)
    total_amount_grass = models.DecimalField(max_digits=10, decimal_places=2)
    rate = models.DecimalField(max_digits=6, decimal_places=2)
    final_price = models.DecimalField(max_digits=10, decimal_places=2)
    due_amount = models.DecimalField(max_digits=10, decimal_places=2)
    amount_to_be_paid = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Grass for {self.location} by {self.owner_name}"


class DailyProduction(models.Model):
    date = models.DateField()
    evening_milk = models.DecimalField(max_digits=10, decimal_places=2)
    morning_milk = models.DecimalField(max_digits=10, decimal_places=2)
    total_milk = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Daily Production for {self.date}"

    def save(self, *args, **kwargs):
        self.total_milk = self.evening_milk + self.morning_milk
        super().save(*args, **kwargs)


class Customer(models.Model):
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    address = models.TextField()
    due_amount = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    payment_received = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)

    def __str__(self):
        return self.name


class Payment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
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
        return f"Payment of {self.customer} on {self.date}"

    def save(self, *args, **kwargs):
        self.customer.payment_received += self.amount
        self.customer.due_amount -= self.amount
        self.customer.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.customer.payment_received -= self.amount
        self.customer.due_amount += self.amount
        self.customer.save()
        super().delete(*args, **kwargs)

    def update(self, *args, **kwargs):
        self.customer.payment_received -= self.amount
        self.customer.due_amount += self.amount
        self.customer.save()
        super().update(*args, **kwargs)


class DailyDelivery(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField()
    morning_milk = models.DecimalField(max_digits=10, decimal_places=2)
    evening_milk = models.DecimalField(max_digits=10, decimal_places=2)
    total_milk = models.DecimalField(max_digits=10, decimal_places=2)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    final_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Daily Delivery of {self.customer} on {self.date}"

    def save(self, *args, **kwargs):
        self.total_milk = self.morning_milk + self.evening_milk
        self.final_price = self.total_milk * self.rate
        self.customer.total_amount += self.final_price
        self.customer.due_amount += self.final_price
        self.customer.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.customer.total_amount -= self.final_price
        self.customer.due_amount -= self.final_price
        self.customer.save()
        super().delete(*args, **kwargs)

    def update(self, *args, **kwargs):
        self.customer.total_amount -= self.final_price
        self.customer.due_amount -= self.final_price
        self.customer.save()
        super().update(*args, **kwargs)
