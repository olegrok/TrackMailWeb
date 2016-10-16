from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class Like(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='his_likes')
    photo = models.ForeignKey('photos.Photo', related_name='likes')
    class Meta:
        unique_together = (('author', 'photo'),)
