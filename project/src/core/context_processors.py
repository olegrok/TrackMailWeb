from django.contrib.auth.views import login
from django.contrib.auth.forms import AuthenticationForm

def context_login(request):
    return {'forma':login(request)}