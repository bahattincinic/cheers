from django.db import models
from django.contrib.postgres.fields import JSONField


class Report(models.Model):
    # AHP Step-1 Data
    criterion_priority = JSONField()
    # AHP Step-2 Data
    criterion_supplier_score = JSONField()
    # AHP Step-3 Data
    criterion_compare = JSONField()
    # AHP Step-4 Data
    supplier_compare = JSONField()

    # Store criterions and suppliers state when report has created.
    criterions = JSONField()
    suppliers = JSONField()

    # only show completed report in reports page.
    is_completed = models.BooleanField(default=False)

    created_by = models.ForeignKey('auth.User')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s report' % self.id
