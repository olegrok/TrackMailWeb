from django.conf.urls import url
from .views import PhotoList, PhotoDetail, CreatePhoto, EditPhoto
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from application.settings import LOGIN_URL

urlpatterns = [
    url(r'^list/$', PhotoList.as_view(), name="list"),
    url(r'^(?P<pk>\d+)/$', PhotoDetail.as_view(), name="photo"),
    url(r'(?P<pk>\d+)/edit/$', EditPhoto.as_view(), name='photo_edit'),
    url(r'^newphoto/$', login_required(CreatePhoto.as_view(), login_url=LOGIN_URL), name='create_photo'),
]