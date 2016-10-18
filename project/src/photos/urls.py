from django.conf.urls import url
from .views import *
from django.contrib import admin


urlpatterns = [
    url(r'^list/$', PhotoList.as_view(), name="list"),
    url(r'^(?P<pk>\d+)/$', PhotoView.as_view(), name="detail"),
    #url(r'^(?P<photos_id>\d+)/$', show_photo),
]