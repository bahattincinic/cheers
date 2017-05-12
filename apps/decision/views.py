from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse

from criterion.models import Criterion, CriterionScore
from supplier.models import Supplier


class CriterionHierarchyView(LoginRequiredMixin, TemplateView):
    template_name = 'decision/criterion_hierarchy.html'

    def get_context_data(self, **kwargs):
        context = super(CriterionHierarchyView, self).get_context_data(
            **kwargs)
        context['criterions'] = Criterion.objects.filter(parent__isnull=True)
        return context


class CriterioScoreView(LoginRequiredMixin, TemplateView):
    """
    AHP Step-1
    """
    template_name = 'decision/ahp_criterion_score.html'

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
    template_name = "decision/criterio_weight.html"

    def get_context_data(self, **kwargs):
        context = super(CriterioWeightView, self).get_context_data(
            **kwargs)

        context['suppliers'] = Supplier.objects.all()
        context['criterions'] = Criterion.objects.filter(
            parent__isnull=True)

        context['scores'] = {
            '%s_%s' % (score.criterion_id, score.supplier_id): score.score
            for score in CriterionScore.objects.all()
        }
        return context

    def post(self, request, *args, **kwargs):
        for key, value in request.POST.items():
            if "score" in key:
                _, criterion_id, supplier_id = key.split('_')
                try:
                    score = CriterionScore.objects.get(
                        criterion_id=criterion_id,
                        supplier_id=supplier_id
                    )
                    score.score = value
                    score.save()
                except CriterionScore.DoesNotExist:
                    CriterionScore.objects.create(
                        criterion_id=criterion_id,
                        supplier_id=supplier_id,
                        score=value
                    )
        return HttpResponseRedirect(reverse('criterion-compare'))


class CriterioCompareView(LoginRequiredMixin, TemplateView):
    """
    AHP Step-3
    """
    template_name = "decision/criterio_compare.html"

    def get_context_data(self, **kwargs):
        context = super(CriterioCompareView, self).get_context_data(
            **kwargs)

        context['criterions'] = Criterion.objects.filter(
            parent__isnull=True)

        return context
