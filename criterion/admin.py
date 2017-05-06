from django.contrib import admin

from .models import Criterion, CriterionScore


admin.site.register(Criterion)
admin.site.register(CriterionScore)
