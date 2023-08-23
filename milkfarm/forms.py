from django.forms import ModelForm

from .models import Animal, Labor, Expense, Grass, Payment, DailyProduction, Customer, DailyDelivery


class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'


class LaborForm(ModelForm):
    class Meta:
        model = Labor
        fields = '__all__'


class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'


class GrassForm(ModelForm):
    class Meta:
        model = Grass
        fields = '__all__'


class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'


class DailyProductionForm(ModelForm):
    class Meta:
        model = DailyProduction
        fields = '__all__'


class CustomerFormCreate(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['due_amount', 'total_amount,payment_received']


class CustomerFormUpdate(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class DailyDeliveryForm(ModelForm):
    class Meta:
        model = DailyDelivery
        fields = '__all__'
