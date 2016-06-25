from __future__ import unicode_literals

from django.db import models

class TimeStampedModel(models.Model):
    """
    Abstract model base class that provides
    created and modified fields
    """
    created = models.DateTimeField(
        _('created date'),
        auto_now_add=True,)
    modified = models.DateTimeField(
        _('modification date'),
        auto_now=True,)

    class Meta:
        abstract = True