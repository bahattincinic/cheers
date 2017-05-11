from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy

from supplier.mixins import AjaxableResponseMixin
from .models import Criterion


class CriterionListView(LoginRequiredMixin, ListView):
    queryset = Criterion.objects.order_by('-id')
    template_name = 'criterion/criterions.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(CriterionListView, self).get_context_data(**kwargs)
        context['main_criterions'] = Criterion.objects.filter(
            parent__isnull=True)
        return context


class CriterionCreateView(AjaxableResponseMixin, CreateView):
    model = Criterion
    fields = ['name', 'parent']


class CriterionUpdateView(AjaxableResponseMixin, UpdateView):
    model = Criterion
    fields = ['name', 'parent']


class CriterionDeleteView(DeleteView):
    model = Criterion
    success_url = reverse_lazy('criterions')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)
