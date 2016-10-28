# coding: utf-8

from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser

#AbstractBaseUser
#https://docs.djangoproject.com/en/1.10/topics/auth/customizing/

class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    first_name = models.CharField(('first name'), max_length=30, blank=False)
    email = models.EmailField(('E-mail address'), blank=False, unique=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('mainpage:user', kwargs={'slug': self.username})

    def get_pubs(self):
        return self.photos

    #def create_user(self, username, password, email, first_name, second_name = None, avatar = None):
    #    User.objects.create_user(username, email, password, first_name = first_name, second_name = second_name, avatar = avatar)

