import json

from django.urls import reverse
from django.http import HttpResponseRedirect

from decision.views import BaseStepView


class VikorCalculateView(BaseStepView):
    template_name = 'decision/vikor/vikor_calculate.html'

    def get_context_data(self, **kwargs):
        context = super(VikorCalculateView, self).get_context_data(
            **kwargs)
        context['report'] = self.get_object()
        return context

    def post(self, request, *args, **kwargs):
        report = self.get_object()

        try:
            report.vikor_result = json.loads(request.POST['data'])
            report.is_completed = True
            report.save()
        except (ValueError, TypeError):
            # Invalid JSON yielded
            return HttpResponseRedirect(
                reverse('vikor-calculate', args=[report.id]))

        return HttpResponseRedirect(reverse('vikor-done', args=[report.id]))


class VikorDoneView(BaseStepView):
    template_name = 'decision/vikor/vikor_done.html'

    def get_context_data(self, **kwargs):
        context = super(VikorDoneView, self).get_context_data(
            **kwargs)
        context['report'] = self.get_object()
        return context

    def get(self, request, *args, **kwargs):
        report = self.get_object()
        if not report.is_completed:
            return HttpResponseRedirect(reverse('home'))
        return super(VikorDoneView, self).get(request, *args, **kwargs)
