from django.shortcuts import render, redirect
from .models import Transaction
from django.contrib.auth.decorators import login_required


def transaction_list(request):
    transactions = Transaction.objects.filter(
        household__membership__user=request.user
    )
    return render(request, 'finances/list.html', {'transactions': transactions})


def transaction_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        amount = request.POST.get('amount')
        category = request.POST.get('category')
        date = request.POST.get('date')
        household = request.user.membership.household
        Transaction.objects.create(
            title=title,
            amount=amount,
            category=category,
            date=date,
            paid_by=request.user,
            household=household
        )
        return redirect('transaction_list')
    return render(request, 'finances/form.html')