from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from . models import Post
# Create your views here.
def home(request):
 return render(request,'blog/index.html')


class PostList(ListView):
    model = Post
    context_object_name = 'posts'
 


     

class PostDetails(DetailView):
    model = Post
    context_object_name = 'post'

class CreateView(CreateView):
    model=Post
    fields=['title','description']
    success_url = reverse_lazy('posts')


class PostUpdate(UpdateView):
    model = Post
    fields = ['title','description']
    success_url=reverse_lazy('posts')

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('posts')
