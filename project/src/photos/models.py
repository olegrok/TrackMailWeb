# coding: utf-8

from __future__ import unicode_literals
from django.db import models
from django.conf import settings

class Photo(models.Model):
    photo = models.ImageField(upload_to='photos/', blank=False, null=False)
    description = models.TextField(max_length=1024, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='photos')

    CATEGORIES = (
        ('Life', 'life'),
        ('Nature', 'nature'),
        ('Culture', 'culture'),
        ('Sciense', 'science' ),
        ('Space', 'space'),
        ('News', 'news'),
        ('Humor', 'humor' ),
        ('Information Technology', 'IT' )
    )

    category = models.CharField(blank='True', choices=CATEGORIES, max_length=1024)


    class Meta:
        verbose_name = u'Фотокарточка'
        verbose_name_plural = u'Фотокарточки'
        ordering = ('-pub_date',)

    def __str__(self):
        return str(self.id)
    def count_likes(self):
        return self.likes.count()
    def get_comments(self):
        return self.comments
    def get_absolute_url(self):
    #    from django.urls import reverse
    #    return reverse('photos.Photo.detail', args=[str(self.id)])
        return '/photos/%i/' % self.id
    def get_file_url(self):
        return self.photo.url
