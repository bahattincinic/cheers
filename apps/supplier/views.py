from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.conf import settings

from criterion.models import Criterion
from .models import Supplier
from .mixins import AjaxableResponseMixin


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'supplier/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['supplier_count'] = Supplier.objects.count()
        context['main_criterion_count'] = Criterion.objects.filter(
            parent__isnull=True).count()
        context['child_criterion_count'] = Criterion.objects.filter(
            parent__isnull=False).count()
        context['user_count'] = User.objects.filter(is_active=True).count()
        context['indicators'] = settings.RATIONALITY_INDICATOR
        return context


class SupplierListView(LoginRequiredMixin, ListView):
    queryset = Supplier.objects.order_by('-id')
    template_name = 'supplier/suppliers.html'
    paginate_by = 10


class SupplierCreateView(AjaxableResponseMixin, CreateView):
    model = Supplier
    fields = ['name']


class SupplierUpdateView(AjaxableResponseMixin, UpdateView):
    model = Supplier
    fields = ['name']


class SupplierDeleteView(DeleteView):
    model = Supplier
    success_url = reverse_lazy('suppliers')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)
