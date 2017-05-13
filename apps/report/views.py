from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView

from .models import Report


class ReportListView(LoginRequiredMixin, ListView):
    queryset = Report.objects.filter(is_completed=True).order_by('-id')
    template_name = 'report/list.html'
    paginate_by = 10
