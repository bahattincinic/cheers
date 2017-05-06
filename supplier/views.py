from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView

from .models import Supplier


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'


class SupplierListView(LoginRequiredMixin, ListView):
    model = Supplier
    template_name = 'suppliers.html'
