from .models import Season,SeasonExpense,Expense,Farm,Crop
from django import forms

class FarmForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = ['name', 'location']


class SeasonForm(forms.ModelForm):
    farm = forms.ModelChoiceField(queryset=Farm.objects.all(), required=True, empty_label="Select a farm")
    crop = forms.ModelChoiceField(queryset=Crop.objects.all(), required=True, empty_label="Select a crop")

    class Meta:
        model = Season
        fields = ['farm', 'crop', 'starting_date', 'harvested_crop_amount_tons', 'harvested_crop_price_per_ton',
                  'first_payment', 'second_payment', 'status']
        widgets = {
            'starting_date': forms.DateInput(attrs={'type': 'date', 'required': 'required'}),
        }


class CropForm(forms.ModelForm):
    class Meta:
        model = Crop
        fields = ['name']

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['name']


class SeasonExpenseForm(forms.ModelForm):
    season = forms.ModelChoiceField(queryset=Season.objects.all(), required=True, empty_label="Select a season")
    expense = forms.ModelChoiceField(queryset=Expense.objects.all(), required=True, empty_label="Select an expense")

    class Meta:
        model = SeasonExpense
        fields = ['season', 'expense', 'amount']
        widgets = {
            'amount': forms.TextInput(attrs={'required': 'required'}),
        }
