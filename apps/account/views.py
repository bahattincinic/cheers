from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView
from django.urls import reverse

from .forms import UserUpdateForm


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'account/update_profile.html'
    form_class = UserUpdateForm
    model = User

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        return reverse('profile-update')
