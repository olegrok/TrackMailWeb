# coding: utf-8

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.conf import settings
from django.http import request, HttpResponseRedirect
from django.template import RequestContext
from django.db.models import Count
from django.urls import reverse
from photos.models import Photo

from .models import User
from .forms import RegistrationForm


class UserView(DetailView):
    model = User
    template_name = 'core/user.html'
    slug_field = 'username'
    context_object_name = 'user_account'

    def get_context_data(self, **kwargs):
        context = super(UserView, self).get_context_data(**kwargs)
        context['profile'] = self.request.user
        return context

    def get_queryset(self):
        queryset = super(UserView, self).get_queryset()
        queryset = queryset.prefetch_related('photos')
        return queryset


class UserEdit(UpdateView):
    model = User
    template_name = 'core/user_edit.html'
    fields = ('email', 'first_name', 'last_name', 'avatar')
    slug_field = 'username'

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.request.user.pk)

        # def get_queryset(self):
        #     return User.objects.filter(username=self.request.user.username)


class RegisterView(CreateView):
    model = User
    template_name = 'core/registration/registration_form.html'
    form_class = RegistrationForm
    success_url = 'mainpage:login'

    def get_success_url(self):
        return reverse(self.success_url)


def home(request):
    popular_photos = Photo.objects.all().annotate(likes_count=Count('likes')).order_by('-likes_count')[:5]
    popular_photos = popular_photos.select_related('author')
    return render(request, context={'photos_list': popular_photos}, template_name='core/home.html')
