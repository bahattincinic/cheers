from django.conf.urls import url

from .views import ReportListView


urlpatterns = [
    url(r'^$', ReportListView.as_view(), name="reports"),
]
