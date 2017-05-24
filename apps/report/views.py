from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Report


class ReportListView(LoginRequiredMixin, ListView):
    queryset = Report.objects.select_related('created_by')\
                             .filter(is_completed=True).order_by('-id')
    template_name = 'report/list.html'
    paginate_by = 10


class ReportDetailView(LoginRequiredMixin, DetailView):
    template_name = 'report/detail.html'
    queryset = Report.objects.select_related('created_by')\
                             .filter(is_completed=True)

    def get_context_data(self, **kwargs):
        context = super(ReportDetailView, self).get_context_data(
            **kwargs)
        report = self.get_object()
        context['child_criterions'] = filter(lambda x: x['parent'] is not None,
                                             report.criterions)
        return context
