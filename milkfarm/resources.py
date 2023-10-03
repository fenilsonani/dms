from import_export import resources
from .models import Customer, DailyProduction, Animal, Labor, Expense, Grass, Payment, DailyDelivery


class CustomerResource(resources.ModelResource):
    class Meta:
        model = Customer


class DailyProductionResource(resources.ModelResource):
    class Meta:
        model = DailyProduction


class AnimalResource(resources.ModelResource):
    class Meta:
        model = Animal


class LaborResource(resources.ModelResource):
    class Meta:
        model = Labor


class ExpenseResource(resources.ModelResource):
    class Meta:
        model = Expense


class GrassResource(resources.ModelResource):
    class Meta:
        model = Grass


class PaymentResource(resources.ModelResource):
    class Meta:
        model = Payment


class DailyDeliveryResource(resources.ModelResource):
    class Meta:
        model = DailyDelivery