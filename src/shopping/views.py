from django.shortcuts import render, redirect
from .models import ShoppingItem
from django.contrib.auth.decorators import login_required


@login_required
def shopping_list(request):
    items = ShoppingItem.objects.filter(household__membership__user=request.user)
    return render(request, 'shopping/list.html', {'items': items})


@login_required
def add_item(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        household = request.user.membership.household
        ShoppingItem.objects.create(title=title, added_by=request.user, household=household)
        return redirect('shopping_list')
    return render(request, 'shopping/form.html')