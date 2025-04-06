from django.shortcuts import get_object_or_404, render, redirect
from .models import ShoppingItem
from django.contrib.auth.decorators import login_required


def shopping_list(request):
    items = ShoppingItem.objects.all()
    return render(request, 'shopping_list.html', {'items': items})


def add_item(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        household = request.user.membership.household
        ShoppingItem.objects.create(title=title, added_by=request.user, household=household)
        return redirect('shopping_list')
    return render(request, 'add_idem.html')


