# coding: utf-8

from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404, reverse, redirect
from django.views.generic import ListView, CreateView, UpdateView

from comments.models import Comment
from .forms import SearchForm
from .models import Photo


class PhotoList(ListView):
    model = Photo
    template_name = 'photos_list.html'
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
        return queryset

    def get_context_data(self, **kwargs):
        context = super(PhotoList, self).get_context_data(**kwargs)
        context['search_form'] = self.search_form
        context['categories'] = Photo.CATEGORIES
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
        for pair in self.model.CATEGORIES:
            if self.category in pair:
                self.category = pair[0]
                break
        return queryset.filter(category=self.category)


#Кажется useless

'''
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

    def get_success_url(self):
        return reverse('photos:photo', args=[str(self.get_form().instance.pk)])


class EditPhoto(UpdateView):
    model = Photo
    template_name = 'photo_edit.html'
    fields = ('description', 'category')

    def get_queryset(self):
        return Photo.objects.filter(author=self.request.user)