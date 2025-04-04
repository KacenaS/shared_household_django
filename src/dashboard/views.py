from django.shortcuts import render
from chores.models import Chore
from finances.models import Transaction
from shopping.models import ShoppingItem
# from pets.models import CatFeedingLog
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    household = request.user.membership.household
    chores = Chore.objects.filter(household=household)
    transactions = Transaction.objects.filter(household=household)
    shopping = ShoppingItem.objects.filter(household=household, is_bought=False)
    # fed_today = CatFeedingLog.objects.filter(household=household, timestamp__date=now().date()).exists()
    return render(request, 'dashboard/index.html', {
        'chores': chores,
        'transactions': transactions,
        'shopping': shopping,
        # 'fed_today': fed_today
    })