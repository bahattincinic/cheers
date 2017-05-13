from django.db import models


class Criterion(models.Model):
    name = models.CharField(max_length=100, unique=True)
    parent = models.ForeignKey('self', null=True, blank=True)

    def __str__(self):
        return str(self.id)
