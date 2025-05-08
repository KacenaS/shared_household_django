from django import forms
from finances.models import Transaction  


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['title', 'amount', 'date', 'category']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'amount': forms.NumberInput(attrs={'step': '0.01'}),
        }
        labels = {
            'title': 'Title',
            'amount': 'Amount',
            'description': 'Description',
            'date': 'Date',
        }