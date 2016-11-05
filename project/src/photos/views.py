# coding: utf-8
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404, reverse, redirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.http import HttpResponseRedirect
from django.contrib.auth.views import redirect_to_login

from application.settings import LOGIN_URL
from comments.forms import CommentForm
from comments.models import Comment
from categories.models import Category
from .forms import SearchForm
from .models import Photo


class PhotoList(ListView):
    model = Photo
    template_name = 'photos/photos_list.html'
    context_object_name = 'photo'

    def dispatch(self, request, *args, **kwargs):
        self.search_form = SearchForm(request.GET)
        return super(PhotoList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Photo.objects.all()
        if self.search_form.is_valid():
            queryset = queryset.filter(description__icontains=self.search_form.cleaned_data['search'])
            queryset = queryset.order_by(self.search_form.cleaned_data['sort'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super(PhotoList, self).get_context_data(**kwargs)
        context['search_form'] = self.search_form
        context['categories'] = Category.get_categories()
        return context


class PhotoCategoryView(PhotoList):
    slug_field = 'category'

    def dispatch(self, request, *args, **kwargs):
        self.category = kwargs['slug']
        return super(PhotoCategoryView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super(PhotoCategoryView, self).get_queryset()
        if self.category == 'all':
            return queryset
        return queryset.filter(category__short_name=self.category)


class PhotoDetail(DetailView):
    model = Photo
    context_object_name = 'photo'
    template_name = 'photos/photo.html'
    success_url = '.'

    def dispatch(self, request, *args, **kwargs):
        self.user = request.user
        self.comment_form = CommentForm
        return super(PhotoDetail, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PhotoDetail, self).get_context_data(**kwargs)
        context['comment_form'] = self.comment_form
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.comment_form(request.POST)
        if request.user.is_anonymous():
            return redirect_to_login(next=reverse('photos:photo', args=[str(self.object.pk)]), login_url=LOGIN_URL)
        if form.is_valid():
            comment = Comment()
            comment.author = request.user
            comment.text = form.cleaned_data['comment']
            comment.content_type = ContentType.objects.get_for_model(self.model)
            comment.object_id = self.object.pk
            comment.save()
        return HttpResponseRedirect(self.success_url)

class CreatePhoto(CreateView):
    model = Photo
    template_name = 'photos/create_photo.html'
    fields = ('photo', 'description', 'category')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreatePhoto, self).form_valid(form)

    def get_success_url(self):
        return reverse('photos:photo', args=[str(self.object.pk)])


class EditPhoto(UpdateView):
    model = Photo
    template_name = 'photos/photo_edit.html'
    fields = ('description', 'category')

    def get_queryset(self):
        return Photo.objects.filter(author=self.request.user)