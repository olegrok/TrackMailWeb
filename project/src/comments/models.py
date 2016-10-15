from __future__ import unicode_literals

from django.db import models

class Comment(models.Model):
    text = models.TextField(max_length=1024)
    photo = models.ForeignKey('photos.Photo')