from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from households.models import Membership


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('homepage')  # or your desired page

    def form_valid(self, form):
        user = form.save()
        household = form.cleaned_data['household']
        Membership.objects.create(user=user, household=household)
        #login(self.request, user)  # optional auto-login
        return super().form_valid(form)