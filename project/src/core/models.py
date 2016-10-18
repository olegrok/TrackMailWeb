from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    first_name = models.CharField(('first name'), max_length=30, blank=False)
    email = models.EmailField(('E-mail address'), blank=False, unique=True)

    #@models.permalink
    def get_absolute_url(self):
        #print(("user.view", [self.username]))
        #return "user.view" % self.username
        return "/users/%s" % self.username

    def get_pubs(self):
        return self.photos
