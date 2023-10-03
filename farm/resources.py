from import_export import resources

from .models import Farm, Season, SeasonExpense, Expense, Crop


class FarmResource(resources.ModelResource):
    class Meta:
        model = Farm


class SeasonResource(resources.ModelResource):
    class Meta:
        model = Season


class SeasonExpenseResource(resources.ModelResource):
    class Meta:
        model = SeasonExpense


class ExpenseResource(resources.ModelResource):
    class Meta:
        model = Expense


class CropResource(resources.ModelResource):
    class Meta:
        model = Crop
