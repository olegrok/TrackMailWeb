from django.conf.urls import url, include
from .views import home, UserView
from django.contrib import admin

urlpatterns = [
    url(r'^$', home, name='home'),
    #todo
    url(r'^(?P<slug>\w+)/$', UserView.as_view(), name="user"),
    #url(r'^users/(\w+)/$', 'users.view.user')
]