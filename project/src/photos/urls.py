from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^photos/$', PhotoList.as_view(), name="list"),
]