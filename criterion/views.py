from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Criterion


class CriterionListView(LoginRequiredMixin, ListView):
    queryset = Criterion.objects.order_by('-id')
    template_name = 'criterions.html'
    paginate_by = 10
