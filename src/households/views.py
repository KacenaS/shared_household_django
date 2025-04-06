from django.shortcuts import render, redirect
from .models import Household, Membership
from django.contrib.auth.decorators import login_required


def create_household(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        household = Household.objects.create(name=name)
        Membership.objects.create(user=request.user, household=household)
        return redirect('dashboard')
    return render(request, 'households/create.html')


def join_household(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        household = Household.objects.get(name=name)
        Membership.objects.create(user=request.user, household=household)
        return redirect('dashboard')
    return render(request, 'households/join.html')