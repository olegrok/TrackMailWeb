# coding: utf-8

from __future__ import unicode_literals
from django.db.models import ImageField, DateTimeField, TextField, ForeignKey, Model
from django.conf import settings
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.urls import reverse
from categories.models import Category

class Photo(Model):
    photo = ImageField(upload_to='photos/', blank=False, null=False, verbose_name='Фотокарточка')
    description = TextField(max_length=1024, blank=True, verbose_name='Описание')
    pub_date = DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    author = ForeignKey(settings.AUTH_USER_MODEL, related_name='photos', verbose_name='Автор')
    comments = GenericRelation('comments.Comment', related_query_name='comments', verbose_name='Отзывы')
    category = ForeignKey(Category, related_name='photos', verbose_name='Категория', blank=True)


    class Meta:
        verbose_name = u'Фотокарточка'
        verbose_name_plural = u'Фотокарточки'
        ordering = ('-pub_date',)

    def __str__(self):
        return str(self.id)
    def likes(self):
        return self.likes
    def get_comments(self):
        return self.comments
    def get_absolute_url(self):
        return reverse('photos:photo', args=[str(self.pk)])
    def get_edit_url(self):
        return reverse('photos:photo_edit', args=[str(self.pk)])
    def get_file_url(self):
        return self.photo.url
