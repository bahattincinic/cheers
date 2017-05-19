from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Topic


class TopicListView(LoginRequiredMixin, ListView):
    queryset = Topic.objects.order_by('-id')
    template_name = 'help/list.html'
    paginate_by = 10


class TopicDetailView(LoginRequiredMixin, DetailView):
    template_name = 'help/detail.html'
    queryset = Topic.objects.all()
