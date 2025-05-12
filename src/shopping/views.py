from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages

from .models import ShoppingItem
from .forms import ShoppingItemForm
from households.models import Membership


class ShoppingListView(LoginRequiredMixin, TemplateView):
    template_name = 'shopping_list.html'

    def get_household(self):
        try:
            return Membership.objects.get(user=self.request.user).household
        except Membership.DoesNotExist:
            return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        household = self.get_household()

        if household:
            context['items'] = ShoppingItem.objects.filter(
                household=household,
                is_bought=False
            ).order_by('-is_urgent', 'added_at')

            context['bought_items'] = ShoppingItem.objects.filter(
                household=household,
                is_bought=True
            ).order_by('-added_at')
        else:
            context['items'] = []
            context['bought_items'] = []
            context['error'] = "You don't belong to a household."

        return context

    def post(self, request, *args, **kwargs):
        item_ids = request.POST.getlist('bought_items')
        self.bought_item(item_ids)
        messages.success(request, f"{len(item_ids)} item(s) marked as bought.")
        return redirect('shopping_list')

    def bought_item(self, item_ids):
        household = self.get_household()
        if household:
            ShoppingItem.objects.filter(id__in=item_ids, household=household).update(is_bought=True)


class AddItemView(LoginRequiredMixin, CreateView):
    model = ShoppingItem
    form_class = ShoppingItemForm
    template_name = 'add_item.html'
    success_url = reverse_lazy('shopping_list')

    def form_valid(self, form):
        try:
            membership = Membership.objects.get(user=self.request.user)
        except Membership.DoesNotExist:
            return render(self.request, 'error.html', {
                'message': "You don't belong to any household."
            })

        item = form.save(commit=False)
        item.added_by = self.request.user
        item.household = membership.household
        item.save()
        return super().form_valid(form)
