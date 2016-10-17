from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView, ListView

from .models import Photo

class PhotoList(ListView):
    template_name = 'photos_list.html'
    context_object_name = 'photo'
    model = Photo

class PhotoView(DetailView):
    model = Photo
    template_name = "photo.html"
    context_object_name = 'photo'

def show_photo(request, photos_id=0):
    return render(request, 'detailed_template.html', {"photos_id" : photos_id})
