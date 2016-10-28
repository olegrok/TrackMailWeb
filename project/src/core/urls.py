from django.conf.urls import url, include
from .views import home, UserView, UserCreate, register
from django.contrib import admin
from django.contrib.auth.views import login, logout


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^accounts/logout/$', logout, {'next_page' : '/'}, name='logout'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/register/$', register, {'template_name':'registration/registration_form.html'}, name='register'),


    #url(r'accounts/', include('registration.urls'), name='accounts_registration'),
    #url(r'^accounts/login/$', login, {'template_name': 'login.html'}),
    url(r'^users/(?P<slug>\w+)/$', UserView.as_view(), name="user"),
]