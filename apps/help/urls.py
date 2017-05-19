from django.conf.urls import url

from .views import TopicListView, TopicDetailView


urlpatterns = [
    url(r'^$', TopicListView.as_view(), name="topics"),
    url(r'^(?P<pk>[0-9]+)/$', TopicDetailView.as_view(),
        name="topic-detail"),
]
