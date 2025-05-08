from django import forms
from .models import Household


class CreateHouseholdForm(forms.ModelForm):
    class Meta:
        model = Household
        fields = ['name']


class JoinHouseholdForm(forms.Form):
    name = forms.CharField(label="Household Name")