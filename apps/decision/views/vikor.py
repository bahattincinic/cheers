from decision.views import BaseStepView


class VikorCalculateView(BaseStepView):
    template_name = 'decision/vikor/vikor_calculate.html'

    def get_context_data(self, **kwargs):
        context = super(VikorCalculateView, self).get_context_data(
            **kwargs)
        context['report'] = self.get_object()
        return context


class VikorDoneView(BaseStepView):
    template_name = 'decision/vikor/vikor_done.html'

    def get_context_data(self, **kwargs):
        context = super(VikorDoneView, self).get_context_data(
            **kwargs)
        context['report'] = self.get_object()
        return context
