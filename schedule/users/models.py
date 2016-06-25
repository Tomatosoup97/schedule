from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

class BasicUser(AbstractUser):
	pass

class ClientProfile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)

class HostProfile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)