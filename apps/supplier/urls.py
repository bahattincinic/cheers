from django.conf.urls import url

from .views import (
    SupplierListView, SupplierCreateView,
    SupplierUpdateView, SupplierDeleteView)


urlpatterns = [
    url(r'^$', SupplierListView.as_view(), name="suppliers"),
    url(r'^add/$', SupplierCreateView.as_view(), name="supplier-create"),
    url(r'^(?P<pk>[0-9]+)/$', SupplierUpdateView.as_view(),
        name="supplier-update"),
    url(r'^(?P<pk>[0-9]+)/delete$', SupplierDeleteView.as_view(),
        name="supplier-delete"),
]
