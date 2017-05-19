from django.conf.urls import url

from decision.views.ahp import (
    CriterioScoreView,
    CriterioWeightView, CriterioCompareView,
    CreateAhpView, CriterioGlobalWeightView,
    SupplierCompareView, AhpResultView
)
from decision.views.vikor import (
    VikorCalculateView, VikorDoneView
)


urlpatterns = [
    url(r'^ahp/create-ahp/$',
        CreateAhpView.as_view(),
        name="create-ahp"),
    url(r'^ahp/step-1/criterion-score/(?P<pk>[0-9]+)/$',
        CriterioScoreView.as_view(),
        name="criterion-score"),
    url(r'^ahp/step-2/criterion-weight/(?P<pk>[0-9]+)/$',
        CriterioWeightView.as_view(),
        name="criterion-weight"),
    url(r'^ahp/step-3/criterion-compare/(?P<pk>[0-9]+)/(?P<parent_pk>[0-9]+)/$', # noqa
        CriterioCompareView.as_view(),
        name="criterion-compare"),
    url(r'^ahp/step-3/criterion-global-weight/(?P<pk>[0-9]+)/$',
        CriterioGlobalWeightView.as_view(),
        name="criterion-global-weight"),
    url(r'^ahp/step-4/supplier-compare/(?P<pk>[0-9]+)/(?P<criterion_pk>[0-9]+)/$', # noqa
        SupplierCompareView.as_view(),
        name="supplier-compare"),
    url(r'^ahp/step-5/result/(?P<pk>[0-9]+)/$',
        AhpResultView.as_view(),
        name="ahp-result"),

    url(r'^vikor/step-1/calculate/(?P<pk>[0-9]+)/$',
        VikorCalculateView.as_view(),
        name="vikor-calculate"),
    url(r'^vikor/step-2/result/(?P<pk>[0-9]+)/$',
        VikorDoneView.as_view(),
        name="vikor-done"),
]
