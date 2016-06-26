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
    end = models.DateTimeField(_('end of the meeting'), blank=True, null=True)

    private = models.BooleanField(_('private'),
        default=True,
        help_text=_('mark if you want this meeting not to be seen by clients'))
    public = models.BooleanField(_('public'),
        default=False,
        help_text=_('mark if you want this meeting to be public' \
                    ' (visible for everyone)'))

    hosts = models.ManyToManyField(settings.AUTH_USER_MODEL, db_index=True)
    clients = models.ManyToManyField(ClientProfile, db_index=True, blank=True)

    tags = models.ManyToManyField('Tag', verbose_name=_('tags'), blank=True)
    category = models.ForeignKey(
        'Category', verbose_name=_('category'), blank=True)

    slug = models.SlugField(_('url name'), editable=False)

    class Meta:
        verbose_name = _('meeting')
        verbose_name_plural = _('meetings')
        unique_together = ('private', 'public')
        ordering = ['start']

    def duration(self):
        if self.end:
            return self.end - self.start
        return None

    def save(self, *args, **kwargs):
        # Create slug on creation
        if not self.id:
            self.slug = slugify(self.title)
        super(Meeting, self).save(*args, **kwargs)

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
