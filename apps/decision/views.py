from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse

from criterion.models import Criterion


class CriterionHierarchyView(LoginRequiredMixin, TemplateView):
    template_name = 'criterion_hierarchy.html'

    def get_context_data(self, **kwargs):
        context = super(CriterionHierarchyView, self).get_context_data(
            **kwargs)
        context['criterions'] = Criterion.objects.filter(parent__isnull=True)
        return context


class CriterioScoreView(LoginRequiredMixin, TemplateView):
    """
    AHP Step-1
    """
    template_name = 'ahp_criterion_score.html'

    def get_context_data(self, **kwargs):
        context = super(CriterioScoreView, self).get_context_data(
            **kwargs)
        context['criterions'] = Criterion.objects.filter(
            parent__isnull=True)
        return context

    def post(self, request, *args, **kwargs):
        for key, value in request.POST.items():
            if "score" in key:
                _, criterion_id = key.split('_')
                criterion = Criterion.objects.get(
                    id=criterion_id)
                criterion.priority = value
                criterion.save()
        return HttpResponseRedirect(reverse('criterion-weight'))


class CriterioWeightView(LoginRequiredMixin, TemplateView):
    """
    AHP Step-2
    """
    template_name = "criterio_weight.html"
