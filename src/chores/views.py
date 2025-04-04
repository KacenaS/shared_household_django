from django.shortcuts import render, redirect
from .models import Chore
from django.contrib.auth.decorators import login_required


@login_required
def chore_list(request):
    chores = Chore.objects.filter(household__membership__user=request.user)
    return render(request, 'chores/list.html', {'chores': chores})

@login_required
def chore_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        due_date = request.POST.get('due_date')
        assigned_to = request.user
        is_recurring = request.POST.get('is_recurring') == 'on'
        recurrence_days = request.POST.get('recurrence_days') or None
        household = request.user.membership.household
        Chore.objects.create(
            title=title, assigned_to=assigned_to, due_date=due_date,
            is_recurring=is_recurring, 
            recurrence_days=recurrence_days, 
            household=household
        )
        return redirect('chore_list')
    return render(request, 'chores/form.html')