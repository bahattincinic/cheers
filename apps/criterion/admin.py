from django.contrib import admin

from .models import Criterion


class CriterionAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent',)


admin.site.register(Criterion, CriterionAdmin)
