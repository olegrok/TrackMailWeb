# coding: utf-8
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import QueryDict, request
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.contrib.contenttypes.models import ContentTypeManager, ContentType
from django.core.exceptions import ValidationError

from .models import Photo
from comments.models import Comment
from comments.forms import CommentForm

class PhotoList(ListView):
    template_name = 'photos_list.html'
    context_object_name = 'photo'
    model = Photo

#Кажется useless

'''
class PhotoView(DetailView):
    model = Photo
    template_name = "photo.html"
    context_object_name = 'photo'

    def get_context_data(self, **kwargs):
        context = super(PhotoView, self).get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context



class CreateCommentView(CreateView):
    model = Comment
    fields = ('text')

    def get_success_url(self):
        return reverse('photos:photo')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateCommentView, self).form_valid(form)
'''


class PhotoDetail(CreateView):
    model = Comment
    template_name = 'photo.html'
    fields = ('text', )
    success_url = '.'

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.photo = get_object_or_404(Photo, id=pk)
        return super(PhotoDetail, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PhotoDetail, self).get_context_data(**kwargs)
        context['photo'] = self.photo
        return context

    def form_valid(self, form):
        if self.request.user.is_anonymous():
            #raise ValidationError('You are not registred')
            return redirect('mainpage:login')
        form.instance.author = self.request.user
        form.instance.content_type = ContentType.objects.get_for_model(Photo)
        form.instance.object_id = self.photo.pk
        return super(PhotoDetail, self).form_valid(form)

    def get_success_url(self):
        return '.'

class CreatePhoto(CreateView):
    model = Photo
    template_name = 'create_photo.html'
    fields = ('photo', 'description', 'category')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreatePhoto, self).form_valid(form)


class EditPhoto(UpdateView):
    model = Photo
    template_name = 'photo_edit.html'
    fields = ('description', 'category')