from django.conf.urls import url
from .views import *
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from application.settings import LOGIN_URL

urlpatterns = [
    url(r'^list/$', PhotoList.as_view(), name="list"),
    url(r'^(?P<pk>\d+)/$', PhotoDetail.as_view(), name="photo"),
    url(r'^(?P<pk>\d+)/likes/$', PhotoLikesCount.as_view(), name="photo_likes"),
    url(r'^all/likes/$', PhotosLikesView.as_view(), name="likes"),
    url(r'(?P<pk>\d+)/edit/$', login_required(EditPhoto.as_view(), login_url=LOGIN_URL), name='photo_edit'),
    url(r'^newphoto/$', login_required(CreatePhoto.as_view(), login_url=LOGIN_URL), name='create_photo'),
    url(r'^list/(?P<slug>\w+)', PhotoCategoryView.as_view(), name='list_category'),
]
