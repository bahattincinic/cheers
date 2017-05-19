from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from supplier.views import DashboardView
from account.views import ProfileUpdateView


urlpatterns = [
    url(r'^$', DashboardView.as_view(), name="home"),
    url(r'^criterions/', include('criterion.urls')),
    url(r'^suppliers/', include('supplier.urls')),
    url(r'^decision/', include('decision.urls')),
    url(r'^reports/', include('report.urls')),
    url(r'^help/', include('help.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^admin/editor/', include('redactor.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/update-profile$', ProfileUpdateView.as_view(),
        name="profile-update"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
