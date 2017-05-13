from django.contrib import admin

from .models import Report


class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_by', 'is_completed', 'created_at',)


admin.site.register(Report, ReportAdmin)
