from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

class BasicUser(AbstractUser):
    
    def __str__(self):
        return self.first_name + self.last_name

class ClientProfile(models.Model):
    """
    Profile for meeting's Clients
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='client')

    def __str__(self):
        return self.first_name + self.last_name + 'Client'

class HostProfile(models.Model):
    """
    Profile for meeting Hosts
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='host')

    def __str__(self):
        return self.first_name + self.last_name + 'Host'