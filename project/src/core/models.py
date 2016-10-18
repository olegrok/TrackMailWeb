from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser

#AbstractBaseUser
#https://docs.djangoproject.com/en/1.10/topics/auth/customizing/

class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    first_name = models.CharField(('first name'), max_length=30, blank=False)
    email = models.EmailField(('E-mail address'), blank=False, unique=True)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('users:user', kwargs={'slug': self.username})

    def get_pubs(self):
        return self.photos
