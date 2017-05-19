from django.db import models
from django.utils.encoding import smart_text
from django.utils.encoding import python_2_unicode_compatible

from redactor.fields import RedactorField


@python_2_unicode_compatible
class Topic(models.Model):
    title = models.CharField(max_length=255)
    content = RedactorField()
    summary = models.TextField(null=True, blank=True)
    show_home = models.BooleanField(default=False)

    def __str__(self):
        return smart_text(self.title)
