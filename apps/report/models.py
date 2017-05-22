from django.db import models
from django.contrib.postgres.fields import JSONField
from django.utils.encoding import smart_text
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Report(models.Model):
    # AHP Step-1 Data
    criterion_priority = JSONField()
    # AHP Step-2 Data
    criterion_supplier_score = JSONField()
    # AHP Step-3 Data
    criterion_compare = JSONField()
    # AHP Step-4 Data
    supplier_compare = JSONField()
    # vikor results
    vikor_result = JSONField()

    # Store criterions and suppliers state when report has created.
    criterions = JSONField()
    suppliers = JSONField()

    # only show completed report in reports page.
    is_completed = models.BooleanField(default=False)

    created_by = models.ForeignKey('auth.User')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return smart_text(self.id)

    @staticmethod
    def serialize_criterions():
        from criterion.models import Criterion
        criterions = []
        for cr in Criterion.objects.all():
            if cr.parent_id:
                criterions.append({
                    'id': cr.id,
                    'name': cr.name,
                    'parent': {
                        'id': cr.parent.id,
                        'name': cr.parent.name,
                        'count': cr.parent.criterion_set.count()
                    }
                })
            else:
                criterions.append({
                    'id': cr.id,
                    'name': cr.name,
                    'parent': None,
                    'childs': [
                        {
                            "id": child.id,
                            "name": child.name
                        }
                        for child in cr.criterion_set.all()
                    ]
                })
        return criterions

    @staticmethod
    def serialize_suppliers():
        from supplier.models import Supplier

        return [
            {
                'id': supplier.id,
                'name': supplier.name
            }
            for supplier in Supplier.objects.all()
        ]

    @staticmethod
    def create_report(created_by):
        """
        Create Initial Report.
        """

        report = Report()
        report.created_by = created_by
        report.criterion_priority = {}
        report.vikor_result = {}
        report.criterion_supplier_score = []
        report.criterion_compare = {}
        report.supplier_compare = {}
        report.criterions = Report.serialize_criterions()
        report.suppliers = Report.serialize_suppliers()
        report.save()
        return report

    def get_parent_criterions(self):
        return filter(lambda x: x['parent'] is None, self.criterions)

    def get_child_criterions(self):
        return filter(lambda x: x['parent'] is not None, self.criterions)
