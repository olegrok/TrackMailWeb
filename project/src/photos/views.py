from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView
from django.views.generic import ListView

from .models import Photo

class PhotoList(ListView):
    temlate_name = 'photos/list.html'
    model = Photo('photos/templates/photos/list.html')

class PhotoView(DetailView):
    template_name = "photo.html"
    context_object_name = 'photo'

def show_photo(request, photos_id=0):
    return render(request, 'detailed.html', {"photos_id" : photos_id})

