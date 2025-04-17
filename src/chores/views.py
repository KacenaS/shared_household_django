# views.py

from django.shortcuts import render, redirect
from .models import Chore
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.utils import timezone


def chore_list(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        if 'clear_completed' in request.POST:
            Chore.objects.filter(is_done=True).delete()
        else:
            done_ids = request.POST.getlist('done_chore_ids')
            if done_ids:
                Chore.objects.filter(id__in=done_ids).update(is_done=True, completed_at=timezone.now())
        return redirect('chore_list')

    chores = Chore.objects.filter(
        Q(household__membership__user=request.user) | Q(household__isnull=True)
    ).distinct()
    return render(request, 'list.html', {'chores': chores})

def chore_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        due_date = request.POST.get('due_date')
        is_recurring = request.POST.get('is_recurring') == 'on'

        recurrence_days = request.POST.get('recurrence_days')
        recurrence_days = int(recurrence_days) if recurrence_days else None

        assigned_to = request.user if request.user.is_authenticated else None
        household = (
            getattr(request.user, 'membership', None).household
            if request.user.is_authenticated and hasattr(request.user, 'membership')
            else None
        )

        Chore.objects.create(
            title=title,
            due_date=due_date,
            assigned_to=assigned_to,
            is_recurring=is_recurring,
            recurrence_days=recurrence_days,
            household=household
        )
        return redirect('chore_list' if request.user.is_authenticated else '/')

    return render(request, 'form.html')
