# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-26 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='private',
            field=models.BooleanField(default=True, help_text='mark if you want this meeting not to be seen by clients', verbose_name='private'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='public',
            field=models.BooleanField(default=False, help_text='mark if you want this meeting to be public (visible for everyone)', verbose_name='public'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='slug',
            field=models.SlugField(editable=False, verbose_name='url name'),
        ),
        migrations.AlterUniqueTogether(
            name='meeting',
            unique_together=set([('private', 'public')]),
        ),
    ]