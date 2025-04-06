from django.shortcuts import render
from chores.models import Chore
from finances.models import Transaction
from shopping.models import ShoppingItem
from households.models import Household
# from pets.models import CatFeedingLog
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required


def homepage(request):
    household = Household.objects.first()
    chores = Chore.objects.filter(household=household)
    transactions = Transaction.objects.filter(household=household)
    shopping = ShoppingItem.objects.filter(household=household, is_bought=False)
    # fed_today = CatFeedingLog.objects.filter(household=household, timestamp__date=now().date()).exists()
    return render(request, 'homepage.html', {
        'chores': chores,
        'transactions': transactions,
        'shopping_list': shopping,
        'household': household,
        # 'fed_today': fed_today
    })