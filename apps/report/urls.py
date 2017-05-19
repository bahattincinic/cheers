from django.conf.urls import url

from .views import ReportListView, ReportDetailView


urlpatterns = [
    url(r'^$', ReportListView.as_view(), name="reports"),
    url(r'^(?P<pk>[0-9]+)/$', ReportDetailView.as_view(),
        name="report-detail"),
]
