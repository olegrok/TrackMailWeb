# coding: utf-8

from __future__ import unicode_literals
from django.db.models import Model, CharField, TextField, SlugField
from django.urls import reverse
from django.utils.cache import caches
cache = caches['default']


class Category(Model):
    title = CharField(max_length=40, verbose_name=u'Название', blank=False)
    short_name = SlugField(max_length=15, verbose_name=u'Обозначение', blank=False)
    description = TextField(max_length=1024, verbose_name=u'Описание', blank=True)

    class Meta:
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('photos:list_category', args=[str(self.short_name)])

    @staticmethod
    def get_categories():
        categories = cache.get('categories')
        if categories is None:
            categories = [(category.title, category.short_name) for category in Category.objects.all()]
            cache.set('categories', categories, 1500)
        return categories
        # return [(category.title, category.short_name) for category in Category.objects.all()]


