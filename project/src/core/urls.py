from django.conf.urls import url
from .views import *
from django.contrib import admin

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^users/(?P<pk>\d+)/$', UserView.as_view(), name="user"),
]