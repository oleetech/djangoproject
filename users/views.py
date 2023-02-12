from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LogoutView


def home(request):
 return HttpResponse('a')

    
class MyLoginView(LoginView):
  template_name = 'users/login.html'
  redirect_authenticated_user = True
  def get_success_url(self):
    return reverse_lazy('home')


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'users/register.html'

    def get_success_url(self):
      return reverse_lazy('home')

class MylogoutView (LogoutView):
  pass




