# coding: utf-8

from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.conf import settings
from django.http import request, HttpResponseRedirect
from django.template import RequestContext
from django.urls import reverse

from .models import User
from .forms import RegistrationForm

class UserView(DetailView):
    model = User
    template_name = "user.html"
    context_object_name = 'user'
    slug_field = 'username'

class RegisterView(CreateView):
    model = User
    template_name = 'registration/registration_form.html'
    form_class = RegistrationForm
    success_url = 'mainpage:login'

    def get_success_url(self):
        from django.urls import reverse
        return reverse(self.success_url)


def register(request, template_name = 'registration/registration_form.html',
             redirect_field_name=None): #reverse('mainpage:register')

    if redirect_field_name == None:
        redirect_field_name = reverse('mainpage:login')

    form = RegistrationForm(data=request.POST or None, files=request.FILES or None)
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST, files=request.FILES or None)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                username=data['username'],
                email=data['email'],
                password=data['password1']
            )
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.avatar = data['avatar']
            user.save()
            return redirect(redirect_field_name)
    return render(request, template_name, {'form':form})





def home(request):
    return render(request, 'home.html')