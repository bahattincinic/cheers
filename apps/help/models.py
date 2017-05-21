from django.db import models
from django.utils.encoding import smart_text
from django.utils.encoding import python_2_unicode_compatible
from django.urls import reverse
from django.utils.text import slugify

from redactor.fields import RedactorField


@python_2_unicode_compatible
class Topic(models.Model):
    title = models.CharField(max_length=255)
    content = RedactorField()
    summary = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return smart_text(self.title)

    def get_absolute_url(self):
        return reverse('topic-detail', args=[self.id, slugify(self.title)])
