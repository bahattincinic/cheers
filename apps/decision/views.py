import json

from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django.shortcuts import get_object_or_404

from criterion.models import Criterion
from supplier.models import Supplier
from report.models import Report


class CriterionHierarchyView(LoginRequiredMixin, TemplateView):
    template_name = 'decision/criterion_hierarchy.html'

    def get_context_data(self, **kwargs):
        context = super(CriterionHierarchyView, self).get_context_data(
            **kwargs)
        context['criterions'] = Criterion.objects.filter(parent__isnull=True)
        return context


class CreateAhpView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        report = Report()
        report.created_by = request.user
        report.criterion_priority = {}
        report.criterion_supplier_score = []
        report.criterion_compare = {}
        report.criterions = {
            criterion.id: {
                'name': criterion.name,
                'parent': criterion.parent_id
            }
            for criterion in Criterion.objects.all()
        }
        report.save()
        return HttpResponseRedirect(
            reverse('criterion-score', args=[report.id]))


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
        context['report'] = get_object_or_404(
            Report, id=self.kwargs['pk'],
            created_by=self.request.user,
            is_completed=False)
        return context

    def post(self, request, *args, **kwargs):
        report = get_object_or_404(
            Report, id=self.kwargs['pk'],
            created_by=self.request.user,
            is_completed=False
        )
        report.criterion_priority = {}

        for key, value in request.POST.items():
            if "score" in key:
                _, criterion_id = key.split('_')
                report.criterion_priority[criterion_id] = value

        report.save()
        return HttpResponseRedirect(
            reverse('criterion-weight', args=[report.id]))


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
        context['report'] = get_object_or_404(
            Report, id=self.kwargs['pk'],
            created_by=self.request.user,
            is_completed=False)
        return context

    def post(self, request, *args, **kwargs):
        report = get_object_or_404(
            Report, id=self.kwargs['pk'],
            created_by=self.request.user,
            is_completed=False
        )
        report.criterion_supplier_score = []

        for key, value in request.POST.items():
            if "score" in key:
                _, criterion_id, supplier_id = key.split('_')
                report.criterion_supplier_score.append({
                    'criterion_id': criterion_id,
                    'supplier_id': supplier_id,
                    'score': value
                })
        report.save()
        return HttpResponseRedirect(
            reverse('criterion-compare', args=[report.id, 0]))


class CriterioGlobalWeightView(LoginRequiredMixin, TemplateView):
    """
    AHP Step-3
    """
    template_name = "decision/criterio_global_weight.html"

    def get_context_data(self, **kwargs):
        context = super(CriterioGlobalWeightView, self).get_context_data(
            **kwargs)

        context['suppliers'] = Supplier.objects.all()
        context['criterions'] = Criterion.objects.filter(
            parent__isnull=False)
        context['report'] = get_object_or_404(
            Report, id=self.kwargs['pk'],
            created_by=self.request.user,
            is_completed=False)
        return context


class CriterioCompareView(LoginRequiredMixin, TemplateView):
    """
    AHP Step-3
    """
    template_name = "decision/criterio_compare.html"

    def get_context_data(self, **kwargs):
        context = super(CriterioCompareView, self).get_context_data(
            **kwargs)

        queryset = Criterion.objects.all()
        parent_pk = int(self.kwargs['parent_pk'])
        if parent_pk == 0:
            queryset = queryset.filter(parent__isnull=True)
            parent = None
        else:
            parent = get_object_or_404(Criterion, pk=parent_pk)
            queryset = queryset.filter(parent=parent)

        context['criterions'] = queryset
        context['parent'] = parent

        context['report'] = get_object_or_404(
            Report, id=self.kwargs['pk'],
            created_by=self.request.user,
            is_completed=False)

        context['random_indicator'] = settings.RATIONALITY_INDICATOR.get(
            context['criterions'].count())

        return context

    def post(self, request, *args, **kwargs):
        report = get_object_or_404(
            Report, id=self.kwargs['pk'],
            created_by=self.request.user,
            is_completed=False
        )

        parent_pk = int(self.kwargs['parent_pk'])
        if parent_pk != 0:
            get_object_or_404(Criterion, pk=parent_pk)

        report.criterion_compare[parent_pk] = json.loads(request.POST['data'])
        report.save()

        missins_criterion = Criterion.objects.filter(
            parent__isnull=True).exclude(
            id__in=report.criterion_compare.keys()).first()

        if missins_criterion:
            return HttpResponseRedirect(
                reverse('criterion-compare',
                        args=[report.id, missins_criterion.id]))

        if '0' not in report.criterion_compare.keys():
            return HttpResponseRedirect(
                reverse('criterion-compare',
                        args=[report.id, 0]))

        return HttpResponseRedirect(
            reverse('criterion-global-weight', args=[report.id]))
