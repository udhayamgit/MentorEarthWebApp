# -*- coding: utf-8 -*-
# All imports

from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from stream_django import activity
from stream_django.feed_manager import feed_manager
from django_countries.fields import CountryField
#Models

class write(models.Model):
    user = models.ForeignKey('auth.user')
    title = models.CharField(max_length=160)
    industry = models.CharField(max_length=50)
    text = models.CharField(max_length=1500)
    created_at = models.DateTimeField(auto_now_add=True)

class Follow(models.Model):
    user = models.ForeignKey('auth.User', related_name='friends')
    target = models.ForeignKey('auth.User', related_name='followers')
    created_at = models.DateTimeField(auto_now_add=True)

class Meta:
    unique_together = ('user', 'target')

class write(activity.Activity, models.Model):
        user = models.ForeignKey('auth.user')
        title = models.CharField(max_length=160)
        industry = models.CharField(max_length=50)
        text = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)

        @property
        def activity_object_attr(self):
            return self
