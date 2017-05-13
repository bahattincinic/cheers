from django.db import models
from django.contrib.postgres.fields import JSONField


class Report(models.Model):
    criterion_priority = JSONField()
    criterion_supplier_score = JSONField()
    criterion_compare = JSONField()

    criterions = JSONField()

    is_completed = models.BooleanField(default=False)

    created_by = models.ForeignKey('auth.User')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s report' % self.id
