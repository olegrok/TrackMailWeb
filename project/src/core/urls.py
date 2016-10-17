from django.conf.urls import url
from .views import *
from django.contrib import admin

urlpatterns = [
    url(r'^$', home, name='home'),
    #todo
    url(r'^users/(?P<slug>\w+)/$', UserView.as_view(), name="user"),
]