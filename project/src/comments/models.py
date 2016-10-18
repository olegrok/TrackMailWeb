from __future__ import unicode_literals
from django.conf import settings
from django.db import models

class Comment(models.Model):
    text = models.TextField(max_length=1024)
    photo = models.ForeignKey('photos.Photo', related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments')
    pub_date = models.DateTimeField(auto_now_add=True)
    ordering = ('-created_at',)
