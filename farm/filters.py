import django_filters

from .models import Farm, Season, SeasonExpense, Expense, Crop


class FarmFilter(django_filters.FilterSet):
    class Meta:
        model = Farm
        fields = ['name', 'location']


class SeasonFilter(django_filters.FilterSet):
    class Meta:
        model = Season
        fields = ['farm', 'crop', 'starting_date', 'harvested_crop_amount_tons', 'harvested_crop_price_per_ton',
                  'first_payment', 'second_payment', 'status']


class SeasonExpenseFilter(django_filters.FilterSet):
    class Meta:
        model = SeasonExpense
        fields = ['season', 'expense', 'amount']


class ExpenseFilter(django_filters.FilterSet):
    class Meta:
        model = Expense
        fields = ['name']


class CropFilter(django_filters.FilterSet):
    class Meta:
        model = Crop
        fields = ['name']