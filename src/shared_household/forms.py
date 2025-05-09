from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from households.models import Household  # or wherever your model is


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    household = forms.ModelChoiceField(queryset=Household.objects.all(), required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'household']