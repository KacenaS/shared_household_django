from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Chore
from households.models import Membership
from django.utils.timezone import now
from django.shortcuts import redirect
from django.db.models import Q
from .models import Chore
from households.models import Membership


class ChoreListView(ListView):
    model = Chore
    template_name = 'list.html'
    context_object_name = 'chores'

    def get_queryset(self):
        user = self.request.user
        membership = Membership.objects.filter(user=user).select_related('household').first()
        household = membership.household if membership else None
        return Chore.objects.filter(household=household) if household else Chore.objects.none()

    def post(self, request, *args, **kwargs):
        if 'clear_completed' in request.POST:
            Chore.objects.filter(is_done=True).delete()
        else:
            done_ids = request.POST.getlist('done_chore_ids')
            if done_ids:
                Chore.objects.filter(id__in=done_ids).update(is_done=True, completed_at=now())
        return redirect('chore_list')  # Adjust if your URL name is different


class ChoreCreateView(CreateView):
    model = Chore
    template_name = 'form.html'
    fields = ['title', 'due_date', 'is_recurring', 'recurrence_days']  # Don't include household or assigned_to directly
    success_url = reverse_lazy('chore_list')  # Adjust if your URL name is different

    def form_valid(self, form):
        user = self.request.user
        form.instance.assigned_to = user
        membership = Membership.objects.filter(user=user).select_related('household').first()
        form.instance.household = membership.household if membership else None
        return super().form_valid(form)
