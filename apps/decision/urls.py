from django.conf.urls import url

from .views import (
    CriterionHierarchyView, CriterioScoreView,
    CriterioWeightView, CriterioCompareView,
    CreateAhpView
)


urlpatterns = [
    url(r'^criterion-hierarchy/$',
        CriterionHierarchyView.as_view(),
        name="criterion-hierarchy"),
    url(r'^create-ahp/$',
        CreateAhpView.as_view(),
        name="create-ahp"),
    url(r'^step-1/criterion-score/(?P<pk>[0-9]+)/$',
        CriterioScoreView.as_view(),
        name="criterion-score"),
    url(r'^step-2/criterion-weight/(?P<pk>[0-9]+)/$',
        CriterioWeightView.as_view(),
        name="criterion-weight"),
    url(r'^step-3/criterion-compare/(?P<pk>[0-9]+)/$',
        CriterioCompareView.as_view(),
        name="criterion-compare"),
]
