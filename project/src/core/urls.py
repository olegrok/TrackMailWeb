from django.conf.urls import url, include
from .views import home, UserView, register, RegisterView
from django.contrib import admin
from django.contrib.auth.views import login, logout, password_change

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^accounts/logout/$', logout, {'next_page' : '/'}, name='logout'),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/password_change/$', password_change,{'template_name':'registration/password_change.html', 'post_change_redirect':'/'}, name='password_change'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    #url(r'^accounts/register/$', register, {'template_name':'registration/registration_form.html'}, name='register'),
    url(r'^accounts/register/$', RegisterView.as_view(), name='register'),
    url(r'^users/(?P<slug>\w+)/$', UserView.as_view(), name="user"),
]