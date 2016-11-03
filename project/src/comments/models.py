# coding: utf-8

from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.db.models import TextField, DateTimeField, ForeignKey, Model, PositiveIntegerField
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


class Comment(Model):

    content_type = ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    comments = GenericRelation('comments.Comment', related_name = 'comments')

    text = TextField(blank=False, max_length=1024, verbose_name='Комментарий')
    author = ForeignKey(settings.AUTH_USER_MODEL, blank=False, related_name='comments', verbose_name='Автор')
    pub_date = DateTimeField(auto_now_add=True, verbose_name='Дата публикации')


    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return '%i by %s' % (self.content_object.id, self.author)