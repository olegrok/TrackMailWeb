# coding: utf-8

from __future__ import unicode_literals

from django.db import models
from django.db.models import ForeignKey
from django.conf import settings


class Like(models.Model):
    author = ForeignKey(settings.AUTH_USER_MODEL, related_name='his_likes', verbose_name='Владелец')
    photo = ForeignKey('photos.Photo', related_name='likes', verbose_name='Фотокарточка')
    class Meta:
        unique_together = (('author', 'photo'),)
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'

    def __str__(self):
        return '%i by %s' % (self.photo.id, self.author)
