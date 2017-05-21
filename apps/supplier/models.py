from django.db import models
from django.utils.encoding import smart_text
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Supplier(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return smart_text(self.name)
