from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

from report.models import Report
from criterion.models import Criterion


class BaseStepView(LoginRequiredMixin, TemplateView):

    def get_object(self):
        return get_object_or_404(
            Report, id=self.kwargs['pk'],
            created_by=self.request.user,
            is_completed=False
        )

    def get_parent_criterions(self):
        return Criterion.objects.filter(parent__isnull=True)

    def get_child_criterions(self):
        return Criterion.objects.filter(parent__isnull=False)
