from django.db import models


class Criterion(models.Model):
    name = models.CharField(max_length=100, unique=True)
    parent = models.ForeignKey('self', null=True, blank=True)
    priority = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class CriterionScore(models.Model):
    criterion = models.ForeignKey(Criterion)
    supplier = models.ForeignKey('supplier.Supplier')
    score = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "%s supplier %s criterion score" % (
            self.supplier.name, self.criterion.name)

    class Meta:
        unique_together = (('criterion', 'supplier'))
