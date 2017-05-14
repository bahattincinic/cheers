from django.conf.urls import url

from .views import (
    CriterionHierarchyView, CriterioScoreView,
    CriterioWeightView, CriterioCompareView,
    CreateAhpView, CriterioGlobalWeightView,
    SupplierCompareView, AhpResultView
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
    url(r'^step-3/criterion-compare/(?P<pk>[0-9]+)/(?P<parent_pk>[0-9]+)/$',
        CriterioCompareView.as_view(),
        name="criterion-compare"),
    url(r'^step-3/criterion-global-weight/(?P<pk>[0-9]+)/$',
        CriterioGlobalWeightView.as_view(),
        name="criterion-global-weight"),
    url(r'^step-4/supplier-compare/(?P<pk>[0-9]+)/(?P<criterion_pk>[0-9]+)/$',
        SupplierCompareView.as_view(),
        name="supplier-compare"),
    url(r'^step-5/ahp-result/(?P<pk>[0-9]+)/$',
        AhpResultView.as_view(),
        name="ahp-result"),
]
