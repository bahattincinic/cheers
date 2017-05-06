from django.conf.urls import url

from .views import (
    CriterionListView, CriterionCreateView,
    CriterionUpdateView, CriterionDeleteView)


urlpatterns = [
    url(r'^$', CriterionListView.as_view(), name="criterions"),
    url(r'^add/$', CriterionCreateView.as_view(), name="criterion-create"),
    url(r'^(?P<pk>[0-9]+)/$', CriterionUpdateView.as_view(),
        name="criterion-update"),
    url(r'^(?P<pk>[0-9]+)/delete$', CriterionDeleteView.as_view(),
        name="criterion-delete"),
]
