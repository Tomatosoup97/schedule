from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.db import models

from slugify import slugify

from users.models import ClientProfile
from core.models import TimeStampedModel

class Meeting(TimeStampedModel):
    """
    Meeting created by host(s) for client(s),
    marked on calendar,
    can be private or public
    """
    title = models.CharField(_('title'), max_length=100, db_index=True)
    description = models.TextField(_('description'))
    image = models.ImageField(_('image'), upload_to='meeting/%Y/%m', blank=True)
    location = models.CharField(_('location'), max_length=100, blank=True)

    start = models.DateTimeField(_('start of the meeting'), db_index=True)
    duration = models.DateTimeField(_('duration'), blank=True, null=True)
    end = models.DateTimeField(_('end of the meeting'), blank=True, null=True)
    private = models.BooleanField(_('private'),
        default=True,
        help_text=_('unmark if you want this meeting to be seen by clients'))
    public = models.BooleanField(_('public'),
        default=False,
        help_text=_('mark if you want this meeting to be public' \
                    '(for everyone)'))

    hosts = models.ManyToManyField(settings.AUTH_USER_MODEL, db_index=True)
    clients = models.ManyToManyField(ClientProfile, db_index=True, blank=True)

    tags = models.ManyToManyField('Tag', verbose_name=_('tags'), blank=True)
    category = models.ForeignKey(
        'Category', verbose_name=_('category'), blank=True)

    slug = models.SlugField(_('url name'))

    class Meta:
        verbose_name = _('meeting')
        verbose_name_plural = _('meetings')
        ordering = ['start']

    def save(self, *args, **kwargs):
        # create slug on creation
        if not self.id:
            self.slug = slugify(self.title)

        # Autofill duration or end time
        if self.end and not self.duration:
            self.duration = self.start - self.end
        elif self.duration and not self.end:
            self.end = self.start + self.duration

        super(Meeting, self).save(*args, **kwargs)

    def duration(self):
        if duration:
            return duration
        return 'Unknown'

    def __str__(self):
        return self.title

class Category(models.Model):
    COLORS = (
            ('white', _('white')),
            ('grey', _('grey')),
            ('red', _('red')),
            ('green', _('green')),
            ('blue', _('blue')),
            ('yellow', _('yellow')),
        )

    name = models.CharField(_('name'), max_length=80)
    color = models.CharField(
        _('color'),
        choices = COLORS,
        max_length=20,
        default='white')

    class Meta:
        verbose_name = _('catagory')
        verbose_name_plural = _('categories')

    def __str__(self):
        return self.name

class Tag(models.Model):
    """
    Short tag to provide brief information
    and improve searching mechanism
    """
    name = models.CharField(_('name'), max_length=40)

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')

    def __str__(self):
        return self.name
