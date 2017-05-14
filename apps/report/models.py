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

    @staticmethod
    def create_report(created_by):
        """
        Create Initial Report.
        """
        from criterion.models import Criterion
        from supplier.models import Supplier

        report = Report()
        report.created_by = created_by
        report.criterion_priority = {}
        report.criterion_supplier_score = []
        report.criterion_compare = {}
        report.supplier_compare = {}
        report.criterions = {
            criterion.id: {
                'name': criterion.name,
                'parent': criterion.parent_id
            }
            for criterion in Criterion.objects.all()
        }
        report.suppliers = {
            supplier.id: supplier.name
            for supplier in Supplier.objects.all()
        }
        report.save()
        return report
