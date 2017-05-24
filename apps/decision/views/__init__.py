from django.views.generic import TemplateView
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

from report.models import Report


class BaseStepView(LoginRequiredMixin, TemplateView):

    def get_object(self):
        return get_object_or_404(
            Report, id=self.kwargs['pk'],
            created_by=self.request.user,
            is_completed=False
        )

    def get_parent_criterion(self, report):
        parent_pk = int(self.kwargs['criterion_pk'])
        parent = filter(lambda x: str(x['id']) == str(parent_pk),
                        report.criterions)
        if len(parent) == 0:
            raise Http404('Criterion does not exist')
        return parent[0]
