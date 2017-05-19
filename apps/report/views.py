from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Report


class ReportListView(LoginRequiredMixin, ListView):
    queryset = Report.objects.filter(is_completed=True).order_by('-id')
    template_name = 'report/list.html'
    paginate_by = 10


class ReportDetailView(LoginRequiredMixin, DetailView):
    template_name = 'report/detail.html'
    queryset = Report.objects.filter(is_completed=True)
