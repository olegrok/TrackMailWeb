from django.db import models
from django.db.models import Q, Count


class PhotosQuerySet(models.QuerySet):
    def shown_list(self):
        queryset = self.annotate(comments_count=Count('comments', distinct=True), likes_count=Count('likes', distinct=True))
        return queryset

    def shown_detail(self):
        return self.prefetch_related('comments__author', 'author', 'category').annotate(comments_count=Count('comments'))