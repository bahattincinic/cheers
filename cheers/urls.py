from django.conf.urls import url, include
from django.contrib import admin

from supplier.views import DashboardView
from account.views import ProfileUpdateView


urlpatterns = [
    url(r'^$', DashboardView.as_view(), name="home"),
    url(r'^criterions/', include('criterion.urls')),
    url(r'^suppliers/', include('supplier.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/update-profile$', ProfileUpdateView.as_view(),
        name="profile-update"),
]
