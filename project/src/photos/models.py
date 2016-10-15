from __future__ import unicode_literals

from django.db import models
from django.conf import settings

class Photo(models.Model):
    photo = models.ImageField(upload_to='Images', blank=False, null=False)
    description = models.TextField(max_length=1024, blank=True, null = True)
    pub_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
