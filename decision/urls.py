from django.conf.urls import url

from .views import (
    CriterionHierarchyView, CriterioScoreView,
    CriterioWeightView)


urlpatterns = [
    url(r'^criterion-hierarchy/$', CriterionHierarchyView.as_view(),
        name="criterion-hierarchy"),
    url(r'^criterion-score/$', CriterioScoreView.as_view(),
        name="criterion-score"),
    url(r'^criterion-weight/$', CriterioWeightView.as_view(),
        name="criterion-weight"),
]
