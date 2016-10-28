from django.conf.urls import url
from .views import PhotoList, PhotoDetail #, PhotoView, CreateCommentView
from django.contrib import admin


urlpatterns = [
    url(r'^list/$', PhotoList.as_view(), name="list"),
    url(r'^(?P<pk>\d+)/$', PhotoDetail.as_view(), name="photo"),
]