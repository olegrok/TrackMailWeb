# coding: utf-8

from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser


# AbstractBaseUser
# https://docs.djangoproject.com/en/1.10/topics/auth/customizing/

class User(AbstractUser):
    avatar = models.ImageField(u'фото профиля', upload_to='avatars', blank=False, default=u'avatars/default-avatar.jpg')
    first_name = models.CharField(u'имя', max_length=30, blank=False)
    last_name = models.CharField(u'фамилия', max_length=30, blank=True)
    email = models.EmailField(u'e-mail', blank=False, unique=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('mainpage:user', kwargs={'slug': self.username})

    def get_pubs(self):
        return self.photos
