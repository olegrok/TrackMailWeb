# coding: utf-8

from __future__ import unicode_literals
from django.db import models
from django.conf import settings

class Photo(models.Model):
    photo = models.ImageField(upload_to='photos/static/', blank=False, null=False)
    description = models.TextField(max_length=1024, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    verbose_name = u'Фотокарточка'
    verbose_name_plural = u'Фотокарточки'
    ordering = ('-created_at',)

    def count_likes(self):
        return self.likes.count()
    def get_comments(self):
        return self.comments

