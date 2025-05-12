from django import forms
from .models import ShoppingItem

class ShoppingItemForm(forms.ModelForm):
    class Meta:
        model = ShoppingItem
        fields = ['title', 'category', 'is_urgent']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'is_urgent': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
