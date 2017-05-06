from django.conf.urls import url, include
from django.contrib import admin

from criterion.views import CriterionListView
from supplier.views import DashboardView


urlpatterns = [
    url(r'^$', DashboardView.as_view(), name="home"),
    url(r'^criterions/$', CriterionListView.as_view(), name="criterions"),
    url(r'^suppliers/', include('supplier.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]
