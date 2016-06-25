from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.db import models

from slugify import slugify

from users.models import ClientProfile
from core.models import TimeStampedModel

class Meeting(TimeStampedModel):
    """
    Meeting created by host(s) for client(s)
    """
    title = models.CharField(_('title'), max_length=100)
    description = models.TextField(_('description'))
    image = models.ImageField(_('image'), upload_to='meeting/%Y/%m', blank=True)
    location = models.CharField(_('location'), max_length=100, blank=True)

    start = models.DateTimeField(_('start of the meeting'))
    end = models.DateTimeField(_('end of the meeting'), blank=True, null=True)
    published = models.BooleanField(_('published'),
        help_text=_('mark if you want to publish meeting to public')

    hosts = models.ManyToManyField(settings.AUTH_USER_MODEL)
    clients = models.ManyToManyField(ClientProfile)

    category = models.ForeignKey('Category', verbose_name=_('category'))
    tags = models.ManyToManyField('Tag', verbose_name=_('tags'))

    slug = models.SlugField(_('url name'))

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Meeting, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(_('name'), max_length=80)

    def __str__(self):
        return self.name

class Tag(models.Model):
    """
    Short tag to provide brief information
    and improve searching mechanism
    """
    name = models.CharField(_('name'), max_length=40)

    def __str__(self):
        return self.name
