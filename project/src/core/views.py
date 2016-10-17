from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView, ListView
from .models import User

class UserView(DetailView):
    model = User
    template_name = "user.html"
    context_object_name = 'user'
    #pk_url_kwarg = 'username'
    slug_field = 'username'

def home(request):
    return render(request, 'home.html')