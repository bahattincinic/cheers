import json

from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django.shortcuts import get_object_or_404

from criterion.models import Criterion
from report.models import Report
from supplier.models import Supplier
from decision.views import BaseStepView


class CreateAhpView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        if Criterion.objects.filter(parent__isnull=True).count() == 0 or \
                Criterion.objects.filter(parent__isnull=False).count() == 0 or\
                Supplier.objects.count() == 0:
            # no data
            return HttpResponseRedirect(reverse('home'))

        report = Report.create_report(request.user)
        return HttpResponseRedirect(
            reverse('criterion-score', args=[report.id]))


class CriterioScoreView(BaseStepView):
    """
    AHP Step-1
    """
    template_name = 'decision/ahp/ahp_criterion_score.html'

    def get_context_data(self, **kwargs):
        context = super(CriterioScoreView, self).get_context_data(
            **kwargs)
        context['report'] = self.get_object()
        return context

    def post(self, request, *args, **kwargs):
        report = self.get_object()
        report.criterion_priority = {}

        for key, value in request.POST.items():
            if "score" in key:
                _, criterion_id = key.split('_')
                report.criterion_priority[criterion_id] = value

        report.save()
        return HttpResponseRedirect(
            reverse('criterion-weight', args=[report.id]))


class CriterioWeightView(BaseStepView):
    """
    AHP Step-2
    """
    template_name = "decision/ahp/criterio_weight.html"

    def get_context_data(self, **kwargs):
        context = super(CriterioWeightView, self).get_context_data(
            **kwargs)

        context['report'] = self.get_object()
        return context

    def post(self, request, *args, **kwargs):
        report = self.get_object()
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


class CriterioGlobalWeightView(BaseStepView):
    """
    AHP Step-3
    """
    template_name = "decision/ahp/criterio_global_weight.html"

    def get_context_data(self, **kwargs):
        context = super(CriterioGlobalWeightView, self).get_context_data(
            **kwargs)

        report = self.get_object()
        criterions = report.get_child_criterions()
        context['report'] = report
        context['next_url'] = reverse('supplier-compare',
                                      args=[report.id, criterions[0]['id']])
        return context


class CriterioCompareView(BaseStepView):
    """
    AHP Step-3
    """
    template_name = "decision/ahp/criterio_compare.html"

    def get_context_data(self, **kwargs):
        context = super(CriterioCompareView, self).get_context_data(
            **kwargs)
        report = self.get_object()

        parent_pk = int(self.kwargs['criterion_pk'])
        if parent_pk == 0:
            queryset = report.get_parent_criterions()
            parent = None
        else:
            parent = self.get_parent_criterion(report)
            queryset = parent['childs']

        context['object_list'] = queryset
        context['parent'] = parent
        context['step'] = 3
        context['page_type'] = 'criterio'
        context['report'] = report

        context['random_indicator'] = settings.RATIONALITY_INDICATOR.get(
            len(context['object_list']))

        context['progress_data'] = {
            cr['name']: str(cr['id']) in report.criterion_compare.keys()
            for cr in report.get_parent_criterions()
        }

        return context

    def post(self, request, *args, **kwargs):
        report = self.get_object()

        parent_pk = int(self.kwargs['criterion_pk'])
        if parent_pk != 0:
            self.get_parent_criterion(report)

        try:
            report.criterion_compare[str(parent_pk)] = json.loads(
                request.POST['data'])
            report.save()
        except (ValueError, TypeError):
            # Invalid JSON yielded
            return HttpResponseRedirect(
                reverse('criterion-compare',
                        args=[report.id, parent_pk]))

        missins_criterion = filter(
            lambda x: str(x['id']) not in report.criterion_compare.keys(),
            report.get_parent_criterions())

        if len(missins_criterion) > 0:
            return HttpResponseRedirect(
                reverse('criterion-compare',
                        args=[report.id, missins_criterion[0]['id']]))

        if '0' not in report.criterion_compare.keys():
            return HttpResponseRedirect(
                reverse('criterion-compare',
                        args=[report.id, 0]))

        return HttpResponseRedirect(
            reverse('criterion-global-weight', args=[report.id]))


class SupplierCompareView(BaseStepView):
    """
    AHP Step-4
    """
    template_name = "decision/ahp/criterio_compare.html"

    def get_context_data(self, **kwargs):
        context = super(SupplierCompareView, self).get_context_data(
            **kwargs)

        report = self.get_object()

        context['page_type'] = 'supplier'
        context['step'] = 4
        context['parent'] = self.get_parent_criterion(report)
        context['report'] = report
        context['object_list'] = report.suppliers

        context['random_indicator'] = settings.RATIONALITY_INDICATOR.get(
            len(context['object_list']))

        context['progress_data'] = {
            criterion['name']: str(criterion['id']) in
            report.supplier_compare.keys()
            for criterion in report.get_child_criterions()
        }

        return context

    def post(self, request, *args, **kwargs):
        report = self.get_object()
        criterion = get_object_or_404(
            Criterion, pk=self.kwargs['criterion_pk'])

        try:
            report.supplier_compare[str(criterion.id)] = json.loads(
                request.POST['data'])
            report.save()
        except (ValueError, TypeError):
            # Invalid JSON yielded
            return HttpResponseRedirect(
                reverse('supplier-compare',
                        args=[report.id, criterion.id]))

        missins_criterion = filter(
            lambda x: str(x['id']) not in report.supplier_compare.keys(),
            report.get_child_criterions())

        if len(missins_criterion) > 0:
            return HttpResponseRedirect(
                reverse('supplier-compare',
                        args=[report.id, missins_criterion[0]['id']]))

        return HttpResponseRedirect(
            reverse('ahp-result', args=[report.id]))


class AhpResultView(BaseStepView):
    """
    AHP Step-5
    """
    template_name = "decision/ahp/ahp_result.html"

    def get_context_data(self, **kwargs):
        context = super(AhpResultView, self).get_context_data(
            **kwargs)
        context['report'] = self.get_object()
        return context
