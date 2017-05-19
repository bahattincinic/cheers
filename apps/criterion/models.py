from django.db import models
from django.utils.encoding import smart_text
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Criterion(models.Model):
    name = models.CharField(max_length=100, unique=True)
    parent = models.ForeignKey('self', null=True, blank=True)

    def __str__(self):
        return smart_text(self.name)
