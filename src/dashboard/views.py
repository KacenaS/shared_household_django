from django.views.generic import TemplateView
from chores.models import Chore
from finances.models import Transaction
from shopping.models import ShoppingItem
from households.models import Household, Membership
# from pets.models import CatFeedingLog
from django.utils.timezone import now
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render


class HomepageView(LoginRequiredMixin, TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        membership = Membership.objects.filter(user=user).select_related('household').first()
        household = membership.household if membership else None

        context['household'] = household
        if household:
            context['chores'] = Chore.objects.filter(household=household)
            context['transactions'] = Transaction.objects.filter(household=household)
            context['shopping_list'] = ShoppingItem.objects.filter(household=household, is_bought=False)
            # context['fed_today'] = CatFeedingLog.objects.filter(household=household, timestamp__date=now().date()).exists()
        else:
            context['chores'] = []
            context['transactions'] = []
            context['shopping_list'] = []
            # context['fed_today'] = False

        return context

