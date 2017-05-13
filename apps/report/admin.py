from django.contrib import admin

from .models import Report


class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_by', 'is_completed', 'created_at',)
    readonly_fields = ('criterion_priority',
                       'criterion_supplier_score',
                       'criterion_compare',
                       'criterions',
                       'suppliers',)


admin.site.register(Report, ReportAdmin)
