from django.shortcuts import render, redirect
from finances.models import Transaction
from finances.forms import TransactionForm  # Import TransactionForm from the forms module
from households.models import Household  # Import Household model
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, FormView


class TransactionListView(ListView):
    model = Transaction
    template_name = 'finances/list.html'
    context_object_name = 'transactions'


class TransactionCreateFormView(FormView):
    template_name = 'finances/form.html'
    form_class = TransactionForm  

    def form_valid(self, form):
        transaction = form.save(commit=False)
        household = Household.objects.first()
        if household is None:
            raise ValueError("No Household exists. Please create one first.")
        transaction.household = household
        transaction.save()
        return redirect('transaction_list')
