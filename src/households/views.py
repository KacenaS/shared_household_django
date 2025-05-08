from django.views.generic.edit import FormView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Household, Membership
from .forms import CreateHouseholdForm, JoinHouseholdForm
from django.shortcuts import get_object_or_404
from households.models import Household


class HouseholdListView(ListView):
    model = Household
    template_name = 'list.html'
    context_object_name = 'households'

    def get_queryset(self):
        return Household.objects.all()


class CreateHouseholdView(LoginRequiredMixin, FormView):
    template_name = 'create.html'
    form_class = CreateHouseholdForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        household = form.save()
        Membership.objects.create(user=self.request.user, household=household)
        return super().form_valid(form)


class JoinHouseholdView(LoginRequiredMixin, FormView):
    template_name = 'join.html'
    form_class = JoinHouseholdForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        household_name = form.cleaned_data['name']
        household = get_object_or_404(Household, name=household_name)
        Membership.objects.get_or_create(user=self.request.user, household=household)
        return super().form_valid(form)